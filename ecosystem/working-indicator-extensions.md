---
title: Pi Working / Thinking Indicator Extensions
type: ecosystem
updated: 2026-05-29
sources:
  - pi-mono
  - pi-mono-working-indicator-example
  - pi-animations
  - pi-spinner-dustydonkey
  - pi-fancy-loader
  - shitty-extensions-ultrathink
tags: [extension, tui, spinner, animation, working-indicator]
entries:
  - id: pi-animations
    name: pi-animations
    repo: arpagon/pi-animations
    npm: pi-animations
    role: multi-state-animation-suite
    notes: "21 terminal animations (demoscene fire, Matrix rain, Pac-Man, aurora, starfield, a `crush` character-scrambler, pi-pulse, shimmer, …) in 1-line and 3-line variants, ANSI true color + Nerd Font glyphs. Distinctive: **three distinct animation states** — thinking (`thinking_start`/`thinking_end`), working (`agent_start`/`agent_end`), tool (`tool_execution_start`/`tool_execution_end`), with priority thinking > tool > working. Per-state assignment (`/animation thinking:aurora working:matrix3 tool:fire3`), configurable width (full/50/custom), interactive `/animation showcase` browser, random mode. 1-line animations ride `ctx.ui.setWorkingMessage()` alongside pi's braille spinner; 3-line use a widget. MIT, single author, 2 releases. Feature-complete but no commits since creation day (2026-03-20) — watch staleness."
  - id: pi-spinner-dustydonkey
    name: "@dustydonkey/pi-spinner"
    repo: HarshalRathore/pi-spinner
    npm: "@dustydonkey/pi-spinner"
    role: claude-code-style-shimmer-verbs
    notes: "The closest match to the Claude Code / Crush busy aesthetic: replaces pi's braille spinner with frame presets + **rotating status verbs** + a gentle per-character **shimmer** sweep. 6 frame presets (Claude star sequence, braille, pulse, dot, star, none), 5 verb presets (187 Claude Code verbs, short, technical, fun, custom). Idle-aware — shimmer pauses while waiting on sub-agents / user input to avoid flicker. `/spinner` and `/verbs` slash commands, custom frames/interval, settings persist under `workingSpinner` in `.pi/settings.json`. MIT, single author, fresh (created 2026-05). Highest npm pull of the three despite low stars."
  - id: pi-fancy-loader
    name: pi-fancy-loader
    npm: pi-fancy-loader
    role: spinner-palette-randomizer
    notes: "50+ Unicode spinner sequences (braille, orbital, progress bars), dynamic HSL color palettes (random hue/sat/lightness jitter), 100+ Claude-Code-inspired verb phrases ('Cogitating', 'Vibecoding Internally'). Auto-activates on `agent_start` (random spinner + palette), restores on `agent_end`, updates working message on tool calls. Commands: `/loader-info`, `/loader-random`, `/loader-preview`, `/loader-pick`. MIT per package.json. **npm-only — no public source repo**, single published version (2026-05-10), opaque to code-quality audit; treat with the usual caution for unauditable packages that run in-process."
  - id: shitty-extensions-ultrathink
    name: "ultrathink (shitty-extensions)"
    repo: hjanuschka/shitty-extensions
    role: rainbow-easter-egg
    notes: "Not a spinner replacement — a `/ultrathink` toggle that renders a rainbow-animated 'ultrathink' effect with a Knight-Rider shimmer. Easter-egg / novelty, bundled inside the popular shitty-extensions collection rather than standalone. Mentioned for completeness; pick one of the three dedicated extensions above for an actual working-indicator."
  - id: pi-mono-working-indicator-example
    name: "pi-mono working-indicator.ts / titlebar-spinner.ts"
    repo: earendil-works/pi-mono
    role: platform-primitive
    notes: "Not an extension to install — the built-in API and examples everything above builds on. `ctx.ui.setWorkingIndicator({ frames: [...] })` (custom animated/static/hidden frames, added in pi-mono #3413), `ctx.ui.setWorkingMessage(text)` (replace loader text inline), `ctx.ui.setWorkingVisible(false)` (hide the loader row). Example extensions: `working-indicator.ts` (custom frames), `titlebar-spinner.ts` (braille spinner in the terminal title), and a rainbow-text custom editor effect. Start here if you want to build your own."
---

# Pi Working / Thinking Indicator Extensions

The strip Pi shows while the agent is busy — the spinner and "Working…"
text below the editor — is customizable. Several extensions replace
it with richer animations and rotating status verbs, in the style of
Claude Code's and Crush's playful busy widgets.

This is a distinct niche from two neighbours:

- [Footer / Powerline Extensions](footer-extensions.md) — the
  *persistent* status bar (model, cost, branch). Always visible, not
  tied to the busy state.
- [Tool-Call Rendering Extensions](tool-rendering-extensions.md) — how
  *tool output* and thinking-step *content* render. (Structured
  thinking-step rendering like `fluxgear/pi-thinking-steps` lives
  there, not here — it renders the reasoning text, not the spinner.)

What this page covers is specifically the **transient busy
indicator** during streaming / thinking / tool execution.

## The platform primitive

Everything here builds on pi core's working-indicator API (added in
[`pi-mono#3413`](https://github.com/badlogic/pi-mono/issues/3413)):

- `ctx.ui.setWorkingIndicator({ frames: [...] })` — custom animated or
  static frames (or hide it).
- `ctx.ui.setWorkingMessage("Thinking deeply…")` — replace the loader
  *text* inline, keeping pi's braille spinner.
- `ctx.ui.setWorkingVisible(false)` — hide the loader row entirely.

The core examples `working-indicator.ts` and `titlebar-spinner.ts`
show both the inline-frames and terminal-title approaches. If you want
something bespoke, fork one of those rather than installing.

## The three dedicated extensions

### `@dustydonkey/pi-spinner` — the Crush / Claude Code look

Rotating status verbs with a per-character shimmer sweep, explicitly
"inspired by Claude Code." This is the truest match if what you want
is the *clean shimmering-verb* aesthetic Crush popularized — not flashy
graphics, just polished motion and a hint of what the agent is doing
("Analyzing…", "Planning…"). 187 Claude-Code verbs by default,
idle-aware so it doesn't flicker during sub-agent waits, fully tunable
via `/spinner` and `/verbs`, settings persist. Single-author and young,
but the most-pulled of the three on npm.

### `arpagon/pi-animations` — the maximalist suite

21 animations from demoscene fire to Matrix rain to Pac-Man, in 1-line
and 3-line variants, true color + Nerd Font. The only one that
distinguishes **three states** (thinking / working / tool) and lets you
assign a different animation to each — e.g. aurora while reasoning,
matrix while generating, fire while a tool runs. It even ships a
`crush` character-scrambler animation. The richest feature set and the
most stars, but feature-frozen since its creation day — watch for
staleness against a fast-moving Pi, and note it leans on Nerd Font
glyphs and true-color terminals.

### `pi-fancy-loader` — spinner + palette randomizer

50+ spinner sequences with randomized HSL color palettes and 100+
whimsical verbs, with an interactive `/loader-pick` previewer. Sits
between the other two in spirit: more visual variety than pi-spinner,
less stateful structure than pi-animations. **Caveat:** it's published
to npm with no public source repository, so you can't audit it before
install — a real consideration for an extension that runs in-process
every turn.

## Picking guide

| What you want | Pick |
|---|---|
| **The Crush / Claude Code shimmering-verb look** | [`@dustydonkey/pi-spinner`](https://github.com/HarshalRathore/pi-spinner) — closest aesthetic match, idle-aware, auditable |
| **Different animations per thinking/working/tool state, or flashy graphics** | [`arpagon/pi-animations`](https://github.com/arpagon/pi-animations) — richest suite, true color + Nerd Font; mind the staleness |
| **Lots of spinner/palette variety with a picker** | [`pi-fancy-loader`](https://www.npmjs.com/package/pi-fancy-loader) — but it's unauditable (npm-only) |
| **Build your own** | pi core's `setWorkingIndicator()` + the `working-indicator.ts` example |
| **A novelty rainbow toggle, not a real indicator** | `ultrathink` in [`shitty-extensions`](https://github.com/hjanuschka/shitty-extensions) |

Terminal requirements matter here: `pi-animations` assumes true-color
and Nerd Font glyphs; `pi-spinner`'s default presets degrade more
gracefully on plain terminals.

## See also

- [Footer / Powerline Extensions](footer-extensions.md) — persistent status bar (orthogonal; many users run both).
- [Tool-Call Rendering Extensions](tool-rendering-extensions.md) — tool output and thinking-step content rendering.
- [Theme Extensions](theme-extensions.md) — colors these indicators inherit from.
- [How to Evaluate a Pi Extension](../references/evaluation.md) — for current adoption / maintenance signals and the code-quality recipe (relevant to the npm-only `pi-fancy-loader`).
