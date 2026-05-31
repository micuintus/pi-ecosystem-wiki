---
title: Pi Claude Pro/Max Subscription Extensions
type: ecosystem
updated: 2026-05-31
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
  - pi-anthropic-oauth
tags: [extension, claude, anthropic, subscription, oauth, provider]
entries:
  - id: pi-claude-code-use
    name: "@benvargas/pi-claude-code-use"
    repo: ben-vargas/pi-packages
    npm: "@benvargas/pi-claude-code-use"
    role: payload-patcher-native-path
    notes: "Keeps Pi's built-in Anthropic OAuth transport entirely. Hooks `before_provider_request` and applies the smallest payload changes needed for Claude-Code-shaped requests: system-prompt phrase rewrites (`pi itself` → `the cli itself`), tool filtering against the Claude Code allowlist, and MCP-style aliasing (`web_search_exa` → `mcp__exa__web_search`). Companion-tool discovery via `sourceInfo` baseDir + path-segment match; jiti-based capture shim re-registers tool definitions under MCP aliases without touching the original `execute` closure. `message_end` hook unaliases tool-call names back to canonical before Pi executes. Integrates at **four** lifecycle points (`session_start`, `before_agent_start`, `message_end`, `before_provider_request`) and **mutates the session's active-tools list** to register/activate the MCP aliases — a broader session-state surface than a pure payload patch; deep-clones each payload per request. Auto-alias coverage is hardcoded to the author's own companions (`pi-exa-mcp`, `pi-firecrawl`) plus user `toolAliases`; OAuth is detected via Pi's official `modelRegistry.isUsingOAuth`. v1.0.x (declared stable). **Never invokes Claude Code itself** — leakage surface for CC features is structurally zero. 779 LOC src + 1,298 LOC tests (1.67× ratio). Empirical fingerprint observation in the README: Anthropic OAuth appears to fingerprint tool *names*, accepting `mcp__exa__web_search` while rejecting `web_search_exa`."
  - id: pi-anthropic-auth
    name: "@gotgenes/pi-anthropic-auth"
    repo: gotgenes/pi-anthropic-auth
    npm: "@gotgenes/pi-anthropic-auth"
    role: payload-patcher-billing-header
    notes: "Sibling of pi-claude-code-use in Shape A (payload patcher, never invokes Claude Code) but bets on a *different* Anthropic fingerprint signal — so it is complementary, not a subset. Re-registers Pi's built-in `anthropic` provider as a thin override: no model-list change, native transport preserved, `/login anthropic` and API-key behaviour untouched; activates only when it detects an Anthropic OAuth payload (by sniffing system-block markers — not Pi's `isUsingOAuth` API — so it is more exposed if Pi changes that identity block). One hook (`before_provider_request`) plus a thin `oauth` override reusing Pi's native login/refresh; stateless. Core technique: reconstructs Claude Code's `x-anthropic-billing-header` (`cc_version`, `cc_entrypoint`, and `cch` = truncated sha256 of the first user message plus a sampled-char salt) and prepends it as a system block — it forges the CC billing fingerprint rather than renaming tools. System-prompt shaping is surgical and anchor-based: removes Pi-identifying paragraphs by anchor string and swaps in a minimal neutral preamble, preserving project context and extension snippets (resilient to upstream Pi rewording). Two correctness fixes ride along: splits assistant turns where text trails a `tool_use` block (Anthropic rejects that ordering) and hardens OAuth refresh (keeps the prior refresh token when Anthropic omits a rotated one). Does **no** tool-name aliasing or filtering — the axis pi-claude-code-use specialises in. v0.5.0, 11 releases, CI, ~1:1 src:test files; intentionally minimal by design — its `docs/comparison-to-similar-projects.md` argues against the heavier full-transport replacement of `leohenon/pi-anthropic-oauth`."
  - id: pi-anthropic-oauth
    name: pi-anthropic-oauth
    repo: leohenon/pi-anthropic-oauth
    npm: pi-anthropic-oauth
    role: full-provider-replacement
    notes: "Shape C — a full replacement of Pi's anthropic provider, not a payload patch. Re-registers `anthropic` with its own OAuth implementation (PKCE, `claude.ai/oauth/authorize` + `platform.claude.com` token exchange, local-callback with manual-paste fallback), its own `streamSimple` transport calling `api.anthropic.com` directly with the OAuth token, and its own message/tool conversion layer — bundling `@anthropic-ai/sdk` as a runtime dependency. Reconstructs Pi's model list and adds Opus 4.8 by default. Impersonates Claude Code at the environment level: CC-compatible OAuth headers + prompt shaping, and auto-creates a `~/.Claude Code` → `~/.pi` symlink. README explicitly targets the main Pro/Max budget (\"No API key or extra usage needed\") and warns it may violate Anthropic's terms. Actively maintained against Anthropic auth changes, but ships no tests in-repo. Architecturally the oh-my-pi 'reverse-engineer the CC OAuth flow' approach packaged as a standalone extension rather than a fork."
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

**Short answer:** to run your Claude Pro/Max subscription in Pi with
the smallest blast radius, use a Shape A *payload patcher* —
`pi-claude-code-use` (dodges tool-name fingerprinting) or
`pi-anthropic-auth` (forges the billing-header fingerprint). They
attack different signals, never invoke Claude Code, and can even be
combined. Reach for the Shape B *provider proxy* `pi-claude-bridge`
only if you actually want Claude Code's own features (AskClaude, CC
skills, sub-agents, plan mode) — it costs real per-turn overhead. If
you don't want an extension at all, `/login anthropic` works at
extra-usage rates. To chase the *main* Pro/Max budget rather than
extra-usage, the Shape C *provider replacement* `pi-anthropic-oauth`
goes furthest — and is the heaviest and most ToS-risky.

Several extensions exist for "use my Claude subscription in Pi." They
split into three **structurally distinct** shapes that are easy to
confuse but solve different problems and have very different
performance, correctness, and risk characteristics.

For the platform-level context — how Pi's built-in OAuth route works,
what Anthropic's third-party-tool detection does, and why
extra-usage billing happens — see
[Anthropic Auth & Billing in Pi](anthropic-auth-and-billing.md).
This page surveys the *extensions* that operate on top of that
baseline.

## The three shapes

| | What it intercepts | What carries the request | Side-effects on Pi |
|---|---|---|---|
| **Shape A — payload patcher** (native path) | `before_provider_request` hook | Pi's existing Anthropic OAuth transport | Payload patches: tool-name aliasing, system-prompt rewrites, and/or a forged billing header |
| **Shape B — provider proxy** (delegated path) | Registers a new provider | Claude Code SDK or CLI subprocess | Whole alternate inference path with its own state machine |
| **Shape C — provider replacement** (self-owned transport) | Re-registers `anthropic` | Its own `streamSimple` transport straight to `api.anthropic.com` | Replaces OAuth + transport + model list; impersonates Claude Code at the environment level (`~/.Claude Code` symlink) |

That structural choice dominates every comparison below.

### Shape A — payload patcher (native path)

Keeps Pi using Pi's built-in `anthropic` provider with your OAuth
credentials. The extension hooks `before_provider_request` and
rewrites the outbound payload to look more like Claude Code — the
goal is to avoid Anthropic's third-party-tool fingerprinting and
"extra usage" classification. No new provider, no subprocess, no
SDK, no Claude Code installed.

The two Shape A extensions target **different fingerprint signals**,
so they are complementary rather than a big-vs-small pair:

- [`@benvargas/pi-claude-code-use`](https://github.com/ben-vargas/pi-packages) — bets that
  Anthropic fingerprints **tool names**. MCP-style aliasing
  (`web_search_exa` → `mcp__exa__web_search`) with jiti-shim capture
  of companion tool definitions, tool filtering against the CC
  allowlist, `tool_choice` and message-history rewriting, alias-
  activation tracking with user-vs-auto provenance, plus system-prompt
  phrase rewrites. The most-developed patcher.
- [`@gotgenes/pi-anthropic-auth`](https://github.com/gotgenes/pi-anthropic-auth) — bets that
  Anthropic fingerprints the **billing header**. Reconstructs Claude
  Code's `x-anthropic-billing-header` (`cc_version` / `cc_entrypoint` /
  content-hash) as a forged system block, plus anchor-based minimal
  system-prompt de-fingerprinting and an OAuth refresh-token hardening
  fix. Does no tool aliasing; thin override of the built-in `anthropic`
  provider by design.

Practical consequence for your toolset: `pi-claude-code-use` filters
unknown flat-named tools out of the model's view (rescue them via its
`toolAliases` config), whereas `pi-anthropic-auth` exposes every Pi
tool unchanged.

**Which Shape A patcher?** They are close on raw size (~700–800 LOC
src, ~1.7× test ratio each) and both are genuinely well-built — the
difference is *surface*, not sloppiness:

- **Smaller blast radius** — `pi-anthropic-auth`. One hook
  (`before_provider_request`) plus a thin `oauth` override reusing Pi's
  native login/refresh; stateless pure functions across
  single-responsibility modules; zero runtime dependencies;
  structurally shares the payload (no deep clone).
- **Larger surface, more capable** — `pi-claude-code-use`. Tool-name
  aliasing is the whole reason to pick it, but it costs more: four
  lifecycle hooks (`session_start`, `before_agent_start`,
  `message_end`, `before_provider_request`), it **mutates the session's
  active-tools list**, holds module-level singleton state, carries a
  `jiti` dependency to dynamically load other extensions' code (around
  the absent Pi tool-introspection API), and deep-clones each payload.
  Auto-aliasing is hardcoded to the author's own companions
  (`pi-exa-mcp`, `pi-firecrawl`) plus your `toolAliases`. It is
  carefully engineered for that complexity — sectioned, defensive,
  cross-platform, broad test-export surface — and is declared stable
  (1.x) where `pi-anthropic-auth` is pre-1.0.
- **Pi-idiomatic — both ways** — `pi-anthropic-auth` reuses Pi's native
  OAuth helpers and adds no tools or state, but *sniffs* OAuth state
  from system-block markers in the payload; `pi-claude-code-use`
  detects OAuth via Pi's official `modelRegistry.isUsingOAuth` API,
  which is more robust if Pi changes that identity block.
- **Adoption** — close. npm installs currently favour
  `pi-anthropic-auth`; repo stars favour `pi-claude-code-use`, but that
  count is the whole `pi-packages` monorepo (a confounded signal).
  Query live signals via [evaluation.md](../references/evaluation.md).

Net: `pi-anthropic-auth` is the leaner, lower-surface, zero-dependency
build; `pi-claude-code-use` is the more capable and more mature one, at
a larger session-state surface. Choose it when you specifically need
its tool-name disguise; run both for belt-and-suspenders against
whichever signal Anthropic enforces.

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

### Shape C — full provider replacement (self-owned transport)

Re-registers Pi's `anthropic` provider but replaces almost everything
behind it: its own OAuth login/refresh, its own `streamSimple`
transport calling `api.anthropic.com` directly with the OAuth token,
and its own message/tool conversion. It neither rides Pi's transport
(Shape A) nor delegates to a Claude Code process (Shape B) — it
*impersonates* Claude Code: CC-shaped headers, prompt shaping, and a
`~/.Claude Code` → `~/.pi` symlink so the environment looks like a CC
install. The deepest intervention here, and the only shape that openly
targets the **main Pro/Max budget** rather than extra-usage.

- [`leohenon/pi-anthropic-oauth`](https://github.com/leohenon/pi-anthropic-oauth) — the
  sole entry. Reimplements OAuth (PKCE + `claude.ai` authorize +
  `platform.claude.com` token exchange, with manual-paste callback
  fallback), bundles `@anthropic-ai/sdk`, reconstructs the model list
  (adds Opus 4.8 by default), and self-warns that it may violate
  Anthropic's terms. Actively maintained against auth changes, but
  ships no tests in-repo — cat-and-mouse by nature.

## Picking guide

| What you actually want | Pick |
|---|---|
| **"Use my Claude subscription in Pi, with the smallest blast radius"** | **`pi-claude-code-use`** or **`pi-anthropic-auth`** (Shape A). Both stay on Pi's native code path with zero structural per-turn overhead and cannot leak Claude Code features (they never invoke it). Pick by which fingerprint signal trips you — see the next two rows. |
| **Fingerprint trips on tool names** | `pi-claude-code-use`. MCP-style tool aliasing (`web_search_exa` → `mcp__exa__web_search`), companion-tool capture, filtering against the CC allowlist. |
| **Fingerprint trips on the billing header — or you want a thin provider override + OAuth refresh hardening** | `pi-anthropic-auth`. Forges Claude Code's `x-anthropic-billing-header` and minimises the system prompt; does no tool aliasing. A different bet from `pi-claude-code-use`, not a subset — the two can be combined. |
| **You want Claude Code's features inside Pi (AskClaude tool, CC skills, sub-agents, plan mode)** | `pi-claude-bridge` (Shape B). The only path that actually delivers those features. Costs CC's system-prompt overhead per cold-start session; mitigated by session resume + strict-mcp-config + cloud-MCP suppression + autocompact disable. |
| **You'll accept a heavier, ToS-riskier full provider replacement to chase the *main* Pro/Max budget (and want newest models like Opus 4.8)** | `pi-anthropic-oauth` (Shape C). Reimplements OAuth + transport and impersonates Claude Code at the environment level. No in-repo tests; treat as cat-and-mouse. |
| **You need to route Claude-flavored traffic through a proxy provider** | `pi-anthropic-messages` (adjacent). Protocol-level Anthropic-messages bridge. |
| **You want one login to reach multiple subscriptions** | `pi-proxy-models` (adjacent). CLIProxyAPIPlus wrapper. |
| **You don't actually need a Pi-side extension** | `/login anthropic` and accept the extra-usage warning. See [Anthropic Auth & Billing in Pi](anthropic-auth-and-billing.md). |

## Three-axis comparison (code-read findings)

### Closest to "using my Claude subscription in Pi"

**Either Shape A patcher** (`pi-claude-code-use` or
`pi-anthropic-auth`), by a wide margin. Both literally use your
Anthropic subscription credentials through Pi's normal OAuth
transport, just with payload tweaks to dodge fingerprinting. The
bridge isn't using your subscription "in Pi" — it's using your
subscription *through Claude Code*, which is then used as Pi's LLM
backend. Two different things.

### Least token waste

Ranked best to worst:

1. **Shape A patchers (`pi-claude-code-use`, `pi-anthropic-auth`)** —
   zero structural overhead. Same payload Pi was going to send anyway,
   with string substitutions, tool-name renames, or a forged billing
   header. Cache works at Pi's normal cache_control breakpoints.
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

1. **Shape A patchers (`pi-claude-code-use`, `pi-anthropic-auth`)** —
   *cannot leak Claude Code features because they never invoke Claude
   Code.* Leakage surface is structurally zero. Pure-function
   transforms, good test ratios (1.67× for pi-claude-code-use, ~1:1
   src:test files for pi-anthropic-auth), simple control flow. Failure
   modes confined to "Anthropic changes the fingerprint shape" — a
   tractable correctness problem.
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

- [Anthropic Auth & Billing in Pi](anthropic-auth-and-billing.md) — the platform-level baseline this page sits on top of.
- [pi-claude-bridge](pi-claude-bridge.md) — deep-dive on the dominant Shape B extension.
- [claude-agent-sdk-pi](claude-agent-sdk-pi.md) — deep-dive on the original Shape B (no-resume) implementation.
- [Provider Extensions](provider-extensions.md) — for the broader landscape of non-built-in providers.
- [References — How to Evaluate a Pi Extension](../references/evaluation.md) — for current adoption / maintenance signals on each entry above.
