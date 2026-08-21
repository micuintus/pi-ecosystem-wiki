---
title: Pi Year One, and How It Compares to opencode
type: comparison
updated: 2026-08-21
sources:
  - pi-mono
  - pi-releases
  - pi-extensions-docs
  - opencode-repo
  - opencode-changelog
  - opencode-core-v2
  - martianlee-opencode-architecture
  - bitter-frontier-pi-profile
  - tensorlake-agent-comparison
  - bswen-pi-vs-others
tags: [comparison, opencode, history, architecture]
---

# Pi Year One, and How It Compares to opencode

## Short answer

Pi and opencode are not competing implementations of the same idea; they
disagree about **where a coding agent should keep its complexity**. opencode
puts it in the product — a headless engine with many front-ends, MCP, LSP,
subtasks and permissions built in. Pi puts it in *your* config — four tools
in core and an extension API rich enough that everything else is somebody's
package.

Pi's first year did not soften that stance. It hardened it: the core stayed
small while the *extension surface* grew until third parties could ship
things that would be core features anywhere else, including entire model
providers.

## Pi's first year in numbers

The repository opened 2025-08-09 and reached **v0.84.2** by 2026-08-20 —
essentially the whole project life is one year, across ~5,650 commits.

| Period | Commits | What it was |
|---|---|---|
| Aug–Oct 2025 | ~270 | `packages/ai` first: provider abstraction, models.dev integration, streaming |
| Nov 2025 | 280 | the agent/TUI takes shape; rapid minor releases begin |
| Dec 2025 | 868 | **the extension platform lands** — skills, commands, compaction hooks |
| Jan 2026 | **1,227** | peak: `registerTool`, `pi.events`, `setActiveTools`, plan-mode |
| Feb–Aug 2026 | ~400–500/mo | steady: providers, compaction, telemetry, harness v2 |

The shape of that curve is the story. A four-month burst built the extension
platform; everything since has been consolidation at a remarkably even
cadence, with the release rhythm slowing from several minors a week to
roughly one every one-to-two weeks.

### The primitives, and when they arrived

| Primitive | First shipped |
|---|---|
| Skills | v0.19.0 (Dec 2025) |
| `registerCommand`, `session_before_compact` | v0.31.0 (Dec 2025) |
| `setActiveTools`, plan-mode | v0.34.0 (Jan 2026) |
| `registerTool`, `pi.events` | v0.35.0 (Jan 2026) |
| Provider registry (OAuth refactor) | v0.50.0 (Jan 2026) |
| **Native extension providers** (`accept native extension providers`) | v0.81.0 (Jul 2026) |
| Telemetry package, harness v2 | v0.84.0 (Aug 2026) |

v0.81.0 is the quiet milestone. Once an extension can register a **complete
provider with its own auth**, "Pi supports provider X" stops being a
roadmap question — which is precisely why the
[provider](../ecosystem/provider-extensions.md) and
[Claude-subscription](../ecosystem/claude-subscription-extensions.md)
clusters exist.

### What did *not* change

No MCP in core. No subagents in core. No approval prompts, no governance
layer. Every one of those is a live, crowded extension category instead —
the [subagent survey](../ecosystem/subagent-extensions.md) alone tracks
~30 implementations of a feature both competitors ship built-in. The refusal
is the product decision, and it held for a year.

## opencode today

opencode moved to the **`anomalyco/opencode`** org and is on the **v1.18.x**
line — a versioning gap that flatters neither project, since opencode's 1.x
reflects a product with a stability promise while Pi's 0.x reflects an API
still deliberately in motion.

Architecturally it is the mirror image of Pi:

- **Headless server first.** `opencode serve` runs an HTTP/OpenAPI engine
  (default port 4096); the TUI, web app, desktop Electron client, Slack bot
  and IDE integrations are all *clients* of it.
- **Bun runtime, Effect-ts core.** The "Core V2" work moved provider
  discovery, credentials and events into typed Effect services.
- **Batteries included.** 75+ providers via the AI SDK and models.dev, MCP,
  LSP, first-class `subtask`, permissions, session sharing.
- **Vercel AI SDK owns the loop.** `streamText()` executes tools; opencode
  orchestrates around it.

## Head-to-head

| | Pi | opencode |
|---|---|---|
| **Core philosophy** | minimal core, extend everything | integrated product |
| **Built-in tools** | 4 (`read`/`write`/`edit`/`bash`) | large set incl. LSP-aware |
| **Who owns the loop** | Pi itself (`packages/agent`) | Vercel AI SDK `streamText()` |
| **Persistence** | JSONL session files on disk | SQLite / durable event log |
| **Async model** | plain async/await | Effect-ts |
| **Subagents** | extensions only (~30 of them) | built-in `subtask` |
| **MCP** | extension only | built-in |
| **Front-ends** | TUI (plus community VS Code ext) | TUI, web, desktop, Slack, IDE — all on one server |
| **Extension API** | very large and the main event | present, smaller role |
| **Versioning** | 0.x, moves fast | 1.x, stability promise |

### Where each genuinely wins

**Pi wins on adaptability.** The extension API is the product, and it shows:
extensions can replace the system prompt, swap providers, rewrite compaction,
own the editor, and register tools the model discovers at runtime. If your
workflow is unusual, Pi bends to it. Its JSONL-on-disk sessions are also
plainly inspectable — the property the whole
[recall/compaction](../ecosystem/compaction-extensions.md) cluster is built
on.

**opencode wins on cohesion.** One server, many surfaces is a genuinely
better answer for teams who want the same agent in a terminal, a browser and
Slack without gluing anything. Built-in MCP/LSP/permissions means no
per-feature package-shopping, no version-skew between six authors' packages,
and no tool-name collisions — a failure mode Pi users meet regularly.

### The cost nobody advertises

Pi's model pushes integration risk onto the user. Multiple extensions
claiming the same tool name genuinely break each other; abandoned packages
are your problem; and evaluating five implementations of one feature is a
real tax — this wiki exists because of it. opencode's cost is the mirror:
when the built-in behaviour is not what you want, you are negotiating with a
product rather than writing 40 lines.

## Choosing

| If you… | Pick |
|---|---|
| want a terminal agent that adapts to a bespoke workflow | Pi |
| want the same agent in terminal, browser, Slack, IDE | opencode |
| need MCP/LSP working today without curation | opencode |
| want to *build* agent tooling, not just use it | Pi |
| value a stability promise over velocity | opencode |
| run local/open-weight models with a thin harness | either; both are provider-agnostic |

## Caveats

- **Popularity figures for both projects are unreliable.** Published star
  and download counts for Pi in mid-2026 range from ~15k to ~80k depending
  on the article, with several sources showing signs of automated
  generation. Use the recipes in [evaluation](evaluation.md) to query live
  numbers instead of trusting any figure quoted in prose, here or elsewhere.
- **"opencode2" is informal.** The upstream project is `opencode`; the "2"
  refers to the Core V2 / v1.x-era rewrite, not a separately released
  product.
- **Feature tables age badly.** MCP-in-core and subagents-in-core are the
  two most likely to move; re-verify against the changelogs before relying
  on either.

## See also

- [Subagent extensions](../ecosystem/subagent-extensions.md) — the ~30
  answers to opencode's one built-in `subtask`
- [Provider extensions](../ecosystem/provider-extensions.md) — what
  v0.81.0's native extension providers unlocked
- [MCP integration](../ecosystem/mcp-integration.md) — closing the one gap
  opencode ships by default
