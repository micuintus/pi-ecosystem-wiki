---
title: Microsoft Teams Integration for Pi
type: synthesis
updated: 2026-08-21
sources:
  - cli-microsoft365
  - atc0005-send2teams
  - yusufaltunbicak-microsoft-teams-cli
  - msgraph-teams-messaging
  - msgraph-chat-post-messages
  - composio-teams-pi
  - msteams-agent-skills
  - nicobailon-pi-mcp-adapter
tags: [teams, microsoft, messaging, integration, mcp]
---

# Microsoft Teams Integration for Pi

## Short answer

There is **no native Microsoft Teams extension for Pi**. Use the
[`m365` CLI](https://github.com/pnp/cli-microsoft365) from `bash`, and add a
skill if you use it often. An MCP route exists via Composio if you need
Graph-wide coverage with managed auth.

This is the mirror image of [Slack](slack-extensions.md), which has five
distinct extension shapes. Teams has none — the ecosystem simply has not been
built, so the answer is CLI or MCP.

## First: `pi-teams` is not Microsoft Teams

Searching npm or GitHub for "pi teams" returns a dozen packages, and **none of
them touch Microsoft Teams**. They are all *agent team* orchestration —
spawning multiple Pi agents that coordinate:

`burggraf/pi-teams`, `@vadimcomanescu/pi-teams`, `josorio7122/pi-teams`,
`gmlemus/pi-teams`, `KristjanPikhof/pi-agents-team`, `nixihz/pi-agent-teams`,
`linys77/pi-agentteam`, `@tmustier/pi-agent-teams`, `@patimweb/pi-team`.

Those belong to the [subagent survey](subagent-extensions.md). The collision is
worth stating plainly because the search results are actively misleading: the
word "teams" in this ecosystem means *agent teams*, not Microsoft's product.

## The CLI route

### `m365` — the substantial one

[`pnp/cli-microsoft365`](https://github.com/pnp/cli-microsoft365) is the
community standard for driving Microsoft 365 from a terminal, and covers Teams
properly:

```bash
m365 teams message send --teamId <id> --channelId <id> --message "build 4711 failed"
m365 teams chat message send --userEmails a@x.com,b@x.com --message "..."
m365 teams chat message send --chatName "Release" --message "..."
```

It authenticates once and covers far more than messaging (teams, channels,
membership, meetings), so it is the right base if Teams is part of a wider M365
workflow. Because it is a real CLI with stable subcommands, wrapping it in a
`SKILL.md` is the natural Pi integration — the same pattern as
[Google Workspace](google-workspace.md) and the Jenkins CLI skill in
[Jenkins and CI](jenkins-and-ci-integration.md). No such Teams skill is
published yet; writing one is a small job.

### Smaller, single-purpose options

- [`atc0005/send2teams`](https://github.com/atc0005/send2teams) — a tiny Go
  binary that posts to a channel webhook. Built for Nagios-style pass/fail
  notifications. If all you want is "tell a channel the build broke," this is
  the whole solution, and it needs no Azure app registration.
- [`yusufaltunbicak/microsoft-teams-cli`](https://github.com/yusufaltunbicak/microsoft-teams-cli)
  — chat and send from the terminal with **no Azure app registration, admin
  consent or API keys**, by extracting an MSAL token via Playwright. That is
  also the caveat: it drives a browser session, it is unofficial and
  unaffiliated with Microsoft, and it is likely to violate corporate policy.
  Read it before running it anywhere managed.
- **PowerShell** — `New-MgTeamChannelMessage` from the Microsoft Graph module,
  if the machine is already PowerShell-shaped.

### Raw Graph

`POST /teams/{id}/channels/{id}/messages` and
`POST /chats/{id}/messages` are one `curl` each once you hold a token, e.g.
from `az account get-access-token` with `ChannelMessage.Send`. Reasonable for
CI glue; a poor default for an agent, for the same reason raw `curl` is a poor
default against Jenkins — the model re-derives the call every time.

## The MCP route

[Composio publishes a Microsoft Teams toolkit with a documented Pi
integration](https://composio.dev/toolkits/microsoft_teams/framework/pi-agent),
which handles OAuth for you. As with every MCP route in Pi, remember that
**Pi has no core MCP client** — you also need an adapter extension (see
[MCP integration](mcp-integration.md)), so it is two moving parts. Worth it if
you want broad Teams/Graph coverage without minting tokens yourself; overkill
if you only need to post messages.

## Auth, briefly

Teams is Entra ID / Graph, so the awkward part is never the API call:

| Route | Registration needed | Good for |
|---|---|---|
| Incoming webhook (`send2teams`) | none — a channel URL | one-way notifications |
| `m365` CLI | uses its own multi-tenant app; admin consent may be required | general use |
| Graph + `az` token | existing Azure app / service principal | CI pipelines |
| Composio MCP | none by you — Composio holds the OAuth app | quick start, if a third-party broker is acceptable |
| MSAL-via-Playwright | none | personal machines only; policy risk |

The practical blocker in most companies is **admin consent**, not code. Check
what your tenant permits before choosing.

## A note on Microsoft's own "agent skills"

Microsoft publishes a `teams-dev` agent skill for Claude Code, Cursor and
Copilot. It is for **building Teams bots and apps** — Teams SDK scaffolding and
API context — not for sending messages from your agent. Useful if you are
developing a Teams app; irrelevant if you want your coding agent to post to a
channel.

## Picking guide

| Goal | Do this |
|---|---|
| Notify a channel when something finishes | `send2teams` with an incoming webhook |
| Post to channels and chats regularly | `m365` from `bash`; add a `SKILL.md` |
| Teams plus wider M365 (calendar, membership, meetings) | `m365`, same route |
| Broad Graph coverage, managed OAuth | Composio MCP + Pi MCP adapter |
| CI pipeline posting | Graph + service-principal token |
| Personal machine, no tenant permissions | `microsoft-teams-cli` — check policy first |

## Caveats

- **No Pi extension exists.** If one appears, expect the name to be taken by
  agent-team packages; look for `msteams` rather than `teams`.
- **Webhooks are one-way.** Anything conversational needs Graph and real auth.
- **`microsoft-teams-cli` is unofficial** and browser-token-based. Convenient,
  and the kind of thing that ends a security review badly.
- **Nothing here is Teams-side automation.** Reacting to Teams messages needs a
  bot registration and a public endpoint — a different project from letting
  Pi send a message.

## See also

- [Slack Extensions](slack-extensions.md) — the same problem where the
  ecosystem *did* get built; five shapes, useful as a template for what a Teams
  extension would look like
- [MCP Integration](mcp-integration.md) — why the MCP route costs two
  components in Pi
- [Google Workspace](google-workspace.md) — the CLI-plus-skill pattern this
  page recommends, already worked out
- [Subagent Extensions](subagent-extensions.md) — where every `pi-teams`
  package actually belongs
