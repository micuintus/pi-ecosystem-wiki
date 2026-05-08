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
---

# Pi Web Search Extensions

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
| Skill-first (no extension) | **`brave-search` skill** in [`badlogic/pi-skills`](https://github.com/badlogic/pi-skills) | SKILL.md + bash, no schema registration. Requires Brave API key. |

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

## See also

- [Web Search Providers](../references/web-search-providers.md) — backend reference and routing guidance for the major providers
- [How to Evaluate a Pi Extension](../references/evaluation.md) — for current vital signs of any of the above
