---
title: claude-agent-sdk-pi — Bridge to Anthropic's Agent SDK
type: ecosystem
updated: 2026-05-25
sources:
  - claude-agent-sdk-pi
  - claude-agent-sdk-pi-pr-8
  - claude-agent-sdk-pi-pr-10
  - anthropic-claude-agent-sdk
  - pi-pr-3286
  - pi-issue-3299
  - opus-47-adaptive
  - pi-claude-bridge
tags: [extension, claude-agent-sdk, integration]
---

# claude-agent-sdk-pi

`claude-agent-sdk-pi` is the bridge between Pi and Anthropic's
`@anthropic-ai/claude-agent-sdk`. It lets Pi route inference through
the Claude Agent SDK rather than calling the Anthropic API directly.

## Fork landscape

```
anthropics/claude-agent-sdk-typescript  (upstream Anthropic)
        ↓
prateekmedia/claude-agent-sdk-pi        (community-maintained Pi adapter)
        ↓
forks                                    (in-flight fixes downstream)
```

The npm-published version of `prateekmedia/claude-agent-sdk-pi` can be
ahead of the GitHub master branch — checking only one is unreliable;
both must be inspected before pinning a version.

## Install

Idiomatic install is via Pi's extension install path; registration is
verified by the extension/skill appearing in `pi`'s listing under
`[Extensions]`/`[Skills]`. Bare `npm install -g` does not always
register.

## Open PRs / fixes worth tracking

- **[PR #8](https://github.com/prateekmedia/claude-agent-sdk-pi/pull/8)** —
  adds `settingSources` and `strictMcpConfig` working alongside
  `appendSystemPrompt`.
- **[PR #10](https://github.com/prateekmedia/claude-agent-sdk-pi/pull/10)** —
  fix for hallucinated USER responses on Opus 4.7.

## Thinking-mode mapping (Opus 4.7 case study)

Pi exposes generic thinking modes (`think:high`, `think:xhigh`, etc.)
that are mapped per-model at the SDK boundary. Goal is portability;
failure mode is silent breakage when a new model changes its thinking
config shape.

### Symptom

Opus 4.7 with `think:high` showed *no* thinking blocks in
`claude-agent-sdk-pi`. Sonnet 4.6 worked. OpenCode (Zen provider)
showed thinking on Opus 4.7 — confirming model-side was fine and the
gap was in the Pi SDK adapter.

### Root cause

Opus 4.6/4.7 and Sonnet 4.6 dropped the legacy max-tokens-style
thinking config and require **adaptive** thinking with
`display: "summarized"`. Without `display`, the SDK streams thinking
events the wrapper silently drops.

### Fix

- **[pi-mono PR #3286](https://github.com/badlogic/pi-mono/pull/3286)** —
  model-specific thinking-mode mapping in the core.
- SDK-side companion patch in `claude-agent-sdk-pi`.

### `xhigh` vs `max` mapping decision

Opus 4.7 evaluation chart: `xhigh` at ~71% / ~104k tokens, `max` at
~74% / ~210k tokens. ~2× tokens for ~3 percentage points.

**Decision** ([PR #3286 review](https://github.com/badlogic/pi-mono/pull/3286)):
pi-`xhigh` should **not** map to provider-`max` given the cost gap.

**Asymmetry with Opus 4.6**: Opus 4.6 has no native `xhigh` rung
(only `low/medium/high/max`), so pi-`xhigh → max` is the only way to
reach the ceiling. Opus 4.7 has both `xhigh` and `max` natively, so
pi-`xhigh` maps to provider-`xhigh`, leaving provider-`max`
unreachable. Intentional cost/quality separation.

`packages/ai/scripts/generate-models.ts` carries adjacent hardcoded
branches:

```ts
if (model.id.includes("opus-4-6")) mergeThinkingLevelMap(model, { xhigh: "max" });
if (model.id.includes("opus-4-7")) mergeThinkingLevelMap(model, { xhigh: "xhigh" });
```

[Issue #3299](https://github.com/badlogic/pi-mono/issues/3299)
proposed a 6th pi rung to expose provider-`max`. Auto-closed; no
maintainer reopened.

### Extensibility

Per-model `thinkingLevelMap` is the canonical extensibility mechanism.
Each model declares its own ceiling and provider-value mappings;
adapter code consumes the map without per-model branches.

## Notes

- `~/.pi/agent/settings.json` carries `hideThinkingBlock` (Ctrl+R by
  default) — only hides display, doesn't disable generation.
- For the broader question of which routes hit which Anthropic billing
  bucket, see [Anthropic Subscription Auth in
  Pi](anthropic-subscription-auth.md).

## See also

- [Claude Pro/Max Subscription Extensions](claude-subscription-extensions.md) — niche survey covering this extension, its dominant fork, and the alternate payload-patcher shape
- [Anthropic Subscription Auth in Pi](anthropic-subscription-auth.md) — OAuth, API key, Foundry routes and which one hits the main subscription budget
- [pi-claude-bridge](pi-claude-bridge.md) — downstream extension that builds on this adapter to run CC as a Pi provider (subscription route) and as an AskClaude sub-agent. Adds the **session-resume** optimization that this upstream is missing — strictly less token-wasteful on any multi-turn session.
- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes
