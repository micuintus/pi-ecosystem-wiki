---
title: Tool-Call Rendering Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - MasuRii-pi-tool-display
  - vinyroli-pi-tool-view
  - danielmlevans-pi-tool-display
  - tynanbe-pi-tool-display
  - pi-built-in-tool-renderer
  - pi-minimal-mode
  - pi-diff-extension
  - pi-issue-851
tags: [extension, tool-rendering, ui]
---

# Tool-Call Rendering Extensions

Pi extensions that customize how tool calls and their results display
in the TUI. The dominant theme: **OpenCode-style compact rendering
plus richer file-edit diffs**.

Pi's default tool-call rendering is functional but verbose, and
diff rendering for write/edit operations is minimal compared to
OpenCode and Claude Code. Several community extensions close that
gap. Pi tracks the underlying refactor as
[Issue #851 — Normalize built-in tool rendering API](https://github.com/badlogic/pi-mono/issues/851):
the proposal is to align built-in tools (`read`, `bash`, `edit`,
`write`) with the public `ToolDefinition` `renderCall` /
`renderResult` API that extensions already use.

## Extensions

### `MasuRii/pi-tool-display` — the canonical implementation

130 stars, the reference. "OpenCode-style tool rendering for the Pi
coding agent."

- Compact tool calls by default
- Richer diff rendering for file edits (closer to OpenCode/Claude
  Code)
- Output truncation for long results
- Improvements to thinking-label display and the native user prompt
  box
- Re-registers each built-in tool, delegates execution to the
  original, replaces `renderCall` / `renderResult`

### Forks of pi-tool-display

| Fork | Notes |
|---|---|
| **`vinyroli/pi-tool-view`** | Active fork. Same feature set; rebrand. |
| **`danielmlevans/pi-tool-display`** | Fork; same feature set. |
| **`tynanbe/pi-tool-display`** | Fork; same feature set. |

The fork landscape suggests upstream cadence and feature requests are
diverging — typical of a 1-author project that gets popular. No
canonical merger has emerged yet.

### Reference / example extensions in pi-mono

These ship inside `pi-mono` itself and serve as patterns the
community extensions build on:

| Extension | Path | What it shows |
|---|---|---|
| `built-in-tool-renderer.ts` | `examples/extensions/` | Re-register built-ins with custom `renderCall` / `renderResult`, delegating execution to originals. The pattern that all rendering extensions use. |
| `minimal-mode.ts` | `examples/extensions/` | Three display modes (Standard / Expanded / Minimal) toggleable with `Ctrl+O`. Demonstrates per-call render switching. |
| `diff.ts` | `.pi/extensions/` (in repo, not example) | `/diff` slash command — shows modified/deleted/new files from `git status` and opens the selected file in VS Code's diff view. Different layer (out-of-TUI viewer) from the inline-diff extensions. |

## Pattern (across all rendering extensions)

```ts
// Re-register the built-in with the same name
pi.registerTool("edit", {
  // delegate execution to the original
  execute: original.execute,
  // override only display
  renderCall: (input) => /* compact call display */,
  renderResult: (result) => /* rich diff display */,
});
```

This is the only sanctioned pattern today because Pi's built-in tools
have hardcoded rendering inside `ToolExecutionComponent`. Once
[Issue #851](https://github.com/badlogic/pi-mono/issues/851) lands,
overrides will be a first-class registration concern rather than a
re-registration trick.

## Comparison with other agents

| Agent | Default diff rendering | Customization |
|---|---|---|
| **Pi** | Minimal | Re-register tool with `renderCall` / `renderResult` |
| **OpenCode** | Polished, syntax-highlighted | Built-in; less extension-customizable |
| **Claude Code** | Polished | Closed-source; not customizable |

Pi's gap is real but bridgeable in user space, which is why this
niche has produced multiple competing extensions rather than one
winner.

## Tool-rendering vs status-bar extensions

Tool-call rendering (this page) is **inline message-stream UI**.
Status bars / footers / hash-anchored editor replacements live below
the input box and are surveyed in
[Footer and Hashline Extensions](footer-and-hashline-extensions.md).
Some extensions (e.g. `pi-tool-display`) touch both surfaces in one
package, which is why they sometimes show up cross-listed in package
catalogs.
