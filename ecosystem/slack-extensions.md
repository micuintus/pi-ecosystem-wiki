---
title: Pi Slack Extensions
type: ecosystem
updated: 2026-10-14
sources:
  - salesforce-sf-slack
  - dreki-gg-pi-slack
  - gugu91-slack-bridge
  - pinet-slack-bridge-npm
  - tintinweb-pi-messenger-bridge
  - e9n-pi-channels
  - mariozechner-pi-mom
  - pi-mom-npm
  - samfoy-pi-slack-bot
  - daniel-silva-perez-pi-slack-agents
  - slack-mcp-docs
  - korotovsky-slack-mcp-server
  - artale-pi-notify
  - merlinbr-pi-agent-notify
  - nicobailon-pi-mcp-adapter
tags: [slack, integration, messaging, mcp, notifications]
entries:
  - id: sf-slack
    name: sf-slack
    repo: salesforce/sf-pi
    role: agent-tools-readwrite
    notes: "Most complete in-pi tool set (10 tools): search/history/threads, resolve, research, channels, users, files, canvases r/w, send + schedule. User-token (xoxp) only; OAuth or paste via /sf-slack panel; runtime scope probing + dynamic tool gating; HITL confirm on all writes"
  - id: dreki-pi-slack
    name: "@dreki-gg/pi-slack"
    repo: dreki-gg/pi-extensions
    npm: "@dreki-gg/pi-slack"
    role: agent-tools-readwrite
    notes: "8 tools (read + post/edit/delete own messages, file download). Bot token (xoxb) for reads, user token (xoxp) only for search. Effect-based client; bot must be invited to channels. Broken on Pi 1.2: past-chats `extractReferenceTokens(event.prompt)` reaches `text.matchAll` on an undefined prompt; the rest of the bundle is unaffected"
  - id: pinet-slack-bridge
    name: "@pinet/slack-bridge"
    repo: gugu91/extensions
    npm: "@pinet/slack-bridge"
    role: assistant-mesh
    notes: "Slack-assistant app on Socket Mode: slack_inbox/send/react/read/upload/schedule + dispatcher + canvases. Broker/follower Pinet mesh for multi-agent coordination over Slack; manifest deploy tooling; optional mesh-secret auth"
  - id: pi-messenger-bridge
    name: pi-messenger-bridge
    repo: tintinweb/pi-messenger-bridge
    npm: pi-messenger-bridge
    role: messenger-bridge
    notes: "Bridges Slack/Telegram/WhatsApp/Discord/Matrix into pi. Slack via Socket Mode (xoxb+xapp). Challenge-based 6-digit auth, trusted-user model; pi-native sendUserMessage()+turn_end"
  - id: e9n-pi-channels
    name: "@e9n/pi-channels"
    repo: espennilsen/pi
    npm: "@e9n/pi-channels"
    role: messenger-bridge
    notes: "Two-way channel extension; Slack adapter (Socket Mode + Web API) plus Telegram/webhook/custom. Incoming messages routed as prompts; notify tool sends out. Persistent (RPC) or stateless"
  - id: pi-mom
    name: "@mariozechner/pi-mom"
    repo: badlogic/pi-mono
    npm: "@mariozechner/pi-mom"
    role: standalone-bot
    notes: "First-party self-managing Slack bot (packages/mom) powered by pi: runs bash, writes its own skills/tools, manages credentials, per-channel sandboxes. REMOVED from the earendil-works fork; lives in badlogic/pi-mono upstream"
  - id: samfoy-pi-slack-bot
    name: pi-slack-bot
    repo: samfoy/pi-slack-bot
    role: standalone-bot
    notes: "DM-based bot exposing pi as a coding agent. Per-thread sessions, streaming, model/thinking/cwd switching, file/diff pickers, !commands, WebSocket attach server. Socket Mode, locked to one SLACK_USER_ID. git clone, not a pi package"
  - id: pi-slack-agents
    name: pi-slack-agents
    repo: daniel-silva-perez/pi-slack-agents
    role: standalone-bot
    notes: "Multi-agent system: pi --rpc per agent, Redis mailbox pattern, call_agent tool, Socket Mode. git clone"
  - id: slack-mcp-server
    name: slack-mcp-server
    repo: korotovsky/slack-mcp-server
    role: mcp-server
    notes: "Generic Slack MCP server (xoxp/xoxb) usable from pi via pi-mcp-adapter. Official @slack/mcp-server also exists. The 'if an MCP server exists' path"
  - id: artale-pi-notify
    name: "@artale/pi-notify"
    repo: arosstale/pi-notify
    npm: "@artale/pi-notify"
    role: notification-out
    notes: "Output-only: desktop toasts + Slack/Discord webhooks, notification history"
  - id: merlinbr-pi-agent-notify
    name: pi-agent-notify
    repo: merlinbr/pi-agent-notify
    role: notification-out
    notes: "Output-only attention/done alerts. Discord webhooks shipping; Slack listed as planned"
---

# Pi Slack Extensions

Connecting Pi and Slack splits into five shapes that solve genuinely
different problems — from "let the agent read/post in Slack" to "run Pi as
a Slack bot." Pick by **direction of control**: do you want Pi to *use*
Slack (tools), Slack to *drive* Pi (bridge/bot), or just to be *pinged*
(notifications).

## Short answer

- **Agent reads/searches Slack and posts with a confirmation step** —
  [`sf-slack`](https://github.com/salesforce/sf-pi/tree/main/extensions/sf-slack)
  is the most complete (10 tools, user-token, scope-gated, human-in-the-loop
  on every write). For a lighter npm-installable read tool with optional
  posting, use
  [`@dreki-gg/pi-slack`](https://github.com/dreki-gg/pi-extensions/tree/main/packages/slack).
- **Drive your Pi from your phone via Slack** — a messenger bridge:
  [`pi-messenger-bridge`](https://github.com/tintinweb/pi-messenger-bridge)
  (also Telegram/WhatsApp/Discord/Matrix) or
  [`@e9n/pi-channels`](https://github.com/espennilsen/pi/tree/main/extensions/pi-channels).
- **A persistent Slack bot that *is* a Pi agent** —
  [`@mariozechner/pi-mom`](https://registry.npmjs.org/@mariozechner/pi-mom)
  (first-party, self-managing) or
  [`samfoy/pi-slack-bot`](https://github.com/samfoy/pi-slack-bot).
- **Many Pi agents coordinating through Slack** —
  [`@pinet/slack-bridge`](https://www.npmjs.com/package/@gugu910/pi-slack-bridge)
  (broker/follower mesh).
- **Already on MCP** — point [`pi-mcp-adapter`](../ecosystem/mcp-integration.md)
  at a [Slack MCP server](https://docs.slack.dev/ai/slack-mcp-server).
- **Just ping me when a task finishes** —
  [`@artale/pi-notify`](https://github.com/arosstale/pi-notify) (webhooks).

## Contents

- [The five shapes](#the-five-shapes)
- [Shape A — In-pi Slack tool extensions](#shape-a--in-pi-slack-tool-extensions)
- [Shape B — Messenger bridges](#shape-b--messenger-bridges)
- [Shape C — Standalone bots that expose Pi](#shape-c--standalone-bots-that-expose-pi)
- [Shape D — Generic MCP route](#shape-d--generic-mcp-route)
- [Shape E — Notifications to Slack](#shape-e--notifications-to-slack)
- [Auth model cheat-sheet](#auth-model-cheat-sheet)
- [Comparison](#comparison)
- [Picking a Slack integration](#picking-a-slack-integration)
- [See also](#see-also)

## The five shapes

| Shape | Direction | What it is | Examples |
|---|---|---|---|
| **A — Agent tools** | Pi → Slack | LLM-callable tools to read/search/post | `sf-slack`, `@dreki-gg/pi-slack`, `@pinet/slack-bridge` |
| **B — Messenger bridge** | Slack → Pi | Remote users prompt Pi from a chat app | `pi-messenger-bridge`, `@e9n/pi-channels` |
| **C — Standalone bot** | Slack → Pi | A long-running bot process that *is* a Pi agent | `pi-mom`, `samfoy/pi-slack-bot`, `pi-slack-agents` |
| **D — MCP** | Pi → Slack | Generic Slack MCP server behind `pi-mcp-adapter` | `@slack/mcp-server`, `korotovsky/slack-mcp-server` |
| **E — Notification** | Pi → Slack | Fire-and-forget alerts, no read-back | `@artale/pi-notify`, `pi-agent-notify` |

Shapes A and D both give the agent Slack *tools*; the difference is
whether the integration is a native Pi extension (A) or a generic MCP
server wired in through an adapter (D). Shapes B and C both let Slack
drive Pi; the difference is whether Pi stays your normal interactive
session with a bridge layered on (B) or runs headless as a dedicated
bot process (C).

## Shape A — In-pi Slack tool extensions

The agent gets LLM-callable tools and Slack appears in the system prompt.

### `sf-slack` (salesforce/sf-pi)

The most complete Slack tool surface in the ecosystem. It registers **10
tools** — `slack` (search / thread / history / permalink), `slack_resolve`
(fuzzy channel/user resolution), `slack_research` (agentic strict-to-broad
search), `slack_channel`, `slack_user`, `slack_file`, `slack_canvas`
(read + write), `slack_send`, `slack_schedule`, and `slack_time_range`
(deterministic date-range normalization) — plus an auth provider and a
`/sf-slack` status/connect command.

Distinctive engineering:

- **User-token only** (`xoxp-`). OAuth v2 (`user_scope`) or paste a token
  into the `/sf-slack` panel, which writes to Pi's central auth store.
- **Runtime scope probing** — on `session_start` it calls `auth.test`,
  reads the `X-OAuth-Scopes` response header, and **dynamically gates**
  tools whose scopes the workspace did not grant, keeping the system
  prompt clean. A partial grant degrades gracefully instead of failing.
- **Human-in-the-loop writes** — `slack_send` and `slack_schedule` confirm
  via `ctx.ui.confirm()` in interactive mode and **refuse** in headless
  modes (`pi -p`, RPC) unless `SLACK_ALLOW_HEADLESS_SEND=1`. `@channel`/
  `@here`/`@everyone` pings flip the confirm default to Cancel; every send
  (including dry-runs and cancellations) is appended to a session audit
  trail viewable with `/sf-slack sent`.
- All tools are read-only except canvas create/edit, `slack_send`, and
  `slack_schedule`.

Part of the `salesforce/sf-pi` extension repo (not separately on npm).

### `@dreki-gg/pi-slack`

A focused, npm-installable Slack tool set: `slack_list_channels`,
`slack_read_messages`, `slack_read_thread`, `slack_search`,
`slack_download_file`, `slack_post_message`, `slack_edit_message`,
`slack_delete_message`. Reads use a **bot token** (`xoxb-`); only
`slack_search` needs a **user token** (`xoxp-`, `search:read`), because
Slack's `search.messages` is user-token-only. Built on
[Effect](https://effect.website) for typed errors, retries, and rate-limit
handling. The bot must be `/invite`d to each channel or reads return
`not_in_channel`; a `.pi/slack.json` sets a default channel and message
limit. `/slack` shows token/config status.

Install: `pi install @dreki-gg/pi-slack`.

### `@pinet/slack-bridge` (gugu91/extensions)

More than a tool set — a Slack **assistant app** plus a multi-agent
**Pinet mesh**. Tools include `slack_inbox` (hot-path drain of pending
messages), `slack_send`, `slack_react`, `slack_read`, `slack_upload`,
`slack_schedule`, a `slack` dispatcher for non-hot actions, and canvases.
On Socket Mode, it runs a **broker/follower** architecture: a broker agent
watches Slack, routes work to worker agents in isolated git worktrees,
nudges stalled threads, and tracks ownership, with scheduled wake-ups,
a checked-in Slack App Manifest (`pnpm deploy:slack`), and optional
shared-secret mesh auth. This is the heavyweight "agents coordinating
through Slack" option.

Install: `pi install npm:@pinet/slack-bridge`.

## Shape B — Messenger bridges

Slack (and friends) become a remote front-end for your normal Pi session.

### `pi-messenger-bridge` (tintinweb)

Bridges **Slack, Telegram, WhatsApp, Discord, and Matrix** into Pi so
remote users can prompt your agent from a chat app. Slack uses Socket Mode
(`xoxb-` bot token + `xapp-` app token). New users authenticate with a
**6-digit challenge code** shown in your Pi terminal; trusted/admin users
are managed via DM commands. Per-channel enable modes (`all` /`mentions` /
`trusted-only`), a `/msg-bridge` menu, and a single-instance lock guard
against duplicate polling when sub-agents spawn. Built on Pi's native
`sendUserMessage()` + `turn_end` rather than a tool-loop hack.

Install: `pi install npm:pi-messenger-bridge`.

### `@e9n/pi-channels` (espennilsen/pi)

A two-way channel extension with a **Slack adapter** (Socket Mode + Web
API) alongside Telegram, webhook, and custom adapters. Incoming messages
are routed to the agent as prompts; the agent replies through the `notify`
tool (`send`, `send_file`, `list`, `test`). The chat bridge runs in
**persistent** (RPC subprocess with memory) or **stateless** (isolated
per message) mode, with per-sender rules, idle timeout, and a concurrency
cap. An event-bus API (`channel:send` / `channel:receive` /
`channel:register`) lets other extensions message through it.

Install: `pi install npm:@e9n/pi-channels`.

## Shape C — Standalone bots that expose Pi

A dedicated long-running process; Pi runs headless behind the bot.

### `@mariozechner/pi-mom` (badlogic/pi-mono `packages/mom`)

"Mom (Master Of Mischief)" — a **self-managing** Slack bot powered by the
Pi coding agent. She runs bash, reads/writes files, and installs her own
tools, writes her own CLI "skills," and configures credentials
autonomously, maintaining a separate sandbox/working dir per channel.
First-party (Mario Zechner's monorepo) and published as
`@mariozechner/pi-mom` (`npm install -g @mariozechner/pi-mom`).

> **Fork note:** `packages/mom` was **removed from the earendil-works
> fork** (`earendil-works/pi-mono`); it lives only in the upstream
> `badlogic/pi-mono`. The published npm package tracks upstream.

### `samfoy/pi-slack-bot`

A Slack bot that exposes Pi as a conversational coding agent in **DMs**.
Each Slack thread maps to its own Pi `AgentSession` with full history;
responses stream with tool indicators and auto-split for length. Project
picker (fuzzy match or buttons), interactive file picker, and `!commands`
(`!model`, `!thinking`, `!cwd`, `!new`, `!sessions`, `!plan`, `!prompt`,
…); unrecognized `!command`s forward to Pi as `/command`. Socket Mode
(`xoxb-` + `xapp-`), locked to a single `SLACK_USER_ID`. A WebSocket
attach server lets external processes stream into threads. Run via
`git clone` + `npm start` (systemd notes included) — not a pi package.

### `daniel-silva-perez/pi-slack-agents`

A multi-agent system: a Node controller on Slack Socket Mode spawns
`pi --rpc` agents, each isolated in its own process, communicating via a
**Redis mailbox** pattern. A `call_agent` Pi extension lets agents message
one another with correlation/reply and timeout. Configurable agent roster
(e.g. `researcher`, `coder`) with per-agent system prompts and tools.
`git clone` + `npm run dev`.

## Shape D — Generic MCP route

Any Slack MCP server can be wired into Pi through
[`pi-mcp-adapter`](../ecosystem/mcp-integration.md) by adding it to
`mcpServers`. Options include Slack's **official `@slack/mcp-server`** and
community servers such as `korotovsky/slack-mcp-server` (`xoxp`/`xoxb`),
`karbassi/slack-mcp`, and `mmorency2021/slack-mcp`. This is the path the
[MCP Integration](../ecosystem/mcp-integration.md) page alludes to when it
lists "third-party APIs (Slack, …) — good if an MCP server exists." Prefer
a native Shape-A extension when one fits: it gives tighter scope gating,
HITL confirmation, and a smaller prompt surface than a generic MCP server
exposing every Slack verb.

## Shape E — Notifications to Slack

Output-only: Pi pings a Slack channel on attention/completion, with no
read-back.

- **`@artale/pi-notify`** — cross-platform desktop toasts plus
  **Slack/Discord webhooks** and notification history.
- **`merlinbr/pi-agent-notify`** — attention/blocked/done alerts; Discord
  webhooks ship today, **Slack is listed as planned**.
- `@e9n/pi-channels`' webhook adapter can also POST to a Slack incoming
  webhook if you only need outbound.

For the broader notification landscape (desktop/sound/voice, background
notify), these overlap with general notification extensions tracked in the
catalogs; this page covers only the Slack-relevant subset.

## Auth model cheat-sheet

Slack token types decide what each integration can do:

| Token | Prefix | Who acts | Needed for |
|---|---|---|---|
| Bot token | `xoxb-` | the app/bot | reading channels the bot is in, posting as the bot |
| User token | `xoxp-` | you | `search.messages`, acting as yourself, canvases |
| App-level token | `xapp-` | the app | **Socket Mode** (event stream, no public webhook) |

- **Tool extensions** lean on bot or user tokens. `sf-slack` is
  user-token-only (search + act-as-you); `@dreki-gg/pi-slack` uses a bot
  token for reads and a user token only for search.
- **Bridges and bots** need Socket Mode, so they require an `xapp-` token
  **plus** an `xoxb-` bot token.
- Slack scopes are **additive** — re-running OAuth adds scopes; to remove
  scopes you revoke and re-authorize.

## Comparison

| Extension | Shape | In-pi? | Read | Write | Auth | Install |
|---|---|---|---|---|---|---|
| `sf-slack` | A tools | yes | yes (search/history/canvas/files) | yes, HITL | `xoxp` (OAuth/paste) | part of sf-pi |
| `@dreki-gg/pi-slack` | A tools | yes | yes | post/edit/delete own | `xoxb` (+`xoxp` for search) | `pi install @dreki-gg/pi-slack` |
| `@pinet/slack-bridge` | A tools + mesh | yes | yes | yes | Socket Mode (`xoxb`+`xapp`) | `pi install npm:@pinet/slack-bridge` |
| `pi-messenger-bridge` | B bridge | yes (ext) | n/a (prompts in) | replies out | Socket Mode (`xoxb`+`xapp`) | `pi install npm:pi-messenger-bridge` |
| `@e9n/pi-channels` | B bridge | yes (ext) | n/a (prompts in) | replies out | Socket Mode (`xoxb`+`xapp`) | `pi install npm:@e9n/pi-channels` |
| `@mariozechner/pi-mom` | C bot | no (process) | n/a | acts in channel | Socket Mode | `npm i -g @mariozechner/pi-mom` |
| `samfoy/pi-slack-bot` | C bot | no (process) | n/a | DM replies | Socket Mode + single user | git clone |
| `pi-slack-agents` | C bot | no (process) | n/a | replies | Socket Mode + Redis | git clone |
| Slack MCP server | D mcp | via adapter | yes | depends on server | `xoxp`/`xoxb` | `pi-mcp-adapter` + `mcpServers` |
| `@artale/pi-notify` | E notify | yes (ext) | no | webhook out | incoming webhook | npm |
| `pi-agent-notify` | E notify | yes (ext) | no | webhook (Slack planned) | webhook | git |

> Live signals (stars, downloads, last-push, maintenance) are intentionally
> not inlined here; query them at read-time with the recipes in
> [`references/evaluation.md`](../references/evaluation.md).

## Picking a Slack integration

| If you want… | Use | Why |
|---|---|---|
| The agent to search/read Slack and post safely | **`sf-slack`** | 10 tools, scope-gated, HITL on every write, audit trail |
| A lightweight read tool, npm-simple, optional posting | **`@dreki-gg/pi-slack`** | bot-token reads, Effect client, small surface |
| Many Pi agents coordinating through Slack | **`@pinet/slack-bridge`** | broker/follower mesh, inbox, manifest deploy |
| To drive Pi from your phone (Slack + others) | **`pi-messenger-bridge`** | multi-messenger, challenge auth, pi-native |
| A multi-adapter two-way channel inside your session | **`@e9n/pi-channels`** | Slack/Telegram/webhook adapters, RPC or stateless |
| A persistent self-managing Slack bot | **`@mariozechner/pi-mom`** | first-party, builds its own tools |
| A DM coding-agent bot for one user | **`samfoy/pi-slack-bot`** | per-thread sessions, streaming, pickers |
| To standardize on MCP across tools | **Slack MCP server** + `pi-mcp-adapter` | reuse one server across MCP clients |
| Only a ping when Pi finishes/needs you | **`@artale/pi-notify`** | webhook out, no read scopes |

## See also

- [MCP Integration](mcp-integration.md) — wiring a Slack MCP server via `pi-mcp-adapter`
- [Provider Extensions](provider-extensions.md) — auth-store and OAuth patterns Slack extensions reuse
- [How to Evaluate a Pi Extension](../references/evaluation.md) — live vital signs and code-quality recipes
- [Pi Ecosystem Catalogs and Awesome-Lists](../references/catalogs.md) — where to find newer entries
