---
title: Pi Claude Pro/Max Subscription Extensions
type: ecosystem
updated: 2026-10-13
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
  - pi-anthropic-auth-architecture
  - pi-anthropic-auth-claude-code-version
  - pi-anthropic-messages-ts
  - pi-interactive-mode-ts
  - pi-system-prompt-ts
  - gotgenes-pi-packages-issue-883
  - hermes-agent-issue-72171
  - pi-anthropic-oauth-pr-23
  - pi-anthropic-oauth-pr-33
  - pi-anthropic-oauth-pr-35
  - pi-claude-bridge-changelog
  - pi-claude-bridge-issue-140
  - ben-vargas-pi-packages-pr-37
  - pi-claude-cli-issue-32
  - support-agent-sdk-plan
  - support-usage-credits
  - support-monthly-api-credits
  - claude-code-legal
  - pi-claude-pro
  - pi-claude-max
  - pi-claude-request-compat
  - saccolabs-pi-claude-cli
  - pi-claude-agent-sdk
  - pi-claude-code-provider
  - pi-sub-anthropic
  - pi-claude-plan
  - pi-thinking-binding
  - pi-anthropic-image-cap
  - pi-anthropic-vertex
  - pi-models-docs
tags: [extension, claude, anthropic, subscription, oauth, provider]
entries:
  - id: pi-claude-code-use
    name: "@benvargas/pi-claude-code-use"
    repo: ben-vargas/pi-packages
    npm: "@benvargas/pi-claude-code-use"
    role: payload-patcher-native-path
    notes: "Shape A payload patcher on Pi's built-in Anthropic OAuth transport; never invokes Claude Code. 2.x derives `mcp__<server>__<tool>` aliases from `pi.getAllTools()` for every non-core tool (no hardcoded companions, no `jiti`), un-aliases them in displayed prose through `pi.registerMarkdownTransformer()`, and since 2.2.1 handles Pi 0.86 `tool_addition`/`tool_removal` entries so historical aliases keep the prompt cache. Sends no billing block. The maintainer reports no live OAuth testing since 2026-09-11."
  - id: pi-anthropic-auth
    name: "@gotgenes/pi-anthropic-auth"
    repo: gotgenes/pi-anthropic-auth
    npm: "@gotgenes/pi-anthropic-auth"
    role: payload-patcher-billing-header
    notes: "Shape A and the most actively maintained shaper. Since 0.5.1 a `streamSimple` wrapper around Pi's own `anthropic` transport, so compaction and `ctx.modelRegistry.streamSimple()` callers are shaped too; callers of pi-ai's `compat.streamSimple` are not. Activates on `sk-ant-oat` tokens. Prepends the `x-anthropic-billing-header` block, follows the per-model `cc_version` floor (Opus 5.5 needs 2.1.280) and retries once at the version Anthropic names, replaces Pi's preamble with four neutral lines, drops the `docs` section and keeps `project_context` byte-identical. Since 2.0.0 it uses Pi's built-in login and refresh. `/anthropic-auth:status` shows shaped providers, plan, rate-limit tier and usage-credit state. No tool aliasing."
  - id: pi-anthropic-oauth
    name: pi-anthropic-oauth
    repo: leohenon/pi-anthropic-oauth
    npm: pi-anthropic-oauth
    role: full-provider-replacement
    notes: "Shape C: replaces Pi's `anthropic` provider with its own OAuth and transport; now uses Pi's model registry and ships tests. 0.2.2 namespaces unknown tools as `mcp__pi__<name>`; 0.3.0 reads `TranscriptContext` and adds a billing block with the identity line 'You are a Claude agent, built on Anthropic's Claude Agent SDK.' Its sanitizer runs over the whole system prompt, project context included, and in the default `aggressive` mode rewrites every standalone `pi`/`Pi` to `Claude Code`. Warns that it may violate Anthropic's terms."
  - id: pi-claude-bridge
    name: pi-claude-bridge
    repo: elidickinson/pi-claude-bridge
    npm: pi-claude-bridge
    role: provider-via-cc-sdk
    notes: "Shape B: provider `claude-bridge` through `query()` from `@anthropic-ai/claude-agent-sdk`; Pi executes tools. Session resume via `cc-session-io`, `--strict-mcp-config`, cloud MCP off, auto-compact off. 0.7.0 removed `provider.appendSystemPrompt` and `provider.settingSources` (Claude Code now receives the `AGENTS.md`/`CLAUDE.md` files Pi loads) and made AskClaude opt-in; 0.8.0 moved to Pi 0.86 `TranscriptContext`; 0.9.0 refuses a turn whose append contains Pi's base prompt. Claude Code's own settings sources stay at their default, so `~/.claude/settings.json` hooks fire in bridge turns."
  - id: claude-agent-sdk-pi
    name: claude-agent-sdk-pi
    repo: prateekmedia/claude-agent-sdk-pi
    npm: claude-agent-sdk-pi
    role: provider-via-cc-sdk-original
    notes: "The original Shape B bridge that pi-claude-bridge forked from. No session resume. Unmaintained against Pi 0.86 and later; it still reads `context.tools` and `context.systemPrompt`, which Pi 0.86 removed from provider input, so on current Pi no Pi tools or prompt reach Claude Code (inference from code)."
  - id: pi-claude-cli
    name: pi-claude-cli
    repo: rchern/pi-claude-cli
    npm: pi-claude-cli
    role: provider-via-cc-cli-subprocess
    notes: "Shape B through `claude -p` with `--resume` and strong test discipline, but since Pi 0.84 print mode (`pi -p`) and nested agent loops fail with 'No API provider registered for api: pi-claude-cli' (issue #32). `@saccolabs/pi-claude-cli` is the maintained fork."
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
    repo: ovitinhooo/pi-proxy-models
    role: multi-subscription-proxy
    notes: "Exposes CLIProxyAPIPlus models to Pi's model picker, routing each model family through its native streaming API (Anthropic Messages / OpenAI Chat Completions / Google Generative AI). One `/login` to CLIProxyAPIPlus reaches Claude Code, Gemini CLI, OpenAI Codex, GitHub Copilot, Kiro, GLM, etc. with their native features (prompt caching for Claude, thinking for Gemini) intact. Multi-subscription consolidation rather than Claude-specific."
  - id: pi-claude-pro
    name: pi-claude-pro
    repo: HugoLopes45/pi-claude-pro
    npm: pi-claude-pro
    role: payload-patcher-billing-header
    notes: "Shape A, new in October 2026. Claude Code user agent, `x-app`, session header and billing block; moves Pi's `docs` section to the start of the first user message; footer with five-hour and weekly usage from `anthropic-ratelimit-unified-*` headers; stops retries on a spent limit. Its README asks for a single `anthropic` handler, so not alongside `pi-anthropic-auth`."
  - id: pi-claude-max
    name: pi-claude-max
    repo: bradennss/pi-claude-max
    npm: pi-claude-max
    role: payload-patcher-billing-header
    notes: "Shape A. A `before_provider_request` hook that adds a billing block with `cc_entrypoint=cli`."
  - id: pi-claude-request-compat
    name: pi-claude-request-compat
    repo: vazzma/pi-claude-request-compat
    npm: pi-claude-request-compat
    role: payload-patcher-own-provider
    notes: "Shape A under its own provider name `claude-compat`, on Pi's Anthropic transport and login flow, with a wire profile derived from oh-my-pi. Never falls back to `anthropic`."
  - id: saccolabs-pi-claude-cli
    name: "@saccolabs/pi-claude-cli"
    repo: agustinsacco/pi-claude-cli
    npm: "@saccolabs/pi-claude-cli"
    role: provider-via-cc-cli-subprocess
    notes: "Shape B. Maintained fork of `pi-claude-cli`: Pi's system prompt replaces Claude Code's, tools over MCP, `--no-session-persistence`, CLI auto-compaction off."
  - id: pi-claude-agent-sdk
    name: pi-claude-agent-sdk
    repo: pi-pod/pi-claude-agent-sdk
    npm: pi-claude-agent-sdk
    role: provider-via-cc-sdk-fork
    notes: "Shape B. Fork of `pi-claude-bridge` that hands Pi's stored Anthropic OAuth credential to the Claude Code child instead of Claude Code's own login."
  - id: pi-claude-code-provider
    name: pi-claude-code-provider
    repo: chem/pi-claude-code-provider
    npm: pi-claude-code-provider
    role: provider-via-cc-cli-subprocess
    notes: "Shape B. Unmodified `claude` in print mode; Pi owns tools and history. Mothballed; the README points to `pi-claude-bridge`."
  - id: pi-sub-anthropic
    name: pi-sub-anthropic
    repo: spksoft/pi-sub-anthropic
    npm: pi-sub-anthropic
    role: full-provider-replacement
    notes: "Shape C. Separate `pi-sub-anthropic` provider ported from oh-my-pi, with its own `fetch` transport reproducing Claude Code's wire fingerprint; pinned, no self-update."
  - id: pi-claude-plan
    name: pi-claude-plan
    repo: sunipan/pi-claude-plan
    npm: pi-claude-plan
    role: full-provider-replacement
    notes: "Shape C. Separate `claude-plan` provider and PKCE login, ported from `opencode-anthropic-auth`, with `mcp_` tool mapping. Reads the pre-0.86 `context.tools`."
  - id: pi-thinking-binding
    name: "@luan.sh/pi-thinking-binding"
    repo: luan/agents
    npm: "@luan.sh/pi-thinking-binding"
    role: overhead-reducer
    notes: "Strips thinking blocks once after a system-prompt or tool change invalidates them, instead of Anthropic dropping them on every turn."
  - id: pi-anthropic-image-cap
    name: "@ogulcancelik/pi-anthropic-image-cap"
    repo: ogulcancelik/pi-extensions
    npm: "@ogulcancelik/pi-anthropic-image-cap"
    role: overhead-reducer
    notes: "Drops the oldest images from outgoing Anthropic requests at Claude Code's thresholds (24 MB or 100 images)."
---

# Pi Claude Pro/Max Subscription Extensions

To use a Claude Pro/Max subscription in Pi with nothing from Claude
Code in the context, run `@gotgenes/pi-anthropic-auth` alone. It wraps
Pi's own Anthropic transport, adds the Claude Code billing block that
Anthropic now checks, swaps Pi's preamble for four neutral lines, drops
the `docs` section, and never starts Claude Code. Turn usage credits
off at claude.ai/settings/usage, so a request Anthropic classifies as
third-party fails instead of being billed per token. For Claude without
that classifier, Max and Team plans now include monthly API credits
that Pi spends through an API key (see
[Status, October 2026](#status-october-2026)).

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

## Status, October 2026

Anthropic's rules for subscription logins in third-party tools:

| Date | Change |
|---|---|
| 2026-04-04 | Plan limits stop covering third-party harnesses; their usage draws from extra usage ([anthropic-third-party-end]), which Anthropic's help center now calls usage credits ([support-usage-credits]) |
| 2026-06-15 | A planned Agent SDK billing change is paused: "Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription limits." ([support-agent-sdk-plan]) |
| 2026-10-07 | Monthly API credits for Max (5x: $100, 20x: $200) and Team ($20 or $100 per seat, pooled, capped at $500), spent through a Console organization on the Claude API, Managed Agents and the Agent SDK; not on interactive Claude Code, and not for Pro ([support-monthly-api-credits], [support-agent-sdk-plan]) |

The current legal page says subscription OAuth "is designed to support
ordinary use of Claude Code and other native Anthropic applications",
that third-party developers may not "route requests through Free, Pro,
or Max plan credentials on behalf of their users", and that Anthropic
may enforce this "without prior notice" ([claude-code-legal]). The
support article above still says third-party apps draw from plan
limits. Pi prints its own warning while subscription auth is active:
"Third-party harness usage draws from extra usage and is billed per
token" ([pi-interactive-mode-ts]).

What Anthropic checks on an OAuth request, as measured by extension
and harness authors:

| Signal | Evidence |
|---|---|
| Claude Code transport identity: `user-agent: claude-cli/<version>`, `x-app: cli`, betas `claude-code-20250219` and `oauth-2025-04-20`, and the system line "You are Claude Code, Anthropic's official CLI for Claude." | Pi core sends all of these for OAuth tokens ([pi-anthropic-messages-ts]); necessary, not sufficient ([hermes-agent-issue-72171]) |
| A billing-header block in `system` (`x-anthropic-billing-header: cc_version=...; cc_entrypoint=...; cch=...`) | A 28 KB Pi prompt on Opus 5 returned 400 without the block and 200 with it; short prompts pass either way ([pi-anthropic-auth-architecture]) |
| `cc_version` per model | Older versions are refused with `claude_code_version_too_old`; Fable 5.1 needs 2.1.251, Opus 5.5 needs 2.1.280 ([pi-anthropic-auth-claude-code-version]) |
| Harness vocabulary in `system`, scored cumulatively | Pi's `docs` line with both "custom providers (docs/custom-provider.md)" and "pi packages (docs/packages.md)" returns 400 even through the real Claude Code binary; either phrase alone passes ([gotgenes-pi-packages-issue-883]). Pi 1.2.0 still carries both phrases ([pi-system-prompt-ts]) |
| Tool names outside Claude Code's set | In requests without a billing block, one unmapped tool name triggered the 400; `mcp__<server>__<tool>` names passed ([pi-anthropic-oauth-pr-23]) |

A request classified as third-party draws from usage credits; with none
left, it fails with "You're out of extra usage"
([hermes-agent-issue-72171]).

## The three shapes

| | What it intercepts | What carries the request | Side-effects on Pi |
|---|---|---|---|
| **Shape A: payload patcher** (native path) | `before_provider_request` hook or a `streamSimple` wrapper | Pi's existing Anthropic OAuth transport | Payload patches: tool-name aliasing, system-prompt rewrites, and/or a forged billing header |
| **Shape B: provider proxy** (delegated path) | Registers a new provider | Claude Code SDK or CLI subprocess | Whole alternate inference path with its own state machine |
| **Shape C: provider replacement** (self-owned transport) | Re-registers `anthropic` or registers its own provider | Its own transport straight to `api.anthropic.com` | Replaces OAuth and transport; `pi-anthropic-oauth` also symlinks `~/.Claude Code` to `~/.pi` |

That structural choice dominates every comparison below.

### Shape A — payload patcher (native path)

Keeps Pi using Pi's built-in `anthropic` provider with your OAuth
credentials. The extension hooks `before_provider_request`, or wraps the
provider's `streamSimple`, and rewrites the outbound payload to look
more like Claude Code. The goal is to avoid Anthropic's third-party-tool fingerprinting and
"extra usage" classification. No new provider, no subprocess, no
SDK, no Claude Code installed.

### Correction: the two patchers no longer bet on equal signals

This page described `pi-claude-code-use` and `pi-anthropic-auth` as
complementary bets on two fingerprint signals, tool names versus the
billing header. Measurements since June show three independent
triggers: a missing billing block, Pi vocabulary in `system`, and tool
names outside Claude Code's set (see
[Status, October 2026](#status-october-2026)). Both extensions changed
shape.

- [`@gotgenes/pi-anthropic-auth`](https://github.com/gotgenes/pi-anthropic-auth)
  wraps the `anthropic` provider's `streamSimple`, so compaction and
  `ctx.modelRegistry.streamSimple()` callers are shaped too. It
  prepends the billing block, follows each model's `cc_version` floor,
  replaces Pi's preamble with four neutral lines, drops the `docs`
  section and keeps project context byte-identical. It uses Pi's
  built-in login and adds no tools ([pi-anthropic-auth-architecture]).
- [`@benvargas/pi-claude-code-use`](https://github.com/ben-vargas/pi-packages)
  aliases every non-core tool to `mcp__<server>__<tool>` and rewrites
  three prompt phrases. It sends no billing block, and its maintainer
  has not tested it against a live subscription since 2026-09-11
  ([ben-vargas-pi-packages-pr-37]).

The two compose: `pi-anthropic-auth` runs other extensions'
`before_provider_request` handlers first and shapes last. A quick test
for whether tool names are the trigger (inference from
[pi-anthropic-oauth-pr-23], not a published measurement): if a real
session fails with the third-party 400 and passes when started with
`--tools read,bash,edit,write`, add `pi-claude-code-use`.

Newer Shape A packages: `pi-claude-pro` (billing block, moves `docs`
into the first user message, five-hour and weekly usage footer; never
next to `pi-anthropic-auth`), `pi-claude-max` (billing block from a
`before_provider_request` hook) and `pi-claude-request-compat` (a
separate `claude-compat` provider on Pi's transport).

### Shape B — provider proxy (delegated path)

Registers a new provider that routes LLM calls to Claude Code (as an
SDK query or CLI subprocess). Pi still executes tools locally; CC's
own tool execution is denied so it stays purely as the LLM backend.
Trades off significant per-turn overhead (CC's `claude_code` preset
system prompt on every cold start) for access to Claude Code's
features.

- [`elidickinson/pi-claude-bridge`](https://github.com/elidickinson/pi-claude-bridge):
  Agent SDK through `query()`, with session resume. Since 0.7.0 Claude
  Code receives the `AGENTS.md` and `CLAUDE.md` files Pi loads, the
  `appendSystemPrompt` and `settingSources` options are gone, and
  AskClaude is opt-in. 0.9.0 refuses a turn whose append contains Pi's
  base prompt, which Anthropic's scorer rejects even through the real
  binary ([pi-claude-bridge-changelog]). Claude Code's own settings
  sources stay at their default, so `~/.claude/settings.json` hooks run
  inside bridge turns. On three prompts with Opus 5.5 and no tools,
  issue #140 counted 23,780 tokens through the bridge with default
  settings against 9,397 for the `claude` CLI directly
  ([pi-claude-bridge-issue-140]).
- [`pi-claude-agent-sdk`](https://github.com/pi-pod/pi-claude-agent-sdk):
  a bridge fork that hands Pi's stored Anthropic OAuth credential to
  the Claude Code child.
- [`prateekmedia/claude-agent-sdk-pi`](https://github.com/prateekmedia/claude-agent-sdk-pi):
  the original, without session resume. It still reads `context.tools`
  and `context.systemPrompt`, which Pi 0.86 removed from provider input
  (inference: no Pi tools or prompt reach Claude Code on current Pi).
- [`rchern/pi-claude-cli`](https://github.com/rchern/pi-claude-cli):
  `claude -p` with `--resume`; since Pi 0.84, print mode (`pi -p`) and
  nested agent loops fail ([pi-claude-cli-issue-32]). The fork
  [`@saccolabs/pi-claude-cli`](https://github.com/agustinsacco/pi-claude-cli)
  replaces Claude Code's system prompt with Pi's, serves tools over MCP
  and turns CLI auto-compaction off.
- [`pi-claude-code-provider`](https://github.com/chem/pi-claude-code-provider):
  unmodified `claude -p`; mothballed in favor of `pi-claude-bridge`.
- Forks of `pi-claude-bridge` (schwa, tycronk20): no demonstrated
  divergence or adoption beyond the canonical fork.

### Shape C — full provider replacement (self-owned transport)

Re-registers Pi's `anthropic` provider but replaces almost everything
behind it: its own OAuth login/refresh, its own `streamSimple`
transport calling `api.anthropic.com` directly with the OAuth token,
and its own message/tool conversion. It neither rides Pi's transport
(Shape A) nor delegates to a Claude Code process (Shape B) — it
*impersonates* Claude Code: CC-shaped headers, prompt shaping, and a
`~/.Claude Code` → `~/.pi` symlink so the environment looks like a CC
install. The deepest intervention here.

- [`leohenon/pi-anthropic-oauth`](https://github.com/leohenon/pi-anthropic-oauth):
  own PKCE login and transport. It now uses Pi's model registry and
  ships tests. 0.2.2 namespaces unknown tools as `mcp__pi__<name>`
  ([pi-anthropic-oauth-pr-23]); 0.3.0 reads `TranscriptContext`
  ([pi-anthropic-oauth-pr-33]) and adds a billing block with the identity
  line "You are a Claude agent, built on Anthropic's Claude Agent SDK."
  ([pi-anthropic-oauth-pr-35]).
  Its sanitizer runs over the whole system prompt, project context
  included: in the default `aggressive` mode every standalone `pi` or
  `Pi` becomes `Claude Code`.
- [`pi-sub-anthropic`](https://github.com/spksoft/pi-sub-anthropic): a
  separate provider ported from oh-my-pi, with its own `fetch`
  transport reproducing Claude Code's wire fingerprint.
- [`pi-claude-plan`](https://github.com/sunipan/pi-claude-plan): a
  separate `claude-plan` provider ported from `opencode-anthropic-auth`;
  it reads the pre-0.86 `context.tools`.

## Picking guide

| What you actually want | Pick |
|---|---|
| Claude subscription in Pi, model only, nothing from Claude Code | `pi-anthropic-auth` alone, with usage credits off. |
| Real sessions still fail with the third-party 400 while `--tools read,bash,edit,write` passes (inference, see Shape A) | Add `pi-claude-code-use` for tool-name aliasing. |
| A footer with five-hour and weekly usage | `pi-claude-pro`, instead of `pi-anthropic-auth`, never next to it. |
| Claude Code's own features in Pi (AskClaude, Claude Code skills and subagents) | `pi-claude-bridge`. Expect Claude Code's settings, hooks and preset in every turn. |
| Claude without the subscription classifier | An API key; Max and Team monthly API credits pay for it. Run `/logout anthropic` first, since a stored login wins over `ANTHROPIC_API_KEY` ([pi-models-docs]). |
| Claude through another gateway | GitHub Copilot, OpenCode Zen or Amazon Bedrock, all built into Pi. Pi's Vertex catalog has no Claude models; [`@twogiants/pi-anthropic-vertex`](https://github.com/twoGiants/pi-anthropic-vertex) adds them. |
| Keep working when the subscription limit hits | A router from [Model Routing Extensions](model-routing-extensions.md). |
| Less Claude-specific overhead | `@luan.sh/pi-thinking-binding` (drops invalidated thinking once), `@ogulcancelik/pi-anthropic-image-cap` (caps images). |

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

#### Correction: no measurement backs this ranking

The ranking below reasons about overhead added on top of Pi's own
payload. The one published measurement points the other way: in a
no-tool test with Opus 5.5, `pi-anthropic-auth` used 38,868 tokens
where the bridge used 21,650, and the official `claude` CLI used fewer
than either ([pi-claude-bridge-issue-140]). Treat the order as a
statement about added overhead, not about totals.

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
2. **`pi-claude-cli`**: best test discipline of the four, but print
   mode and nested agent loops fail since Pi 0.84
   ([pi-claude-cli-issue-32]).
3. **`pi-claude-bridge`** — complex state machine; leakage surface
   is *explicitly enumerated and mitigated* (cloud MCP off,
   autocompact off, MCP auto-load off). Each mitigation is one
   place the abstraction could break. Battle-tested but the surface
   is much larger than Shape A.
4. **`claude-agent-sdk-pi`** — same complexity as (3) without
   resume, without tests, without diag-dump paths. The most fragile.

## When to switch from `pi-claude-bridge` to `pi-anthropic-auth`

The bridge buys Claude Code's features (AskClaude, Claude Code skills
and subagents). If you use none of them, `pi-anthropic-auth` adds no Claude Code
settings or hooks and has a smaller failure surface. It does not save
tokens by default: in issue #140's no-tool test, one cold-start prompt
took 10,532 tokens through `pi-anthropic-auth` and 5,922 through the
bridge ([pi-claude-bridge-issue-140]). The two use different provider names
(`claude-bridge` versus `anthropic`), so both can stay installed while
you compare.

## See also

- [Model Routing, Fallback and Usage-Limit Recovery Extensions](model-routing-extensions.md): keep working on another model when the subscription limit hits
- [Anthropic Auth & Billing in Pi](anthropic-auth-and-billing.md) — the platform-level baseline this page sits on top of.
- [pi-claude-bridge](pi-claude-bridge.md) — deep-dive on the dominant Shape B extension.
- [claude-agent-sdk-pi](claude-agent-sdk-pi.md) — deep-dive on the original Shape B (no-resume) implementation.
- [Provider Extensions](provider-extensions.md) — for the broader landscape of non-built-in providers.
- [References — How to Evaluate a Pi Extension](../references/evaluation.md) — for current adoption / maintenance signals on each entry above.
