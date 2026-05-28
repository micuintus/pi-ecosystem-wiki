---
title: Pi Prompt Extensions
type: ecosystem
updated: 2026-05-28
sources:
  - pi-mono
  - pi-sticky-prompt
  - pi-prompt-history
  - pi-readline-search
  - pi-session-search
  - pi-prompt-composer
  - pi-prompt-template-model
  - true-queue
  - pi-copilot-queue
  - pi-better-messages-cache
  - pi-cache-graph
tags: [extension, prompt, editor, prompt-cache, queue]
entries:
  - id: pi-sticky-prompt
    name: pi-sticky-prompt
    repo: alonmartin2222/pi-sticky-prompt
    npm: pi-sticky-prompt
    role: floating-input-widget
    notes: "Two-part extension: TS extension + native macOS HUD (`PiStickyPrompt.app`). Pi runs in normal terminal scrollback, so scrolling up to read history scrolls the input prompt out of view; the HUD is an `NSPanel` (`.floating` level, `.canJoinAllSpaces`) auto-docked to the bottom of whichever screen hosts a terminal, sitting above every app including fullscreen Ghostty / Terminal / iTerm. Multi-session aware — each pi session publishes `~/.pi/agent/sockets/pi-<pid>.{sock,json}`; HUD scans descriptors, picks one, talks LF-delimited JSON over the UDS. Global hotkey `⌘⌥P`, `⌘L` session picker, `⌘M` collapse, `Esc` aborts current turn (twice → hide). Auto-refocuses the host terminal after Enter. macOS 13+ Apple Silicon. HUD delivered via `brew install --cask pi-sticky-prompt`."
  - id: pi-prompt-history
    name: pi-prompt-history
    repo: vedang/pi-prompt-history
    role: ctrl-r-prompt-search
    notes: "Ctrl+R-style reverse search over prior **user prompts** parsed from `~/.pi/agent/sessions/` JSONL. SQLite-backed index (size+mtime change detection, incremental). Floating overlay; seeds query from current editor contents. Local scope = sessions with exact-equal `cwd`; Global scope = all sessions, with Current-session / Same-cwd / Other-cwd grouping. Primary action `copy` (paste into editor) or `resume` (fork from the chosen prompt, or restore the whole session) — fork-from-prompt is the unique-value action vs. siblings. Slash commands: `/prompt-history`, `/prompt-history-global`, `/prompt-history-reindex [global]`, `/prompt-history-status`. Engineering discipline is high for a solo project (strict TS, biome + knip + jscpd, three test tiers). License: WTFPL via `LICENSE.txt` (package.json `\"license\": null` — mismatch)."
  - id: pi-readline-search
    name: pi-readline-search
    repo: mrshu/pi-readline-search
    npm: pi-readline-search
    role: readline-style-ctrl-r
    notes: "GNU Readline-style Ctrl+R reverse search in-editor over **current branch** history — both prompts and `!bash` commands. Ctrl+R / ↑ older, Ctrl+S / ↓ newer, Enter accept, Esc cancel. Tiny single-file extension. **Status: stale** (no commits in 90+ days as of 2026-05-28 against a fast-moving Pi). MIT."
  - id: pi-session-search
    name: pi-session-search
    repo: samfoy/pi-session-search
    npm: pi-session-search
    role: hybrid-fts-semantic-search
    notes: "Indexes, summarizes, and searches past pi coding sessions — not just user prompts but the whole session content. **FTS5 keyword search** always on (zero-config, no API keys). When an embedder is configured, adds **semantic embeddings** and fuses keyword + cosine-similarity scores via **Reciprocal Rank Fusion**. Optional auto-summarization. Browse-and-read model rather than copy-into-editor. MIT, strict TS, CI publish workflow, semver-tagged releases. The dominant adoption signal in the niche."
  - id: pi-prompt-composer
    name: pi-prompt-composer
    npm: pi-prompt-composer
    role: prompt-template-authoring
    notes: "Build composer-owned slash commands from plain Markdown prompts under `composed/`. Flat files become single slash commands; directories become grouped commands with Tab-completable subcommands, rich interactive selector, automatic missing-argument collection. `engine: liquid` frontmatter unlocks `if`, `for`, filters. Visible dispatch — the rendered prompt is shown before send."
  - id: pi-prompt-template-model
    name: pi-prompt-template-model
    npm: pi-prompt-template-model
    role: per-template-model-binding
    notes: "Adds `model`, `skill`, and `thinking` frontmatter keys to pi prompt templates. Invoking the template auto-switches to the named model, sets a thinking level, injects the named skill's context, then **restores your previous model when the turn finishes** — so a `/debug-python` template can run on a stronger model with tmux skill loaded without manual switching."
  - id: true-queue
    name: true-queue
    repo: Krystofee/true-queue
    role: hidden-task-queue
    notes: "Counter-pattern to steering. Steering injects future tasks into the current context — LLMs then rush to the last one (goal anchoring / completion bias). Queuing with a `+` prefix *hides* future tasks from the model: each task is sent as a fresh prompt only after the previous finishes. `++prefix` adds a pre-flight confirmation. `/queue` (or Ctrl+Q) opens an editor overlay (reorder / edit / pause / resume). Exposes an `enqueue_task` tool so the agent itself can defer work. Bundles a `sequential-isolation` skill."
  - id: pi-copilot-queue
    name: pi-copilot-queue
    repo: ayagmar/pi-copilot-queue
    npm: pi-copilot-queue
    role: ask-user-driven-queue
    notes: "TaskSync-style queue gated by an `ask_user` tool. Provider-targeted (defaults to `github-copilot`): injects an `ask_user` loop policy into the system prompt for managed providers, reinforces `tool_choice: required` (OpenAI-style) / `tool_choice: { type: \"any\" }` (Anthropic-style) so the model actually calls it. FIFO queue or cycling autopilot prompts. While a managed run is active, interactive input is captured into the queue by default instead of triggering a new turn. Status line shows elapsed time, ask_user call count, direct-reply misses; hygiene warnings at configurable thresholds (default 120 min / 50 calls). Settings UI via `/copilot-queue settings`."
  - id: pi-better-messages-cache
    name: pi-better-messages-cache
    repo: mcowger/pi-better-messages-cache
    npm: "@mcowger/pi-better-messages-cache"
    role: provider-cache-breakpoint
    notes: "Provider-level: implements the **dual cache-breakpoint** strategy for Anthropic-API-compatible providers, marking *both* the last assistant `tool_use` block and the last user message block with `cache_control` (built-in only marks the user message). Same shape as OpenCode / Kilo Code / Roo Code. Enforces Anthropic's 4-breakpoint hard cap (keeps system markers + newest, drops oldest). Also fixes a streaming control-character bug where raw `\\t` / `\\n` inside tool-call JSON crashed `JSON.parse` and left tool args as `{}` — replaces SDK `stream()` with `create().asResponse()` + `parseJsonWithRepair`. Reported impact on MiniMax / Kimi: near-zero cache hits → 80%+. Implements [`badlogic/pi-mono#1737`](https://github.com/badlogic/pi-mono/pull/1737), declined upstream. Registers via `pi.registerProvider(\"anthropic\", { api: \"anthropic-messages\", streamSimple })`, transparent to model definitions."
  - id: pi-cache-graph
    name: pi-cache-graph
    repo: championswimmer/pi-cache-graph
    npm: pi-cache-graph
    role: cache-observability
    notes: "Companion to pi-context-prune. `/cache graph` opens a TUI overlay with three switchable views — per-turn cache-hit %, cumulative cache-hit %, cumulative token volumes (input / cacheWrite / cacheRead) with distinct glyphs and a dynamic scale. `/cache stats` shows a per-assistant-message table with active-branch and whole-tree cumulative totals. `/cache export` writes the same data to `<session-name>.csv`. Cache hit % = `cacheRead / (input + cacheRead + cacheWrite)`."
---

# Pi Prompt Extensions

The single user-facing surface called "the prompt" actually spans
four distinct layers of the stack. The ecosystem has extensions
operating on each.

1. **Prompt input UX** — *where you type, what's around the editor.*
2. **Prompt-template authoring** — *named, reusable prompts behind a
   slash command.*
3. **Prompt queueing** — *delivery scheduling between you and the
   model.*
4. **Prompt-cache layer** — *how the assembled prompt is marked for
   provider-side caching, and how to see what hit and what missed.*

This page surveys all four. Compaction is a separate concern — see
[Compaction Extensions](compaction-extensions.md). Pi's built-in
editor / message-queue / steering behavior is documented in
[`usage.md`](https://pi.dev/docs/latest/usage); the extensions below
are deltas on top of that.

## 1. Prompt input UX

The editor is the bottom strip of the pi TUI. Built-in features
(Enter to send, Alt+Enter to queue a follow-up, Esc to abort and
restore queued messages, image paste, `/` slash menu, autocomplete)
already cover the common case. Two patterns extend this:

### `pi-sticky-prompt` — out-of-TUI floating editor

Pi runs in normal terminal scrollback, **not** alternate-screen mode.
The good news: your conversation history scrolls. The bad news: when
you scroll up, the input prompt scrolls *off* with everything else.

[`alonmartin2222/pi-sticky-prompt`](https://github.com/alonmartin2222/pi-sticky-prompt)
fixes that by externalizing the editor: a tiny native macOS
`NSPanel` (`.floating` level, `.canJoinAllSpaces`) docks itself to
the bottom of whichever screen has a terminal app open, talks to
live pi sessions over a Unix domain socket, and stays glued there
above every other window — including fullscreen Ghostty / iTerm /
Terminal.

The extension half (npm: `pi-sticky-prompt`) is the socket server:
each pi session writes `~/.pi/agent/sockets/pi-<pid>.{sock,json}`.
The HUD half (Homebrew cask: `pi-sticky-prompt`) is the floating
window itself, scanning the descriptor directory and attaching to
the most-recent live session. Multi-session aware — `⌘L` opens a
picker. Global hotkey `⌘⌥P` toggles visibility from anywhere.

A status dot encodes turn state (green idle / yellow streaming / red
disconnected). Sending while streaming **steers** the current turn
rather than queueing — the same boundary the TUI editor honors.

Sibling pattern to [pi-remote / pi-remote-web-ui](web-ui-and-remote-access.md)
but inverted: pi-remote puts the *whole* pi TUI in a browser, while
pi-sticky-prompt lifts just the *editor* out and leaves the
scrollback in your terminal.

Constraints: macOS 13+ Apple Silicon, Swift-built HUD app.

### Searching past prompts and sessions

Three extensions sit in this niche, with meaningfully different scopes
and mechanisms:

| | Mechanism | Scope | Primary action | Status |
|---|---|---|---|---|
| [`vedang/pi-prompt-history`](https://github.com/vedang/pi-prompt-history) | SQLite FTS over user prompts | All sessions, grouped Current / Same-cwd / Other-cwd | Copy into editor, *or* fork target session at the chosen prompt | active, solo |
| [`mrshu/pi-readline-search`](https://github.com/mrshu/pi-readline-search) | In-memory string-contains, Readline-style | **Current branch only** — prompts + `!bash` | Replace editor text | **stale** (no recent commits) |
| [`samfoy/pi-session-search`](https://github.com/samfoy/pi-session-search) | **FTS5 keyword + optional semantic embeddings**, hybrid via Reciprocal Rank Fusion | All sessions, indexed and summarizable | Browse / read past sessions | active, dominant adoption |

`pi-readline-search` is the lightest — one keystroke, current branch,
classical shell-history feel — but appears stale on a fast-moving
target.

`pi-prompt-history` is the classical Ctrl+R-for-prompts model with a
sharper persistence layer (SQLite, incremental size+mtime indexing,
Local/Global cwd scopes). Its unique-value action is **fork-from-prompt**:
resume a target session, fork at the chosen user message, pre-fill the
prompt text. License is WTFPL via `LICENSE.txt` with a `package.json`
license-field mismatch — fine for personal use, may trip corporate
policy filters.

`pi-session-search` is doing real IR over the whole session content,
not just prompts. FTS5 keyword search is always on with zero config;
optional semantic embeddings fuse BM25 + cosine-similarity scores via
Reciprocal Rank Fusion. Browse-and-read rather than copy-into-editor.
The dominant adoption signal in the niche and the only entry with
MIT + CI + multi-author maintenance.

These compose without conflict (different commands / keybindings).
If you want both "Ctrl+R for prompts with fork-from-prompt" and
"search the body of past sessions", install
`pi-prompt-history` + `pi-session-search`.

## 2. Prompt-template authoring

Pi already supports prompt templates as Markdown files. Two
extensions extend what they can do:

- **[`pi-prompt-composer`](https://www.npmjs.com/package/pi-prompt-composer)**
  — turns the `composed/` directory into composer-owned slash
  commands. Flat `.md` → single command; directory → grouped command
  with Tab-completable subcommands, automatic missing-argument
  collection, an interactive selector, and Liquid templating
  (`engine: liquid` unlocks `if`, `for`, filters). Visible dispatch
  shows the rendered prompt before send.
- **[`pi-prompt-template-model`](https://www.npmjs.com/package/pi-prompt-template-model)**
  — adds `model`, `skill`, and `thinking` frontmatter to any prompt
  template. Invoking the template switches to that model, sets the
  thinking level, loads the skill context, runs the turn, then
  *restores your previous model on completion*. A
  `/debug-python` template can run on Sonnet with the `tmux` skill
  loaded without you flipping settings.

The two compose cleanly: `pi-prompt-composer` shapes the slash
surface, `pi-prompt-template-model` shapes the model/skill behavior
behind each template.

## 3. Prompt queueing

Pi's built-in queue has two delivery modes:

- **Enter while streaming** = *steering* — delivered after the
  current assistant turn finishes its tool calls, **inside the same
  context**, before the next LLM call.
- **Alt+Enter while streaming** = *follow-up* — delivered after the
  entire run completes.

Two extensions reshape this:

### `true-queue` — hide future tasks from the model

[`Krystofee/true-queue`](https://github.com/Krystofee/true-queue)
argues that *steering* is the wrong primitive when you have a list
of future tasks: LLMs that see queued work in their context anchor
on completion and rush early tasks. The fix is to hide future work
entirely. `+message` queues a task the model never sees; when the
current turn finishes, the next `+` task is sent as a fresh prompt.
`++` adds a pre-flight confirmation. `Ctrl+Q` / `/queue` opens an
editor overlay for reorder / edit / pause / resume. An
`enqueue_task` tool lets the agent itself defer work. Bundles a
`sequential-isolation` skill.

### `pi-copilot-queue` — `ask_user`-tool-driven queue

[`ayagmar/pi-copilot-queue`](https://github.com/ayagmar/pi-copilot-queue)
takes the TaskSync approach. Instead of hiding tasks structurally,
it gives the model an `ask_user` tool and a loop policy in the
system prompt that tells it to call the tool after every completed
step. The extension intercepts those calls — if the user has queued
responses, the next one is returned; otherwise (in autopilot mode) a
cycling prompt is returned; otherwise the call waits for user input
or returns a configured fallback. Provider-gated (defaults to
`github-copilot`); reinforces `tool_choice: required` /
`tool_choice: { type: "any" }` so the model actually calls the tool.
Tracks elapsed time, ask_user call count, direct-reply misses; emits
hygiene warnings at configurable thresholds.

**Tradeoff:** `true-queue` is provider-agnostic and works on any
model — it sits between you and pi's normal turn machinery.
`pi-copilot-queue` works at the model behavior layer (system prompt
+ tool injection + tool_choice forcing) and therefore needs a model
that respects forced tool calls; the win is that the model can also
decide *when* it's ready for the next input.

## 4. Prompt-cache layer

The "prompt" sent to the provider on each turn is the entire
conversation prefix. Provider-side caches reuse that prefix only up
to the most recent `cache_control` marker, so cache hit rate is
mostly a function of where those markers sit. Two extensions
operate here:

### `pi-better-messages-cache` — fix dual cache breakpoints

[`mcowger/pi-better-messages-cache`](https://github.com/mcowger/pi-better-messages-cache)
implements the **dual cache-breakpoint** strategy: mark the last
assistant `tool_use` block *and* the last user message block with
`cache_control`, instead of just the user message. On MiniMax / Kimi
(Anthropic-API-compatible) this lifts cache hit rate from near-zero
to 80%+ — the preceding assistant `tool_use` + `thinking` blocks fell
*outside* the cached window with single-marker behavior. The strategy
matches what OpenCode, Kilo Code, and Roo Code do. The extension also
enforces Anthropic's 4-breakpoint hard cap (drops the oldest
message-level marker first) and fixes a streaming bug where raw
control characters in tool-call JSON crashed `JSON.parse` and left
tool args as `{}`. Registered via `pi.registerProvider` for the
`anthropic-messages` API — transparent to every model that uses it,
no per-model config. Originally proposed as
[`pi-mono#1737`](https://github.com/badlogic/pi-mono/pull/1737),
declined upstream.

### `pi-cache-graph` — observe cache hits and misses

[`championswimmer/pi-cache-graph`](https://github.com/championswimmer/pi-cache-graph)
adds `/cache graph` (TUI overlay with three switchable views:
per-turn cache-hit %, cumulative %, cumulative token volumes by
glyph), `/cache stats` (per-assistant-message table with active-branch
and whole-tree totals), and `/cache export` (CSV at project root).
Originally built as observability for
[`pi-context-prune`](https://github.com/championswimmer/pi-context-prune)
so you can see whether pruning is helping or hurting cache reuse, but
useful with any compaction or pruning extension on this wiki.

Cache hit % = `cacheRead / (input + cacheRead + cacheWrite)` —
denominator is the full prompt size that hit the provider this turn.
Anthropic-style providers report `cacheWrite` separately;
OpenAI-style providers report `cacheWrite = 0` and the formula
behaves identically.

## Recommendation matrix

| Situation | Default pick |
|---|---|
| **Scrolling history loses your input prompt (macOS)** | [`pi-sticky-prompt`](https://github.com/alonmartin2222/pi-sticky-prompt) — floating macOS HUD over UDS |
| **You retype the same prompts and want fork-from-prompt** | [`pi-prompt-history`](https://github.com/vedang/pi-prompt-history) — Ctrl+R + SQLite-indexed reverse search |
| **You want to actually search the body of past sessions** | [`pi-session-search`](https://github.com/samfoy/pi-session-search) — FTS5 + optional semantic embeddings, hybrid via RRF |
| **You have lots of project-local templates with structure** | [`pi-prompt-composer`](https://www.npmjs.com/package/pi-prompt-composer) for the slash surface + [`pi-prompt-template-model`](https://www.npmjs.com/package/pi-prompt-template-model) for per-template model/skill switching |
| **You want sequential isolation of queued tasks** | [`true-queue`](https://github.com/Krystofee/true-queue) — `+`-prefixed hidden queue |
| **You want the model to drive the queue (TaskSync-style)** | [`pi-copilot-queue`](https://github.com/ayagmar/pi-copilot-queue) — `ask_user` tool + forced tool_choice |
| **MiniMax / Kimi / other Anthropic-compatible providers wasting cache** | [`pi-better-messages-cache`](https://github.com/mcowger/pi-better-messages-cache) — dual cache_control markers |
| **You don't know if your cache is actually hitting** | [`pi-cache-graph`](https://github.com/championswimmer/pi-cache-graph) — `/cache graph`, `/cache stats`, `/cache export` |

## See also

- [Compaction Extensions](compaction-extensions.md) — what to do when
  the prompt prefix gets too long (pruning, observation ledgers,
  algorithmic compaction). Cache strategy and compaction strategy
  interact: every compaction is an automatic cache miss.
- [TODO List Extensions](todo-extensions.md) — a different shape of
  "tell the agent what to do next"; mostly orthogonal to queueing.
- [Web UI and Remote/Mobile Access](web-ui-and-remote-access.md) —
  for fully externalizing pi to a browser, of which
  `pi-sticky-prompt` is the lightest-touch variant (just the
  editor).
- [References — How to Evaluate a Pi Extension](../references/evaluation.md)
  — for live popularity / maintenance signals.
