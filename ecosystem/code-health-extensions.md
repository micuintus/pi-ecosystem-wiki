---
title: Pi Code Health Extensions
type: ecosystem
updated: 2026-10-14
sources:
  - pi-lens
tags: [extension, lsp, diagnostics, code-health]
entries:
  - id: pi-lens
    name: pi-lens
    repo: apmantza/pi-lens
    npm: pi-lens
    role: realtime-diagnostics
    notes: "Real-time LSP, linter, formatter and type feedback inside Pi: the model sees diagnostics before the turn is wasted. The OpenCode-style diagnose-after-edit loop, as a Pi extension. Emerging niche; sole reviewed entry."
---

# Pi Code Health Extensions

An emerging niche: fast compiler and type feedback fed back into the
agent loop, so the model fixes its own errors without a full test run.
OpenCode ships this built in (LSP diagnostics after edits); in Pi it
is one extension so far.

- [`apmantza/pi-lens`](https://github.com/apmantza/pi-lens) —
  real-time language-server, linter, formatter and type feedback in
  the session. Catches errors at edit time rather than at test time.

What belongs here next: any extension that runs language servers or
linters for Pi and reports diagnostics per edit. Not covered: one-shot
lint commands over `bash` (no extension needed for those).

## See also

- [Tool-Call Rendering Extensions](tool-rendering-extensions.md): the
  display layer diagnostics render through
- [Model Routing Extensions](model-routing-extensions.md): smaller
  models benefit most from cheap external verification
- [How to Evaluate a Pi Extension](../references/evaluation.md)
