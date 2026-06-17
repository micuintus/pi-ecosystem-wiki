---
title: Pi Provider Extensions
type: ecosystem
updated: 2026-06-17
sources:
  - awtotty-pi-opencode
  - lnilluv-pi-opencode-go-rotation
  - mosquito-tokenfactory-pi
  - mdsitton-pi-opencode-provider
  - pi-issue-1757
  - pi-issue-3348
  - oh-my-pi-pr-310
  - openclaw-pr-67556
  - nebius-token-factory
  - eurouter-ai
  - llmbase-ai
  - tensorix-ai
  - aki-io
  - juicefactory-ai
  - infomaniak-ai
  - cortecs-ai
  - wayland-ai
  - mistral-ai
  - kimi-k2-6
  - stackit-ai-model-serving
  - scaleway-generative-apis
  - scaleway-managed-inference
  - eurouter-about
  - eurouter-hn-comment
  - llmbase-eyloo
  - tensorix-ltd
  - juicefactory-founders
  - infomaniak-about
  - aki-io-berlin
  - langdock-berlin
  - xydra-labs
  - exalsius
  - berlin-ai-labs
  - polarise
  - vective
  - basebox
  - sovereignty-washing-cispe
  - aws-european-sovereign-cloud
  - azure-eu-data-boundary
  - google-cloud-eu-sovereign
  - pi-model-router
  - pi-provider-litellm
  - aki-io-models
  - polarise-baremetal
  - basebox-llm-recommendations
  - nervur-architecture
  - micuintus-pi-eurouter
  - apmantza-pi-free
  - pi-kilocode
  - ditfetzt-pi-cline-free
  - aadishv-pi-agy
  - cfal-pi-models-dev
  - MasuRii-pi-model-discovery
entries:
  - id: awtotty-pi-opencode
    name: pi-opencode
    repo: awtotty/pi-opencode
    npm: pi-opencode
    role: static-provider
    notes: "Static OpenCode Zen + Go provider; 40+ models mapped manually"
  - id: lnilluv-pi-opencode-go-rotation
    name: pi-opencode-go-rotation
    repo: lnilluv/pi-opencode-go-rotation
    npm: "@lnilluv/pi-opencode-go-rotation"
    role: key-rotation
    notes: "Reactive key rotation for OpenCode Go; watchdog stall detection; multi-key commands"
  - id: mosquito-tokenfactory-pi
    name: tokenfactory-pi
    repo: mosquito/tokenfactory-pi
    npm: tokenfactory-pi
    role: dynamic-provider
    notes: "Runtime model discovery for Nebius Token Factory; fetches live catalog on startup"
  - id: micuintus-pi-eurouter
    name: pi-eurouter
    repo: micuintus/pi-eurouter
    npm: pi-eurouter
    role: dynamic-provider
    notes: "EUrouter provider; fetches live model catalog; thinking-level map for reasoning models"
  - id: apmantza-pi-free
    name: pi-free-providers
    repo: apmantza/pi-free
    role: free-multi-provider
    notes: "Multi-provider free-tier bundle: Kilo, Cline, NVIDIA NIM, LLM7, ZenMux, CrofAI, Ollama Cloud, SambaNova, and more"
  - id: pi-kilocode
    name: pi-kilocode
    npm: pi-kilocode
    role: free-provider
    notes: "Kilo Gateway provider with device-auth OAuth; fetches live catalog; free tier available"
  - id: ditfetzt-pi-cline-free
    name: pi-cline-free-models
    repo: ditfetzt/pi-cline-free-models
    npm: pi-cline-free-models
    role: free-provider
    notes: "Cline free models provider; OAuth via SSO; dynamic catalog fetch on startup"
  - id: mdsitton-pi-opencode-provider
    name: pi-opencode-provider
    npm: pi-opencode-provider
    role: dynamic-provider
    notes: "Runtime model discovery for OpenCode Zen + Go; unconditionally replaces both built-in providers; no test suite; pi.dev/npm only"
  - id: pi-model-router
    name: pi-model-router
    npm: pi-model-router
    role: model-router
    notes: "Routes model group names to concrete provider/model pairs; 24 providers; no Pi-specific EU provider extensions found"
  - id: pi-provider-litellm
    name: pi-provider-litellm
    repo: balcsida/pi-provider-litellm
    role: proxy-provider
    notes: "Discovers models from a self-hosted LiteLLM proxy; can front any OpenAI-compatible endpoint including EU providers"
  - id: cfal-pi-models-dev
    name: pi-models-dev
    repo: cfal/pi-models-dev
    role: dynamic-provider
    notes: "Runtime models.dev catalog fetcher; opts into replacing specific built-ins via PI_MODELS_DEV_OVERRIDE_PROVIDERS; per-model compat via models.json"
  - id: MasuRii-pi-model-discovery
    name: pi-model-discovery
    repo: MasuRii/pi-model-discovery
    npm: pi-model-discovery
    role: dynamic-discovery-framework
    notes: "General multi-provider discovery framework; cache-first + background refresh; declines pi-mono-managed provider IDs by default"
---

# Pi Provider Extensions

Third-party provider extensions for Pi that add or augment LLM backends.
Pi ships with built-in providers for OpenCode Zen, OpenCode Go, Nebius,
and many others; these extensions exist when users want **runtime model
discovery** (new models without waiting for a Pi release) or **key-management
utilities** (rotation, quota bypass) that the core does not provide.

> **Looking for Claude Pro/Max specifically?** This page covers the
> general provider landscape (OpenCode, Nebius, EU/privacy-forward
> backends). For bringing an Anthropic subscription into Pi — the
> payload-patcher vs provider-proxy shapes, the SDK/CLI bridges, and
> the billing implications — see
> [Claude Pro/Max Subscription Extensions](claude-subscription-extensions.md)
> and [Anthropic Auth & Billing in Pi](anthropic-auth-and-billing.md).

## TL;DR

- **Using OpenCode Zen or Go?** Pi has built-in providers — no extension
  needed. Only install a discovery extension if you want newer models than
  Pi's baked snapshot. Prefer `cfal/pi-models-dev` (scoped opt-in override,
  preserves built-in compat via `models.json`); `mdsitton/pi-opencode-provider`
  works but unconditionally replaces both built-ins and ships no tests.
  `MasuRii/pi-model-discovery` is the heavy general framework, overkill for
  OpenCode Go alone.
- **Hitting OpenCode Go rate limits with multiple keys?** Install
  `pi-opencode-go-rotation` — it rotates keys reactively; it's a
  key-management companion, not a provider.
- **Using Nebius Token Factory?** Pi has a built-in provider — no extension
  needed. Only install `tokenfactory-pi` if you are on an older Pi version
  or specifically want runtime catalog discovery.
- **Want EU-hosted open-weight models via EUrouter?** Install
  `pi install npm:pi-eurouter` — live catalog fetch, thinking-level map
  for reasoning models, EU-hosted routing.
- **Want free inference without a paid API key?** See
  [Free inference providers](#free-inference-providers) —
  `pi-free-providers`, `pi-kilocode`, and `pi-cline-free-models` all
  expose free or free-tier models.
- **Prefer a simple static mapping?** `awtotty/pi-opencode` is a minimal
  git-installable alternative, though it lags behind built-in support.
- **No Pi-specific extensions exist for most EU providers** (STACKIT,
  Scaleway, LLMbase, Tensorix, Juice Factory, Infomaniak, AKI.IO, etc.),
  though `pi-eurouter` covers EUrouter specifically. For others: use Pi's
  built-in generic OpenAI provider with a custom `baseUrl`, or install
  `balcsida/pi-provider-litellm` to discover models through a LiteLLM
  proxy. See
  [EU / privacy-forward providers — the gap](#eu--privacy-forward-providers--the-gap).

## What each extension does

### `awtotty/pi-opencode` — static OpenCode Zen + Go provider

A minimal provider extension that registers OpenCode Zen (pay-as-you-go)
and OpenCode Go (subscription credits) as first-class Pi providers.
It maps 40+ models across GPT, Claude, Gemini, GLM, Kimi, Qwen, and MiniMax
to the correct backend endpoints (OpenAI Chat Completions or Anthropic
Messages). Model IDs are hardcoded in the extension source; new models
require an extension update.

Install via git URL or clone into `~/.pi/agent/extensions/`. Requires
`OPENCODE_API_KEY` environment variable.

### `mdsitton/pi-opencode-provider` — runtime OpenCode model discovery

Replaces the built-in `opencode` and `opencode-go` providers with
**runtime-discovered** model lists. On every Pi startup it fetches
OpenCode's live `/models` endpoints, merges metadata from `models.dev`,
and registers the resolved catalog. New OpenCode models appear immediately
without waiting for a Pi release. Falls back to conservative defaults
(128k context, 16k max tokens) if metadata is unavailable.

The author notes that this extension is not strictly required — Pi has
built-in OpenCode support — but the built-in list is statically generated
at build time. This extension is for users who want the freshest catalog.

Install: `pi install npm:pi-opencode-provider`. Then run `/login` and select
OpenCode Zen or OpenCode Go to store the API key through the OAuth flow.

> **Caveat (2026-06-17 audit):** it **unconditionally** replaces both
> built-in providers, discarding Pi's curated `compat`/`thinkingLevelMap`
> overrides for models like Kimi K2.6, DeepSeek V4 Flash, and MiniMax —
> with no per-model override mechanism. The package also ships **no test
> suite** (only `typecheck`), which is the wiki evaluation page's explicit
> red flag for extensions that touch every request. Prefer
> `cfal/pi-models-dev` (below) where built-in compat must be preserved.

### `cfal/pi-models-dev` — scoped models.dev discovery

A runtime [models.dev](https://models.dev) catalog fetcher with a
deliberately opt-in design: **it does not replace Pi built-ins unless
explicitly named** in `PI_MODELS_DEV_OVERRIDE_PROVIDERS`. Pointed at
`PI_MODELS_DEV_OVERRIDE_PROVIDERS=opencode-go`, it fetches the live
models.dev catalog and registers `opencode-go` models (including models
Pi's baked snapshot is missing) while leaving `opencode`, `zai`, and
every other built-in provider untouched.

Provider and per-model `compat` overrides are mergeable via
`~/.pi/agent/models.json` (`providers[id].compat` and
`modelOverrides`), so the hand-tuned flags Pi's generator applies to
Kimi/DeepSeek/MiniMax/Qwen can be re-attached instead of lost. The
catalog is cached (24h TTL, `PI_MODELS_DEV_OFFLINE` for cache-only).

Installed from git (not yet on npm at time of writing):

```bash
pi install git:github.com/cfal/pi-models-dev
PI_MODELS_DEV_OVERRIDE_PROVIDERS=opencode-go pi --list-models
```

> **Scope/freshness note:** single-author, no tagged releases, git-only
> at audit time — treat as `[experimental]` under the evaluation page's
> maturity tags. The codebase is TypeScript-strict with a `bun test`
> suite covering conversion and filtering, and zero `any`/`@ts-ignore`.

### `MasuRii/pi-model-discovery` — general multi-provider discovery framework

The most extensive discovery package in the ecosystem: cache-first
registration with background refresh, debounce, provenance tracking, an
idempotent registrar with explicit ownership semantics, and a `/pi-model-discovery`
catalog command. Enriches discovered models from models.dev and OpenRouter,
classifies free-tier models, and covers OpenAI-compatible, Ollama,
LM Studio, llama.cpp, and Anthropic-compatible backends.

For the OpenCode Go use case specifically there is a **functional
mismatch**: by design it declines to auto-import provider IDs whose
credentials are owned by Pi Mono (i.e. an `opencode-go` entry already in
`auth.json`), to avoid duplicate ownership. It will therefore not
replace Pi's baked `opencode-go` list without manual per-provider config
in `config.json`. Best suited to users who want unified discovery across
**many** self-hosted / local / paid providers, not a drop-in OpenCode Go
refresh.

Install: `pi install npm:pi-model-discovery`.

### `lnilluv/pi-opencode-go-rotation` — multi-key rotation for OpenCode Go

Not a provider itself, but a **key-management companion** for the
OpenCode Go provider. It rotates between multiple API keys when rate
limits (HTTP 429) or silent stalls are detected. The extension is
best-effort and reactive: it does not check quotas ahead of time, but
switches keys as soon as OpenCode surfaces an error.

Features:
- **Surfaced-error rotation**: detects 429 / quota errors and marks the
  current key on cooldown (default 60 min), then switches to the next
  available key via `setRuntimeApiKey`.
- **Silent-stall watchdog**: if an `opencode-go` request has no stream
  activity for a configurable window (default 90s), the extension aborts
  the turn, rotates keys, and rewrites the abort as a retryable timeout.
- **Key management commands**: `/opencode add`, `/opencode rm`,
  `/opencode use`, `/opencode next`, `/opencode status`, plus cooldown
  and watchdog configuration.

Keys are stored in `~/.pi/agent/opencode-keys.json` with `0600` permissions.
Pair with Pi's built-in auto-retry (`maxRetries` >= number of keys) for
best results.

### `mosquito/tokenfactory-pi` — runtime Nebius Token Factory discovery

Discovers the live Nebius Token Factory model catalog on startup and
registers all tool-capable models as the `nebius` provider. No static
model list is baked in; the extension queries
`GET /v1/models?verbose=true` from the Token Factory API, filters for
models with `tools` support and `->text` output modality, and registers
them via `pi.registerProvider()`.

All models use the `openai-completions` API with
`compat: { supportsDeveloperRole: false, maxTokensField: "max_tokens" }`.

Install: `pi install npm:tokenfactory-pi`. Requires `NEBIUS_API_KEY`.

### `micuintus/pi-eurouter` — EUrouter provider

A Pi provider extension for [EUrouter](https://eurouter.ai) — an Amsterdam-based
OpenAI-compatible routing service with 120+ EU-hosted models.

The extension fetches the live EUrouter model catalog from
`https://api.eurouter.ai/api/v1/models` on startup, converts each entry
to Pi's model format, and registers them as the `eurouter` provider. It falls
back to a two-model list (Kimi K2.6 and DeepSeek V3) if the API is unreachable.

**Thinking support:** Models that advertise `reasoning_effort` in
`supported_parameters` are marked `reasoning: true` and receive a
`thinkingLevelMap` mapping Pi's thinking levels to EUrouter's effort strings
(`minimal → "low"`, `xhigh → "high"`).

Login: `/login` → "Use an API key" → "EUrouter" → paste your `eur_...` key.

Install: `pi install npm:pi-eurouter`. Published on npm as `pi-eurouter`.

### `balcsida/pi-provider-litellm` — LiteLLM proxy adapter

Discovers models from a self-hosted LiteLLM proxy and registers them
under the `litellm` provider. Supports `/login litellm` and
`/litellm-refresh`. Tries `/model/info` first, falls back to `/v1/models`.

Because LiteLLM itself can proxy to any OpenAI-compatible backend, this
extension is the **closest thing to a universal EU-provider adapter** in
Pi today. You can point LiteLLM at STACKIT, Scaleway, LLMbase, EUrouter,
AKI.IO, or any other EU endpoint, then let Pi discover the models through
this extension.

## Built-in vs extension providers

Pi's core already ships built-in providers for OpenCode Zen, OpenCode Go,
and Nebius Token Factory (see
[`packages/coding-agent/docs/providers.md`](https://github.com/earendil-works/pi-mono/blob/main/packages/coding-agent/docs/providers.md)).
The extensions above exist for three specific gaps:

| Gap | Built-in behavior | Extension remedy |
|---|---|---|
| **Static model list** | Models generated at Pi build time from `models.dev` | `cfal/pi-models-dev`, `mdsitton/pi-opencode-provider`, and `tokenfactory-pi` all fetch live catalogs on every startup |
| **Subscription login friction** | Built-in OpenCode Go requires manual `OPENCODE_API_KEY` env var | `pi-opencode-provider` adds `/login` → OAuth flow (pick Zen or Go, store key via Pi's auth UI) |
| **Key rotation / quota bypass** | Single `OPENCODE_API_KEY`; no rotation logic | `pi-opencode-go-rotation` rotates across multiple keys reactively |

**Why `cfal/pi-models-dev` is the recommended discovery pick:** it solves
the static-catalog gap while respecting Pi's curated built-ins — opt-in
override means a stale `opencode-go` snapshot can be refreshed without
clobbering the `compat`/`thinkingLevelMap` flags Pi's generator tuned for
Kimi/DeepSeek/MiniMax/Qwen on the models the built-in list already carries.
`mdsitton/pi-opencode-provider` solves the same gap and adds a `/login`
OAuth flow, but replaces both built-ins unconditionally and ships no tests.
`MasuRii/pi-model-discovery` is the most complete framework but its
ownership model keeps it off pi-mono-managed provider IDs by default.

`tokenfactory-pi` only solves the catalog problem; you still set
`NEBIUS_API_KEY` as an environment variable. Both extensions are
optional on current Pi releases — if you are happy with the built-in
static lists and manual key management, skip them.

## Comparison: OpenCode extensions

| Extension | Discovery | Key rotation | Commands | Built-in replace | Tests | Public repo |
|---|---|---|---|---|---|---|
| `awtotty/pi-opencode` | Static (hardcoded) | None | None | No | No | Yes |
| `mdsitton/pi-opencode-provider` | Runtime (live API) | None | None | Unconditional (opencode + opencode-go) | No | No (npm/pi.dev only) |
| `cfal/pi-models-dev` | Runtime (models.dev) | None | None | Opt-in per provider via env | Yes (`bun test`) | Yes |
| `MasuRii/pi-model-discovery` | Runtime (multi-source) | None | `/pi-model-discovery` | Declines pi-mono-managed IDs | Yes (`node:test`) | Yes |
| `lnilluv/pi-opencode-go-rotation` | None (uses built-in or another provider) | Reactive + watchdog | `/opencode *` | N/A (auth layer) | No | Yes |

`awtotty/pi-opencode` is the simplest but least maintained; new models
require a code change. `cfal/pi-models-dev` is the pick when you want
newer OpenCode Go models without losing Pi's hand-tuned `compat` flags —
it overrides only what you name in `PI_MODELS_DEV_OVERRIDE_PROVIDERS`.
`mdsitton/pi-opencode-provider` also works but replaces both built-ins
unconditionally and ships no tests. `MasuRii/pi-model-discovery` is the
most engineered option but its ownership model won't touch `opencode-go`
without manual config — best for multi-provider discovery, not OpenCode Go alone.
`lnilluv/pi-opencode-go-rotation` is orthogonal — pair it with any of the
provider extensions if you have multiple OpenCode Go keys.

## Free inference providers

Three extensions expose models with no (or minimal) per-request cost.

### `apmantza/pi-free` — multi-provider free-tier bundle

The most comprehensive free inference extension. Registers multiple
providers and filters each to show only free-tier models by default.
Providers include:

- **Free**: Kilo (OAuth), Cline (OAuth), LLM7 gateway (100 req/hr)
- **Freemium**: NVIDIA NIM (1,000 free req/month), Ollama Cloud,
  SambaNova (20–480 RPM, no credit card)
- **Paid with free models**: OpenRouter, ZenMux, CrofAI, Codestral
  (Mistral Experiment plan: 2 req/min, 1B tokens/month), DeepInfra
  ($5 trial credit), Novita AI (3 free models)
- **Dynamic (API key required)**: Mistral, Groq, Cerebras, xAI,
  Hugging Face, OpenCode, FastRouter

Per-provider `/toggle-{provider}` commands switch between free-only
and all-models view. OAuth for Kilo and Cline opens automatically in a
browser. Adds Coding Index benchmark scores to model names.

Install: `pi install git:github.com/apmantza/pi-free`

### `pi-kilocode` — Kilo Gateway provider

A thin provider extension for [Kilo Code's](https://kilo.ai) gateway,
which itself routes to hundreds of models (Anthropic, OpenAI, Google,
Mistral, etc.) through a single OpenAI-compatible endpoint. Kilo offers
a free tier with a selection of capable models.

The extension fetches the live Kilo model catalog from
`https://api.kilo.ai/api/gateway/models`, caches it on disk, and
registers text-capable models under the `kilo` provider. Uses Kilo's
device-auth OAuth login flow.

Install: `pi install npm:pi-kilocode`

### `ditfetzt/pi-cline-free-models` — Cline free models

Exposes Cline's free-tier models (historically Kimi K2.5, MiniMax,
and others) as a Pi provider. OAuth via SSO (Google, GitHub, Microsoft)
opens in a browser and handles the callback automatically. The extension
fetches the live catalog from Cline's API on every Pi startup so newly
added free models appear automatically.

Install: `pi install npm:pi-cline-free-models`

## Antigravity / Gemini CLI extensions

Pi v0.71.0 removed built-in Google Gemini CLI and Antigravity support. 
Community extensions have emerged to restore access to Google's AI models 
via your Google account subscription.

### `aadishv/pi-agy` — Antigravity OAuth + CLIProxyAPI proxy

Provides access to Gemini and Claude models through Google's Antigravity 
platform using your Google account subscription. Works by running a local 
proxy that translates Pi's Anthropic API calls to Antigravity's format.

**Models available:**
- `gemini-claude-opus-4-5-thinking`
- `gemini-claude-sonnet-4-5-thinking` 
- `gemini-claude-sonnet-4-5`
- `gemini-3-pro-preview`

**How it works:**
1. `pi-agy login` opens browser for Google OAuth (uses Antigravity's client ID)
2. `pi-agy proxy start` launches CLIProxyAPI on localhost:8317
3. Pi is configured to use the proxy for Anthropic API calls
4. Proxy translates to Antigravity's cloudcode-pa.googleapis.com API

**Features:**
- Uses your actual Google account subscription (no separate API key)
- Supports both Gemini and Claude models via Antigravity
- Automatic token refresh
- Per-model routing available via `pi-antigravity-rotator` extension

Install: `pi install git:github.com/aadishv/pi-agy`

### `tuxevil/pi-antigravity-rotator` — Multi-account rotation proxy

Distributes Antigravity API usage across multiple Google accounts with:
- Per-model routing (Gemini Pro, Flash, Claude each use separate accounts)
- Real-time quota tracking
- Automatic token management
- Infringement detection

Useful if you have multiple Google accounts with Antigravity access and 
want to avoid rate limits.

Install: `pi install npm:pi-antigravity-rotator`

### `vedang/pi-antigravity-image-gen` — Image generation tool

Adds a `generate_image` tool backed by:
- Google's Veo/Imagen models via Antigravity
- Vertex AI fallback
- Inline terminal rendering

Install: `pi install npm:@benvargas/pi-antigravity-image-gen`

## EU / privacy-forward providers — the gap

**No Pi-specific extensions exist for EU providers.** STACKIT, Scaleway,
EUrouter, LLMbase, Tensorix, Juice Factory, Infomaniak, AKI.IO, Langdock
all expose OpenAI-compatible APIs, so Pi's built-in generic OpenAI
provider (`baseUrl` override) or `balcsida/pi-provider-litellm`
(LiteLLM proxy) covers them.

For a quick orientation on the EU routing landscape: **OpenRouter**
(US, the incumbent, 500+ models), **Eden AI** (France, funded, 500+
models, strongest EU-based alternative), **Cortecs** (EU, enterprise
router, 150+ endpoints), **Orq.AI** and **Requesty** (EU, early stage),
and **EUrouter** (Netherlands, unfunded solo founder, 120+ models).
No dedicated Pi extension exists for any of them — the gap is real.

## Recommendation matrix

| Your situation | Recommendation |
|---|---|
| Use OpenCode Zen/Go (normal case) | Pi built-in — no extension needed |
| Want newest OpenCode Go models between Pi releases (keep built-in compat) | `pi install git:github.com/cfal/pi-models-dev` + set `PI_MODELS_DEV_OVERRIDE_PROVIDERS=opencode-go` |
| Multiple OpenCode Go keys / hitting rate limits | `pi install npm:@lnilluv/pi-opencode-go-rotation` |
| Use Nebius Token Factory (normal case) | Pi built-in — no extension needed |
| Nebius on an older Pi version | `pi install npm:tokenfactory-pi` |
| Need an EU provider for open-weight models | Pi generic OpenAI provider with EU `baseUrl` — no extension needed |
| Just starting out with OpenCode | Use Pi's built-in providers; extensions are optional |

## See also

- [Pi built-in provider documentation](https://github.com/earendil-works/pi-mono/blob/main/packages/coding-agent/docs/providers.md)
- [Pi Packages — official catalog](https://pi.dev/packages)
- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes
- [Anthropic Auth & Billing in Pi](anthropic-auth-and-billing.md) — OAuth and API-key auth patterns

