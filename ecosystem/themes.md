---
title: Pi Theme Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - pi-themes-docs
  - leblancfg-pi-ansi-themes
  - juanibiapina-pi-tokyonight
  - danielcherubini-pi-dracula
  - dracula-pi-coding-agent
  - joelhooks-pi-theme-catppuccin-mocha
  - otahontas-pi-coding-agent-catppuccin
  - victor-pi-curated-themes
  - ironin-pi-curated-themes
  - hasit-pi-community-themes
  - vinyroli-pi-codex-theme
  - tomsej-pi-ext
  - astrofoundry-pi-astro
  - awesome-pi-site
tags: [extension, theme, ui]
entries:
  - id: pi-ansi-themes
    name: pi-ansi-themes
    repo: leblancfg/pi-ansi-themes
    role: terminal-ansi
    notes: "Uses only the 16 standard ANSI colors; inherits from the terminal's existing Tokyo Night / Catppuccin / Dracula / Nord / Gruvbox / Solarized scheme rather than overriding it."
  - id: pi-tokyonight
    name: pi-tokyonight
    repo: juanibiapina/pi-tokyonight
    npm: pi-tokyonight
    role: single-port
    notes: "Tokyo Night port. tokyonight-moon variant available."
  - id: pi-dracula
    name: pi-dracula (danielcherubini)
    repo: danielcherubini/pi-dracula
    npm: pi-dracula
    role: single-port
    notes: "Community Dracula port. Tuned for diff readability and subdued borders."
  - id: dracula-official
    name: dracula/pi-coding-agent
    repo: dracula/pi-coding-agent
    role: single-port
    notes: "Official Dracula theme repo (draculatheme.com/pi-coding-agent). Includes Dracula PRO."
  - id: pi-theme-catppuccin-mocha
    name: pi-theme-catppuccin-mocha
    repo: joelhooks/pi-theme-catppuccin-mocha
    role: single-port
    notes: "Catppuccin Mocha mapped across all 51 pi color tokens from the official style guide."
  - id: pi-coding-agent-catppuccin
    name: pi-coding-agent-catppuccin
    repo: otahontas/pi-coding-agent-catppuccin
    role: single-port
    notes: "All four Catppuccin flavours (Latte, Frappé, Macchiato, Mocha)."
  - id: pi-curated-themes-victor
    name: pi-curated-themes (victor-software-house)
    repo: victor-software-house/pi-curated-themes
    role: bundle
    notes: "65 dark themes adapted from iTerm2-Color-Schemes to pi's 51-token model. Includes Catppuccin Mocha, Dracula, Tokyo Night, Nord, Gruvbox, etc."
  - id: pi-curated-themes-ironin
    name: pi-curated-themes (iRonin)
    repo: iRonin/pi-curated-themes
    role: bundle
    notes: "Same upstream as victor-software-house/pi-curated-themes; parallel repository."
  - id: pi-community-themes
    name: pi-community-themes
    repo: hasit/pi-community-themes
    role: bundle
    notes: "Community-curated theme bundle with installer."
  - id: pi-codex-theme
    name: "@vinyroli/pi-codex-theme"
    repo: vinyroli/pi-codex-theme
    npm: "@vinyroli/pi-codex-theme"
    role: distinct-ui
    notes: "Codex-inspired tighter UI. More than a colour swap — modifies layout/density."
  - id: tomsej-pi-ext
    name: tomsej/pi-ext
    repo: tomsej/pi-ext
    role: collection-with-themes
    notes: "Personal extensions+skills+themes collection. Includes Catppuccin variants among other items."
  - id: astrofoundry-pi-astro
    name: "@astrofoundry/pi-astro"
    repo: astrofoundry/pi-astro
    npm: "@astrofoundry/pi-astro"
    role: collection-with-themes
    notes: "Personal pi customizations bundle (extensions, skills, prompts, themes)."
---

# Pi Theme Extensions

Pi ships only `dark` and `light` as built-in themes. Everything else
comes from the community. The `awesome-pi.site` catalog tracks **131
themes** in this category, so this page does not try to enumerate
every single-author colour palette — it covers the distinct
*approaches* to theming and names representative implementations of
each.

## How Pi themes work (very short)

Pi themes are JSON files defining 51 colour tokens (accent, border,
borderAccent, success, error, warning, muted, dim, text, thinkingText,
plus tool/diff/syntax categories). Pi loads them from:

- Built-in: `dark`, `light`
- Global: `~/.pi/agent/themes/*.json`
- Project: `.pi/themes/*.json`
- Packages: `themes/` directory or `pi.themes` entries in `package.json`
- Settings: `themes` array of files or directories
- CLI: `--theme <path>` (repeatable)

Hot-reload: edit the active theme file and pi picks up the change
immediately. Source: [pi.dev/docs/latest/themes](https://pi.dev/docs/latest/themes).

> Pi can create themes itself — `/theme` and a description is enough
> for a starting point. Many community themes started this way.

## Five theme strategies

### 1. Terminal-ANSI inheritance (no override)

Use only the 16 standard ANSI colours so the theme inherits whatever
your terminal is already configured with — Tokyo Night, Catppuccin,
Dracula, Nord, Gruvbox, Solarized, etc. Single Pi theme, infinite
colour schemes via terminal config.

- **`leblancfg/pi-ansi-themes`** — the canonical implementation. One
  Pi theme that doesn't fight your terminal palette.

Best when: your terminal is already themed and you want Pi to match
without duplicating configuration.

### 2. Single colour-scheme port

One repo per colour scheme. Maps the scheme's hex palette across all
51 of Pi's colour tokens.

| Scheme | Repos |
|---|---|
| Tokyo Night | `juanibiapina/pi-tokyonight` |
| Dracula | `dracula/pi-coding-agent` (official), `danielcherubini/pi-dracula` (community) |
| Catppuccin | `joelhooks/pi-theme-catppuccin-mocha` (Mocha-only), `otahontas/pi-coding-agent-catppuccin` (all four flavours) |

Best when: you want a precise port of a specific palette and don't
mind that Pi's colours are decoupled from your terminal's.

### 3. Curated bundle (many themes, one install)

One package shipping dozens of themes. Switch with `/theme <name>`.

- **`victor-software-house/pi-curated-themes`** — 65 dark themes
  adapted from iTerm2-Color-Schemes. Includes Catppuccin Mocha,
  Dracula, Tokyo Night, Nord, Gruvbox, Aura, Atom, Black Metal
  variants, and more.
- **`iRonin/pi-curated-themes`** — parallel curated bundle, same
  iTerm2 lineage.
- **`hasit/pi-community-themes`** — community-curated set with
  installer.

Best when: you want to try several palettes without hunting individual
repos.

### 4. Distinct UI style (more than colour)

A theme that also alters layout, density, or visual structure — not
just colour swaps.

- **`@vinyroli/pi-codex-theme`** — Codex-inspired tighter UI; less
  empty space; reorganized layout. Maintained as an "independent
  derivative" rather than a pure theme.

Best when: you specifically want a different *visual structure*, not a
recolouring of the default one.

### 5. Personal-collection themes

Many authors ship themes inside their broader extensions+skills+prompts
bundle rather than as standalone packages. The themes are usually
secondary to the bundle's main purpose.

- **`tomsej/pi-ext`** — large extension bundle that also ships
  Catppuccin variants and others.
- **`@astrofoundry/pi-astro`** — personal customisations bundle
  including themes.

Best when: you're already adopting that author's broader workflow.

## Picking a theme strategy

| If you want… | Pick |
|---|---|
| Pi to match your already-themed terminal | `pi-ansi-themes` |
| One specific colour scheme, precisely ported | The single-port repo for that scheme (Catppuccin → joelhooks or otahontas; Dracula → official; Tokyo Night → juanibiapina) |
| To browse and switch among many themes | `victor-software-house/pi-curated-themes` |
| A different *visual layout*, not just colours | `@vinyroli/pi-codex-theme` |
| To bundle theming with broader workflow customisation | A personal collection (`tomsej/pi-ext`, `@astrofoundry/pi-astro`) or write your own |
| To create a new theme | Use `/theme` with Pi itself; iterate with hot-reload |

## Live signals

Stars, downloads, and last-push are not inlined here — see
[How to Evaluate a Pi Extension](../references/evaluation.md) for
recipes. The `entries:` frontmatter lists `repo:` and `npm:` for each
theme so vitals are one command away.

Specific to themes: the **dependency footprint should be ~zero**. A
theme that pulls runtime dependencies is a smell. Most themes here
ship only JSON files plus a thin loader.

## See also

- [Pi Themes documentation](https://pi.dev/docs/latest/themes) — official format reference
- [Footer / Powerline Extensions](footer-extensions.md) — visual-layer extensions that compose with themes
- [Pi Ecosystem Catalogs](../references/catalogs.md) — `awesome-pi.site` indexes 131 themes total
