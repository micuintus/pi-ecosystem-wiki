---
title: pi-claude-bridge — Claude Code as Pi provider + sub-agent
type: ecosystem
updated: 2026-05-25
sources:
  - pi-claude-bridge
  - claude-agent-sdk-pi
  - anthropic-claude-agent-sdk
  - anthropic-third-party-end
  - pi-discussion-2950
tags: [extension, claude-agent-sdk, claude-code, subscription, askclaude]
---

# pi-claude-bridge

`pi-claude-bridge` (Eli Dickinson, `npm:pi-claude-bridge`) is a Pi
extension that runs Anthropic's **Claude Code** binary as a subprocess
via `@anthropic-ai/claude-agent-sdk`, bridging Pi's tools and skills
into the CC session and exposing CC back to Pi in two roles:

1. **Provider** — `claude-bridge/<model>` registers as a normal Pi
   provider; pick it via `/model`. Pi's TUI is unchanged.
2. **AskClaude tool** — when running under any *other* provider, Pi's
   LLM can delegate a sub-task to Claude Code as a child agent.

It is a downstream of [claude-agent-sdk-pi](claude-agent-sdk-pi.md):
the provider skeleton, tool-name mapping, and settings loading
originate there. This fork adds streaming, MCP tool bridging,
session resume/persistence, context sync, thinking support, skills
forwarding, and the AskClaude tool.

## Why it exists

To use your **Claude Max/Pro subscription** as an LLM source inside
Pi without forking Pi or reverse-engineering the OAuth flow.

The mechanism is structural rather than evasive: Anthropic's
third-party detector pattern-matches Claude Code's system prompt
content (see
[Anthropic Subscription Auth](anthropic-subscription-auth.md#detection-mechanism)).
Because pi-claude-bridge launches the **real Claude Code binary** —
not a custom client talking to `api.anthropic.com` — Anthropic sees
Claude Code, and subscription routing applies. The author's own
framing: *"only the real Claude Code is touching the API and it's to
enable local development, not to steal API calls."*

This is the same structural trick `oh-my-pi` uses, but as an
**extension** rather than a fork.

## Architecture at a glance

```
pi TUI                                   ┌─────────────┐
   │  (Pi keeps its tools, theme,         │   Claude    │
   │   skills, AGENTS.md, footer)         │   Code      │
   │                                      │  (subproc)  │
   ▼                                      └──────┬──────┘
pi provider: claude-bridge ───►  Agent SDK query ─┤
                                                  ▼
Pi tools ────► registered as MCP ────► CC sees them as MCP tools
Pi skills ───► extracted from system prompt ──► appended to CC system prompt
AGENTS.md ──► path-rewritten (.pi → .claude) ──► appended to CC system prompt
                                                  │
                          tool_use ◄──────────────┘
                          │
                          ▼
                      Pi executes the tool, returns result
                                                  │
                                                  ▼
                                       CC continues / yields text
```

Pi remains the execution host. CC is reduced to "the brain that picks
the next tool call" — its native Read/Write/Edit/Bash are intentionally
not invoked because Pi's equivalents are bridged in over MCP and CC
is launched with `tools: []`.

## Two modes

### Provider mode

`/model` → `claude-bridge/claude-opus-4-7`, `claude-opus-4-6`,
`claude-sonnet-4-6`, `claude-haiku-4-5`.

- Pi's tools are bridged into CC as MCP tools; `tools: []` is passed
  to the SDK so no default CC tools leak in.
- Pi's skills block and AGENTS.md are appended to CC's system prompt
  (toggleable via `provider.appendSystemPrompt: false`).
- Bash gets a forced 120-second timeout to match CC's default, since
  Pi's bash has no default timeout.
- `DISABLE_AUTO_COMPACT=1` is set on the CC subprocess — Pi owns
  context management and propagates its own `/compact` event into the
  bridge; letting CC autocompact too would race Pi's threshold and
  trip CC's anti-thrashing guard (issue #8).
- `--strict-mcp-config` is set unconditionally to suppress MCP
  servers from `~/.claude.json` / `.mcp.json`. Claude.ai cloud MCP
  (Gmail/Drive/Figma/Canva via OAuth) is always blocked via
  `ENABLE_CLAUDEAI_MCP_SERVERS=0`.

### AskClaude mode

When the active provider is *not* `claude-bridge`, the extension
registers an `AskClaude` Pi tool. Pi's LLM can call it to delegate.
Parameters:

- `prompt` — task or question
- `mode` — `read` (default), `none`, `full` (`full` lockable via
  `askClaude.allowFullMode: false`)
- `model` — `opus` / `sonnet` / `haiku` / full ID
- `thinking` — `off` / `minimal` / `low` / `medium` / `high` / `xhigh`
- `isolated` — `true` for a clean CC session with no Pi conversation
  history

Tool blocklists per mode (from `src/index.ts:146-163`):

| Mode | Blocked CC tools |
|---|---|
| `full` | `AskUserQuestion`, `EnterPlanMode`/`ExitPlanMode`, `ToolSearch`, `ScheduleWakeup` |
| `read` | above + `Write`, `Edit`, `Bash`, `NotebookEdit`, worktree/cron/team mutations |
| `none` | above + `Read`, `Glob`, `Grep`, `Agent`, `WebFetch`, `WebSearch` |

`mode: "none"` reduces CC to a pure reasoning call.

## Configuration

`~/.pi/agent/claude-bridge.json` (global) or
`.pi/claude-bridge.json` (project; merged over global):

```json
{
  "askClaude": {
    "enabled": true,
    "allowFullMode": true,
    "defaultIsolated": false,
    "appendSkills": true
  },
  "provider": {
    "appendSystemPrompt": true,
    "settingSources": ["user", "project"],
    "strictMcpConfig": true,
    "pathToClaudeCodeExecutable": "/home/you/.nix-profile/bin/claude"
  }
}
```

`pathToClaudeCodeExecutable` is required on **NixOS** and other
non-FHS distros where the SDK's bundled musl/glibc `claude` binary
can't run; point it at a Nix-installed CC.

## What you can and cannot shut off

A natural question for users who want the subscription budget but
**not** Claude Code's memory, AGENTS.md handling, or tool catalog:

| Surface | Off-switch | Effect |
|---|---|---|
| Pi tools bridged into CC | Always: `tools: []` is passed | No Pi tools leaked as CC-native; only Pi-MCP path |
| CC native tools (Read/Write/Edit/Bash/...) in provider mode | **None exposed** | The `claude_code` SDK preset still describes them in the system prompt. Pi's MCP tools are what actually executes; the preset descriptions remain token overhead and behavior anchors. |
| CC `CLAUDE.md` memory (user + project) | `provider.settingSources: []` (with `appendSystemPrompt: false`) | Memory load suppressed |
| Pi `AGENTS.md` + skills append | `provider.appendSystemPrompt: false` | Pi-side context not forwarded |
| Filesystem MCP from `~/.claude.json` / `.mcp.json` | `provider.strictMcpConfig: true` (default) | Suppressed |
| Claude.ai cloud MCP (Gmail/Drive/Figma/Canva) | Always blocked | `ENABLE_CLAUDEAI_MCP_SERVERS=0` set on subprocess env |
| CC autocompact thrashing | Always: `DISABLE_AUTO_COMPACT=1` | Manual `/compact` in CC still works; Pi drives autocompact |
| CC tool surface in AskClaude path | `mode` parameter (`read`/`none`/`full`) | Per-mode `disallowedTools` enforced |
| `systemPrompt.preset: "claude_code"` itself | **Not exposed** | No config to swap to a blank/custom system prompt in provider mode. Feature-request territory. |

So a "pure subscription LLM, no Claude-Code-side memory or settings"
configuration looks like:

```json
{
  "provider": {
    "appendSystemPrompt": false,
    "settingSources": [],
    "strictMcpConfig": true
  }
}
```

That kills Pi's append, CC's memory load, and filesystem MCP. The
`claude_code` preset still loads — there is no first-class way to
strip CC's personality and native-tool descriptions from the system
prompt while still using the SDK.

## Relationship to other routes

| Route | Hits main subscription budget? | Pi-native UX? |
|---|---|---|
| Pi `/login` → Anthropic OAuth | No — extra-usage bundle only (post-April-2026) | Yes |
| `ANTHROPIC_API_KEY` | No — pay-as-you-go | Yes |
| `oh-my-pi` fork (CC SDK wrapping) | Yes (structural) | Yes — but you're on a fork |
| **`pi-claude-bridge` extension** | **Yes (structural)** | **Yes — base Pi + extension** |
| Foundry env vars | Enterprise budget | Yes |

`pi-claude-bridge` is the "extension-level" answer to the question
[discussion #2950](https://github.com/earendil-works/pi-mono/discussions/2950)
asks: *can you get CC-SDK-wrapped subscription access without
forking?* Yes, at the cost of running CC as a subprocess.

## Picking between `claude-agent-sdk-pi` and `pi-claude-bridge`

For subscription-route use specifically (Claude Max/Pro budget inside
Pi), both extensions reach the same billing bucket via the same
structural mechanism — they launch the real `claude` binary through
`@anthropic-ai/claude-agent-sdk`, so Anthropic's prompt-content
detector sees Claude Code. The billing outcome is identical. The
difference is what surrounds that core call.

| Capability | `claude-agent-sdk-pi` (upstream) | `pi-claude-bridge` (fork) |
|---|---|---|
| Streaming responses | basic | yes, with partial-message support |
| Pi tools → CC via MCP | partial | full bridging with ID-based tool-result matching |
| Session resume / persistence | no | yes (cc-session-io; sessionId preserved across provider switches) |
| Opus 4.7 thinking (`--thinking-display=summarized`) | needs PR #10 | shipped since 0.3.1 |
| Pi `/compact` propagation | no | subscribes to `session_compact` + `session_tree` events |
| CC autocompact thrashing fix (issue #8) | no | `DISABLE_AUTO_COMPACT=1` + REBUILD path |
| MCP isolation (`--strict-mcp-config` + cloud MCP off) | partial | unconditional |
| AskClaude sub-agent tool | no | yes (gateable via `askClaude.enabled`) |
| AGENTS.md + skills forwarding | no | yes, with `.pi` → `.claude` path rewriting |
| NixOS support | no explicit knob | `pathToClaudeCodeExecutable` |
| Release cadence | sporadic; npm/master skew known | active (0.4.0 on 2026-05-04) |

**Recommendation: `pi-claude-bridge`** for day-to-day subscription
use. The pieces missing upstream (session persistence, compact
handling, thinking-display fix, MCP isolation) will bite within a few
turns of real work. Pick the upstream only if you want the smaller
dependency surface, are willing to lose session resume, or are
contributing patches at that layer.

### Token cost

Both pay the same fixed cost of the `claude_code` SDK preset (CC's
personality + native-tool descriptions in the system prompt). On top
of that floor, pi-claude-bridge wastes meaningfully fewer tokens —
and the dominant reason is structural, not incremental.

#### The structural difference: tool declaration strategy

`claude-agent-sdk-pi` (upstream) declares CC's native tools to the
model and then refuses execution at runtime. From `index.ts:32, 682,
966-971`:

```ts
const DEFAULT_TOOLS = ["Read", "Write", "Edit", "Bash", "Grep", "Glob"];
// ...
tools: sdkTools,          // = DEFAULT_TOOLS when context.tools is empty
canUseTool: async () => ({ behavior: "deny",
  message: "Tool execution is unavailable in this environment." }),
```

CC's model is *told* it has `Read`/`Write`/`Edit`/`Bash`/`Grep`/`Glob`
available. Their full tool schemas land in the system prompt. When
the model picks one — which it will, given CC is trained to prefer
its native tools — the SDK denies at runtime and feeds back a denial
string as the tool result. The model re-plans with the denial in
context and tries again.

`pi-claude-bridge` (`src/index.ts:1010`):

```ts
tools: [],
```

CC's tool list contains only Pi's MCP-bridged tools. The native
schemas are never declared, so the model routes directly to Pi's
tools without a denial loop.

#### Per-turn cost example

User says *"read `foo.ts` and tell me what it does."* Pi has its own
`read` tool registered.

**Upstream:**
1. CC sees `Read` (native) **and** `mcp__custom-tools__read` (Pi-bridged) declared.
2. Model picks `Read` (training bias toward native).
3. SDK denies → "Tool execution is unavailable" returned as `tool_result`.
4. Model now has the denial in context, re-plans, picks `mcp__custom-tools__read`.
5. Pi executes; model answers.

Two model turns instead of one, plus both tool schemas in the prompt,
plus the denial echoed back in context.

**pi-claude-bridge:**
1. CC sees only `mcp__custom-tools__read`.
2. Model picks it; Pi executes; model answers.

One turn. No denial loop. No CC-native schema overhead.

#### Cumulative drivers

| Surface | Upstream | pi-claude-bridge | Per-turn impact |
|---|---|---|---|
| CC native tool schemas in prompt | `tools: sdkTools` (6 builtins by default) | `tools: []` | Saves the schema text + eliminates denial loops |
| Denied tool calls re-fed as `tool_result` | Yes — `canUseTool: deny` returns denial message | N/A | Saves 1–N extra model turns per user turn |
| `--strict-mcp-config` | Default `!appendSystemPrompt` → **OFF** when `appendSystemPrompt: true` (the default) | Always ON | Without it, `~/.claude.json` + `.mcp.json` MCP server descriptions land in the prompt |
| Claude.ai cloud MCP (Gmail/Drive/Figma/Canva) | Not suppressed | `ENABLE_CLAUDEAI_MCP_SERVERS=0` always set | Large tool catalogs leak in if user has ever logged into claude.ai |
| `CLAUDE.md` memory load | Default `settingSources` loads `user` + `project` | Suppressible via `settingSources: []` | Saves the full CLAUDE.md text per turn |
| Session resume across turns | **None** — no resume logic | Yes, via `cc-session-io` (sessionId preserved across provider switches) | Without resume, full re-tokenization every turn → prompt-cache miss → 5–10× more billable input on cache-warm paths |
| CC autocompact in parallel with Pi's | Not suppressed | `DISABLE_AUTO_COMPACT=1` | Double-compact = double cache-flush + thrashing-guard refusals |
| Tool-result delivery | FIFO match by position | Match by `toolCallId` | FIFO can silently mis-deliver under parallel calls → model retries |

#### Order-of-magnitude

- Multi-turn session with several tool calls: upstream commonly runs
  **2–5× higher** token usage, driven mostly by (a) the denial-loop
  re-planning and (b) prompt-cache miss on every turn.
- One-shot query with no local MCP and no thinking: gap narrows to
  **~10–30%**, mostly from the leaked tool-schema text and any
  unsuppressed MCP descriptions.
- Long-running sessions with `/compact`: gap *widens* further because
  the upstream has no compact-event subscription, so CC ends up
  re-importing the full pre-compact history into a fresh session
  each turn.

**Empirical observation (2026-05-27)**: real-world day-to-day usage
through pi-claude-bridge confirms the structural analysis above —
noticeable reduction in per-session token burn against the same
subscription quota relative to running the SDK route. Consistent with
the predicted multi-turn 2–5× gap rather than the single-shot
10–30% one, suggesting the denial-loop and prompt-cache-miss effects
dominate in practice.

The CHANGELOG entry for 0.4.0 calls out the structural piece
directly: *"Use `tools: []` instead of `disallowedTools` blocklist —
switch from blocking specific tools to explicitly passing an empty
tools list, preventing any new default tools from silently leaking
into bridge sessions."* That single change is the load-bearing one;
session resume, strict MCP, cloud-MCP off, and autocompact off are
the multipliers on top.

**Neither is the right route if you want to drop CC's personality.**
For users who specifically don't want Claude Code's memory or native
tool catalog, neither extension lets you swap the `claude_code` SDK
preset. If that's a hard requirement, the right path is a direct
`ANTHROPIC_API_KEY` provider (pay-as-you-go, no subscription) where
you control the system prompt fully — see
[Anthropic Subscription Auth in Pi](anthropic-subscription-auth.md).

## Caveats

- **Depends on Anthropic's TOS posture and the CC preset.** If
  Anthropic ever tightens the detector to inspect tool-call patterns
  (not just system prompt content), the structural route closes.
- **`claude_code` preset is load-bearing.** Pi cannot fully control
  the system prompt CC sees. Users who want a "neutral" Opus call
  inside Pi are better served by direct API key or a non-CC provider.
- **No Pi-side TUI for AskClaude streaming.** AskClaude is a single
  tool call; the user sees progress but not interactive CC widgets
  (PlanMode, AskUserQuestion, etc. — those are blocked in all modes).
- **NixOS users must set `pathToClaudeCodeExecutable`.**
- Subprocess overhead per query (one CC spawn per turn unless
  resuming).

## See also

- [Claude Pro/Max Subscription Extensions](claude-subscription-extensions.md) — niche survey, the alternate payload-patcher shape, and a decision matrix for when *not* to use this bridge
- [claude-agent-sdk-pi](claude-agent-sdk-pi.md) — upstream community Agent SDK adapter that this extension forks
- [Anthropic Subscription Auth in Pi](anthropic-subscription-auth.md) — full routing/billing matrix and the detector mechanism
- [Provider Extensions](provider-extensions.md) — broader provider landscape
- Repo: [`elidickinson/pi-claude-bridge`](https://github.com/elidickinson/pi-claude-bridge)
