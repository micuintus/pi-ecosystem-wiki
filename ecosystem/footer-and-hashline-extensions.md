---
title: Pi Footer, Powerline and Hashline Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - pi-powerline-footer
  - pi-fancy-footer
  - pi-powerbar
  - pi-vitals
  - diegopetrucci-pi-extensions
  - tomsej-pi-ext
  - pi-hashline-edit
  - pi-hashline-readmap
  - oh-my-pi
  - bruclan-pi-hashline-edit
  - kcosr-codemap
  - whamp-pi-read-map
tags: [extension, footer, powerline, hashline, edit]
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
  - id: pi-hashline-edit
    name: pi-hashline-edit
    repo: RimuruW/pi-hashline-edit
    npm: pi-hashline-edit
    role: hashline-edit-focused
    notes: "Replaces read/edit only. Hash-anchored line editing with stale-anchor detection. 20+ test files. 'Fail hard, be predictable.' Inspired by oh-my-pi."
  - id: bruclan-pi-hashline-edit
    name: pi-hashline-edit (bruclan)
    repo: bruclan/pi-hashline-edit
    role: hashline-fork
    notes: "Fork of RimuruW/pi-hashline-edit."
  - id: pi-hashline-readmap
    name: pi-hashline-readmap
    repo: coctostan/pi-hashline-readmap
    npm: pi-hashline-readmap
    role: hashline-full-overhaul
    notes: "Replaces read/edit/grep/ls/find. Structural file maps for 18 languages. Symbol-aware nav. ast_search. Bash output compression. 60+ test files."
  - id: kcosr-codemap
    name: codemap
    repo: kcosr/codemap
    role: hashline-adjacent
    notes: "Codemap navigation extension; lighter alternative in the hashline-edit space."
  - id: whamp-pi-read-map
    name: pi-read-map
    repo: Whamp/pi-read-map
    npm: pi-read-map
    role: hashline-adjacent
    notes: "Lightweight read-map navigation extension."
  - id: oh-my-pi
    name: oh-my-pi
    repo: can1357/oh-my-pi
    role: full-fork
    notes: "Full pi-mono fork — not an extension. Origin of the hashline concept; both standalone hashline extensions credit it. Requires switching off pi-mono entirely."
---

# Pi Footer, Powerline and Hashline Extensions

Survey of Pi extensions that customize the footer/status bar and of those
that replace the built-in `read`/`edit` tools with hash-anchored line
references.

For current vital signs (stars, weekly downloads, last push) of any
entry, see [How to Evaluate a Pi Extension](../references/evaluation.md).

## Footer / powerline / status bar

### pi-powerline-footer (nicobailon)

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

#### `/vibe` and `workingVibeMode` setting

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

### pi-fancy-footer (mavam)

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

### pi-powerbar (juanibiapina)

Event-driven segment architecture (tmux-like left/right alignment).
Any extension can emit `powerbar:update` to add segments — no imports
needed. Built-in segments: git-branch, tokens, context-usage, provider,
model, subscription usage. Progress bars with block/continuous styles.
Configurable via `pi-extension-settings` (`/extension-settings`).
Placement above or below editor.

Very modular (separate `powerbar-context`, `powerbar-git`, etc.). Has
tests. Uses `biome.json`. Praised for clean architecture; load-order
sensitivity is a known friction point.

### pi-vitals (mcowger)

Customizable left/right segments. Git integration (branch, staged,
unstaged, untracked). Token tracking (input/output/total/cache
read/write). Context awareness. Thinking level indicator. Nerd Font
auto-detection + ASCII fallback. Live updates. Config via
`~/.pi/agent/powerline.json`.

Small codebase, no deps. Lightweight alternative to
`pi-powerline-footer`.

### minimal-footer (diegopetrucci/pi-extensions)

Minimal two-line layout: `<git-branch> <repo-name>` then
`<context-%> <model> • <thinking>`. Optional "DUMB ZONE" indicator.
OpenAI Codex 5-hour and 7-day usage tracking. Narrow-terminal fallback
to one line. Bundled with other useful extensions (oracle,
permission-gate, notify).

### custom-footer (tomsej/pi-ext)

Compact powerline-style single line:

```
~/project (main) │ ↑12k ↓8k $0.42 │ 42%/200k │ ⚡ claude-sonnet-4 • medium
```

Part of `pi-ext` collection (12+ extensions: leader-key, tool-pills,
review, telescope, session-snap, handoff, permissions, cmux). Not
installable standalone from npm — install full `pi-ext` or use package
filtering.

### pi-powerline (unscoped npm)

"Powerline-style UI extensions for pi coding agent (custom editor,
breadcrumb, footer, header)." Broader UI overhaul package; limited
public info beyond the npm listing.

## Hashline / edit-tool replacements

### pi-hashline-edit (RimuruW)

Replaces built-in `read` and `edit`. Hash-anchored line editing:
`LINE#HASH:` prefix on every line. Custom 16-char alphabet
(`ZPMQVRWSNKTXJBYH`) to avoid collisions with code. xxHash32 for
hashing. Four edit ops (replace, append, prepend, replace_text).
Stale-anchor detection (hash mismatch = file changed, reject edit).
Chained edits with fresh-anchor return. Diff preview. Atomic writes
(temp-file-then-rename). Symlink/hardlink preservation. Per-file
mutation queue. Hidden legacy compatibility for old `oldText`/`newText`.

Very well tested (20+ test files). Uses Bun. Inspired by oh-my-pi
(credited in README). Stated philosophy: "fail hard, be predictable" —
stale anchors always fail; no silent relocation.

### bruclan/pi-hashline-edit

Fork of RimuruW/pi-hashline-edit. Same overall feature set; check the
fork's history for divergence before installing.

### pi-hashline-readmap (coctostan)

Unified replacement for stock `read`, `edit`, `grep`, `ls`, `find`.
Hash-anchored reads and edits (`LINE:HASH|content`). Structural file
maps (readmap) — 18 language mappers: TS, JS, Python, Rust, Go, Java,
Swift, Shell, C/C++, Clojure, SQL, JSON/JSONL, Markdown, YAML, TOML,
CSV/TSV. Symbol-aware navigation (`read symbol: "foo"`). `ast_search`
via ast-grep. `write` tool with auto directory creation. Optional `nu`
tool (Nushell structured exploration). Bash output compression (RTK)
for test runners, builds, Git, Docker, linters, package managers, HTTP,
transfer tools. `replace_symbol` edit op. Syntax-regression validator
(warn/block/off). Context-hygiene system. Doom-loop detection.

Extensive test suite (60+ test files). Highest adoption among
hashline tools when last surveyed. "One extension instead of stacking
overlapping packages" is the value prop.

### Lighter alternatives in the hashline space

- **`kcosr/codemap`** — codemap navigation, lighter than the
  full `pi-hashline-readmap`.
- **`Whamp/pi-read-map`** — lightweight read-map navigation
  extension.

These overlap with `pi-hashline-readmap`'s structural-map idea but
without the full edit-replacement machinery.

### oh-my-pi (can1357) — fork, not extension

Full pi-mono **fork**, not an installable extension. Hash-anchored
edits originated here (both standalone hashline extensions credit it).
Optimized tool harness. LSP integration (40+ languages). Python tool
with IPython kernel. TTSR (Time Traveling Streamed Rules) — zero-cost
context rules. Interactive code review (`/review`). Task/subagent
system with bundled agents. Commit tool with AI-powered conventional
commits. Bash mode. Browser tool. Autonomous memory.

Massive monorepo (Rust + TypeScript). CI/CD with GitHub Actions.
Requires switching off pi-mono entirely.

## Recommendation matrix

### Footer

| Goal | Best choice | Why |
|---|---|---|
| Default, most features | **pi-powerline-footer** | Highest adoption, zero deps, active maintenance |
| Maximum customization | **pi-fancy-footer** | Unique widget API and interactive TUI config editor |
| Composability across extensions | **pi-powerbar** | Event-driven; multiple extensions contribute segments |
| Minimalism | **diegopetrucci minimal-footer** or **pi-vitals** | Two lines, no fuss; or simple JSON config |

### Hashline

| Goal | Best choice | Why |
|---|---|---|
| Focused edit safety only | **pi-hashline-edit** | Replaces just read/edit; excellent test coverage |
| Complete workflow overhaul | **pi-hashline-readmap** | Replaces 5 tools, structural maps, AST search, bash compression |
| Light navigation only | **kcosr/codemap** or **Whamp/pi-read-map** | Structural maps without the full edit-replacement machinery |
| Full forked experience | **oh-my-pi** | Original concept, broad tooling, but means leaving pi-mono |

## See also

- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes
- [Themes](themes.md) — separate visual layer that composes with these
- [Tool-Call Rendering Extensions](tool-rendering-extensions.md) — message-stream rendering vs the status-bar layer covered here
