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
---

# Pi Web Search Extensions

Comparison of published Pi web search extensions and skills.

## Overview

| Package | Author | Type | Stars | Forks | Open Issues | Weekly npm | Monthly npm |
|---|---|---|---|---|---|---|---|
| **`pi-web-access`** | nicobailon | Extension | 427 | 67 | 34 | **7,408** | **~21,800** |
| **`pi-codex-web-search`** | ayagmar | Extension | 17 | 1 | 0 | 35 | ~150 |
| **`pi-free-web-search`** | Albertobelleiro | Extension | 0 | 0 | 3 | 57 | ~250 |
| **`pi-web-extension`** | NicoAvanzDev | Extension | 1 | 1 | 0 | 28 | ~120 |
| **`@coctostan/pi-exa-gh-web-tools`** | coctostan | Extension | 1 | 2 | 1 | 13 | ~55 |
| **`pi-web-utils`** | shantanugoel | Extension | 2 | 0 | 0 | 14 | ~60 |
| **`@aemonculaba/pi-search`** | eysenfalk | Extension | 3 | 1 | 3 | 24 | ~100 |
| **`brave-search`** | badlogic/pi-skills | **Skill** | — | — | — | N/A | N/A |
| **`@joemccann/pi-exa`** | joemccann | Extension | — | — | — | — | — |
| **`pi-exa-search`** | najibninaba | Extension | — | — | — | — | — |

Numbers as of 2026-05-05.

## Code quality

| Package | TS Files | Tests | CI | tsconfig | Lint | Notes |
|---|---|---|---|---|---|---|
| `pi-web-access` | 23 | 2 | No | No | None | 2300-line monolith, no TS config, no CI, 34 open issues |
| `pi-free-web-search` | 22 | 6 | Yes | Yes | `tsc` | Modular, health tracking, token-efficient modes, prompts + skills |
| `@coctostan/pi-exa-gh-web-tools` | 41 | 23 | No | Yes | `tsc` | Most-tested. Caching, batching, dedup, CLI binary |
| `pi-codex-web-search` | 10 | 3 | Yes | Yes | ESLint + Prettier | Codex JSONL parsing, budget tracking, retry logic |
| `pi-web-extension` | 3 | 1 | Yes | Yes | oxlint + oxfmt | Minimal but linted, tested, focused |
| `pi-web-utils` | 9 | 0 | No | Yes | `tsc` | Clean architecture, zero tests, no CI |
| `@aemonculaba/pi-search` | 1 + CJS | 1 | Yes | No | None | Single file, CJS build, policy injection |
| `brave-search` (skill) | 2 JS | 0 | No | No | None | Lightweight, no browser, headless |

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

`pi-web-access` dominates by usage (~300x nearest competitor by weekly
downloads). It wins on features, not on engineering quality (2300-line
monolith, no CI, 34 open issues at survey time). Long tail of niche
extensions exists; clear opening for a well-engineered competitor.

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
