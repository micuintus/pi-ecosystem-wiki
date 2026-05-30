---
title: Pi Slash-Command Discovery & Palette Extensions
type: ecosystem
updated: 2026-05-30
sources:
  - pi-mono
  - pi-favorites-commands
  - tomsej-pi-ext
  - pi-command-center
  - pi-inline-slash-extension
tags: [extension, tui, slash-commands, palette, discoverability]
entries:
  - id: pi-favorites-commands
    name: pi-favorites-commands
    repo: alonmartin2222/pi-favorites-commands
    npm: pi-favorites-commands
    role: favorite-reorder-dropdown
    notes: "Star and reorder slash commands so they surface at the top of the `/` autocomplete dropdown (default sort is alphabetical, which buries the few you use daily). `/favorites` opens a centered overlay: `space` toggles ★, `⇧↑`/`⇧↓` reorders within the favorites section, type-to-filter. Works across all command sources pi reports — built-ins, extension commands, prompt templates, skill commands. Persists to `~/.pi/agent/data/slash-favorites.json` (plain JSON array, hand-editable, dotfile-syncable). Mechanism: installs a `CustomEditor` subclass that wraps pi's built-in `CombinedAutocompleteProvider`, re-sorting favorites first and decorating labels with ★; shadows `setAutocompleteProvider` so the pin survives pi's internal re-installs (theme change, `/reload`). Caveats (author-documented): mirrors pi's built-in command list locally (not exported from the public API, so a new built-in needs a bump), and wrapping the provider bypasses per-command argument autocomplete (`getArgumentCompletions`). Zero runtime deps. MIT, single author. Same author as pi-sticky-prompt."
  - id: tomsej-pi-ext-leader-key
    name: "leader-key palette (tomsej/pi-ext)"
    repo: tomsej/pi-ext
    role: which-key-command-palette
    notes: "Part of the tomsej/pi-ext collection (footer, tool pills, semantic git review, session archiving, handoff, cmux). The relevant piece here is the **leader-key palette**: `Ctrl+X` opens a floating command palette in the style of Vim's which-key / Emacs leader key — a modal launcher for actions rather than a reorder of the `/` dropdown. Collection is MIT, single author, the most-starred entry in this niche."
  - id: pi-command-center
    name: pi-command-center
    repo: w-winter/dot314
    npm: pi-command-center
    role: commands-cheat-sheet-widget
    notes: "A scrollable commands **cheat-sheet** rendered as a widget above the editor, toggled by a keybinding (configured in `config.json`: toggle / scrollUp / scrollDown / page keys). Optionally includes built-in interactive commands in the listing. Reference/discovery surface — shows what's available — rather than a reorder or launcher. Lives in the `w-winter/dot314` monorepo. MIT."
  - id: pi-inline-slash-extension
    name: pi-inline-slash-extension
    repo: datspike/pi-inline-slash-extension
    role: inline-slash-ux-fix
    notes: "Adjacent fix, not a palette. Makes slash autocomplete trigger where people actually type — inside normal text and on the second line, not just at the start of an empty editor — and stops a leading absolute path (`/home/user/file.ts`) from being misrouted as a slash command. UX correctness layer beneath the discovery tools above. MIT, single author, recent but low-activity."
  - id: pi-builtin-slash
    name: "pi core / autocomplete + /hotkeys"
    repo: earendil-works/pi-mono
    role: baseline
    notes: "Baseline everything here builds on. Typing `/` opens command completion via the built-in `CombinedAutocompleteProvider`, sorted alphabetically across built-ins, extension commands, `/skill:name`, and prompt templates. `/hotkeys` lists shortcuts. There is no built-in favoriting, reordering, or palette — hence this niche. Note open issue [#2983](https://github.com/earendil-works/pi/issues/2983): there's no public extension API yet for custom `@` autocomplete providers, which is why pi-favorites-commands resorts to wrapping the editor."
---

# Pi Slash-Command Discovery & Palette Extensions

Install a handful of extensions, themes, skills, and prompt templates
and Pi's `/` menu fills up fast. The built-in autocomplete sorts
everything alphabetically, so the two commands you run ten times a day
sit a long scroll from the top. This niche is about **navigating and
organizing the command surface** — distinct from *authoring* commands
(prompt templates, see [Prompt Extensions](prompt-extensions.md)).

## Short answer

- **Want your most-used commands pinned to the top of `/`?**
  [`pi-favorites-commands`](https://github.com/alonmartin2222/pi-favorites-commands)
  — star + reorder, persisted to disk. The most-adopted, most-focused
  option.
- **Prefer a modal launcher (which-key / leader-key) over the `/` dropdown?**
  the **leader-key palette** in [`tomsej/pi-ext`](https://github.com/tomsej/pi-ext)
  (`Ctrl+X`).
- **Just want to see everything available as a reference?**
  [`pi-command-center`](https://www.npmjs.com/package/pi-command-center)
  — a toggleable cheat-sheet widget.

## Three shapes

The niche splits by *how* you reach a command:

1. **Reorder the native dropdown** — keep typing `/`, but your
   favorites float to the top with a ★. `pi-favorites-commands`. Lowest
   behavior change; you don't learn a new gesture.
2. **Modal palette / launcher** — a separate keybinding (`Ctrl+X`)
   opens a floating picker, decoupled from the editor's `/`. The
   leader-key palette in `tomsej/pi-ext`. Familiar to Vim/Emacs users;
   good when you want commands reachable without clearing the editor.
3. **Cheat-sheet / reference widget** — `pi-command-center` renders the
   command list as a scrollable widget above the editor. Discovery and
   recall, not fast invocation.

Plus an adjacent **UX-correctness** layer:
[`pi-inline-slash-extension`](https://github.com/datspike/pi-inline-slash-extension)
fixes *where* slash autocomplete fires (mid-text, second line) and
stops absolute paths from being misrouted as commands. It composes
under any of the three.

## Why this is a wrapping hack, not a clean integration

Worth knowing before you install: Pi exposes no public API for
extensions to reorder or contribute to the `/` autocomplete (open
issue [`#2983`](https://github.com/earendil-works/pi/issues/2983) asks
for the analogous `@` provider API). So `pi-favorites-commands`
achieves its pin by **subclassing the editor** and wrapping
`CombinedAutocompleteProvider`, plus shadowing `setAutocompleteProvider`
to survive pi's internal re-installs. Consequences:

- It **mirrors pi's built-in command list locally** — a new built-in
  command won't be starrable until the extension bumps its mirror.
- It **bypasses per-command argument autocomplete**
  (`getArgumentCompletions`) — direct typing of `/cmd <arg>` still
  works, but the dropdown won't suggest arguments.

These are inherent to the wrapping approach until Pi ships a first-class
autocomplete-contribution API. The palette and cheat-sheet shapes sidestep
the editor entirely and don't carry this caveat.

## Picking guide

| Situation | Pick |
|---|---|
| **Keep the `/` workflow, just float favorites to the top** | [`pi-favorites-commands`](https://github.com/alonmartin2222/pi-favorites-commands) |
| **Vim/Emacs muscle memory; want a `Ctrl+X` launcher** | leader-key palette in [`tomsej/pi-ext`](https://github.com/tomsej/pi-ext) |
| **Discoverability — "what commands do I even have?"** | [`pi-command-center`](https://www.npmjs.com/package/pi-command-center) cheat-sheet widget |
| **Slash autocomplete misfires mid-text / paths misrouted** | [`pi-inline-slash-extension`](https://github.com/datspike/pi-inline-slash-extension) (composes with any above) |
| **Don't want a wrapping hack; fine with alphabetical** | pi core `/` + `/hotkeys` |

## See also

- [Prompt Extensions](prompt-extensions.md) — *authoring* the commands
  this page helps you *find* (prompt-template composers, per-template
  model binding) and the broader editor-input UX.
- [Tool-Call Rendering Extensions](tool-rendering-extensions.md) — other
  editor/TUI-surface customizations.
- [How to Evaluate a Pi Extension](../references/evaluation.md) — for
  current adoption / maintenance signals on each entry above.
