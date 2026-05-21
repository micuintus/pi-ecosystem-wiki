---
title: Pi Provider Extensions
type: ecosystem
updated: 2026-05-19
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
    notes: "Runtime model discovery for OpenCode Zen + Go; replaces built-in providers; pi.dev/npm only"
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
---

# Pi Provider Extensions

Third-party provider extensions for Pi that add or augment LLM backends.
Pi ships with built-in providers for OpenCode Zen, OpenCode Go, Nebius,
and many others; these extensions exist when users want **runtime model
discovery** (new models without waiting for a Pi release) or **key-management
utilities** (rotation, quota bypass) that the core does not provide.

## TL;DR

- **Using OpenCode Zen or Go?** Pi has built-in providers — no extension
  needed. Only install `pi-opencode-provider` if you want **live model
  discovery** (new OpenCode models appear without waiting for a Pi release).
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
| **Static model list** | Models generated at Pi build time from `models.dev` | `pi-opencode-provider` and `tokenfactory-pi` both fetch live catalogs on every startup |
| **Subscription login friction** | Built-in OpenCode Go requires manual `OPENCODE_API_KEY` env var | `pi-opencode-provider` adds `/login` → OAuth flow (pick Zen or Go, store key via Pi's auth UI) |
| **Key rotation / quota bypass** | Single `OPENCODE_API_KEY`; no rotation logic | `pi-opencode-go-rotation` rotates across multiple keys reactively |

**Why `pi-opencode-provider` is a bigger win than `tokenfactory-pi`:**
`pi-opencode-provider` solves *two* problems — it fetches the live model
catalog (like `tokenfactory-pi` does for Nebius) *and* it replaces the
manual env-var setup with Pi's native `/login` OAuth flow. For OpenCode
Go specifically, that means you pick "Zen" or "Go" from the Pi login
menu instead of exporting `OPENCODE_API_KEY` by hand.

`tokenfactory-pi` only solves the catalog problem; you still set
`NEBIUS_API_KEY` as an environment variable. Both extensions are
optional on current Pi releases — if you are happy with the built-in
static lists and manual key management, skip them.

## Comparison: OpenCode extensions

| Extension | Discovery | Key rotation | Commands | Install size | Public repo |
|---|---|---|---|---|---|
| `awtotty/pi-opencode` | Static (hardcoded) | None | None | Minimal (~1 commit) | Yes |
| `mdsitton/pi-opencode-provider` | Runtime (live API) | None | None | Medium | No (npm/pi.dev only) |
| `lnilluv/pi-opencode-go-rotation` | None (uses built-in or another provider) | Reactive + watchdog | `/opencode *` | Medium | Yes |

`awtotty/pi-opencode` is the simplest but least maintained; new models
require a code change. `mdsitton/pi-opencode-provider` is the best
choice for users who want immediate access to new OpenCode models.
`lnilluv/pi-opencode-go-rotation` is orthogonal — pair it with either
provider if you have multiple OpenCode Go keys.

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
| Want newest OpenCode models between Pi releases | `pi install npm:pi-opencode-provider` |
| Multiple OpenCode Go keys / hitting rate limits | `pi install npm:@lnilluv/pi-opencode-go-rotation` |
| Use Nebius Token Factory (normal case) | Pi built-in — no extension needed |
| Nebius on an older Pi version | `pi install npm:tokenfactory-pi` |
| Need an EU provider for open-weight models | Pi generic OpenAI provider with EU `baseUrl` — no extension needed |
| Just starting out with OpenCode | Use Pi's built-in providers; extensions are optional |

## See also

- [Pi built-in provider documentation](https://github.com/earendil-works/pi-mono/blob/main/packages/coding-agent/docs/providers.md)
- [Pi Packages — official catalog](https://pi.dev/packages)
- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes
- [Anthropic Subscription Auth in Pi](anthropic-subscription-auth.md) — OAuth and API-key auth patterns

