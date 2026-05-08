---
title: Pi TODO List Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - pi-mono-todo-example
  - pi-todo-md
  - patriceckhart-pi-todo
  - jayshah-pi-agent-extensions
tags: [extension, todo]
entries:
  - id: pi-mono-todo
    name: "pi-mono examples/extensions/todo.ts"
    repo: badlogic/pi-mono
    role: reference-impl
    notes: "In-tree reference. Tool-only TODO with details-stored state. /todos slash command opens read-only viewer."
  - id: pi-todo-md
    name: pi-todo-md
    repo: forjd/pi-todo-md
    npm: pi-todo-md
    role: external-file
    notes: "Tool + repo-local TODO.md. LLM and human can both edit."
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

Survey of Pi extensions that manage TODO lists — both as LLM-callable
tools and as user-visible widgets. A TODO list is a natural state object
for autonomous agent loops, where each iteration picks the top item,
works it, and updates the list.

## Discriminator: tool-only vs rendered widget vs external file

- **Tool-only**: LLM has a `todo` tool but the list is invisible unless
  the user runs a slash command.
- **Tool + rendered widget**: list updates appear in the TUI as a live,
  persistent widget.
- **Tool + external file**: list lives in `TODO.md` or another sync
  target (Apple Reminders, Linear, etc.); LLM and human can both edit.

Pi has implementations of all three. None match Claude Code's
`TodoWrite` widget polish, but several solve the underlying "shared
state" problem cleanly.

## Surveyed extensions

| Extension | Pattern | State location | UI |
|---|---|---|---|
| **`pi-mono/examples/extensions/todo.ts`** | Tool-only (reference impl) | Session JSONL via `tool_result.details` | `/todos` slash command opens read-only viewer |
| **`forjd/pi-todo-md`** | Tool + repo-local `TODO.md` | `TODO.md` in nearest git root | File visible in editor; LLM uses `todo_md` tool |
| **`patriceckhart/pi-todo`** | Tool + Apple Reminders sync | macOS Reminders ("pi" list) via Swift+EventKit helper | Interactive TUI for browse/edit |
| **`jayshah5696/pi-agent-extensions`** | Bundle including TODO-related items | varies | varies |

## Reference implementation pattern

The `pi-mono` `todo.ts` example is the canonical "state stored in tool
result `details`, branches with the session tree" pattern. Worth
understanding because **any extension that wants branching-safe state
should use it**:

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

When the user forks the session at any point, TODO state automatically
reconstructs to its value at that point — `details` is part of the tool
result message that's part of the branch. No separate file to keep in
sync.

## Polish gap vs Claude Code's `TodoWrite`

Claude Code's `TodoWrite` is a first-class built-in tool with TUI
rendering on every state change. The polish gap is structural:

- Claude Code renders todo updates as a custom message type with a
  sticky widget that follows the message stream.
- Pi extensions can render via `ctx.ui.setWidget("todo", lines)` (used
  by some Ralph-style extensions for status), but this is a single
  status line, not an embedded inline widget.
- The `pi-mono` reference uses a modal viewer (opened via `/todos`) —
  different UX shape.

Closing this gap would require custom message rendering
(`pi.registerCustomMessageRenderer`) or a more capable inline-widget
primitive in `pi-tui`.

## See also

- [Loop and Ralph Extensions](loop-extensions.md) — loop drivers that
  consume TODO state as their iteration source.
