---
title: Pi Model Routing, Fallback and Usage-Limit Recovery Extensions
type: ecosystem
updated: 2026-10-14
sources:
  - pi-virtual-models-doc
  - pi-virtual-models-ts
  - pi-jev-router-example
  - pi-retry-ts
  - pi-provider-retry-ts
  - pi-settings-docs
  - pi-anthropic-messages-ts
  - pi-transform-messages-ts
  - pi-coding-agent-changelog
  - pi-compat-schema-ts
  - pi-issue-6422
  - claude-code-changelog
  - pi-anthropic-auth
  - alexeiled-pi-model-router
  - shuymn-pi-extensions
  - eiei114-pi-model-fallback
  - ohlulu-pi-keep-going
  - fatpandac-pi-auto-models
  - jiangge-pi-router
  - unrelentingfox-pi-model-fallback-alias
  - danialranjha-pi-auto-router
  - weisanju-pi-plugins
  - kivlor-pi-multiplexer
  - kenbanks-peng-pi-virtual-model
  - robertn702-reasoning-router
  - ekil1100-pi-auto
  - chxsong-pi-auto-continue
  - uzunkonak-pi-retry
  - gooyoung-pi-failover
  - cad0p-pi-fallback-provider
  - dev-willbird1936-pi-fallback-models
  - rioliu-pi-tier-router
  - npm-pi-shift-router
  - kasaiarashi-pi-auto-resume
  - npm-pi-jev-effort
  - npm-pi-refusal-guard
  - pi-model-router
  - lnilluv-pi-opencode-go-rotation
  - pi-provider-litellm
  - pi-blackhole
tags: [extension, routing, fallback, failover, rate-limit, virtual-model, anthropic, claude]
entries:
  - id: alexeiled-pi-model-router
    name: "@alexeiled/pi-model-router"
    repo: alexei-led/pi-model-router
    npm: "@alexeiled/pi-model-router"
    role: provider-proxy
    notes: "Provider `router`, one model per profile (`router/<profile>`). Tiers `high`/`medium`/`low`/`micro`, each with `model`, `thinking` and `fallbacks`. Generates through `ctx.modelRegistry.streamSimple()`, so Pi's auth and provider wrappers apply. Any error before the first content event moves the same request to the next fallback; a new user turn starts on the tier's primary again. Optional classifier advisor. Fork of yeliu84/pi-model-router; peers on Pi ^1.1.0; large test suite."
  - id: shuymn-pi-extensions
    name: "fallback/auto (shuymn/pi-extensions)"
    repo: shuymn/pi-extensions
    role: virtual-model-router
    notes: "About 250 lines in three files (`extensions/fallback-model/index.ts`, `lib/fallback-router.ts`, `lib/model-spec.ts`) on `pi.registerVirtualModel()`. On `reason: retry` it records the failed model in router state and returns the first unattempted candidate; Pi's own retry decides which errors qualify. `user` requests start on the first candidate again. GitHub only; the README asks users to copy and adapt it."
  - id: eiei114-pi-model-fallback
    name: pi-model-fallback
    repo: eiei114/pi-model-fallback
    npm: pi-model-fallback
    role: event-hook-switcher
    notes: "At `agent_before_settle` calls `pi.setModel(fallback)`, omits the failed entry with a `context_edit` and returns `continue: true`. Status rules (default 429, 500, 502, 503, 504). Return to the original model is manual (`/model-fallback:reset`); default 429 cooldown 72 hours."
  - id: ohlulu-pi-keep-going
    name: pi-keep-going
    repo: ohlulu/pi-keep-going
    npm: pi-keep-going
    role: wait-and-resume
    notes: "Claude Code style wait: reads `five_hour.resets_at` from Anthropic's OAuth usage endpoint and sends `continue` at the reset plus 90 seconds. No fallback model. Five-hour window only."
  - id: fatpandac-pi-auto-models
    name: pi-auto-models
    repo: Fatpandac/pi-auto-models
    npm: pi-auto-models
    role: event-hook-switcher
    notes: "Primary/fallback pair with thinking levels. Switches on 429/529 or `rate_limit_error` text; returns to the primary only at session start, after checking the OAuth usage endpoint. Forces its pair at every session start."
  - id: jiangge-pi-router
    name: pi-router
    repo: jiangge/pi-router
    npm: pi-router
    role: provider-proxy
    notes: "Provider `router`, failover on 429, 408, 5xx and network errors with a circuit breaker. Sticky routing is on by default and persisted, so a session stays on the fallback until the fallback fails. Summarises context when the target window is smaller."
  - id: unrelentingfox-pi-model-fallback-alias
    name: pi-model-fallback-alias
    repo: unrelentingfox/pi-model-fallback-alias
    npm: pi-model-fallback-alias
    role: provider-proxy
    notes: "Provider `alias` with ordered chains and exponential cooldowns shared across Pi processes; the strongest test discipline in the niche. Rewrites every assistant message to the alias identity, so Claude's signed thinking replays as text."
  - id: danialranjha-pi-auto-router
    name: pi-auto-router
    repo: danialranjha/pi-auto-router
    npm: pi-auto-router
    role: provider-proxy
    notes: "Policy engine, quota pacing, prompt-prefix and keyword intent routing. Generates through `@earendil-works/pi-ai/compat` with tokens read from `auth.json`, outside Pi's provider wrappers, and replaces the system prompt with one that appends a tool-naming section."
  - id: weisanju-pi-plugins
    name: pi-model-auto-router
    repo: weisanju/pi-plugins
    npm: pi-model-auto-router
    role: provider-proxy
    notes: "Load balancing and failover across `models.json` providers. API keys only (no OAuth); routed requests are priced at zero."
  - id: kivlor-pi-multiplexer
    name: "@kivlor/pi-multiplexer"
    npm: "@kivlor/pi-multiplexer"
    role: virtual-model-router
    notes: "Intended to advance to the next model on a 429 retry. Reads `request.failed?.errorMessage`, while Pi passes the text at `failed.message.errorMessage`, so the switch never fires. No repository, no tests."
  - id: kenbanks-peng-pi-virtual-model
    name: "@npm-ken/pi-virtual-model"
    repo: kenbanks-peng/pi-virtual-model
    npm: "@npm-ken/pi-virtual-model"
    role: virtual-model-router
    notes: "Jev classifier picks a `quick`, `balanced` or `deep` option (model plus thinking level) under one provider. No provider failover. No license."
  - id: robertn702-reasoning-router
    name: "@reasoning-router/pi"
    repo: robertn702/reasoning-router
    npm: "@reasoning-router/pi"
    role: effort-router
    notes: "One virtual model per Claude model; a classifier picks only the thinking level. On models with mid-conversation effort, Pi sends effort changes as messages, so the cached prefix survives."
  - id: ekil1100-pi-auto
    name: pi-auto
    repo: ekil1100/pi-auto
    npm: pi-auto
    role: effort-router
    notes: "`before_agent_start` picks a thinking level per prompt (Pi classifier or a chat-model judge) and calls `pi.setThinkingLevel()`. Never changes the model."
  - id: chxsong-pi-auto-continue
    name: pi-auto-continue
    repo: chxsong/pi-auto-continue
    npm: pi-auto-continue
    role: wait-and-resume
    notes: "Waits for a parsed reset (CodexBar, headers, error text) and resumes, by default through a handoff document in a new session. For an Anthropic OAuth 429 without CodexBar, no reset time is visible."
  - id: uzunkonak-pi-retry
    name: "@uzunkonak/pi_retry"
    repo: uzunkonak/pi_retry
    npm: "@uzunkonak/pi_retry"
    role: wait-and-resume
    notes: "Wraps `globalThis.fetch` to record status and headers of failed responses (including `anthropic-ratelimit-unified-*-reset`), waits for the earliest reset or polls, then resumes with a triggered message."
---

# Pi Model Routing, Fallback and Usage-Limit Recovery Extensions

For a Claude-primary setup, `@alexeiled/pi-model-router` is the most
complete pick: per-tier model and thinking level, same-request failover
to a fallback list, and the primary model again on the next user turn,
all through Pi's own transport so OAuth shapers such as
`pi-anthropic-auth` stay in the path. The smallest correct option is a
`pi.registerVirtualModel()` router like shuymn's `fallback/auto`, meant
to be copied and adapted. To wait out a Claude limit on the same model,
as Claude Code does, use `pi-keep-going`.

None of the packages that keep Pi's transport in the path returns to
Claude at the reset time; [Gaps](#gaps) sketches the router that would.

## Contents

- [What Pi core does](#what-pi-core-does)
- [Four shapes](#four-shapes)
- [Comparison](#comparison)
- [Packages with a catch](#packages-with-a-catch)
- [Claude specifics](#claude-specifics)
- [Waiting instead of switching](#waiting-instead-of-switching)
- [Gaps](#gaps)
- [Long tail](#long-tail)
- [Picking a router](#picking-a-router)

## What Pi core does

- `settings.retry` retries a failed request up to 3 times, after 2 s,
  4 s and 8 s, when the error text matches a retryable pattern
  (`rate.?limit`, `429`, `overloaded`, 5xx, network). Quota and billing
  texts (`GoUsageLimitError`, `insufficient_quota`, `out of budget`,
  `quota exceeded`, `billing`) end the turn at once ([pi-retry-ts],
  [pi-settings-docs]).
- Provider-level retry (`retry.provider.maxRetries`) defaults to 0
  ([pi-provider-retry-ts]).
- An Anthropic OAuth rate or usage limit arrives as
  `429 rate_limit_error` with the text "This request would exceed your
  account's rate limit", which names no reset time ([pi-issue-6422]). It
  matches the retryable pattern, so Pi spends its three retries on the
  same model, then ends the turn.
- Virtual models (v0.99.0, experimental) are registered by an extension
  and appear in `/model` like any model. `route(request, ctx)` runs
  before every request with `reason` `user`, `continuation`, `retry` or
  `direct`; on `retry`, `request.failed.message.errorMessage` holds the
  error ([pi-virtual-models-doc], [pi-virtual-models-ts]). Other errors
  Pi does not retry (quota and billing texts, 400s) never reach
  `route()`; a context overflow does, as `retry` after compaction. A
  virtual model cannot route to another virtual model.
- `after_provider_response` fires only after the Anthropic SDK accepts
  a response, so no extension event carries the status or headers of a
  failed request ([pi-anthropic-messages-ts]).
- Signed and redacted thinking is replayed only when provider, API and
  model of the stored message equal the target; otherwise thinking
  becomes text and redacted thinking is dropped
  ([pi-transform-messages-ts]).
- Switching models between turns loses the prompt cache. Returning
  `request.previous` for continuations and `request.failed` for retries
  keeps cache and thinking signatures valid ([pi-virtual-models-doc]).
- `compat.allowedFallbackModels` lists the models Anthropic may use for
  its server-side refusal fallback; it does nothing for usage limits
  ([pi-compat-schema-ts]).

A minimal virtual model, from the Pi docs:

```typescript
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

export default function (pi: ExtensionAPI) {
  pi.registerVirtualModel({
    provider: "router",
    id: "auto",
    name: "Auto",
    thinkingLevels: ["low", "high"],
    route(request, ctx) {
      const sticky = request.failed ?? request.previous;
      if (request.reason !== "user" && sticky) {
        return { model: sticky.model, thinkingLevel: sticky.thinkingLevel ?? "medium" };
      }
      const id = request.thinkingLevel === "high" ? "claude-sonnet-4-5" : "claude-haiku-4-5";
      return { model: ctx.modelRegistry.find("anthropic", id)!, thinkingLevel: "medium" };
    },
  });
}
```

Placed in `~/.pi/agent/extensions/<name>.ts`, it is selected as
`router/auto`. [`jev-router.ts`](https://github.com/earendil-works/pi/blob/06a466935536f8c9bcacb2d5efc0fc021be1bdff/packages/coding-agent/examples/extensions/jev-router.ts)
is the complete example: a classifier picks a strong model for
planning, then one switch to a cheaper model, with the phase kept in
router state ([pi-jev-router-example]).

## Four shapes

| Shape | Hooks in through | Claude transport | Entries |
|---|---|---|---|
| Virtual-model router | `pi.registerVirtualModel()`; Pi dispatches the physical model | Pi's own, wrappers apply | `fallback/auto`, `@npm-ken/pi-virtual-model`, `@reasoning-router/pi`, `@kivlor/pi-multiplexer` |
| Provider proxy | registers a provider (`router/...`) and streams the target itself | Pi's own when it calls `ctx.modelRegistry` or `getProvider().streamSimple`; bypassed through `@earendil-works/pi-ai/compat` | `@alexeiled/pi-model-router`, `pi-router`, `pi-model-fallback-alias`, `pi-auto-router`, `pi-model-auto-router` |
| Event-hook switcher | `pi.setModel()` from `agent_before_settle` or `message_end` | Pi's own | `pi-model-fallback`, `pi-auto-models` |
| Wait and resume | waits for the reset, then sends a continue message | Pi's own | `pi-keep-going`, `pi-auto-continue`, `@uzunkonak/pi_retry` |

Effort routers change only the thinking level: `@reasoning-router/pi`
(virtual model) and `pi-auto` (`pi.setThinkingLevel()` per prompt).

## Comparison

| Package | Fails over on | Switch happens | Back to primary | Model and effort choice |
|---|---|---|---|---|
| `@alexeiled/pi-model-router` | any error before the first content event | same request | next user turn | tiers with model + thinking; optional classifier advisor |
| `fallback/auto` | errors Pi retries | Pi's first retry (2 s) | next user turn | optional `:level` per candidate, else the selected level |
| `pi-model-fallback` | configured statuses (default 429, 500, 502, 503, 504) | after Pi's retries, same run | manual reset; cooldown for later sessions | none |
| `pi-auto-models` | `429`, `rate_limit_error` or "rate limit" in the error text | before Pi's retry | next session start | fixed primary/fallback levels |
| `pi-router` | 429, 408, 5xx, network | same request | none while sticky (default) | capability, latency, cost sort |
| `pi-model-fallback-alias` | auth, connection, HTTP errors before output | same request | after a 5 min to 1 h cooldown | none |
| `pi-auto-router` | broad substring list, including `401` and `400 status code` | same request | after a reset parsed from the error, else 2 min for a 429 | prompt prefixes (`@reasoning`, `@fast`), keyword intent, policy rules |
| `pi-model-auto-router` | transient, quota and config markers | same request | after a 60 s or 12 h cooldown | none |
| `@npm-ken/pi-virtual-model` | none | n/a | n/a | classifier picks quick, balanced or deep |
| `@reasoning-router/pi` | none | n/a | n/a | classifier picks thinking level |
| `pi-auto` | none | n/a | n/a | thinking level per prompt |

`@alexeiled/pi-model-router` config (`~/.pi/agent/model-router.json`,
then select `router/claude`):

```json
{
  "profiles": {
    "claude": {
      "high":   { "model": "anthropic/claude-opus-5-5", "thinking": "high",
                  "fallbacks": ["opencode-go/mimo-v2.6-pro"] },
      "medium": { "model": "anthropic/claude-opus-5-5", "thinking": "medium",
                  "fallbacks": ["opencode-go/mimo-v2.6-pro"] },
      "low":    { "model": "anthropic/claude-haiku-5-5", "thinking": "low",
                  "fallbacks": ["opencode-go/muse-spark-1.3-contributor"] }
    }
  }
}
```

While Claude stays limited, each new user turn first gets a fast 429
from Claude, then runs on the fallback; the first user turn after the
reset runs on Claude again. Without error classification, a malformed
request (a 400) fails over too. The advisor needs a Pi classifier with
credentials, such as `typesafe/jev-latest` or `openai/gpt-6-luna`
([alexeiled-pi-model-router]).

`fallback/auto` needs only a flag:
`pi --model fallback/auto --fallback-model 'anthropic/claude-opus-5-5,opencode-go/mimo-v2.6-pro:high'`
([shuymn-pi-extensions]).

## Packages with a catch

- `pi-auto-router` imports `streamSimple` from
  `@earendil-works/pi-ai/compat` and reads tokens from `auth.json`, so
  Claude requests skip provider wrappers such as `pi-anthropic-auth`.
  Its `before_agent_start` handler appends a "Tool naming (IMPORTANT)"
  section to the system prompt of every session, whichever model is
  selected ([danialranjha-pi-auto-router]). It reads the `five_hour`
  and `seven_day` reset times from Anthropic's OAuth usage endpoint for
  its quota pacing.
- `pi-model-fallback-alias` sets `provider`, `api` and `model` of every
  message to the alias, so Claude's signed thinking replays as text
  after the first turn ([unrelentingfox-pi-model-fallback-alias]).
- `pi-router` keeps the last successful route while `sticky` is on (the
  default); `"sticky": false` lets the primary return after its
  cooldown ([jiangge-pi-router]).
- `@kivlor/pi-multiplexer` reads `request.failed?.errorMessage`; Pi
  passes the text at `failed.message.errorMessage`, so its switch
  never fires ([kivlor-pi-multiplexer], [pi-virtual-models-ts]).
- `pi-model-fallback` defaults to a 72-hour cooldown after a 429; set
  `cooldownMs` per rule (`18000000` for five hours). Its header-based
  cooldowns never see an Anthropic 429, for the reason above
  ([eiei114-pi-model-fallback]).
- `pi-model-auto-router` supports API keys only and prices routed
  requests at zero ([weisanju-pi-plugins]).

## Claude specifics

The reset time of a Claude subscription limit has three sources:

| Source | Used by |
|---|---|
| `GET https://api.anthropic.com/api/oauth/usage` (OAuth token, `anthropic-beta: oauth-2025-04-20`): `five_hour.resets_at` and the weekly window | `pi-keep-going`, `pi-auto-models` (session start), `pi-auto-router` (quota pacing) |
| `anthropic-ratelimit-unified-5h-reset` and related headers on successful responses | `pi-auto-models` |
| Headers of the failed 429, through a `globalThis.fetch` wrapper | `@uzunkonak/pi_retry` |

Routers that leave the physical model on each message (virtual models,
`pi.setModel()` switchers, proxies that forward events unchanged) let
Claude's signed thinking replay when Claude answers again; turns from
the fallback replay as text ([pi-transform-messages-ts]). After a
multi-hour limit, Claude's prompt cache has expired anyway, so the
switch back costs one full prompt read.

`pi-anthropic-auth` wraps the `anthropic` provider's `streamSimple`.
Virtual models, `pi.setModel()` switchers and proxies that dispatch
through `ctx.modelRegistry` keep that wrapper; proxies that call
`@earendil-works/pi-ai/compat` directly do not ([pi-anthropic-auth]).

## Waiting instead of switching

Claude Code 2.1.234 continues a session automatically when a claude.ai
usage limit resets, controlled in `/config` ("Continue automatically
at usage limit") ([claude-code-changelog]). Pi equivalents:

| Package | Reset source for Claude | Resume |
|---|---|---|
| `pi-keep-going` | OAuth usage endpoint, five-hour window | `continue` at reset + 90 s, jobs persisted per branch |
| `pi-auto-continue` | CodexBar, then headers and error text (none for an Anthropic OAuth 429) | handoff to a new session (default) or a follow-up message |
| `@uzunkonak/pi_retry` | failed-response headers through its `fetch` wrapper, then text, then polling | triggered custom message |

A router with fallbacks rarely lets a run end in an error, so waiting
extensions fire only when every fallback failed too. `pi-keep-going`
detects limits by `ctx.model.provider`, so it stays silent while a
virtual or proxy model is selected ([ohlulu-pi-keep-going]).

## Gaps

1. Switch-back is a probe on every user turn
   (`@alexeiled/pi-model-router`, `fallback/auto`), a cooldown timer, a
   session restart, or manual. Among packages that keep Pi's transport,
   none reads the reset time and returns at that moment; `pi-auto-router`
   reads it for quota pacing but generates outside Pi's transport.
2. Pi retries a usage limit and a transient throttle alike. Claude Code
   distinguishes server rate limits from plan usage limits
   ([claude-code-changelog]).
3. `pi-keep-going` reads only the five-hour reset and
   `@uzunkonak/pi_retry` takes the earliest reported window; after a
   spent weekly limit both resume into the same error.
4. An effort router and a fallback router cannot be stacked, because a
   virtual model cannot route to another; one `route()` has to do both.

A virtual model that closes gaps 1 and 3 (sketch, not a published
package). `claudeResetAt()` would call the OAuth usage endpoint with
`ctx.modelRegistry.getApiKeyForProvider("anthropic")` and return the
later reset of the exhausted windows:

```typescript
let blockedUntil = 0;
pi.registerVirtualModel({
  provider: "claude-plus", id: "auto", name: "Claude, MiMo fallback",
  thinkingLevels: ["low", "medium", "high", "xhigh"],
  async route(req, ctx) {
    const claude = ctx.modelRegistry.find("anthropic", "claude-opus-5-5")!;
    const mimo = ctx.modelRegistry.find("opencode-go", "mimo-v2.6-pro")!;
    const failed = req.failed;
    if (req.reason === "retry" && failed?.model.provider === "anthropic" &&
        /rate_limit_error|\b429\b/.test(failed.message.errorMessage ?? "")) {
      blockedUntil = (await claudeResetAt(ctx, req.signal)) ?? Date.now() + 15 * 60_000;
    }
    if (req.reason === "continuation" && req.previous) {
      return { model: req.previous.model, thinkingLevel: req.previous.thinkingLevel ?? req.thinkingLevel };
    }
    const model = Date.now() < blockedUntil ? mimo : claude;
    return { model, thinkingLevel: req.thinkingLevel };
  },
});
```

Task-aware tier and effort choice would sit in the same `route()`, for
example with `ctx.modelRegistry.classify()` as in `jev-router.ts`.

## Long tail

From package descriptions and READMEs; not code-read.

| Package | What it does |
|---|---|
| [`pi-failover`](https://github.com/gooyoung/pi-failover) | backup keys for one provider, then provider failover via `setModel` ([gooyoung-pi-failover]) |
| [`@cad0p/pi-fallback-provider`](https://github.com/cad0p/pi-fallback-provider) | cycles models at `agent_before_settle` after Pi's own recovery ([cad0p-pi-fallback-provider]) |
| [`pi-fallback-models`](https://github.com/dev-willbird1936/pi-fallback-models) | ordered fallbacks after eligible failures, including quota errors ([dev-willbird1936-pi-fallback-models]) |
| [`pi-tier-router`](https://github.com/rioliu/pi-tier-router) | virtual `router/auto` between a flash and a pro model ([rioliu-pi-tier-router]) |
| [`pi-shift-router`](https://www.npmjs.com/package/pi-shift-router) | a small judge picks a cheap or strong tier per message ([npm-pi-shift-router]) |
| [`pi-auto-resume`](https://github.com/kasaiarashi/pi-auto-resume) | waits for `retry-after`, then backs off; quota errors only notify ([kasaiarashi-pi-auto-resume]) |
| [`pi-jev-effort`](https://www.npmjs.com/package/pi-jev-effort) | thinking level per prompt from Jev, clamped by remaining quota ([npm-pi-jev-effort]) |
| [`pi-refusal-guard`](https://www.npmjs.com/package/pi-refusal-guard) | Claude refusal rescue and refusal-fallback retargeting ([npm-pi-refusal-guard]) |

Adjacent, covered elsewhere: key rotation for OpenCode Go
(`pi-opencode-go-rotation`), model-group routing (`pi-model-router`)
and LiteLLM proxy discovery (`pi-provider-litellm`, where LiteLLM itself
can fail over) in [Provider Extensions](provider-extensions.md); fallback chains for
compaction workers (`pi-blackhole`) in
[Compaction Extensions](compaction-extensions.md).

## Picking a router

| If you want | Use | Why |
|---|---|---|
| Claude first, a fallback when limited, Claude again next turn, plus per-tier thinking | `@alexeiled/pi-model-router` | same-request failover through Pi's transport; tiers carry model and thinking |
| The same with the least code | `fallback/auto` (copy its three files, or `pi install` the repo and enable only `fallback-model` in `pi config`) | Pi's retry decides eligibility; state lives on the session branch |
| An npm package that continues the failed run on a fallback | `pi-model-fallback` with `cooldownMs` set | no prompt re-send; return to Claude is manual |
| Claude Code's wait-and-continue | `pi-keep-going` | reads the real five-hour reset from the OAuth usage endpoint |
| Only smarter thinking levels on Claude | `@reasoning-router/pi` (`pi-auto` is broken on Pi 1.2, see above) | effort changes keep the cached prefix on Opus 5.5 |
| Return to Claude exactly at the reset | a custom virtual model ([Gaps](#gaps)) | no package does it yet |

## Pi 1.2 sweep, 2026-10-14

A static sweep of 220 extensions found two breakages in this
category. `pi-auto` passes `task: event.prompt` into `input.task.length`,
which throws on 1.2 custom runs; gate on `event.messageType === "user"`
first. The sibling `one-shot` extension in `shuymn/pi-extensions` reads
`event.prompt.indexOf` unguarded with the same failure; `fallback/auto`
itself is unaffected. Prefer `@reasoning-router/pi` for effort-only
routing until `pi-auto` is fixed. Everything else here is green or
unaffected.

## See also

- [Claude Pro/Max Subscription Extensions](claude-subscription-extensions.md): the OAuth shapers these routers must keep in the path
- [Provider Extensions](provider-extensions.md): fallback targets (OpenCode Go, Nebius, EU providers) and key rotation
- [Pi Year One](../references/pi-year-one.md): when virtual models and the other primitives landed
- [How to Evaluate a Pi Extension](../references/evaluation.md): live adoption and maintenance signals
