---
title: Pi TODO List Extensions
type: ecosystem
updated: 2026-05-10
sources:
  - pi-mono-todo-example
  - pi-todo-md
  - patriceckhart-pi-todo
  - jayshah-pi-agent-extensions
  - mitsuhiko-agent-stuff
  - tintinweb-pi-manage-todo-list
  - tintinweb-pi-tasks
  - edxeth-pi-tasks
  - soleone-pi-tasks
  - popododo-pi-stuff
tags: [extension, todo]
entries:
  - id: pi-mono-todo
    name: "pi-mono examples/extensions/todo.ts"
    repo: earendil-works/pi-mono
    role: reference-impl
    notes: "297 LOC. Tool-only TODO with details-stored state (branches with session JSONL). Custom tool shape (add/update/remove/set-state). /todos slash command opens read-only viewer."
  - id: tintinweb-pi-manage-todo-list
    name: pi-manage-todo-list
    repo: tintinweb/pi-manage-todo-list
    npm: pi-manage-todo-list
    role: minimal-idiomatic
    notes: "506 LOC. Single tool manage_todo_list({operation: read|write, todoList}) — verbatim mirror of GitHub Copilot's tool shape. setWidget factory + theme + strikethrough + /todos. Session-entry persistence (branch-safe). Minimal surface, no DAG."
  - id: edxeth-pi-tasks
    name: pi-tasks (edxeth)
    repo: edxeth/pi-tasks
    npm: "@edxeth/pi-tasks"
    role: full-task-system
    notes: "~1,100 LOC. Fork of tintinweb/pi-tasks reworked toward Claude Code parity. 5 tools (task_create/list/get/update/batch). Dependency DAG with cycle detection. Per-task stats (runtime, tools used, tokens). 3-view widget cycle. Reminders after 10 idle turns. File-backed (~/.pi/tasks/<sessionKey>/) with fork-copy and branch-aware restore."
  - id: tintinweb-pi-tasks
    name: pi-tasks (tintinweb)
    repo: tintinweb/pi-tasks
    npm: "@tintinweb/pi-tasks"
    role: dag-tasks
    notes: "2,061 LOC. 7 tools (TaskCreate/List/Get/Update/Output/Stop/Execute) — verbatim mirror of Claude Code's tool shape. Built-in DAG with deps shown in widget. Animated star spinner. File-backed across sessions."
  - id: soleone-pi-tasks
    name: pi-tasks (Soleone)
    repo: Soleone/pi-tasks
    npm: pi-tasks
    role: pluggable-backend
    notes: "3,566 LOC. Pluggable backend system — beads / TODO.md / others. Heavyweight; the big-tent option."
  - id: mitsuhiko-todos
    name: "todos.ts (mitsuhiko/agent-stuff)"
    repo: mitsuhiko/agent-stuff
    npm: mitsupi
    role: external-file
    notes: "2,082 LOC. File-per-todo in .pi/todos/*.md. Dependency tracking by index. Status indicator widget. Less branch-safe than session-entry-based approaches (file lives outside the JSONL)."
  - id: pi-todo-md
    name: pi-todo-md
    repo: forjd/pi-todo-md
    npm: pi-todo-md
    role: external-file
    notes: "Tool + repo-local TODO.md. LLM and human can both edit the same file. Custom tool shape."
  - id: patriceckhart-pi-todo
    name: pi-todo (patriceckhart)
    repo: patriceckhart/pi-todo
    role: external-sync
    notes: "Tool + Apple Reminders sync via Swift+EventKit. Interactive TUI for browse/edit. macOS only."
  - id: jayshah-pi-extensions-todo
    name: jayshah5696/pi-agent-extensions
    repo: jayshah5696/pi-agent-extensions
    role: bundle
    notes: "Bundle including TODO-related items among other extensions."
---

# Pi TODO List Extensions

## Contents

- [Discriminator](#discriminator-tool-only-vs-rendered-widget-vs-external-file)
- [Surveyed extensions](#surveyed-extensions)
- [Idiomatic LLM-known TODO tool shapes](#idiomatic-llm-known-todo-tool-shapes)
- [Reference implementation pattern](#reference-implementation-pattern)
- [The four-layer widget stack](#the-four-layer-widget-stack)
- [Workflow extensions on top of TODOs](#workflow-extensions-on-top-of-todos)
- [Picking a TODO extension](#picking-a-todo-extension)
- [Why no Pi extension matches Claude Code's polish](#why-no-pi-extension-matches-claude-codes-todowrite-polish)
- [See also](#see-also)

Survey of Pi extensions that manage TODO lists — both as LLM-callable
tools and as user-visible widgets. A TODO list is a natural state
object for autonomous agent loops, where each iteration picks the top
item, works it, and updates the list.

## Discriminator: tool-only vs rendered widget vs external file

- **Tool-only**: LLM has a `todo` tool but the list is invisible
  unless the user runs a slash command.
- **Tool + rendered widget**: list updates appear in the TUI as a
  live, persistent widget.
- **Tool + external file**: list lives in `TODO.md` or another sync
  target (Apple Reminders, Linear, etc.); LLM and human can both
  edit.

Pi has implementations of all three.

## Surveyed extensions

| Extension | LOC | Pattern | Tool shape | Trained-on origin | State | UI |
|---|---|---|---|---|---|---|
| `pi-mono/examples/extensions/todo.ts` | 297 | Tool-only (reference) | Custom (add/update/remove/set-state) | None — bespoke | session `details` (branch-safe) | `/todos` slash, modal viewer |
| **`tintinweb/pi-manage-todo-list`** | **506** | **Tool + widget + slash** | **`manage_todo_list` `{operation: read\|write, todoList}`** | **GitHub Copilot Chat — verbatim** | session `details` (branch-safe) | `setWidget` factory + theme + strikethrough + `/todos` |
| `edxeth/pi-tasks` | ~1,100 | 5 tools + widget + file-backed | `task_create`/`task_list`/`task_get`/`task_update`/`task_batch` | Claude Code — verbatim | file-backed (`~/.pi/tasks/`), fork-copy, branch-aware restore | `setWidget` factory, 3-view cycle, stats inline |
| `tintinweb/pi-tasks` | 2,061 | 7 tools + DAG + file-backed | `TaskCreate`/`TaskList`/`TaskGet`/`TaskUpdate`/`TaskOutput`/`TaskStop`/`TaskExecute` | Claude Code — verbatim | file-backed (cross-session) | Animated spinner, deps shown |
| `Soleone/pi-tasks` | 3,566 | Pluggable backends | Variable per backend | Variable | beads / `todo.md` / etc. | Yes |
| `mitsuhiko/agent-stuff` `todos.ts` | 2,082 | Tool + file-per-todo | Custom (markdown files) | None | `.pi/todos/*.md` | Status indicator |
| `forjd/pi-todo-md` | — | Tool + repo `TODO.md` | `todo_md` | None | `TODO.md` in git root | File visible in editor |
| `patriceckhart/pi-todo` | — | Tool + Apple Reminders sync | Custom + EventKit helper | None | macOS Reminders | Interactive TUI |
| `jayshah5696/pi-agent-extensions` | — | Bundle | Variable | None | Variable | Variable |

## Idiomatic LLM-known TODO tool shapes

LLMs are heavily trained on two TODO-tool shapes. If an extension
matches one of these, the model uses it correctly with **zero
system-prompt fine-tuning**. Inventing a custom shape (the in-tree
reference, `mitsuhiko`, `forjd`, `patriceckhart`) burns prompt tokens
teaching the model your schema.

| Field | Claude Code `TodoWrite` | VSCode Copilot `manage_todo_list` |
|---|---|---|
| Tool name | `TodoWrite` | `manage_todo_list` |
| Wrapper key | `todos` | `todoList` |
| Item label | `content` | `title` |
| Active form | `activeForm` (required) | (none) |
| Status values | `pending` / `in_progress` / `completed` | (Copilot-specific) |
| Operation flag | (none — single tool) | `operation: read\|write` |

The two shapes are **not equivalent**. Models trained primarily on
Claude Code data have a stronger prior for `TodoWrite`; OpenAI- or
Copilot-tuned models lean toward `manage_todo_list`.

| Pi extension | Mirrors |
|---|---|
| `tintinweb/pi-manage-todo-list` | Copilot's `manage_todo_list` verbatim |
| `tintinweb/pi-tasks` | Claude Code's `TodoWrite`/`Task*` family verbatim |
| `edxeth/pi-tasks` | Claude Code's `Task*` family verbatim (with edxeth-specific extensions) |

## Reference implementation pattern

The `pi-mono` `todo.ts` example is the canonical "state stored in
tool result `details`, branches with the session tree" pattern.
Worth understanding because **any extension that wants
branching-safe state should use it**:

```ts
pi.registerTool({
  name: "todo",
  parameters: TodoParams,
  async execute(_id, params, _signal, _onUpdate, _ctx) {
    // ... mutate todos in-memory ...
    return {
      content: [{ type: "text", text: humanReadableStatus }],
      details: { action, todos: [...todos], nextId } as TodoDetails,
    };
  },
});

const reconstructState = (ctx: ExtensionContext) => {
  todos = []; nextId = 1;
  for (const entry of ctx.sessionManager.getBranch()) {
    if (entry.type !== "message") continue;
    const msg = entry.message;
    if (msg.role !== "toolResult" || msg.toolName !== "todo") continue;
    const details = msg.details as TodoDetails | undefined;
    if (details) { todos = details.todos; nextId = details.nextId; }
  }
};

pi.on("session_start", async (_e, ctx) => reconstructState(ctx));
pi.on("session_tree",  async (_e, ctx) => reconstructState(ctx));
```

When the user forks the session at any point, TODO state
automatically reconstructs to its value at that point — `details` is
part of the tool result message that's part of the branch. No
separate file to keep in sync.

`tintinweb/pi-manage-todo-list` follows this pattern. File-backed
extensions (`edxeth/pi-tasks`, `tintinweb/pi-tasks`, `mitsuhiko`)
deliberately trade branch-safety for cross-session/`/compact`
survival.

## The four-layer widget stack

Pi exposes six visibility primitives; a polished TODO experience
uses four of them in stacked layers. No production extension uses
all four; the in-tree reference covers two.

| # | Layer | Primitive | Used by | Status |
|---|---|---|---|---|
| 1 | Action confirmation (per-call) | `renderResult(result, {expanded}, theme, ctx)` returning a TUI Component | `pi-mono/examples/extensions/todo.ts` ("✓ #3 done"); all TODO impls | Standard |
| 2 | Persistent status (always visible) | `ctx.ui.setWidget(key, factory, opts)` — component factory `(tui,theme) => { render(width):string[]; invalidate():void }` | `davebcn87/pi-autoresearch` (collapsed/expanded states, configurable shortcuts); `edxeth/pi-tasks` (3-view cycle, inline stats); `tintinweb/pi-manage-todo-list` (theme + strikethrough) | **Factory form recommended** |
| 3 | Stream-pinned snapshot (Claude Code-style) | `pi.registerMessageRenderer(customType, renderer)` + extension emits `pi.sendMessage({customType, details, display:true})` after meaningful changes | `pi-mono/examples/extensions/message-renderer.ts` (in-tree demo only) | **No production extension uses this** |
| 4 | Modal deep-dive (on-demand) | `/todos` command + `ctx.ui.custom<T>(factory)` | `pi-mono` reference (`/todos`); pi-autoresearch dashboard; mitsuhiko loop preset selector | Standard |

### Why the factory form of `setWidget` is the right baseline

```ts
ctx.ui.setWidget("todos", (tui, theme) => ({
  render(width: number): string[] {
    const safeWidth = Math.max(1, width || getTuiSize(tui).width);
    return state.expanded
      ? renderFullList(state, safeWidth, theme)
      : [renderOneLiner(state, safeWidth, theme)];
  },
  invalidate(): void {},
}));
```

Properties:

- `render(width)` invoked on every TUI repaint — any state mutation
  reflects immediately, no manual `pi.repaint()` plumbing.
- Width-aware: collapses to a one-liner on narrow terminals, expands
  on wide ones.
- Theme-aware: uses `theme.fg("accent", ...)` etc., respects user
  theme switches without code changes.

Most extensions use the simpler `setWidget(key, ["line 1", "line 2"])`
form which doesn't auto-react to terminal resize. The factory form is
strictly more capable.

### Layer 3 is the unrealized polish opportunity

`registerMessageRenderer` lets an extension paint **inline messages
that pin in the chat scroll** — the same UX slot Claude Code uses for
`TodoWrite` widgets that follow the message stream:

```ts
pi.registerMessageRenderer("todo-snapshot", (message, { expanded }, theme) => {
  const { todos } = message.details as { todos: TodoItem[] };
  // ... build a Box with the full TODO list pinned inline ...
  return box;
});

pi.sendMessage({
  customType: "todo-snapshot",
  content: `${doneCount}/${total} done`,
  display: true,
  details: { todos: [...todos] },
});
```

The message lives in the session JSONL with the rest of the chat —
it branches with `/fork`/`/clone`, it compacts naturally, it's
preserved across `/reload`. **No production Pi extension does this
for TODO state.** Closing the gap to Claude Code's `TodoWrite` polish
is mostly Layer 3 work.

## Workflow extensions on top of TODOs

`popododo0720/pi-stuff/workflow-extension` (~7,000 LOC) layers a
deterministic 6-stage workflow (`Plan → Verify Plan → Implement →
Verify Impl → Compound → Done`) on top of a TODO list with a
`set_todos` tool. `transition.ts` enforces stage-to-stage progression
— write/edit tools are blocked outside the implementation stage. Per-TODO
Implement → Verify → Compound cycles. Mandatory git/worktree gate as
TODO #1 if dirty tree at start.

Single-author and stale (last push 2026-03-03), but a useful
proof-of-pattern that state-machine + transition-guards is a workable
shape on Pi — `before_agent_start` is the right hook for deferred
compaction between TODO cycles, header-injected state flag is more
reliable than session-entry parsing for state detection.

## Picking a TODO extension

| Goal | Best choice | Why |
|---|---|---|
| **Minimal idiomatic primitive** (LLM uses it correctly out of the box) | **`tintinweb/pi-manage-todo-list`** | Verbatim Copilot shape, single tool, branch-safe, polished widget. The default recommendation. |
| **Full Claude Code-style task experience** (DAG, stats, reminders) | **`edxeth/pi-tasks`** | Most feature-complete. Verbatim Claude Code shape. File-backed survives `/compact`. Deliberate opinions. |
| **Cross-session task tracking with DAG** | `tintinweb/pi-tasks` | File-backed, dependency tracking, animated widget. Heavier than `manage_todo_list`. |
| **Maximum flexibility** (multiple storage backends) | `Soleone/pi-tasks` | Pluggable beads/markdown/etc. Heavyweight. |
| **Reference for building your own** | `pi-mono/examples/extensions/todo.ts` | The canonical branching-safe `details`-based pattern. 297 LOC. |
| **Sync with macOS Reminders** | `patriceckhart/pi-todo` | Bidirectional Apple Reminders integration. macOS only. |
| **Plain markdown the human edits too** | `forjd/pi-todo-md` | One file in the repo root. No DAG, no widget. |

## Why no Pi extension matches Claude Code's `TodoWrite` polish

Claude Code's `TodoWrite` is a first-class built-in tool with TUI
rendering on every state change. The polish gap in Pi is **structural
in the extensions, not in Pi itself** — Pi exposes everything needed
(see the four-layer stack above); nobody has wired all four layers
together yet. The closest are `tintinweb/pi-manage-todo-list` (L1+L2+L4),
`edxeth/pi-tasks` (L1+L2+L4 with stats), and `davebcn87/pi-autoresearch`
(L1+L2+L4 for autoresearch state, not TODOs). Layer 3
(`registerMessageRenderer`) is unused in production.

## See also

- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes for picking among these
- [Loop and Ralph Extensions](loop-extensions.md) — loop drivers that consume TODO state as their iteration source
- [Subagent Extensions](subagent-extensions.md) — companion survey
