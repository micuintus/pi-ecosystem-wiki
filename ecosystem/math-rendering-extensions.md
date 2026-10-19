---
title: Pi Math Rendering Extensions
type: ecosystem
updated: 2026-10-19
sources:
  - pi-markdown-preview
  - pi-studio
  - pi-better-render
  - pi-better-math
  - pi-formula
  - pi-mermaid-gurpartap
  - pi-mermaid-iamwrm
  - pi-mermaid-tui
  - pi-mermaid-validator
  - pi-diagram-mcuste
  - monotykamary-pi-math
  - fadouse-pi-math
  - pi-sixel-math
  - maaamahahh-pi-math-sixel
  - pi-claude-code-ui-math
  - azarai-pi-math
  - pi-typst
  - pi-bridges
  - geminixiang-pi-mermaid
  - fyeeme-pi-mermaid-viewer
  - tifan-pi-mermaid-open
  - pi-mermaid-server
  - 96ems-pi-mermaid-extra
  - irfansofyana-pi-mermaid-studio
  - tzssangglass-pi-diagram
  - wunluv-pi-mermaid-render
  - pi-rich-renderer
  - pi-terminal-math
tags: [extension, math, latex, rendering, tui, preview]
entries:
  - id: pi-markdown-preview
    name: pi-markdown-preview
    repo: omaclaren/pi-markdown-preview
    npm: pi-markdown-preview
    role: document-preview
    notes: "Rendered Markdown plus LaTeX preview with terminal, live browser and PDF output. Pandoc plus headless Chromium pipeline, MathJax fallback, TeX Live for PDF."
  - id: pi-studio
    name: pi-studio
    repo: omaclaren/pi-studio
    npm: pi-studio
    role: browser-workspace
    notes: "Catalog-level, not code-read. Full browser workspace over a websocket: rendered math and diagrams, response history, file browser, REPL, quizzes, PDF export. Same author as `pi-markdown-preview`, most starred in this niche."
  - id: pi-better-render
    name: pi-better-render
    repo: JeffeyChou/pi-better-render
    npm: pi-better-render
    role: streaming-in-chat
    notes: "Streaming-first in-chat rendering: Markdown and formula images appear as the answer streams. Display-only with a context hook that strips image artifacts before each model request. Ghostty and Kitty first."
  - id: pi-better-math
    name: pi-better-math
    repo: ZhenHuangLab/pi-extensions
    npm: pi-better-math
    role: unicode-display-math
    notes: "Display math as multi-line Unicode art through `registerMarkdownTransformer` and libtexprintf (WASM), in a worker thread with caching and fallback to Pi's built-in handling. Display-only, verified in source, but it also monkey-patches `Markdown.prototype.render` (defensive, documented, fragile across Pi upgrades). GPL-3.0-or-later, the only copyleft license in this niche."
  - id: pi-mermaid-gurpartap
    name: pi-mermaid
    repo: Gurpartap/pi-mermaid
    npm: pi-mermaid
    role: ancestor-unmaintained
    notes: "Code-read (structure only). The original in-chat Mermaid renderer, 89 stars, stale since February with 11 open issues. Two open reports describe an `agent_end` hook that re-triggers the model into an infinite Mermaid loop and pollutes context. Do not install; its forks are the live line."
  - id: pi-mermaid-iamwrm
    name: iamwrm/pi-mermaid
    repo: iamwrm/pi-mermaid
    npm: iamwrm/pi-mermaid
    role: unicode-mermaid
    notes: "Catalog-level, not code-read. Keeps the Mermaid source visible and inserts a Unicode box-drawing preview below the block. Apache-2.0. A Gurpartap fork that switched to the proper renderer hook."
  - id: pi-mermaid-tui
    name: "@ramtinj95/pi-mermaid-tui"
    repo: ramtinJ95/pi-mermaid-tui
    npm: "@ramtinj95/pi-mermaid-tui"
    role: tested-mermaid
    notes: "Catalog-level, not code-read. Terminal-native Unicode Mermaid with zero dependencies. The only package in either niche that ships a real test suite (five files including golden terminal tests). Apache-2.0."
  - id: pi-mermaid-validator
    name: pi-mermaid-validator
    repo: Sereinxm/pi-mermaid-validator
    npm: pi-mermaid-validator
    role: mermaid-lint
    notes: "Catalog-level, not code-read. 63 lines plus one test: annotates Mermaid blocks that fail to render, through the renderer hook. A complement to any renderer, not a renderer itself."
  - id: pi-diagram-mcuste
    name: "@mcuste/pi-diagram"
    repo: mcuste/pi-diagram
    npm: "@mcuste/pi-diagram"
    role: d2-diagrams
    notes: "Catalog-level, not code-read. Diagrams in D2 instead of Mermaid, on Pi and Oh My Pi, with CI. The model writes compact declarative D2; an open issue tracks keeping diagram images out of model context. The pick where Mermaid syntax is the problem."
  - id: pi-formula
    name: pi-formula
    repo: yasuhito/pi-formula
    npm: pi-formula
    role: inline-plus-display
    notes: "Selectable Unicode inline formulas plus MathJax PNG display images, with per-formula safety limits and streaming-safe output. Display-only, verified in README. Japanese README alongside."
  - id: monotykamary-pi-math
    name: "@monotykamary/pi-math"
    repo: monotykamary/pi-math
    npm: "@monotykamary/pi-math"
    role: in-chat-images
    notes: "Catalog-level, not code-read. LaTeX as Kitty-protocol terminal images (MathJax plus resvg stack). Independent implementation of the same stack as `Fadouse/pi-math`; fresher and more downloaded."
  - id: fadouse-pi-math
    name: "@fadouse/pi-math"
    repo: Fadouse/pi-math
    npm: "@fadouse/pi-math"
    role: in-chat-images
    notes: "Catalog-level, not code-read. Earlier Kitty-image renderer on the same stack; stalled since July while the independent sibling ships."
  - id: pi-sixel-math
    name: pi-sixel-math
    repo: GuChongAn/pi-sixel-math
    npm: pi-sixel-math
    role: sixel-images
    notes: "Catalog-level, not code-read. Sixel plus Kitty images through Pi's `registerMessageRenderer`. The pick where Sixel is the only protocol (Windows Terminal)."
  - id: maaamahahh-pi-math-sixel
    name: "@maaamahahh/pi-math-sixel"
    repo: maaamahAhh/pi-math-sixel
    npm: "@maaamahahh/pi-math-sixel"
    role: sixel-images
    notes: "Catalog-level, not code-read. Sixel plus Kitty images on the same stack, Unlicense. Weaker twin of `pi-sixel-math`: no stars, no release since September."
  - id: pi-claude-code-ui-math
    name: pi-claude-code-ui
    repo: FammasMaz/pi-cc-tools
    npm: pi-claude-code-ui
    role: unverified-claim
    notes: "Catalog-level, not code-read. Advertises math rendering but its README never says how; treat as unverified. Listed so the claim is not mistaken for coverage."
  - id: azarai-pi-math
    name: "@azarai/pi-math"
    repo: AzarAI-TOP/pi-math
    npm: "@azarai/pi-math"
    role: model-invoked
    notes: "Catalog-level, not code-read. Different interaction: the model calls a `math` tool and the formula renders via matplotlib mathtext through system python3. No LaTeX install, but a large subset of LaTeX only."
  - id: pi-typst
    name: pi-typst
    repo: iharuya/pi-typst
    npm: pi-typst
    role: typst-images
    notes: "Catalog-level, not code-read. Renders Typst markup (not LaTeX) into Kitty or iTerm images via the Typst CLI. Maintainer-made with CI. The model must write Typst, so it changes the workflow, not just the display."
  - id: pi-bridges-latex
    name: "@artale/pi-bridges /latex"
    npm: "@artale/pi-bridges"
    role: latex-card
    notes: "Catalog-level, not code-read. Dependency-free readable LaTeX card through a `/latex` command, beside its OpenRouter Fusion bridge."
  - id: pi-rich-renderer
    name: pi-rich-renderer
    repo: dbydd/pi-rich-renderer
    npm: pi-rich-renderer
    role: superseded
    notes: "Catalog-level, not code-read. Early in-chat image renderer, 300 lines, untouched since June. Superseded by `pi-better-render` on every axis."
  - id: pi-terminal-math
    name: pi-terminal-math
    repo: ryan-ressmeyer/pi-terminal-math
    npm: pi-terminal-math
    role: superseded
    notes: "Catalog-level, not code-read. Terminal-native LaTeX text, one release in July. Superseded by `pi-better-math` and `pi-formula`."
---

# Pi Math Rendering Extensions

Pi's built-in LaTeX handling flattens math to single-line Unicode,
and Mermaid fences sit as inert code. Twenty-eight packages try to
do better, in four shapes: separate document surfaces, automatic
in-chat rendering, Mermaid renderers, and adjacent tools that
change the workflow instead of the display. Code-read: the five
with `notes` not marked catalog-level. One Mermaid package ships a
real test suite; nothing in the math niche ships tests.

## Separate surfaces (best readability)

`/preview` shows the latest response rendered; `/preview-browser
--live` follows each turn as Pi finishes it; `/preview --pdf`
exports through a real LaTeX engine. The pipeline is heavy (Pandoc,
headless Chromium for terminal screenshots, TeX Live for PDF, CDN
fetches on first use), and previews can contain secrets with
nothing redacted. `pi-studio` from the same author goes further: a
websocket browser workspace with response history, file browser,
REPL sessions, quizzes and PDF export.

## In-chat rendering (no new surface)

| Package | Output | Streams | Display-only proof |
|---|---|---|---|
| `pi-better-render` | Formula images (resvg) | yes, per formula | Replaces the display component; a context hook strips artifacts before each request |
| `pi-better-math` | 2D Unicode art (libtexprintf WASM) | no | `registerMarkdownTransformer`, worker thread, fallback to built-in |
| `pi-formula` | Selectable Unicode inline, MathJax PNG display | yes | README states saved messages and model context keep the original LaTeX |
| `@monotykamary/pi-math` | Kitty images | yes | not verified |
| `pi-sixel-math` | Sixel plus Kitty images | unknown | uses `registerMessageRenderer` |

`pi-better-render` is the strongest in-chat pick on Ghostty or
Kitty: streaming images with an explicit safety net. `pi-formula`
wins where text must stay selectable, and its README documents
per-formula failure limits no rival bothers with.
`@monotykamary/pi-math` beats its independent twin
`@fadouse/pi-math` on freshness and downloads. `pi-sixel-math` is
for Windows Terminal, with `@maaamahahh/pi-math-sixel` its weaker
twin.

## Mermaid diagrams

`pi-better-render` covers Mermaid itself: fences become Unicode
box-drawing through `beautiful-mermaid` (elkjs), downloaded lazily
on the first diagram (~11 MB into
`~/.pi/agent/better-render/deps`, off with
`PI_BETTER_RENDER_MERMAID_INSTALL=0`). Flowchart, state, sequence,
class and ER diagrams; anything else stays a code block.
Standalone alternatives: `iamwrm/pi-mermaid` (Unicode preview below
an undisturbed source block), `@ramtinj95/pi-mermaid-tui`
(terminal-native Unicode, zero dependencies),
`@mcuste/pi-diagram` (D2 instead of Mermaid, on Pi and Oh My Pi,
with CI). `pi-mermaid-validator` is not a renderer: it annotates
blocks that fail to render, beside any of the above. Do not install
`Gurpartap/pi-mermaid`: the 89-star original is stale since
February and open issues describe its `agent_end` hook
re-triggering the model into an infinite Mermaid loop.
Also in the niche, catalog-level and unverified:
`@geminixiang/pi-mermaid`, `@fyeeme/pi-mermaid-viewer`
(browser surface), `@tifan/pi-mermaid-open` (external image
viewer fallback), `pi-mermaid-server` (tabbed editor plus live
preview, ships a 600k-line bundle), `96Ems/pi-mermaid-extra` (28
diagram types), `irfansofyana/pi-mermaid-studio` (stateful
workbench), `@tzssangglass/pi-diagram` (JSON-declared diagrams).
`wunluv/pi-mermaid-render` ships no code in its tarball and is
listed for the record only.

## Code quality across both niches

Hook discipline decides upgrade survival. Clean
(`registerMarkdownTransformer`, verified in source): `pi-formula`,
`iamwrm/pi-mermaid`, `pi-mermaid-validator`. Component swap with a
safety net: `pi-better-render`. Prototype patch
(`Markdown.prototype.render`, defensive and documented, fragile
across Pi upgrades): `pi-better-math`. Tests exist only at
`@ramtinj95/pi-mermaid-tui` (five files, golden terminal tests)
plus one token test each in `pi-mermaid-server` and
`pi-mermaid-validator`. CI badges only on `pi-typst` and
`@mcuste/pi-diagram`. External weight ranges from zero
(`@ramtinj95/pi-mermaid-tui`) through vendored WASM and fonts
(`pi-better-render`, `pi-better-math`) to full toolchain demands
(Pandoc, Chromium, TeX Live for `pi-markdown-preview`). Network at
runtime: `pi-markdown-preview` (CDN fallbacks), `pi-better-render`
(one-time `beautiful-mermaid` install). Secrets: `pi-markdown-preview`
redacts nothing. Sentiment: the Gurpartap loop reports are the
sharpest warning in either niche; `pi-formula` and
`@mcuste/pi-diagram` show healthy maintenance (dependency bumps,
substantive design issues, nothing structural). `pi-rich-renderer` and `pi-terminal-math`
are superseded and listed for the record only.

Two flags: `pi-better-math` is GPL-3.0-or-later, the only copyleft
license in the niche. It also appends a debug log to
`/tmp/pi-better-math.log`.

## Adjacent (different workflow)

`@azarai/pi-math` renders only when the model calls its `math`
tool, through matplotlib and system python3. `pi-typst` needs the
model to write Typst instead of LaTeX. `@artale/pi-bridges`
renders one `/latex` card with no dependencies. `pi-claude-code-ui`
advertises math rendering but its README never says how; treat as
unverified.

## Picking a math setup

| If you want | Use | Why |
|---|---|---|
| Discuss math with the best readability | `pi-markdown-preview`, browser or PDF | Real typeset output, live follow, PDF through TeX Live |
| A workspace around the math | `pi-studio` | Most starred and most maintained, far beyond math |
| Nicer math without leaving the chat | `pi-better-render` | Streaming images, display-only by construction |
| Selectable formulas in prose | `pi-formula` | Unicode inline stays searchable; documented failure limits |
| No image-capable terminal | `pi-better-math` | Pure Unicode art; accept the GPL license and the debug log |
| Diagrams as Unicode, no images ever | `pi-better-render` plus `@ramtinj95/pi-mermaid-tui` | Mermaid without the image path; validator on top catches dead blocks |
| Diagrams where Mermaid syntax is the problem | `@mcuste/pi-diagram` | D2 instead of Mermaid, CI-backed |

## See also

- [Pi UI and Tool Rendering Extensions](tool-rendering-extensions.md): the general rendering survey; these entries are the math slice
- [How to Evaluate a Pi Extension](../references/evaluation.md)
