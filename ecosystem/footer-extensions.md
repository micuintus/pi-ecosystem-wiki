---
title: Pi Footer / Powerline / Status Bar Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - pi-powerline-footer
  - pi-fancy-footer
  - pi-powerbar
  - pi-vitals
  - diegopetrucci-pi-extensions
  - tomsej-pi-ext
  - aliou-pi-extensions
  - hjanuschka-shitty-extensions
tags: [extension, footer, powerline, status-bar]
entries:
  - id: pi-powerline-footer
    name: pi-powerline-footer
    repo: nicobailon/pi-powerline-footer
    npm: pi-powerline-footer
    role: footer-default
    notes: "Powerline-style status bar. 6 presets. Working vibes via /vibe. Editor stash. Bash mode. Dominant in this niche."
  - id: pi-fancy-footer
    name: pi-fancy-footer
    repo: mavam/pi-fancy-footer
    npm: pi-fancy-footer
    role: footer-widget-system
    notes: "Two-line, widget API, interactive /fancy-footer config editor. 17 built-in widgets, 8 context-bar styles, 4 icon families."
  - id: pi-powerbar
    name: pi-powerbar
    repo: juanibiapina/pi-powerbar
    npm: "@juanibiapina/pi-powerbar"
    role: footer-event-driven
    notes: "Event-driven segments — extensions emit powerbar:update with no imports. tmux-like left/right alignment."
  - id: pi-vitals
    name: pi-vitals
    repo: mcowger/pi-vitals
    npm: pi-vitals
    role: footer-minimal-config
    notes: "Configurable left/right segments via ~/.pi/agent/powerline.json. Lightweight."
  - id: diegopetrucci-minimal-footer
    name: minimal-footer (diegopetrucci)
    repo: diegopetrucci/pi-extensions
    npm: "@diegopetrucci/pi-minimal-footer"
    role: footer-minimal
    notes: "Two-line minimal layout. OpenAI Codex usage tracking. Bundled with oracle/permission-gate/notify."
  - id: tomsej-custom-footer
    name: custom-footer (tomsej)
    repo: tomsej/pi-ext
    role: footer-collection
    notes: "Compact powerline single line. Part of 12+ extension pi-ext bundle. Not standalone-installable."
  - id: pi-powerline-unscoped
    name: pi-powerline (unscoped)
    npm: pi-powerline
    role: footer-broader-ui
    notes: "Broader Powerline-style UI extensions. Limited public info beyond npm listing."
  - id: aliou-chrome
    name: chrome (aliou/pi-extensions)
    repo: aliou/pi-extensions
    role: footer-and-header
    notes: "Two-component TUI chrome: header (path breadcrumb, model, token count) + footer (git branch/status, cost). More opinionated layout than standalone footer extensions. Part of aliou's broader collection, not standalone-installable."
  - id: hjanuschka-status-widget
    name: status-widget (shitty-extensions)
    repo: hjanuschka/shitty-extensions
    npm: shitty-extensions
    role: footer-status-indicator
    notes: "Persistent provider/model status indicator in the footer. Single-purpose component. Installable as part of the shitty-extensions bundle."
---

# Pi Footer / Powerline / Status Bar Extensions

Survey of Pi extensions that customize the footer / status bar — the
visual layer that renders below the editor.

For current vital signs (stars, weekly downloads, last push) of any
entry, see [How to Evaluate a Pi Extension](../references/evaluation.md).

## pi-powerline-footer (nicobailon)

Powerline-style status bar inspired by Powerlevel10k and oh-my-pi.
Six presets (default, minimal, compact, full, nerd, ascii). Welcome
overlay with gradient logo and keyboard tips. Working vibes
(AI-generated themed loading messages via `/vibe`). Editor stash
(`Alt+S`). Bash mode with PTY shell session. Fixed editor mode + mouse
scroll toggle. Git branch/status, model name, thinking level, token
usage, cost, context %. Auto Nerd Font detection with ASCII fallback.
Configurable via `~/.pi/agent/settings.json`.

Single-file `index.ts` (large, monolithic but well-organized). No
external dependencies. Active release cadence. Dominant by adoption
in the footer niche.

### `/vibe` and `workingVibeMode` setting

`workingVibeMode` controls how `/vibe` generates the rotating
working-state messages:

| Mode | What it does |
|---|---|
| `file` | Picks from a curated set of pre-written strings |
| `ai` | One small LLM call per `/vibe` change generates themed messages dynamically |

**Known gotcha:** `ai` mode initially fails with
`Error: Failed to generate vibes: No API key for provider: openai-codex`
when the vibe LLM call is bound to a separate provider rather than the
currently-selected Pi model. Fix: ensure the extension version you have
binds to the active Pi model. If it doesn't, switch to `file` mode or
upgrade.

## pi-fancy-footer (mavam)

Two-line fancy status footer (compact, information-dense). Interactive
TUI config editor via `/fancy-footer`. Widget system with 17 built-in
widgets + extension widget API. Context usage bar with compaction
reserve tail. PR number, unresolved review threads, PR CI status. Git
diff stats, ahead/behind. Eight context bar styles (blocks, lines,
circles, parallelograms, diamonds, bars, stars, specks). Four icon
families (nerd, emoji, unicode, ascii). Per-widget layout controls.
Third-party extension widget contribution API.

Modular (`api`, `config-editor`, `render`, `git`, `ci`, `pull-request`).
Has tests. Structured changelog with `manifest.yaml` per release.
Niche but well-crafted; unique widget API.

## pi-powerbar (juanibiapina)

Event-driven segment architecture (tmux-like left/right alignment).
Any extension can emit `powerbar:update` to add segments — no imports
needed. Built-in segments: git-branch, tokens, context-usage, provider,
model, subscription usage. Progress bars with block/continuous styles.
Configurable via `pi-extension-settings` (`/extension-settings`).
Placement above or below editor.

Very modular (separate `powerbar-context`, `powerbar-git`, etc.). Has
tests. Uses `biome.json`. Praised for clean architecture; load-order
sensitivity is a known friction point.

## pi-vitals (mcowger)

Customizable left/right segments. Git integration (branch, staged,
unstaged, untracked). Token tracking (input/output/total/cache
read/write). Context awareness. Thinking level indicator. Nerd Font
auto-detection + ASCII fallback. Live updates. Config via
`~/.pi/agent/powerline.json`.

Small codebase, no deps. Lightweight alternative to
`pi-powerline-footer`.

## minimal-footer (diegopetrucci/pi-extensions)

Minimal two-line layout: `<git-branch> <repo-name>` then
`<context-%> <model> • <thinking>`. Optional "DUMB ZONE" indicator.
OpenAI Codex 5-hour and 7-day usage tracking. Narrow-terminal fallback
to one line. Bundled with other useful extensions (oracle,
permission-gate, notify).

## custom-footer (tomsej/pi-ext)

Compact powerline-style single line:

```
~/project (main) │ ↑12k ↓8k $0.42 │ 42%/200k │ ⚡ claude-sonnet-4 • medium
```

Part of `pi-ext` collection (12+ extensions: leader-key, tool-pills,
review, telescope, session-snap, handoff, permissions, cmux). Not
installable standalone from npm — install full `pi-ext` or use package
filtering.

## pi-powerline (unscoped npm)

"Powerline-style UI extensions for pi coding agent (custom editor,
breadcrumb, footer, header)." Broader UI overhaul package; limited
public info beyond the npm listing.

## chrome (aliou/pi-extensions)

Full TUI chrome — two components that work together: a **header** bar
(current path breadcrumb, active model, token counter) and a **footer**
(git branch + status, session cost). More integrated and opinionated than
the standalone footer packages. Not independently installable; ships
as part of `aliou/pi-extensions`. Best for users already adopting that
collection.

## status-widget (hjanuschka/shitty-extensions)

Small single-purpose footer widget showing the current AI provider and
model status. Useful for quickly seeing which model Pi is using in
multi-provider setups. Ships as part of `shitty-extensions` (npm:
`shitty-extensions`), not as a standalone package.

## Recommendation matrix

| Goal | Best choice | Why |
|---|---|---|
| Default, most features | **pi-powerline-footer** | Highest adoption, zero deps, active maintenance |
| Maximum customization | **pi-fancy-footer** | Unique widget API and interactive TUI config editor |
| Composability across extensions | **pi-powerbar** | Event-driven; multiple extensions contribute segments |
| Minimalism | **diegopetrucci minimal-footer** or **pi-vitals** | Two lines, no fuss; or simple JSON config |

## See also

- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes
- [Themes](theme-extensions.md) — color/style layer that composes with these
- [Tool-Call Rendering Extensions](tool-rendering-extensions.md) — message-stream rendering vs the status-bar layer covered here
- [Hashline Edit Extensions](hashline-edit-extensions.md) — orthogonal tool-behavior layer; `oh-my-pi` ships both worlds in a single fork
