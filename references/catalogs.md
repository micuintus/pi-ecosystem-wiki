---
title: Pi Ecosystem Catalogs and Awesome-Lists
type: reference
updated: 2026-05-08
sources:
  - qualisero-awesome-pi-agent
  - shaftoe-awesome-pi-coding-agent
  - awesome-pi-site
  - pi-dev-packages
  - qualisero-rhubarb-pi
  - kcosr-pi-extensions
  - noahsaso-my-pi
  - oh-my-pi-collection
  - pi-packages-docs
tags: [reference, catalog, navigation]
---

# Pi Ecosystem Catalogs and Awesome-Lists

Where to look when this wiki doesn't cover what you need. The Pi
ecosystem has multiple complementary catalogs, each with a different
shape and update cadence. This page maps them so you can pick the
right one for the job.

## Catalogs at a glance

| Catalog | Type | Size | Update model | Best for |
|---|---|---|---|---|
| **[`pi.dev/packages`](https://pi.dev/packages)** | Official catalog | All published Pi packages | Auto, npm-driven | "What's been published recently?" Authoritative for new packages. |
| **[`qualisero/awesome-pi-agent`](https://github.com/qualisero/awesome-pi-agent)** | Curated awesome-list | ~581★, smaller | Hand-curated + Discord-scraping workflow + PR-driven | Quality filter — entries vetted before inclusion |
| **[`shaftoe/awesome-pi-coding-agent`](https://github.com/shaftoe/awesome-pi-coding-agent) / [`awesome-pi.site`](https://awesome-pi.site/)** | Auto-aggregated directory | 1100+ extensions, 1100+ tools, 131 themes, 253 providers, 16 templates, 114 videos | Daily auto-discovery | Maximum coverage, daily-fresh, browsable web UI with category counts |

Three different philosophies — official-source-of-truth, curated quality, and exhaustive auto-discovery. They overlap but none subsumes the others.

## Curated extension collections

Single-author/team bundles, useful as starting points or to lift extensions piecemeal:

| Collection | Author | Notes |
|---|---|---|
| [`qualisero/rhubarb-pi`](https://github.com/qualisero/rhubarb-pi) | qualisero | Small hooks: `background-notify`, `session-emoji`, `session-color`, others. Each individually installable. |
| [`kcosr/pi-extensions`](https://github.com/kcosr/pi-extensions) | kcosr | Released bundle, semver-tagged. |
| [`noahsaso/my-pi`](https://github.com/noahsaso/my-pi) | noahsaso | Personal Pi extension/skills/agents collection — includes `pi-context`, `pi-interactive-subagents`, browser tools, web tools (skills from `badlogic/pi-skills` and `obra/superpowers`). |
| [`can1357/oh-my-pi`](https://github.com/can1357/oh-my-pi) | can1357 | A Pi fork (not just extensions) bundling Claude Code SDK provider and other patches. See also [Anthropic Subscription Auth in Pi](../ecosystem/anthropic-subscription-auth.md). |

## How catalogs and this wiki relate

```
                        ┌─────────────────────────┐
                        │   pi.dev/packages       │  authoritative npm-published list
                        └────────────┬────────────┘
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        ▼                            ▼                            ▼
 qualisero/awesome-pi-agent    shaftoe/awesome-pi.site     this wiki
 (hand-curated)                (auto-aggregated)           (synthesized surveys)
        │                            │                            │
        └────────── you pick the right shape for your need ───────┘
```

When to use which:

- **\"Is this niche covered yet? Which extensions exist for X?\"** → Start here (this wiki) — the surveys group by use case and compare options. If the niche isn't covered, fall through to:
- **\"Browse a vetted list\"** → `qualisero/awesome-pi-agent`
- **\"Maximum coverage / very recent additions\"** → `awesome-pi.site` or `pi.dev/packages`
- **\"Show me everything one author published\"** → the curated collections above

## Catalog-side automation

`qualisero/awesome-pi-agent` runs a Discord-scraping workflow (per its
[`AGENTS.md`](https://github.com/qualisero/awesome-pi-agent/blob/main/AGENTS.md))
that compares newly-discovered repos against the existing list and
opens PRs. New entries land via standard PR review, so the curation
quality holds even as input volume grows.

`awesome-pi.site` runs daily auto-discovery on GitHub (and other
sources) and renders the result as a browsable web directory with
per-category counts. Easier to browse than scrolling a long markdown
file, but less curated.

## Pi packages — what they are

A Pi package bundles extensions, skills, prompt templates, and themes
distributable via npm or git. Manifest in `package.json` under the
`pi` key, or convention-driven directory layout. Use the `pi-package`
keyword for catalog discoverability. Reference:
[Pi Packages docs](https://pi.dev/docs/latest/packages).

This is the unit that all three top-level catalogs index.
