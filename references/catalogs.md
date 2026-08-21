---
title: Pi Ecosystem Catalogs and Awesome-Lists
type: reference
updated: 2026-08-21
sources:
  - qualisero-awesome-pi-agent
  - shaftoe-awesome-pi-coding-agent
  - awesome-pi-site
  - pi-dev-packages
  - qualisero-rhubarb-pi
  - kcosr-pi-extensions
  - noahsaso-my-pi
  - samfoy-pi-essentials
  - diegopetrucci-pi-extensions
  - narumiruna-pi-extensions
  - tungthedev-pi-extensions
  - edxeth-pi-auto-session-titles
  - oh-my-pi-collection
  - pi-packages-docs
  - mitsuhiko-agent-stuff
  - hjanuschka-shitty-extensions
  - tmustier-pi-extensions
  - aliou-pi-extensions
  - ben-vargas-pi-packages
  - obra-superpowers
tags: [reference, catalog, navigation]
---

# Pi Ecosystem Catalogs and Awesome-Lists

Where to look when this wiki doesn't cover what you need. The Pi
ecosystem has multiple complementary catalogs, each with a different
shape and update cadence. This page maps them so you can pick the
right one for the job.

## Catalogs at a glance

| Catalog | Type | Update model | Best for |
|---|---|---|---|
| **[`pi.dev/packages`](https://pi.dev/packages)** | Official catalog | Auto, npm-driven | "What's been published recently?" Authoritative for new packages. |
| **[`qualisero/awesome-pi-agent`](https://github.com/qualisero/awesome-pi-agent)** | Curated awesome-list | Hand-curated + Discord-scraping workflow + PR-driven | Quality filter — entries vetted before inclusion |
| **[`shaftoe/awesome-pi-coding-agent`](https://github.com/shaftoe/awesome-pi-coding-agent) / [`awesome-pi.site`](https://awesome-pi.site/)** | Auto-aggregated directory | Daily auto-discovery | Maximum coverage, daily-fresh, browsable web UI with category counts. Indexes extensions, tools, themes, providers, templates, and videos. |

Three different philosophies — official-source-of-truth, curated quality, and exhaustive auto-discovery. They overlap but none subsumes the others.

## Curated extension collections

Single-author/team bundles, useful as starting points or to lift extensions piecemeal:

| Collection | Author | Notes |
|---|---|---|
| [`mitsuhiko/agent-stuff`](https://github.com/mitsuhiko/agent-stuff) | mitsuhiko (Pi maintainer) | The Pi maintainer's own bundle. 22+ extensions (loop, review, todos, notify, multi-edit, files, btw, answer, prompt-editor, session-breakdown, whimsical, …) + 19+ skills (commit, github, google-workspace, librarian, web-browser, sentry, tmux, mermaid, …). Two npm distributions: `mitsupi` (common) and `mitsupi-loaded` (all). Canonical reference for Pi idioms. |
| [`hjanuschka/shitty-extensions`](https://github.com/hjanuschka/shitty-extensions) | hjanuschka | Community bundle covering oracle (second opinion from any model), plan-mode (read-only exploration), memory-mode, branch-sessions, cost-tracker, usage-bar, clipboard, handoff, status-widget, ultrathink. npm-published (`shitty-extensions`). |
| [`qualisero/rhubarb-pi`](https://github.com/qualisero/rhubarb-pi) | qualisero | Small, individually-installable hooks: `background-notify`, `session-emoji`, `session-color`, `safe-git`. |
| [`tmustier/pi-extensions`](https://github.com/tmustier/pi-extensions) | tmustier | ralph-wiggum (loop), tab-status, arcade, usage-extension, agent-guidance. |
| [`aliou/pi-extensions`](https://github.com/aliou/pi-extensions) | aliou | Rich collection: breadcrumbs (session search), providers manager, chrome header/footer, git-branch-autocomplete, session-name, models-overrides, session tools. npm-published under `@aliou/`. |
| [`ben-vargas/pi-packages`](https://github.com/ben-vargas/pi-packages) | ben-vargas | Individually-publishable packages with CI and tests: Synthetic provider, Exa MCP, Firecrawl, Antigravity image gen, Claude Code OAuth patch, ancestor-discovery, cut-stack, OpenAI fast/verbosity. Each installable standalone via npm. |
| [`kcosr/pi-extensions`](https://github.com/kcosr/pi-extensions) | kcosr | Released bundle, semver-tagged. codemap, apply-patch, assistant picker, skill-picker, toolwatch (SQLite tool-call auditing). |
| [`noahsaso/my-pi`](https://github.com/noahsaso/my-pi) | noahsaso | Personal collection: pi-context, pi-interactive-subagents, browser tools, web tools, memory, file-watcher, code-ast, antigravity image gen. Skills from `badlogic/pi-skills` and `obra/superpowers`. Includes SETUP.md for agent-guided install. |
| [`can1357/oh-my-pi`](https://github.com/can1357/oh-my-pi) | can1357 | A Pi fork (not just extensions) bundling Claude Code SDK provider and other patches. See also [Anthropic Auth & Billing in Pi](../ecosystem/anthropic-auth-and-billing.md). |
| [`samfoy/pi-essentials`](https://github.com/samfoy/pi-essentials) | samfoy | Quality-of-life set pitched as the baseline every install wants: auto session naming, compact header, clipboard images, image pruning, markdown viewer, screenshots, subagents. |
| [`narumiruna/pi-extensions`](https://github.com/narumiruna/pi-extensions) | narumiruna | TypeScript monorepo, every package published separately under `@narumitw` so nothing is all-or-nothing: automation, planning, language tooling, browser control, web research, Git workflows, config sync. |
| [`tungthedev/pi-extensions`](https://github.com/tungthedev/pi-extensions) | tungthedev | Opinionated default-experience upgrade: custom editor/composer, inline Mermaid rendering, web research, skill loading, boomerang-style context summarization, tool-set/system-prompt switching between Pi/Codex/Droid modes, TUI-first subagent manager. |
| [`diegopetrucci/pi-extensions`](https://github.com/diegopetrucci/pi-extensions) | diegopetrucci | Small guardrail-flavoured set: `confirm-destructive` (gate clear/switch/fork), `context-cap` (cap effective context at 200k to dodge the "dumb zone"), `context-inspector` (`/context`). |

### Standalone utilities worth knowing

- [`edxeth/pi-auto-session-titles`](https://github.com/edxeth/pi-auto-session-titles)
  names sessions automatically once the first request **fully settles** (after
  retries, compaction recovery and queued continuations), using a configurable
  cheap model, and adds `/rename-session` to regenerate from the full branch.
  Notable for restraint: it never overwrites a title another extension set,
  never re-titles after compaction, and deliberately withholds thinking, tool
  results, file contents, bash commands and system prompts from the title
  model — only the request, the final reply, tool names and up to 20 file
  paths. A good worked example of bounding what leaves the machine.

## Cross-agent workflow skills

Not Pi-exclusive but widely used across Pi setups:

| Collection | Notes |
|---|---|
| [`obra/superpowers`](https://github.com/obra/superpowers) | Complete software development methodology as skills: brainstorming → writing-plans → subagent-driven-development → TDD → requesting-code-review → finishing-a-development-branch. Works with Pi, Claude Code, Codex, Gemini CLI, OpenCode, Cursor. In Claude Code's official plugin marketplace. Referenced by `noahsaso/my-pi` and `mitsuhiko/agent-stuff`. |

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

## See also

- [How to Evaluate a Pi Extension](evaluation.md) — vital signs and code-quality recipes for vetting packages from any catalog
- [Pi Web Search Extensions](../ecosystem/web-search-extensions.md) — example of a survey page that sits on top of catalogs
