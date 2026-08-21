---
title: Jenkins and CI Integration for Pi
type: synthesis
updated: 2026-08-21
sources:
  - pi-extensions-docs
  - jenkins-remote-access-api
  - jenkins-scripted-clients-auth
  - jenkins-csrf-protection
  - jenkins-pipeline-rest-api
  - jenkins-log-oom-75081
  - jenkins-mcp-server-plugin
  - t089-jenkins-mcp
  - jordan-jarvis-jenkins-mcp-enterprise
  - adarsh-jenkins-mcp-go
  - lanbaoshen-mcp-jenkins
  - nicobailon-pi-mcp-adapter
tags: [ci, jenkins, build-logs, integration, mcp]
---

# Jenkins and CI Integration for Pi

## Short answer

For **reading build logs** — the dominant use case — write a small native Pi
extension over the Jenkins REST API. Not because the API is hard (it is a
`curl` away), but because the entire problem is **context management**, and
that is exactly what a native tool controls and a shell pipe does not.

A build log is the worst possible shape for an LLM context window: tens of
megabytes, mostly irrelevant, with the useful part (the stack trace, the
failing assertion) buried at the end or scattered across stages. Any
integration that hands the model a whole log has failed, no matter how clean
its transport. Rank the options by *how much log never reaches the context*,
and the answer stops being about Jenkins at all.

## The three integration shapes

| Shape | Moving parts | Context control | Use when |
|---|---|---|---|
| **`bash` + `curl`** | none | none — output hits Pi's generic truncation blindly | one-off triage; you already know the job and build number |
| **MCP server** | MCP server process **+** an MCP adapter extension (Pi has no core MCP) | whatever the server author chose | you already run MCP and want the same tools in several agents |
| **Native Pi extension** | one extension | total — you decide what is even eligible to enter the context | recurring workflow; large or noisy logs; team-wide use |

### Why `bash` + `curl` disappoints

It works on day one and is the right way to *explore* the API. But every
call re-teaches the model the base URL, the auth flag and the endpoint shape,
and a 40 MB `consoleText` arrives as an undifferentiated wall that Pi
truncates by generic rule rather than by relevance. Pi truncates `bash`
output at **50 KB / 2000 lines** — for logs that cut lands in the middle of
whatever you needed.

### Why MCP is a heavier answer than it looks *in Pi*

Pi ships no MCP client in core; MCP arrives through an adapter extension
(see [MCP integration](mcp-integration.md)). So "just use the Jenkins MCP
server" means running **two** extra components — the adapter plus the server
— to reach an HTTP API you could have called directly. The ecosystem is
healthy (an official [Jenkins MCP Server plugin](https://plugins.jenkins.io/mcp-server/),
plus `t089/jenkins-mcp`, `Jordan-Jarvis/jenkins-mcp-enterprise`,
`2001adarsh/jenkins-mcp-go`, `lanbaoshen/mcp-jenkins`), and the better
servers already solve the log-size problem with grep-and-paginate rather than
dumping. MCP earns its keep when the *same* Jenkins tools must serve Pi,
Claude Code and an IDE at once. For Pi alone it is indirection.

Worth knowing before adopting the official plugin: it is a **server-side
Jenkins plugin**, so it needs installing on the controller — a different
political problem than a client-side script, and one third-party author
reports 30 s timeouts against it.

## Jenkins API essentials

### Auth: API token, and no crumb

Use HTTP Basic with `user:api_token` (never the password; token auth also
survives SSO realms where no password exists). The CSRF crumb is the usual
first stumble, and the good news is that it is **not needed**: since Jenkins
2.96 a request authenticated with an API token is exempt from crumb
validation, because crumbs defend against cookie-borne CSRF and token auth is
session-less. Fetch a crumb only if you are stuck authenticating with a real
password.

### Endpoints that matter

| Endpoint | Returns |
|---|---|
| `/job/<job>/api/json?tree=...` | job metadata; `tree=` prunes the payload server-side |
| `/job/<job>/lastBuild/api/json` | status, timing, result of the newest build |
| `/job/<job>/<n>/consoleText` | the whole plain-text log — the thing to avoid for big builds |
| `/job/<job>/<n>/logText/progressiveText?start=<byte>` | **chunked** log from a byte offset |
| `/job/<job>/<n>/wfapi/describe` | pipeline **stage** list with per-stage status |
| `/job/<job>/<n>/execution/node/<id>/wfapi/log` | log for **one stage** only |

`progressiveText` is the important one. It answers with the next chunk plus
an `X-Text-Size` header (the new byte offset) and `X-More-Data` (whether the
build is still writing). That is a cursor: poll a running build by feeding
the previous `X-Text-Size` back as `start`, and tail a finished one by
requesting only its final stretch.

The stage endpoints (from the
[Pipeline: REST API plugin](https://plugins.jenkins.io/pipeline-rest-api))
are the highest-leverage and least-used part of the surface: for a pipeline,
"which stage failed" is a cheap `wfapi/describe` call, after which you fetch
**only the failing stage's log**. That is usually a few KB instead of the
whole run, and it is the single biggest context saving available.

### The trap: huge logs can take down the controller

`logText/progressiveText` on a very large completed log can exhaust the
Jenkins controller's heap ([JENKINS-75081]). This is a server-side failure
caused by *your* client's request, so it is not a Jenkins-team problem you
can wait out. Practical consequences for any integration:

- Never fetch a whole multi-GB log "just to grep it locally."
- Bound every request: ask for a tail window or a stage, not the run.
- Prefer stage logs on pipelines; prefer offset windows elsewhere.

## Designing the extension

Pi's own guidance is unusually blunt here: **"Tools MUST truncate their
output"**, with a built-in ceiling of 50 KB / 2000 lines, and it exports the
utilities to do it (`truncateTail`, `truncateHead`, `formatSize`,
`DEFAULT_MAX_BYTES`, `DEFAULT_MAX_LINES`). For logs the correct one is
`truncateTail` — failures are at the end — paired with the documented
spillover idiom: write the full text to a temp file and tell the model where
it is, so `grep` remains possible without the bytes entering the context.

```ts
const truncation = truncateTail(log, {
  maxLines: DEFAULT_MAX_LINES,
  maxBytes: DEFAULT_MAX_BYTES,
});
let out = truncation.content;
if (truncation.truncated) {
  const file = writeTempFile(log);          // full log stays on disk
  out += `\n\n[Truncated: ${truncation.outputLines} of ${truncation.totalLines} lines`
       + ` (${formatSize(truncation.outputBytes)} of ${formatSize(truncation.totalBytes)}).`
       + ` Full log: ${file}]`;
}
```

A tool surface that matches how failures are actually diagnosed:

| Tool | Job |
|---|---|
| `jenkins_build_status` | result, duration, revision, stage summary — the cheap call that usually answers the question |
| `jenkins_failing_stage` | resolve the failed stage via `wfapi/describe`, return **only** that stage's log tail |
| `jenkins_log_search` | server-agnostic grep with N lines of context, over a bounded window; returns matches, never the log |
| `jenkins_log_tail` | last N KB via `progressiveText`, for non-pipeline jobs |

`jenkins_log_search` is the one that changes daily use: "why did build 4711
fail" becomes a regex for `ERROR|FAILED|Exception` returning a few hundred
bytes, instead of a megabyte the model has to skim.

Configure the base URL and credentials through settings rather than tool
arguments — the token must never be model-visible, and letting the model pass
a URL invites SSRF against internal hosts.

## Picking guide

| Situation | Do this |
|---|---|
| Occasional triage, log already small | `bash` + `curl` with an API token |
| Recurring work, pipelines, big logs | Native extension with the four tools above |
| Same Jenkins tooling across Pi, Claude Code and an IDE | Jenkins MCP server + Pi MCP adapter |
| Controller admin rights and org-wide rollout | Official Jenkins MCP Server plugin (verify the reported timeouts) |
| Log so large that any fetch risks the controller | Stage logs only; never whole-run fetches |

## Caveats

- **Nothing Pi-specific exists yet.** No Jenkins extension appears in the Pi
  package catalog as of 2026-08; this page is a design synthesis, not a
  survey of shipped options.
- **`consoleText` is a footgun at scale** — convenient in a terminal, wrong
  in a tool. Reach for stage logs or offset windows.
- **`tree=` is underused.** Most `api/json` payload bloat disappears with a
  `tree=` filter, which costs one parameter.
- **Blue Ocean's API is deprecated territory**; prefer `wfapi` from the
  Pipeline REST API plugin for stage data.

## See also

- [MCP integration](mcp-integration.md) — how MCP reaches Pi at all
- [Web search extensions](web-search-extensions.md) — the same
  truncate-and-spill discipline for another high-volume source

[JENKINS-75081]: https://github.com/jenkinsci/jenkins/issues/16619
