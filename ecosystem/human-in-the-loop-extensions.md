---
title: Pi Human-in-the-Loop (ask_user_question) Extensions
type: ecosystem
updated: 2026-08-21
sources:
  - juicesharp-rpiv-ask-user-question
  - josephyoung-pi-ask-user-question
  - jqwn-pi-ask-user-question
  - npm-pi-ask-user-question
  - composio-top-pi-extensions
  - pi-extensions-docs
tags: [extension, hitl, ask-user-question, ux]
entries:
  - id: juicesharp-rpiv-ask-user-question
    name: "@juicesharp/rpiv-ask-user-question"
    npm: "@juicesharp/rpiv-ask-user-question"
    role: category-leader
    notes: "By download volume this is one of the most-installed Pi extensions in existence — an order of magnitude above typical extensions in this wiki. One tool, `ask_user_question`, letting the model stop and ask instead of guessing. Actively released."
  - id: josephyoung-pi-ask-user-question
    name: pi-ask-user-question (josephyoung)
    repo: josephyoung/pi-ask-user-question
    role: form-based
    notes: "Uses Pi's built-in dialogs for single questions and one atomic `ctx.ui.custom()` form for grouped/advanced fields (text, textarea, select). The most UI-forward implementation. Note the narrow declared peer range (`>=0.80.2 <0.81.0`) — check compatibility before installing."
  - id: jqwn-pi-ask-user-question
    name: "@jqwn/pi-ask-user-question"
    npm: "@jqwn/pi-ask-user-question"
    role: rich-multi-question
    notes: "Multi-question TUI dialogs with options, descriptions, previews, multi-select and custom free-text answers."
  - id: npm-pi-ask-user-question
    name: pi-ask-user-question
    npm: pi-ask-user-question
    role: minimal
    notes: "Single `askUserQuestion` tool: required `question` string, optional `options` array (multiple choice when present, free text when absent). The smallest surface in the category."
---

# Pi Human-in-the-Loop (`ask_user_question`) Extensions

## Why this category exists

Pi's core has no way for the model to ask you something. It can only act or
stop. So when the request is ambiguous, the model guesses — and a wrong guess
in the first thirty seconds costs the whole session, because everything after
it builds on the wrong interpretation.

These extensions add one tool that lets the model pause and ask. The category
is small in code and unusually large in impact: **by download count the leading
package is among the most-installed Pi extensions anywhere**, which is a strong
signal that the missing primitive was felt widely.

## What they all do

Register a single tool — `ask_user_question` or `askUserQuestion` — that takes
a question and optionally a set of options. The model calls it mid-task, Pi
renders a prompt, and the answer returns as the tool result. Variation between
implementations is almost entirely **UI richness**, not semantics:

| Shape | What you get | Options here |
|---|---|---|
| **Minimal** | one question, optional multiple choice | `pi-ask-user-question` |
| **Rich dialog** | descriptions, previews, multi-select, custom answers | `@jqwn/pi-ask-user-question` |
| **Grouped form** | several fields answered in one atomic `ctx.ui.custom()` form | `josephyoung/pi-ask-user-question` |
| **Category leader** | one tool, heavily adopted, actively maintained | `@juicesharp/rpiv-ask-user-question` |

## Picking guide

| Goal | Pick |
|---|---|
| Install one thing and move on | `@juicesharp/rpiv-ask-user-question` |
| Ask several related things at once (a form, not a quiz) | `josephyoung/pi-ask-user-question` |
| Rich single questions with previews and multi-select | `@jqwn/pi-ask-user-question` |
| Smallest possible surface | `pi-ask-user-question` |

## Caveats

- **One is enough, and two collide.** These register overlapping tool names
  (`ask_user_question` / `askUserQuestion`). Pick one.
- **Peer ranges matter here.** At least one implementation declares a narrow
  Pi version range; a HITL tool that fails to load is worse than none, because
  the model reverts to guessing silently.
- **It changes model behaviour, not just UX.** Once the tool exists the model
  will use it, including when you would rather it just proceeded. If you run
  unattended or overnight sessions, that is a stall risk — scope it out of
  autonomous runs (see [loop extensions](loop-extensions.md)).
- **Not the same as approval gating.** Asking a clarifying question is not
  permission enforcement; for that see
  [permission extensions](permission-extensions.md).

## See also

- [Permission Extensions](permission-extensions.md) — the other half of
  "core has no interaction model": gating dangerous operations
- [Prompt Extensions](prompt-extensions.md) — `ask_user`-driven queues and
  input UX
- [Slash-Command Discovery](slash-command-extensions.md) — keeping the `/`
  palette usable once several of these are installed
