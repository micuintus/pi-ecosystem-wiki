---
title: Pi Hashline / Edit-Tool Replacement Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - pi-hashline-edit
  - pi-hashline-readmap
  - oh-my-pi
  - bruclan-pi-hashline-edit
  - kcosr-codemap
  - whamp-pi-read-map
tags: [extension, hashline, edit, tools]
entries:
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

# Pi Hashline / Edit-Tool Replacement Extensions

Survey of Pi extensions that replace the built-in `read` / `edit`
tools (and sometimes `grep` / `ls` / `find`) with **hash-anchored line
references**. The pattern attaches a short content hash to each line
of every read; subsequent edits must include the matching anchor.
Stale anchor → file changed under the agent → reject the edit instead
of silently relocating it.

This is the family of extensions that fight the most common failure
mode of LLM-driven editing: confidently rewriting a region of a file
that has moved or already changed.

For current vital signs of any entry, see
[How to Evaluate a Pi Extension](../references/evaluation.md).

## Why hashline

Stock `edit` matches a literal `oldText` substring. If the file has
shifted, the substring may match in the wrong place — or worse, match
nowhere and cause the model to re-read, re-guess, and clobber an
earlier change. Hashline replaces the substring contract with a
content-addressed anchor:

```
42#KZJM: const config = loadConfig(path);
```

The model sees `42#KZJM:` on the line. To edit it, it must echo back
`42#KZJM`. If the line has changed since, the hash no longer matches
and the edit is refused with a request to re-read.

## pi-hashline-edit (RimuruW)

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

## bruclan/pi-hashline-edit

Fork of RimuruW/pi-hashline-edit. Same overall feature set; check the
fork's history for divergence before installing.

## pi-hashline-readmap (coctostan)

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

## Lighter alternatives

- **`kcosr/codemap`** — codemap navigation, lighter than the
  full `pi-hashline-readmap`.
- **`Whamp/pi-read-map`** — lightweight read-map navigation
  extension.

These overlap with `pi-hashline-readmap`'s structural-map idea but
without the full edit-replacement machinery. Pick them if you want
better structural navigation but are happy with stock `edit`.

## oh-my-pi (can1357) — fork, not extension

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

| Goal | Best choice | Why |
|---|---|---|
| Focused edit safety only | **pi-hashline-edit** | Replaces just read/edit; excellent test coverage |
| Complete workflow overhaul | **pi-hashline-readmap** | Replaces 5 tools, structural maps, AST search, bash compression |
| Light navigation only | **kcosr/codemap** or **Whamp/pi-read-map** | Structural maps without the full edit-replacement machinery |
| Full forked experience | **oh-my-pi** | Original concept, broad tooling, but means leaving pi-mono |

## See also

- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes
- [Footer / Powerline Extensions](footer-extensions.md) — orthogonal visual layer; `oh-my-pi` ships both worlds in a single fork
- [Tool-Call Rendering Extensions](tool-rendering-extensions.md) — how tool output is rendered, separate from how tools behave
