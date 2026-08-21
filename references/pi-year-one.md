---
title: Pi Year One — How the Extension Platform Arrived
type: reference
updated: 2026-08-21
sources:
  - pi-mono
  - pi-releases
  - pi-extensions-docs
  - bitter-frontier-pi-profile
tags: [history, architecture, extensions]
---

# Pi Year One — How the Extension Platform Arrived

## Why this page exists

Every survey in this wiki is downstream of one fact: Pi's core refuses
features, and the extension API is rich enough that the ecosystem supplies them
instead. That arrangement has a date. Knowing when each primitive landed
explains why some categories are crowded, why others could not exist before
2026, and why version floors in extension manifests cluster where they do.

## The arc in numbers

The repository opened 2025-08-09 and reached **v0.84.2** by 2026-08-20 —
roughly 5,650 commits, so year one is essentially the whole project life.

| Period | Commits | What it was |
|---|---|---|
| Aug–Oct 2025 | ~270 | `packages/ai` first: provider abstraction, models.dev, streaming |
| Nov 2025 | 280 | the agent and TUI take shape; rapid minors begin |
| Dec 2025 | 868 | **the extension platform lands** |
| Jan 2026 | **1,227** | peak: the unified API |
| Feb–Aug 2026 | ~400–500/mo | consolidation: providers, compaction, telemetry, harness v2 |

A four-month burst built the platform; everything since has been steady
consolidation, with releases slowing from several minors a week to roughly one
every one to two weeks.

## "Extensions" existed before the extension platform

This distinction is easy to get wrong. Extensibility was not invented in
January; it was **unified** then.

- **v0.18.0 (2025-12-09)** — `pi.on(...)` exists. Hooks are real.
- Through December there were **two separate, narrower mechanisms**: a `hooks/`
  directory and a `tools/` directory, each with its own contract.
- **v0.35.0 (2026-01-04/05)** — PR **#454**, *"Merge hooks and custom-tools
  into unified extensions system"*, introduces `ExtensionAPI` and
  `loadExtension`. The old directories get deprecation warnings and a
  migration.

So "the extension platform" means that unification: one TypeScript module with
access to tools, commands, events, renderers, UI — and later providers. The
difference is between *reacting to* core behaviour and *replacing* it.

The documentation tracks it exactly:

| Version | `docs/extensions.md` |
|---|---|
| v0.20.0 | 0 lines |
| v0.31.0 | 0 lines |
| **v0.35.0** | **1,053 lines** |
| v0.50.0 | 1,733 |
| v0.70.0 | 2,545 |
| v0.84.0 | 2,987 |

## When each primitive landed

| Primitive | First shipped |
|---|---|
| Skills | v0.19.0 (Dec 2025) |
| `registerCommand`, `session_before_compact` | v0.31.0 (Dec 2025) |
| `registerMessageRenderer` | v0.31.0 (Dec 2025) |
| `setActiveTools`, plan-mode example | v0.34.0 (Jan 2026) |
| `ExtensionAPI`, `loadExtension`, `registerTool`, `pi.events` | **v0.35.0** (Jan 2026) |
| Provider registry (OAuth refactor) | v0.50.0 (Jan 2026) |
| **Native extension providers** | **v0.81.0** (Jul 2026) |
| Telemetry package, harness v2 | v0.84.0 (Aug 2026) |

Two of these are load-bearing for this wiki:

**v0.35.0** is why the [subagent](../ecosystem/subagent-extensions.md),
[todo](../ecosystem/todo-extensions.md) and
[compaction](../ecosystem/compaction-extensions.md) categories exist at all —
`registerTool` plus `pi.events` is the minimum needed to add a tool the model
can call and coordinate state around it.

**v0.81.0** ("accept native extension providers") is the quiet one. Once an
extension can register a **complete provider with its own auth**, "does Pi
support provider X" stops being a roadmap question. That is the enabling change
behind the [provider](../ecosystem/provider-extensions.md) and
[Claude-subscription](../ecosystem/claude-subscription-extensions.md) clusters.

## How minimal the core actually is

Measured against v0.84.2 source, the default context before you type anything:

| | chars |
|---|---|
| Default system prompt (one template, 18 lines) | 1,352 |
| Built-in tool descriptions (5 with prose descriptions) | 1,357 |
| **Baseline** | **~2,709** |

**It is seven built-in tools, not four.** The widely repeated
"`read`/`write`/`edit`/`bash`" line is outdated: `grep`, `find` and `ls` are
also built in. The four-tool framing still describes the *philosophy*
accurately, but not the tool list — worth correcting when you see it quoted
(including in earlier revisions of this wiki).

## What did not change

No MCP in core. No subagents in core. No approval prompts, no permission layer,
no governance. Each is instead a crowded extension category — the
[subagent survey](../ecosystem/subagent-extensions.md) alone tracks ~30
implementations, and [permissions](../ecosystem/permission-extensions.md) and
[human-in-the-loop](../ecosystem/human-in-the-loop-extensions.md) are among the
highest-adoption categories in the whole ecosystem.

That is the honest reading of year one: the refusal held, and it relocated the
cost rather than removing it. The features arrived anyway, as third-party
packages with their own version floors, tool-name collisions and maintenance
risk. Whether that is a good trade depends entirely on whether curating them is
something you enjoy.

## See also

- [How to Evaluate a Pi Extension](evaluation.md) — the framework for judging
  what the ecosystem produced
- [Pi Ecosystem Catalogs](catalogs.md) — where the packages are indexed
- [Permission Extensions](../ecosystem/permission-extensions.md) and
  [Human-in-the-Loop](../ecosystem/human-in-the-loop-extensions.md) — the two
  clearest cases of core refusal creating a market
