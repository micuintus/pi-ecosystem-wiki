---
title: Pi MCP Integration
type: ecosystem
updated: 2026-05-10
sources:
  - nicobailon-pi-mcp-adapter
  - jordyvd-pi-mcp-adapter
  - steimbyte-pi-mcp-extension
  - mitsuhiko-pi-codemode-mcp
  - mariozechner-mcp-vs-cli
  - mariozechner-what-if-no-mcp
  - pi-mcp-adapter-docs
  - spences10-my-pi
tags: [extension, mcp, integration]
entries:
  - id: nicobailon-pi-mcp-adapter
    name: pi-mcp-adapter
    repo: nicobailon/pi-mcp-adapter
    npm: pi-mcp-adapter
    role: adapter
    notes: "608 stars, 23.7K weekly downloads, 29 versions, 4 contributors. Token-efficient proxy tool (~200 tokens vs 10k+ for direct registration). Auto-discovers MCP servers from mcp.json. Servers start on-demand."
  - id: steimbyte-pi-mcp-extension
    name: pi-mcp-extension
    repo: alephtex/pi-mcp-extension
    role: alternative-adapter
    notes: "Alternative to nicobailon's adapter. Claims Zod version conflicts (pi bundles its own Zod, MCP SDK v1.x requires Zod v3 with incompatible signatures)."
  - id: mitsuhiko-pi-codemode-mcp
    name: pi-codemode-mcp
    repo: mitsuhiko/pi-codemode-mcp
    role: experimental
    notes: "Experimental. Two tools: list_mcp_tools (first 20 inline, overflow to temp file), call_mcp (JavaScript sandbox). /mcp command for status, enable/disable, reconnect, auth."
  - id: spences10-my-pi
    name: spences10/my-pi
    repo: spences10/my-pi
    role: bundle
    notes: "Composable Pi setup with MCP, LSP, agent chains, prompt presets, local SQLite telemetry. Built on @mariozechner/pi-coding-agent SDK. Stdio and HTTP/streamable-HTTP servers from mcp.json."
---

# Pi MCP Integration

## Contents

- [What MCP adds (and costs)](#what-mcp-adds-and-costs)
- [Surveyed adapters](#surveyed-adapters)
- [The proxy pattern](#the-proxy-pattern-how-nicobailons-adapter-works)
- [When MCP makes sense](#when-mcp-makes-sense-and-when-it-doesnt)
- [CLI skills as the Pi-native alternative](#cli-skills-as-the-pi-native-alternative)
- [Picking an MCP adapter](#picking-an-mcp-adapter)
- [See also](#see-also)

Survey of Pi extensions that connect to [Model Context Protocol](https://modelcontextprotocol.io/)
(MCP) servers — the standardized way to expose tools, resources, and
prompts to LLMs.

> **Design tension:** Pi's creator [Mario Zechner argues that many MCP
> servers are unnecessary](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp)
> — they flood the context window with verbose tool definitions and
> running-server dependencies that simple CLI tools avoid. Pi's native
> skill system achieves similar capability discovery without the
> protocol overhead. This page surveys the MCP adapters that exist,
> but the ecosystem opinion leans toward CLI-based skills where
> possible.

## What MCP adds (and costs)

MCP standardizes how an agent connects to external capabilities. A
server exposes tools via stdio or HTTP; the adapter registers them as
Pi tools. The benefit is interoperability — one server works with Pi,
Claude Desktop, Cursor, and any other MCP client.

The cost:

- **Context bloat.** A single MCP server can burn 10k+ tokens in tool
definitions. Connect three servers and half your context window is
 gone before the first turn.
- **Running-server dependency.** Each stdio server is a separate
process; HTTP servers need network access and auth.
- **Version fragility.** Zod version mismatches between Pi's bundled
Zod and the MCP SDK have caused runtime errors in the wild.
- **Over-generalization.** Many MCP servers expose 20+ tools to cover
all bases; the agent uses 2–3. CLI tools expose exactly what you
need.

## Surveyed adapters

| Extension | Approach | Token efficiency | Maturity |
|---|---|---|---|
| **`nicobailon/pi-mcp-adapter`** | Single proxy tool (~200 tokens) that discovers and calls MCP tools on-demand | High — proxy avoids upfront registration | Production — 608 stars, 23.7K weekly downloads, 29 versions |
| **`steimbyte/pi-mcp-extension`** | Alternative adapter addressing Zod version conflicts | Same as upstream | Experimental — claims to fix runtime errors nicobailon's has |
| **`mitsuhiko/pi-codemode-mcp`** | JavaScript sandbox approach: `list_mcp_tools` + `call_mcp` | Medium — lists first 20 inline | Experimental — single-author, described as "an experiment" |
| **`spences10/my-pi`** (bundle) | Stdio + HTTP/streamable-HTTP from `mcp.json`, auto-registered as Pi tools | Depends on server count | Early — part of a larger composable setup |

## The proxy pattern — how nicobailon's adapter works

Instead of registering every MCP tool as a separate Pi tool (burning
thousands of tokens), `pi-mcp-adapter` registers **one** proxy tool:

```
mcp_call({server: "filesystem", tool: "read_file", arguments: {...}})
```

The adapter:
1. Reads `mcp.json` (or `claude_desktop_config.json`) to discover servers
2. Starts the server process only when the tool is first called
3. Routes the call and returns the result

This reduces the per-turn token cost from ~10k to ~200, making MCP
viable on context-constrained models.

## When MCP makes sense (and when it doesn't)

| Scenario | MCP | CLI skill |
|---|---|---|
| **Database access** (PostgreSQL, SQLite) | Good — standardized schema introspection | Good — `psql` or `sqlite3` via `bash` tool |
| **Browser automation** | Good — Playwright MCP server is mature | Good — `curl`, `pup`, or custom script |
| **File operations** | Overkill — `read`/`edit`/`bash` builtins suffice | Native — already in Pi |
| **Third-party APIs** (Slack, Notion, GitHub) | Good if an MCP server exists | Good if you prefer simple `curl` wrappers |
| **Custom internal tools** | Poor — you write the server anyway | Good — write a script, call via `bash` |
| **Long-running services** | Poor — each server is a process | Good — stateless scripts |

## CLI skills as the Pi-native alternative

Pi's skill system achieves capability discovery without MCP overhead:

- **Progressive disclosure.** Skills load on-demand; only the active
  skill's tools are in context.
- **No running servers.** Skills are markdown + TypeScript files;
  they run in the same process as the extension.
- **Simpler debugging.** One codebase, one Zod version, one auth
  model.

The tradeoff is interoperability — a Pi skill only works with Pi. An
MCP server works with any MCP client. If you switch agents frequently,
MCP amortizes the setup cost. If you stay in Pi, skills are leaner.

## Picking an MCP adapter

| Goal | Best choice | Why |
|---|---|---|
| **Production MCP on Pi** | **`nicobailon/pi-mcp-adapter`** | Most mature, highest adoption, token-efficient proxy pattern. |
| **Hitting Zod/runtime errors with nicobailon's** | `steimbyte/pi-mcp-extension` | Claims to resolve version conflicts. |
| **Experimenting with sandboxed MCP calls** | `mitsuhiko/pi-codemode-mcp` | JavaScript sandbox approach, `/mcp` management command. |
| **MCP as part of a full composable setup** | `spences10/my-pi` | Bundled with LSP, agent chains, telemetry. |

## See also

- [Web Search Extensions](web-search-extensions.md) — related survey; some search providers expose MCP servers
- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs for vetting adapters
- [Pi Ecosystem Catalogs](../references/catalogs.md) — `pi.dev/packages` indexes `pi-mcp-adapter` under the `mcp` tag
