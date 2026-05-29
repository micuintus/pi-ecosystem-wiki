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
    notes: "21 terminal animations (demoscene fire, Matrix rain, Pac-Man, aurora, starfield, a `crush` character-scrambler, pi-pulse, shimmer, …) in 1-line and 3-line variants, ANSI true color + Nerd Font glyphs. Distinctive: **three distinct animation states** — thinking (`thinking_start`/`thinking_end`), working (`agent_start`/`agent_end`), tool (`tool_execution_start`/`tool_execution_end`), with priority thinking > tool > working. Per-state assignment (`/animation thinking:aurora working:matrix3 tool:fire3`), configurable width (full/50/custom), interactive `/animation showcase` browser, random mode. 1-line animations ride `ctx.ui.setWorkingMessage()` alongside pi's braille spinner; 3-line use a widget. Has a literal `crush` mode — the truest match if you mean Charm Crush's *scramble* effect (vs Claude Code's shimmer-verb line). MIT, single author, 2 releases. **Code-read caveats:** no `isIdle()`/sub-agent guard — its 40–100ms multi-line render loop keeps firing during nested/sub-agent work (flicker + terminal-write pressure exactly when you don't want it); CI is `tsc … || true` (cannot fail); 0 tests; hard true-color + Nerd Font requirement; 3-line variants consume vertical space. Feature-frozen since creation day (2026-03-20) — watch staleness."
  - id: pi-spinner-dustydonkey
    name: "@dustydonkey/pi-spinner"
    repo: HarshalRathore/pi-spinner
    npm: "@dustydonkey/pi-spinner"
    role: claude-code-style-shimmer-verbs
    notes: "The closest match to the Claude Code *shimmer-verb* busy aesthetic: replaces pi's braille spinner with frame presets + **rotating status verbs** + a gentle per-character **shimmer** sweep. 6 frame presets (Claude star sequence, braille, pulse, dot, star, none), 5 verb presets (187 Claude Code verbs, short, technical, fun, custom). **Code-read strength: genuinely idle-aware** — `if (ctx.isIdle()) return` pauses the shimmer while waiting on sub-agents / user input, so no flicker during nested work (the key robustness edge over pi-animations). Gentle render cadence (200ms shimmer, ~3s verb rotation). Uses both `setWorkingIndicator` (spinner frames) and `setWorkingMessage` (verb text). Clean teardown on `agent_end`/`session_shutdown`. Degrades gracefully on plain terminals. `/spinner` and `/verbs` slash commands, settings persist under `workingSpinner` in `.pi/settings.json`. MIT, single author, fresh (last push 2026-05). 0 tests, no CI. Highest npm pull of the three despite low stars."
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

## Two senses of "Crush style"

Worth disambiguating up front, because it splits the choice:

- **Charm Crush's *scramble* effect** (characters churn/resolve) →
  `pi-animations` ships a literal `crush` animation. Truest literal
  match.
- **The polished *shimmer-verb* busy line** (rotating status word with
  a gentle color sweep, à la Claude Code) → `pi-spinner`.

Both get called "Crush style" colloquially; they're different effects.

## The three dedicated extensions

### `@dustydonkey/pi-spinner` — the shimmer-verb look

Rotating status verbs with a per-character shimmer sweep, explicitly
"inspired by Claude Code" — polished motion plus a hint of what the
agent is doing ("Analyzing…", "Planning…"), not flashy graphics. 187
Claude-Code verbs by default, fully tunable via `/spinner` and
`/verbs`, settings persist.

**Code-read strength (the deciding factor for sub-agent users):** it is
genuinely idle-aware — `if (ctx.isIdle()) return` pauses the shimmer
while waiting on sub-agents or user input, so it doesn't flicker or
burn terminal writes during nested work. Gentle cadence (200ms
shimmer, ~3s verb rotation), clean teardown on `agent_end` /
`session_shutdown`, degrades gracefully on plain terminals. Young and
single-author with no tests/CI, but the lightest and best-behaved of
the three.

### `arpagon/pi-animations` — the maximalist suite

21 animations from demoscene fire to Matrix rain to Pac-Man, in 1-line
and 3-line variants, true color + Nerd Font. The only one that
distinguishes **three states** (thinking / working / tool) and lets you
assign a different animation to each — e.g. aurora while reasoning,
matrix while generating, fire while a tool runs. Ships the literal
`crush` scramble animation.

**Code-read caveats:** no `isIdle()`/sub-agent guard — its 40–100ms
multi-line render loop keeps firing during nested/sub-agent work,
exactly when flicker and terminal-write pressure hurt most. CI is
`tsc … || true` (cannot fail), 0 tests, hard true-color + Nerd Font
requirement, and 3-line variants consume vertical space. Most stars,
richest features, but feature-frozen since its creation day
(2026-03-20) — watch staleness against a fast-moving Pi. Best when
you're on a capable terminal, want per-state graphics, and aren't
leaning on sub-agents during the animated phases.

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
| **The Claude Code *shimmer-verb* look; you use sub-agents / long sessions** | [`@dustydonkey/pi-spinner`](https://github.com/HarshalRathore/pi-spinner) — idle-aware (pauses during nested work), lightest, auditable |
| **The literal Charm Crush *scramble*, per-state graphics, capable terminal** | [`arpagon/pi-animations`](https://github.com/arpagon/pi-animations) — ships a `crush` mode + thinking/working/tool states; no idle guard, true-color + Nerd Font, feature-frozen |
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
