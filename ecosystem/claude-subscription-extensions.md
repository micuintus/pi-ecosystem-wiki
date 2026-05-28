---
title: Pi Claude Pro/Max Subscription Extensions
type: ecosystem
updated: 2026-05-28
sources:
  - pi-mono
  - pi-providers-docs
  - anthropic-third-party-end
  - ben-vargas-pi-packages
  - pi-claude-code-use
  - pi-anthropic-auth
  - pi-claude-bridge
  - claude-agent-sdk-pi
  - pi-claude-cli
  - pi-claude-code-fractary
  - pi-anthropic-messages
  - pi-proxy-models
tags: [extension, claude, anthropic, subscription, oauth, provider]
entries:
  - id: pi-claude-code-use
    name: "@benvargas/pi-claude-code-use"
    repo: ben-vargas/pi-packages
    npm: "@benvargas/pi-claude-code-use"
    role: payload-patcher-native-path
    notes: "Keeps Pi's built-in Anthropic OAuth transport entirely. Hooks `before_provider_request` and applies the smallest payload changes needed for Claude-Code-shaped requests: system-prompt phrase rewrites (`pi itself` → `the cli itself`), tool filtering against the Claude Code allowlist, and MCP-style aliasing (`web_search_exa` → `mcp__exa__web_search`). Companion-tool discovery via `sourceInfo` baseDir + path-segment match; jiti-based capture shim re-registers tool definitions under MCP aliases without touching the original `execute` closure. `message_end` hook unaliases tool-call names back to canonical before Pi executes. **Never invokes Claude Code itself** — leakage surface for CC features is structurally zero. 779 LOC src + 1,298 LOC tests (1.67× ratio). Empirical fingerprint observation in the README: Anthropic OAuth appears to fingerprint tool *names*, accepting `mcp__exa__web_search` while rejecting `web_search_exa`."
  - id: pi-anthropic-auth
    name: pi-anthropic-auth
    repo: gotgenes/pi-anthropic-auth
    role: oauth-compat-shim
    notes: "Sibling of pi-claude-code-use in the same sub-niche (payload-patcher on Pi's native OAuth path). Smaller scope — focuses on OAuth compatibility for Claude Pro/Max without replacing Pi's anthropic provider. 11 tagged releases, active maintenance. Less feature-rich than pi-claude-code-use; useful if the latter's tool-aliasing layer is more than you need."
  - id: pi-claude-bridge
    name: pi-claude-bridge
    repo: elidickinson/pi-claude-bridge
    npm: pi-claude-bridge
    role: provider-via-cc-sdk
    notes: "Registers a new `claude-bridge` provider via `query()` from `@anthropic-ai/claude-agent-sdk`. Pi's LLM calls go to Claude Code, Pi still executes tools. **Critical optimization: session resume via `cc-session-io`** — passes `resume: resumeSessionId` so CC reuses its own cache instead of re-sending full history every turn. Mitigation layer hardened against CC feature leakage: `--strict-mcp-config` (ignore `~/.claude.json`/`.mcp.json`), `ENABLE_CLAUDEAI_MCP_SERVERS=0` (suppress claude.ai cloud MCP), `DISABLE_AUTO_COMPACT=1` (Pi owns compaction). Adds AskClaude tool (dispatch sub-task to CC), skills forwarding, MCP tool bridging, custom Pi tool bridging via SDK MCP server. 2,101 LOC src, complex state machine (push/pop context stack for re-entrant subagent queries, pending-MCP-handler map by tool-call ID, deferred-user-message queue for mid-query steers, abort coordination). Inherits from claude-agent-sdk-pi; the de-facto upstream in this sub-niche by adoption."
  - id: claude-agent-sdk-pi
    name: claude-agent-sdk-pi
    repo: prateekmedia/claude-agent-sdk-pi
    npm: claude-agent-sdk-pi
    role: provider-via-cc-sdk-original
    notes: "The original SDK-based bridge that elidickinson/pi-claude-bridge forked from. Same provider shape (registers `claude-agent-sdk`, denies tool execution in CC, bridges custom tools via MCP). **Missing session resume** — rebuilds the full prompt and ships history to a fresh `query()` every turn, no cache reuse across turns, strictly worse token economics than the elidickinson fork on any multi-turn session. 1,258 LOC single file, no test suite visible in repo. Adoption lags the fork (99★ vs 112★, 817 vs 1368 DL/mo)."
  - id: pi-claude-cli
    name: pi-claude-cli
    repo: rchern/pi-claude-cli
    npm: pi-claude-cli
    role: provider-via-cc-cli-subprocess
    notes: "Alternative provider shape: spawns `claude -p` as a subprocess and talks stream-json over stdin/stdout, using `--resume` for cache continuity. Excellent test discipline (5,876 LOC tests against 2,115 LOC src — 2.78× ratio, the highest in the niche), modular structure (process-manager / event-bridge / stream-parser / prompt-builder / control-handler / tool-mapping). Hardened lifecycle: inactivity timeout, force-kill paths, process registry, break-early at `message_stop` to prevent CC auto-executing tools. **Status: stale** — last push 2026-03-22, only 9 commits in 90 days against a fast-moving Pi. Treat as broken until reactivated."
  - id: pi-claude-bridge-schwa
    name: pi-claude-bridge (schwa fork)
    repo: schwa/pi-claude-bridge
    role: provider-via-cc-sdk-fork
    notes: "Fork of elidickinson/pi-claude-bridge. No adoption (0★, no forks-of-fork). No demonstrated divergence beyond personal-use changes. Skip in favor of elidickinson upstream."
  - id: pi-claude-bridge-tycronk
    name: pi-claude-bridge (tycronk20 fork)
    repo: tycronk20/pi-claude-bridge
    role: provider-via-cc-sdk-fork
    notes: "Fork of elidickinson/pi-claude-bridge. No adoption. Skip in favor of elidickinson upstream."
  - id: pi-claude-code-fractary
    name: pi-claude-code
    repo: fractary/pi-claude-code
    role: cc-tool-name-shim
    notes: "Narrow shim only: maps Claude Code tool names (`Grep`, `Glob`, `TaskCreate`, `WebFetch`, etc.) to Pi equivalents so agents/skills authored for Claude Code run inside Pi without modification. Not a subscription router. Adjacent to but doesn't solve the same problem. Stale-ish (last push 2026-03-30)."
  - id: pi-anthropic-messages
    name: pi-anthropic-messages
    repo: BlackBeltTechnology/pi-anthropic-messages
    role: protocol-bridge
    notes: "Protocol-level bridge for Anthropic-messages traffic to non-Anthropic backends — works with direct Anthropic OAuth/API and proxy providers like 9Router, pi-model-proxy. MCP-style tool prefixing, native-tool aliasing, system-prompt compat shims. Adjacent niche: subsidiary if you're routing Claude-flavored traffic through a non-Anthropic provider proxy."
  - id: pi-proxy-models
    name: pi-proxy-models
    repo: victormilk/pi-proxy-models
    role: multi-subscription-proxy
    notes: "Exposes CLIProxyAPIPlus models to Pi's model picker, routing each model family through its native streaming API (Anthropic Messages / OpenAI Chat Completions / Google Generative AI). One `/login` to CLIProxyAPIPlus reaches Claude Code, Gemini CLI, OpenAI Codex, GitHub Copilot, Kiro, GLM, etc. with their native features (prompt caching for Claude, thinking for Gemini) intact. Multi-subscription consolidation rather than Claude-specific."
---

# Pi Claude Pro/Max Subscription Extensions

Several extensions exist for "use my Claude subscription in Pi." They
split into two **structurally distinct** sub-niches that are easy to
confuse but solve different problems and have very different
performance and correctness characteristics.

For the platform-level context — how Pi's built-in OAuth route works,
what Anthropic's third-party-tool detection does, and why
extra-usage billing happens — see
[Anthropic Subscription Auth in Pi](anthropic-subscription-auth.md).
This page surveys the *extensions* that operate on top of that
baseline.

## The two shapes

| | What it intercepts | What carries the request | Side-effects on Pi |
|---|---|---|---|
| **Payload patcher** (native path) | `before_provider_request` hook | Pi's existing Anthropic OAuth transport | Tool aliasing, system-prompt rewrites |
| **Provider proxy** (delegated path) | Registers a new provider | Claude Code SDK or CLI subprocess | Whole alternate inference path with its own state machine |

That structural choice dominates every comparison below.

### Shape A — payload patcher (native path)

Keeps Pi using Pi's built-in `anthropic` provider with your OAuth
credentials. The extension hooks `before_provider_request` and
rewrites the outbound payload to look more like Claude Code — the
goal is to avoid Anthropic's third-party-tool fingerprinting and
"extra usage" classification. No new provider, no subprocess, no
SDK, no Claude Code installed.

- [`@benvargas/pi-claude-code-use`](https://github.com/ben-vargas/pi-packages) — the most-developed
  in this shape. System-prompt phrase rewrites, tool filtering
  against the CC allowlist, MCP-style aliasing with jiti-shim
  capture of companion tool definitions, message-history rewriting,
  alias-activation tracking with user-vs-auto provenance.
- [`gotgenes/pi-anthropic-auth`](https://github.com/gotgenes/pi-anthropic-auth) — smaller scope,
  focuses on OAuth compatibility without the full tool-aliasing
  layer.

### Shape B — provider proxy (delegated path)

Registers a new provider that routes LLM calls to Claude Code (as an
SDK query or CLI subprocess). Pi still executes tools locally; CC's
own tool execution is denied so it stays purely as the LLM backend.
Trades off significant per-turn overhead (CC's `claude_code` preset
system prompt on every cold start) for access to Claude Code's
features.

- [`elidickinson/pi-claude-bridge`](https://github.com/elidickinson/pi-claude-bridge) — Agent SDK
  via `query()`. The de-facto upstream in this sub-niche by every
  adoption signal. Critical optimization: session resume via
  `cc-session-io` so CC reuses its own prompt cache across turns
  instead of re-prefixing the full history each call.
- [`prateekmedia/claude-agent-sdk-pi`](https://github.com/prateekmedia/claude-agent-sdk-pi) —
  the original that the elidickinson fork inherited from. Same
  provider shape but **no session resume** — strictly more token
  waste per multi-turn session. Adoption lags the fork.
- [`rchern/pi-claude-cli`](https://github.com/rchern/pi-claude-cli) — alternative shape: spawns
  `claude -p` subprocess with `--resume` over stream-json. Excellent
  test discipline; currently **stale**.
- Forks of `pi-claude-bridge` (schwa, tycronk20) — no demonstrated
  divergence or adoption beyond the canonical fork.

## Picking guide

| What you actually want | Pick |
|---|---|
| **"Use my Claude subscription in Pi, with the smallest blast radius"** | **`pi-claude-code-use`** (Shape A). Stays on Pi's native code path. Zero structural per-turn overhead. Cannot leak Claude Code features because it never invokes Claude Code. |
| **Smallest possible OAuth compatibility shim** | `pi-anthropic-auth` (Shape A). Smaller scope than `pi-claude-code-use` — useful if you don't need the tool-aliasing layer. |
| **You want Claude Code's features inside Pi (AskClaude tool, CC skills, sub-agents, plan mode)** | `pi-claude-bridge` (Shape B). The only path that actually delivers those features. Costs CC's system-prompt overhead per cold-start session; mitigated by session resume + strict-mcp-config + cloud-MCP suppression + autocompact disable. |
| **You need to route Claude-flavored traffic through a proxy provider** | `pi-anthropic-messages` (adjacent). Protocol-level Anthropic-messages bridge. |
| **You want one login to reach multiple subscriptions** | `pi-proxy-models` (adjacent). CLIProxyAPIPlus wrapper. |
| **You don't actually need a Pi-side extension** | `/login anthropic` and accept the extra-usage warning. See [Anthropic Subscription Auth in Pi](anthropic-subscription-auth.md). |

## Three-axis comparison (code-read findings)

### Closest to "using my Claude subscription in Pi"

**`pi-claude-code-use`** by a wide margin. It literally uses your
Anthropic subscription credentials through Pi's normal OAuth
transport, just with payload tweaks to dodge fingerprinting. The
bridge isn't using your subscription "in Pi" — it's using your
subscription *through Claude Code*, which is then used as Pi's LLM
backend. Two different things.

### Least token waste

Ranked best to worst:

1. **`pi-claude-code-use`** — zero structural overhead. Same payload
   as Pi was going to send anyway, with string substitutions and
   tool-name renames. Cache works at Pi's normal cache_control
   breakpoints.
2. **`pi-claude-bridge`** — significant per-turn overhead (CC's
   `claude_code` preset system prompt on every cold-start session),
   mitigated by session resume + strict-mcp-config + cloud-MCP
   suppression + autocompact disable. Sophisticated engineering but
   the floor is much higher than (1).
3. **`claude-agent-sdk-pi`** — same per-turn overhead as (2) *without*
   the session resume. Strictly worse than the bridge fork on every
   multi-turn session.
4. **`pi-claude-cli`** — comparable to (2) in theory via `--resume`;
   stale in practice.

### Least error-prone / least Claude Code feature leakage

Ranked best to worst:

1. **`pi-claude-code-use`** — *cannot leak Claude Code features
   because it never invokes Claude Code.* Leakage surface is
   structurally zero. Pure-function transform, 1.67× test ratio,
   simple control flow. Failure modes confined to "Anthropic
   changes the fingerprint shape" — a tractable correctness
   problem.
2. **`pi-claude-cli`** — best test discipline of the four (2.78×
   ratio), but stale.
3. **`pi-claude-bridge`** — complex state machine; leakage surface
   is *explicitly enumerated and mitigated* (cloud MCP off,
   autocompact off, MCP auto-load off). Each mitigation is one
   place the abstraction could break. Battle-tested but the surface
   is much larger than Shape A.
4. **`claude-agent-sdk-pi`** — same complexity as (3) without
   resume, without tests, without diag-dump paths. The most fragile.

## When to switch from `pi-claude-bridge` to `pi-claude-code-use`

If you're currently on the bridge and asking whether to switch:
the bridge buys you Claude Code's *features* (AskClaude tool, CC
skills, CC sub-agents, plan mode). If you actually use any of
those, stay on it. If you only use it to "make my Claude
subscription work in Pi" without invoking the CC-specific features,
switching to `pi-claude-code-use` is a Pareto improvement on token
cost, latency, and correctness surface.

The two extensions can coexist — they intercept different code
paths — so A/B testing is cheap.

## See also

- [Anthropic Subscription Auth in Pi](anthropic-subscription-auth.md) — the platform-level baseline this page sits on top of.
- [pi-claude-bridge](pi-claude-bridge.md) — deep-dive on the dominant Shape B extension.
- [claude-agent-sdk-pi](claude-agent-sdk-pi.md) — deep-dive on the original Shape B (no-resume) implementation.
- [Provider Extensions](provider-extensions.md) — for the broader landscape of non-built-in providers.
- [References — How to Evaluate a Pi Extension](../references/evaluation.md) — for current adoption / maintenance signals on each entry above.
