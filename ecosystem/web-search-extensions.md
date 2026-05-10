---
title: Pi Web Search Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - pi-web-access
  - pi-codex-web-search
  - pi-free-web-search
  - pi-web-extension
  - pi-exa-gh-web-tools
  - pi-web-utils
  - aemonculaba-pi-search
  - pi-skills
  - pi-skills-brave-search
  - joemccann-pi-exa
  - pi-exa-search
  - ben-vargas-pi-packages
  - mitsuhiko-agent-stuff
tags: [extension, web-search, skill]
entries:
  - id: pi-web-access
    name: pi-web-access
    repo: nicobailon/pi-web-access
    npm: pi-web-access
    role: full-featured-extension
    notes: "Multi-provider (Exa, Perplexity, Gemini). Video/PDF/GitHub. Dominant by usage. Engineering caveats: large monolith, no CI."
  - id: pi-codex-web-search
    name: pi-codex-web-search
    repo: ayagmar/pi-codex-web-search
    npm: pi-codex-web-search
    role: codex-bridge
    notes: "Delegates to the local codex CLI. Reuses Codex auth, budget tracking, fast/deep modes."
  - id: pi-free-web-search
    name: pi-free-web-search
    repo: Albertobelleiro/pi-free-web-search
    npm: pi-free-web-search
    role: free-multi-engine
    notes: "Yahoo/Google/Bing/DDG/Brave/SearXNG without API keys. Browser fallback. Modular, tested, CI present."
  - id: pi-web-extension
    name: pi-web-extension
    repo: NicoAvanzDev/pi-web-extension
    npm: pi-web-extension
    role: free-minimal
    notes: "Brave HTML scrape + DDG fallback. Token-aware, prompt steering. Minimal but linted/tested."
  - id: pi-exa-gh-web-tools
    name: "@coctostan/pi-exa-gh-web-tools"
    repo: coctostan/pi-exa-gh-web-tools
    npm: "@coctostan/pi-exa-gh-web-tools"
    role: exa-research-cache
    notes: "Exa-only. Research cache, query enhancement, dedup, parallel batch, standalone CLI. Most-tested in this group."
  - id: pi-web-utils
    name: pi-web-utils
    repo: shantanugoel/pi-web-utils
    npm: pi-web-utils
    role: configurable-chain
    notes: "Google/DDG/SearXNG/custom. GitHub clone + local rg/grep. Clean architecture, no tests."
  - id: aemonculaba-pi-search
    name: "@aemonculaba/pi-search"
    repo: eysenfalk/pi-search
    npm: "@aemonculaba/pi-search"
    role: native-codex-tool
    notes: "Uses OpenAI/Codex native web_search only. Policy injection blocks bash curl/wget. Auth priority chain."
  - id: brave-search-skill
    name: brave-search (skill)
    repo: badlogic/pi-skills
    role: skill
    notes: "Pi maintainer's preferred shape: SKILL.md + bash, no extension overhead. Requires BRAVE_API_KEY."
  - id: joemccann-pi-exa
    name: "@joemccann/pi-exa"
    repo: joemccann/pi-exa
    npm: "@joemccann/pi-exa"
    role: exa-minimal
    notes: "Exa-only single tool. Lightest Exa option."
  - id: pi-exa-search
    name: pi-exa-search
    repo: najibninaba/pi-exa-search
    npm: pi-exa-search
    role: exa-minimal
    notes: "Exa-only single tool, parallel to @joemccann/pi-exa."
  - id: ben-vargas-pi-exa-mcp
    name: "@benvargas/pi-exa-mcp"
    repo: ben-vargas/pi-packages
    npm: "@benvargas/pi-exa-mcp"
    role: exa-mcp
    notes: "Exa via MCP adapter. Includes Exa code-context search endpoint. CI and tests. Part of ben-vargas individually-publishable suite."
  - id: ben-vargas-pi-firecrawl
    name: "@benvargas/pi-firecrawl"
    repo: ben-vargas/pi-packages
    npm: "@benvargas/pi-firecrawl"
    role: scraping-search
    notes: "Firecrawl-based: scrape, map (site crawl), search. Excels at structured extraction from known URLs, not open-web discovery. CI and tests."
  - id: mitsuhiko-native-web-search
    name: "native-web-search (mitsuhiko/agent-stuff)"
    repo: mitsuhiko/agent-stuff
    npm: mitsupi
    role: skill
    notes: "Skill that delegates to the model's native web search capability when available. No API key required. Falls back gracefully. Part of mitsupi bundle."
---

# Pi Web Search Extensions

## Contents

- [Approach](#approach)
- [Code quality and engineering shape](#code-quality-and-engineering-shape)
- [What each does](#what-each-does)
- [Market structure](#market-structure)
- [Recommendation matrix](#recommendation-matrix)
- [Author note](#author-note)
- [Setup notes — pi-web-access](#setup-notes-pi-web-access)
- [Routing guidance](#routing-guidance-one-tool-internal-selection)
- [See also](#see-also)

Comparison of published Pi web search extensions and skills.

## Approach

Two distinct deployment shapes: heavyweight **extensions** (register
tools at startup, integrate with Pi's tool system) versus lightweight
**skills** (SKILL.md + bash; what Pi's maintainer ships and recommends
for this niche).

## Code quality and engineering shape

These notes are structural — they don't decay the way star/download
counts do. For current vital signs see
[How to Evaluate a Pi Extension](../references/evaluation.md).

| Package | TS Files | Tests | CI | tsconfig | Lint | Notes |
|---|---|---|---|---|---|---|
| `pi-web-access` | many | minimal | No | No | None | Large monolith, no TS config, no CI; high open-issue count |
| `pi-free-web-search` | many | several | Yes | Yes | `tsc` | Modular, health tracking, token-efficient modes, prompts + skills |
| `@coctostan/pi-exa-gh-web-tools` | many | many | No | Yes | `tsc` | Most-tested. Caching, batching, dedup, CLI binary |
| `pi-codex-web-search` | small | several | Yes | Yes | ESLint + Prettier | Codex JSONL parsing, budget tracking, retry logic |
| `pi-web-extension` | small | small | Yes | Yes | oxlint + oxfmt | Minimal but linted, tested, focused |
| `pi-web-utils` | small | none | No | Yes | `tsc` | Clean architecture, zero tests, no CI |
| `@aemonculaba/pi-search` | tiny | small | Yes | No | None | Single file, CJS build, policy injection |
| `brave-search` (skill) | 2 JS | none | No | No | None | Lightweight, no browser, headless |

## What each does

| Package | Search providers | Fetch | Special features |
|---|---|---|---|
| **`pi-web-access`** | Exa (MCP/direct), Perplexity, Gemini API, Gemini Web (browser cookies) | Readability+Turndown, Jina fallback | Video analysis (YouTube + local), PDF extraction, GitHub cloning, `librarian` skill, curator browser |
| **`pi-free-web-search`** | Yahoo (default), Google, Bing, DDG, Brave, SearXNG | HTTP-first, browser fallback | Free, no API keys; browser automation; health tracking; token-efficient modes; prompt templates + skills |
| **`@coctostan/pi-exa-gh-web-tools`** | Exa only | Readability+Turndown, GitHub clone | Research cache, query enhancement, dedup, parallel batch, content offloading, standalone CLI |
| **`pi-codex-web-search`** | Delegates to local `codex` CLI | Defuddle fallback | Codex auth reuse, budget tracking, fast/deep modes, settings persistence |
| **`pi-web-extension`** | Brave (HTML scrape), DDG fallback | Turndown to temp file | Prompt steering (auto-detects URLs/search intent), token-aware |
| **`pi-web-utils`** | Google, DDG, SearXNG, custom (configurable chain) | markdown.new → Readability+Turndown | GitHub clone + local `rg`/`grep` search, configurable engines |
| **`@aemonculaba/pi-search`** | OpenAI/Codex native `web_search` only | Readability+Turndown, Playwright fallback | Policy injection (blocks bash curl/wget), auth priority chain |
| **`@benvargas/pi-exa-mcp`** | Exa via MCP adapter | Exa content extraction | Code context search (Exa code search endpoint). CI and tests. Single-purpose, cleanly bounded. |
| **`@benvargas/pi-firecrawl`** | Firecrawl (scrape, map, search) | Firecrawl structured extraction | Designed for known URLs and site-crawl patterns, not open-web search. CI and tests. |
| **`native-web-search` (mitsuhiko/agent-stuff)** | Model’s native web search (when available) | — | No API key. Uses whatever native search the active model exposes. Falls back gracefully. Skill pattern, not an extension. |
| **`brave-search` (skill)** | Brave Search API | Readability+Turndown | Lightweight, headless, requires API key |

## Market structure

`pi-web-access` dominates this niche by adoption (orders of magnitude
ahead of any competitor in weekly downloads at survey time). It wins
on features, not on engineering quality. Long tail of niche extensions
exists; clear opening for a well-engineered competitor.

## Recommendation matrix

| Goal | Best choice | Why |
|---|---|---|
| Full features today (video, PDF, multi-provider) | **`pi-web-access`** | Most-used, most-features. Accept the engineering caveats. |
| Free, no API keys | **`pi-free-web-search`** or **`pi-web-extension`** | Browser-scrape fallbacks; no signup. |
| Codex CLI integration | **`pi-codex-web-search`** | Delegates to the local `codex` CLI; reuses auth. |
| Exa-only, minimal | **`@joemccann/pi-exa`** or **`pi-exa-search`** | Single tool, just `EXA_API_KEY`. Bypasses heavier extensions. |
| Exa via MCP + code search | **`@benvargas/pi-exa-mcp`** | MCP-native wiring; includes Exa code search. Tested. |
| Structured site scraping (known URLs) | **`@benvargas/pi-firecrawl`** | Firecrawl excels at known-URL extraction and site-map crawls; not open-web search. |
| Skill-first, no extension overhead | **`brave-search` skill** or **`native-web-search`** | SKILL.md + bash. `brave-search` needs API key; `native-web-search` needs no key but requires a model with native search. |

## Author note

The `brave-search` skill in `badlogic/pi-skills` is the approach Pi's
maintainer ships and recommends — aligning with Pi's "skills > extensions"
philosophy when a SKILL.md + bash script can do the job without the
overhead of an extension.

## Setup notes — `pi-web-access`

- **macOS + Chrome signed into Google**: zero-config. Reads Chrome cookies
  for Gemini Web; first run may prompt Keychain.
- **Linux**: uses `secret-tool` when available; otherwise configure API keys.
- **Windows / no browser**: configure `~/.pi/web-search.json` with
  `perplexityApiKey` and/or `geminiApiKey`. `GEMINI_API_KEY` /
  `PERPLEXITY_API_KEY` env vars take precedence.
- **Optional video frame extraction**: `brew install ffmpeg yt-dlp`.

## Routing guidance — one tool, internal selection

The non-obvious design rule when a Pi setup has *multiple* search
backends configured: **expose one tool to the model, route internally.
Never expose multiple search tools.**

Every major AI product follows this rule. Claude.ai/Code, ChatGPT,
Gemini, and Le Chat all have multiple backends or fallbacks but
present the model with a single search capability:

| Product | Backends | What the model sees |
|---|---|---|
| Claude.ai / Claude Code | Brave Search | One `WebSearch` tool |
| ChatGPT | Bing + OAI index + others | One search capability |
| Gemini | Google Search | One grounding tool |
| Le Chat | Brave Search | One web search tool |

### The right shape

```ts
// One tool — provider chosen internally
{
  name: "web_search",
  parameters: {
    query: string,
    provider: "auto" | "exa" | "brave" | "perplexity" | "gemini",
  }
}

// Implementation routes based on query intent + available keys
function resolveProvider(query, config) {
  if (config.provider !== "auto") return config.provider;
  if (looksLikeCodeQuery(query))  return "exa";    // technical docs/APIs
  if (looksLikeNewsQuery(query))  return "brave";  // current events
  if (config.perplexityKey)       return "perplexity"; // synthesis
  return "gemini"; // fallback
}
```

The model sees a tool description that **does not name specific
providers**:

> `web_search`: Search the web for current information. The tool
> automatically selects the best provider for your query.

### The wrong shape

```ts
brave_search({ query: "..." })       // Which one?
exa_search({ query: "..." })         // When do I use which?
perplexity_search({ query: "..." })  // The model now has to choose every call
```

Multiple visible tools force the model to make a meta-decision on
every search. It will get it wrong, sometimes spectacularly. Never do
this.

### Why this matters when picking extensions

Some Pi web search extensions ship multiple-tool surfaces; others
ship one tool with internal routing. When evaluating, check:

- Does the extension register **one** tool or **several**?
- If several, do their descriptions make the LLM-side choice obvious,
  or do they overlap?
- Can the user override provider selection per-call without that
  override being a separate tool?

Single-tool-with-routing is the right answer at scale. The exception
is genuinely orthogonal capabilities (e.g. `web_search` vs
`fetch_url` vs `youtube_transcript`) — those are different verbs, not
different backends for the same verb.

## See also

- [Web Search Providers](../references/web-search-providers.md) — backend reference and routing guidance for the major providers
- [How to Evaluate a Pi Extension](../references/evaluation.md) — for current vital signs of any of the above
