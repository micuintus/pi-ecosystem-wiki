---
title: Pi Evolve / Code-Optimization Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - pi-autoresearch
  - karpathy-autoresearch
  - openevolve
  - shinkaevolve
tags: [extension, evolve, autoresearch]
---

# Pi Evolve / Code-Optimization Extensions

Single-extension reference page (the niche is currently a category of
one) covering Pi extensions that implement evolutionary code
optimization — try a variant, benchmark it, keep or discard, repeat.

## The niche is nearly empty

Only one production evolve extension exists for Pi today:
**`davebcn87/pi-autoresearch`**. Everything else in the Pi
ecosystem either iterates without variant storage (Ralph extensions) or
doesn't tackle the metric-gated keep/discard pattern at all.

## What counts as an evolve system

For this survey: tries variant → measures with explicit metric → keeps
or discards based on metric → archives lineage. Distinguishing
properties:

- Explicit fitness metric (not just "until done")
- Persists variants (in git history, branches, or files) across iterations
- Keep/discard decision based on the metric
- Archives lineage so later iterations can learn from prior ones

Pi Ralph extensions ([loop-extensions](loop-extensions.md)) are
*iteration* — no metric gating, no variant archive. Complementary but
distinct.

## `davebcn87/pi-autoresearch`

Project signals: well-tagged release history, CHANGELOG present, CI/CD
via GitHub Actions, npm OIDC trusted publishing, multiple contributors.
Production-grade by every structural measure. For current vital signs
(stars, downloads, last push), query as described in
[How to Evaluate a Pi Extension](../references/evaluation.md).

Inspiration: Karpathy's [autoresearch](https://github.com/karpathy/autoresearch)
(single-branch hill-climbing). `pi-autoresearch` is the Pi-native
productionized version, with extension UI, dashboard,
compaction-awareness, and branch-aware resumability.

| Aspect | Implementation |
|---|---|
| LLM tools | `init_experiment`, `run_experiment`, `log_experiment` |
| Variant store | Linear git timeline. Kept experiments → commits (`experiment-NNN-description`). Discards reverted. |
| Index file | `autoresearch.md` — objective, metric, unit, direction, baseline, files-in-scope, ideas-to-try, what's-been-tried |
| Run log | `autoresearch.jsonl` (append-only iteration metadata) |
| Benchmark | `autoresearch.sh` outputs `METRIC name value` lines |
| Correctness gate | Optional `autoresearch.checks.sh` (tests/lint must pass for `keep`) |
| Lifecycle hooks | Optional `autoresearch.hooks/before.sh`, `after.sh` |
| Selection policy | None (pure hill-climbing — always continues from current best) |
| Multi-objective | Primary metric drives keep/discard; secondary metrics monitoring only |
| Compaction-aware | Yes — `session_before_compact` snapshots state losslessly; auto-resume on overflow |
| Confidence scoring | After 3+ runs, compares best improvement vs noise floor (≥2.0× green, 1.0–2.0× yellow, <1.0× red) |
| UI | Status widget always visible, `Ctrl+Shift+T` inline dashboard, `Ctrl+Shift+F` fullscreen, `/autoresearch` command, live HTML export |
| Skills | `autoresearch-create`, `autoresearch-finalize`, `autoresearch-hooks` |

Use cases (from README): test speed, bundle size, LLM training
(val_bpb), build times, Lighthouse scores. Any optimization target with
a measurable metric.

Per-iteration workflow:

1. Agent reads `autoresearch.md` → picks an idea from the ideas list.
2. Agent edits files in scope.
3. Agent runs `./autoresearch.sh` via `run_experiment` (captures METRIC values).
4. Agent runs `./autoresearch.checks.sh` if configured.
5. Agent calls `log_experiment({ status: "keep" | "discard" | "crash", metrics: {...} })`:
   - `keep` → tool commits to git as `experiment-N-description`
   - `discard` → tool reverts working tree
   - `crash` → tool reverts and logs failure
6. Loop fires next iteration; agent re-reads `autoresearch.md` (now updated with the previous attempt).

Critical design rules from the `autoresearch-create` skill:

- Don't commit/revert manually — tools own git ops; manual ops corrupt
  experiment lineage.
- `keep` only when primary metric improved — secondary metrics are
  monitoring, never drive decisions.
- Append to `autoresearch.md` what was tried — build a history the next
  iteration can read.
- Reset on context exhaustion via auto-compaction — loop continues
  automatically.

## Why other Pi loop extensions don't qualify

The 14 Pi Ralph/loop extensions surveyed in
[loop-extensions](loop-extensions.md) all share a structural limitation
that prevents them from being evolve systems:

| Pattern | Why it's not "evolve" |
|---|---|
| Variants A–B (in-process loop drivers) | No metric gate, no variant archive |
| Variant C (subprocess+RPC, `ralph-loop-pi`) | Has bash condition for stopping but no metric-driven keep/discard |
| Variant D (branched-session, `rahulmutt/pi-ralph`) | Each iter is separate branched session, but no metric, no merging back |
| Variant E (PTY-embedded external runtimes) | External tool's responsibility, not Pi-native |
| Variant F (hat-based, `samfoy/pi-ralph`) | Workflow engine, not evolve |
| Variant G (cron-style, `emanuelcasco`) | Scheduled prompts, not evolve |

Even `nicobailon/pi-review-loop` ("review until no issues found") is
iteration without metric persistence. The closest neighbor is
`akijain2000/hermes-loop` — self-improving via skill creation — but it
evolves *capabilities* (skill files), not *code variants* under a metric.

## Research-landscape context

None of the systems below are Pi extensions; they're external systems
and proposals. They form the conceptual backdrop for any Pi-native
evolve work.

| System | Properties | Variant store | Selection |
|---|---|---|---|
| **AlphaEvolve** (DeepMind, closed) | LLM mutation + evolutionary algorithms; discovered first Strassen improvement in 56 years | In-memory archive | MAP-Elites grid |
| **OpenEvolve** (codelion, open) | AlphaEvolve clone — MAP-Elites + islands + migration | Archive + islands | Multi-dim behavior space |
| **ShinkaEvolve** (Sakana, ICLR 2026) | Sample-efficient: novelty rejection + bandit LLM ensemble; SOTA circle packing in ~150 samples | Archive | Power-law + novelty filter |
| **Karpathy autoresearch** | Pure hill-climbing single-branch loop | Single branch + program.md | Always best |

`pi-autoresearch` is structurally Karpathy autoresearch productionized
for Pi. It inherits the single-branch hill-climbing limitation (failed
exploration paths are lost) but adds Pi-grade UX, compaction-awareness,
hooks, and skills.

## Open niche

The "branched variants with markdown ledger across runs" pattern — a
tree of branches indexed by a single ledger file — is **not yet
implemented as a Pi extension**. The hook surface needed
(`agent_end`, `before_agent_start`, `session_before_compact`,
`session_start`, `sendMessage(triggerTurn:true)`, `registerTool`)
already exists in `pi-mono`. No core changes required to build one.

## See also

- [Loop and Ralph Extensions](loop-extensions.md) — iteration patterns
  without metric gating; complementary to evolve systems.
