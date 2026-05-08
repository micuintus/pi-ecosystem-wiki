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
tags: [extension, footer, powerline, hashline, edit]
---

# Pi Footer, Powerline and Hashline Extensions

Survey of Pi extensions that customize the footer/status bar and of those
that replace the built-in `read`/`edit` tools with hash-anchored line
references. Numbers as of 2026-05-05.

## Footer / powerline / status bar

### pi-powerline-footer (nicobailon)

- Repo: [nicobailon/pi-powerline-footer](https://github.com/nicobailon/pi-powerline-footer)
- Stars: 201 · Forks: 41 · Open issues: 15 · Releases: 39 (latest v0.5.1, 2026-05-03)
- npm: `pi-powerline-footer` · ~2,900/wk · ~9,957/mo · 332 KB · 0 deps · MIT

Powerline-style status bar inspired by Powerlevel10k and oh-my-pi.
Six presets (default, minimal, compact, full, nerd, ascii). Welcome
overlay with gradient logo and keyboard tips. Working vibes
(AI-generated themed loading messages via `/vibe`). Editor stash
(`Alt+S`). Bash mode with PTY shell session. Fixed editor mode + mouse
scroll toggle. Git branch/status, model name, thinking level, token
usage, cost, context %. Auto Nerd Font detection with ASCII fallback.
Configurable via `~/.pi/agent/settings.json`.

Single-file `index.ts` (~96 KB) — monolithic but well-organized. No
external dependencies. 39 releases in ~4 months. 4 contributors.
Dominant market share among footer extensions.

### pi-fancy-footer (mavam)

- Repo: [mavam/pi-fancy-footer](https://github.com/mavam/pi-fancy-footer)
- Stars: 6 · Forks: 2 · Open issues: 1 · Releases: 10 (latest v0.5.1, 2026-04-15)
- npm: `pi-fancy-footer` · ~369/wk · MIT

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
2 contributors. Niche but well-crafted; unique widget API.

### pi-powerbar (juanibiapina)

- Repo: [juanibiapina/pi-powerbar](https://github.com/juanibiapina/pi-powerbar)
- Stars: 22 · Forks: 2 · Open issues: 1
- npm: `@juanibiapina/pi-powerbar` · ~555/wk · 78.9 KB · 1 dep · MIT

Event-driven segment architecture (tmux-like left/right alignment).
Any extension can emit `powerbar:update` to add segments — no imports
needed. Built-in segments: git-branch, tokens, context-usage, provider,
model, subscription usage. Progress bars with block/continuous styles.
Configurable via `pi-extension-settings` (`/extension-settings`).
Placement above or below editor.

Very modular (separate `powerbar-context`, `powerbar-git`, etc.). Has
tests. Uses `biome.json`. 3 contributors. Praised for clean
architecture; load-order sensitivity is a known friction point.

### pi-vitals (mcowger)

- Repo: [mcowger/pi-vitals](https://github.com/mcowger/pi-vitals)
- Stars: 6 · Forks: 3 · Open issues: 1
- npm: `pi-vitals` · ~48/wk · MIT

Customizable left/right segments. Git integration (branch, staged,
unstaged, untracked). Token tracking (input/output/total/cache
read/write). Context awareness. Thinking level indicator. Nerd Font
auto-detection + ASCII fallback. Live updates. Config via
`~/.pi/agent/powerline.json`.

Small codebase (~8 files, no deps). 1 contributor. Lightweight
alternative to `pi-powerline-footer`.

### minimal-footer (diegopetrucci/pi-extensions)

- Repo: [diegopetrucci/pi-extensions](https://github.com/diegopetrucci/pi-extensions) (collection)
- Collection stars: 6
- npm: `@diegopetrucci/pi-minimal-footer` · ~266/wk · 4.2 KB · MIT

Minimal two-line layout: `<git-branch> <repo-name>` then
`<context-%> <model> • <thinking>`. Optional "DUMB ZONE" indicator.
OpenAI Codex 5-hour and 7-day usage tracking. Narrow-terminal fallback
to one line. Bundled with other useful extensions (oracle,
permission-gate, notify).

### custom-footer (tomsej/pi-ext)

- Repo: [tomsej/pi-ext](https://github.com/tomsej/pi-ext) (collection)
- Collection stars: 35 · Forks: 2 · MIT

Compact powerline-style single line:

```
~/project (main) │ ↑12k ↓8k $0.42 │ 42%/200k │ ⚡ claude-sonnet-4 • medium
```

Part of `pi-ext` collection (12+ extensions: leader-key, tool-pills,
review, telescope, session-snap, handoff, permissions, cmux). Not
installable standalone from npm — install full `pi-ext` or use package
filtering.

### pi-powerline (unscoped npm)

- npm: `pi-powerline` · ~242/wk

"Powerline-style UI extensions for pi coding agent (custom editor,
breadcrumb, footer, header)." Broader UI overhaul package; limited
public info beyond the npm listing.

## Hashline / edit-tool replacements

### pi-hashline-edit (RimuruW)

- Repo: [RimuruW/pi-hashline-edit](https://github.com/RimuruW/pi-hashline-edit)
- Stars: 44 · Forks: 8 · Open issues: 1 · Releases: 4 (latest v0.5.4, 2026-04-19)
- npm: `pi-hashline-edit` · ~225/wk · MIT

Replaces built-in `read` and `edit`. Hash-anchored line editing:
`LINE#HASH:` prefix on every line. Custom 16-char alphabet
(`ZPMQVRWSNKTXJBYH`) to avoid collisions with code. xxHash32 for
hashing. Four edit ops (replace, append, prepend, replace_text).
Stale-anchor detection (hash mismatch = file changed, reject edit).
Chained edits with fresh-anchor return. Diff preview. Atomic writes
(temp-file-then-rename). Symlink/hardlink preservation. Per-file
mutation queue. Hidden legacy compatibility for old `oldText`/`newText`.

Very well tested: 20+ test files (compute-affected-range, edit-diff,
hashline strict input, hashline apply, parse, recovery, resolve,
path-utils, runtime, compatibility notify, edit preview, edit queue,
edit replace-text, fs-write, permission errors). Uses Bun.
3 contributors. Inspired by oh-my-pi (credited in README).

### pi-hashline-readmap (coctostan)

- Repo: [coctostan/pi-hashline-readmap](https://github.com/coctostan/pi-hashline-readmap)
- Stars: 21 · Forks: 5 · Open issues: 1
- npm: `pi-hashline-readmap` · ~756/wk · MIT

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

Extensive test suite: 60+ test files. 1 contributor. Highest weekly
downloads among hashline tools (~756 vs ~225). "One extension instead
of stacking overlapping packages" is the value prop.

### oh-my-pi (can1357) — fork, not extension

- Repo: [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)
- Stars: 3,946 · Forks: 363 · Open issues: 126 · MIT
- Type: full pi-mono fork

Hash-anchored edits (the original inspiration for `pi-hashline-edit`
and `pi-hashline-readmap`). Optimized tool harness. LSP integration
(11 ops, 40+ languages). Python tool with IPython kernel. TTSR (Time
Traveling Streamed Rules) — zero-cost context rules. Interactive code
review (`/review`). Task/subagent system with 6 bundled agents. Commit
tool with AI-powered conventional commits. Bash mode. Browser tool.
Autonomous memory.

Massive monorepo (Rust + TypeScript). CI/CD with GitHub Actions. The
hashline concept originated here; both standalone hashline extensions
credit it. Requires switching off pi-mono entirely.

## Summary tables

### Footer / powerline

| Extension | Stars | Forks | Weekly DL | Size | Deps | Tested | Presets | Widget API | Nerd Font |
|---|---:|---:|---:|---:|---:|---|---|---|---|
| pi-powerline-footer | 201 | 41 | ~2,900 | 332 KB | 0 | Partial | 6 | No | Auto |
| pi-fancy-footer | 6 | 2 | ~369 | — | — | Yes | 0 (widget-based) | Yes | 4 families |
| pi-powerbar | 22 | 2 | ~555 | 79 KB | 1 | Yes | N/A (event-driven) | Event-based | No |
| pi-vitals | 6 | 3 | ~48 | — | — | No | Custom JSON | No | Auto |
| minimal-footer (diegopetrucci) | 6* | 0 | ~266 | 4 KB | 0 | No | 0 | No | No |
| custom-footer (tomsej/pi-ext) | 35* | 2 | — | — | — | No | 0 | No | No |
| pi-powerline (unscoped) | — | — | ~242 | — | — | — | — | — | — |

*Collection stars, not individual extension.

### Hashline / edit

| Extension | Stars | Forks | Weekly DL | Replaces | Languages | Maps | Tests |
|---|---:|---:|---:|---|---|---|---|
| pi-hashline-edit | 44 | 8 | ~225 | read, edit | — | No | 20+ files |
| pi-hashline-readmap | 21 | 5 | ~756 | read, edit, grep, ls, find | 18 | Yes | 60+ files |
| oh-my-pi | 3,946 | 363 | N/A (fork) | Entire pi-mono | 40+ (LSP) | Yes | CI only |

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
| Full forked experience | **oh-my-pi** | Original concept, broad tooling, but means leaving pi-mono |
