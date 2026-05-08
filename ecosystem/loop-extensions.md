---
title: Pi Loop and Ralph Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - pi-autoresearch
  - mitsuhiko-agent-stuff
  - tmustier-pi-extensions
  - pi-ralph-wiggum
  - pi-review-loop
  - jayshah-pi-agent-extensions
  - samfoy-pi-ralph
  - kostyay-agent-stuff
  - mikeyobrien-pi-ralph
  - emanuelcasco-pi-mono-extensions
  - lnilluv-pi-ralph-loop
  - rahulmutt-pi-ralph
  - mikeyobrien-pi-autoloop
  - akijain-hermes-loop
  - latent-variable-pi-auto-continue
  - ghuntley-ralph
tags: [extension, loop, ralph, autoresearch]
entries:
  - id: pi-autoresearch
    name: pi-autoresearch
    repo: davebcn87/pi-autoresearch
    npm: pi-autoresearch
    role: evolve-driver
    notes: "Karpathy-inspired autoresearch with metric-gated keep/revert. Most adopted in this niche."
  - id: mitsupi-loop
    name: "mitsupi (loop.ts)"
    repo: mitsuhiko/agent-stuff
    npm: mitsupi
    role: in-process-llm-tool
    notes: "Canonical signal_loop_success pattern. Compaction-aware. Bundle (~25 extensions) shares download counts."
  - id: pi-ralph-wiggum
    name: "@tmustier/pi-ralph-wiggum"
    repo: tmustier/pi-extensions
    npm: "@tmustier/pi-ralph-wiggum"
    role: in-process-llm-tool
    notes: "ralph_done advance tool, reflection cadence, parallel loops in one repo."
  - id: pi-review-loop
    name: pi-review-loop
    repo: nicobailon/pi-review-loop
    npm: pi-review-loop
    role: in-process-specialized
    notes: "Code review until 'no issues found'."
  - id: emanuelcasco-loop
    name: emanuelcasco/pi-mono-extensions
    repo: emanuelcasco/pi-mono-extensions
    npm: "@emanuelcasco/pi-mono-extensions"
    role: cron-scheduled
    notes: "/loop [interval] — closest to Claude Code's /loop."
  - id: jayshah-pi-extensions
    name: jayshah5696/pi-agent-extensions
    repo: jayshah5696/pi-agent-extensions
    role: in-process-llm-tool
    notes: "Adapts mitsuhiko's loop.ts with attribution."
  - id: samfoy-pi-ralph
    name: samfoy/pi-ralph
    repo: samfoy/pi-ralph
    role: hat-orchestration
    notes: "YAML preset hats (Planner, Builder, Reviewer)."
  - id: kostyay-agent-stuff
    name: kostyay/agent-stuff
    repo: kostyay/agent-stuff
    role: in-process-llm-tool
    notes: "Independent reimplementation of mitsuhiko's signal_loop_success pattern."
  - id: rhobot-pi-ralph
    name: "@rhobot-dev/pi-ralph"
    repo: mikeyobrien/pi-ralph
    npm: "@rhobot-dev/pi-ralph"
    role: pty-embed
    notes: "PTY-embeds external `ralph` CLI."
  - id: ralph-loop-pi
    name: ralph-loop-pi
    repo: lnilluv/pi-ralph-loop
    npm: ralph-loop-pi
    role: subprocess-rpc
    notes: "Subprocess + RPC + custom rendering. Most feature-complete with RALPH.md, guardrails, pause/resume."
  - id: mikeyobrien-pi-autoloop
    name: mikeyobrien/pi-autoloop
    repo: mikeyobrien/pi-autoloop
    role: pty-embed
    notes: "PTY-embeds external `autoloop` CLI."
  - id: rahulmutt-pi-ralph
    name: "@rahulmutt/pi-ralph"
    repo: rahulmutt/pi-ralph
    npm: "@rahulmutt/pi-ralph"
    role: branched-session
    notes: "New session branch per iteration. Closest to Huntley's original."
  - id: hermes-loop
    name: akijain2000/hermes-loop
    repo: akijain2000/hermes-loop
    role: self-improving
    notes: "Skill creation, context compression, persistent memory."
  - id: pi-auto-continue
    name: "@latent-variable/pi-auto-continue"
    repo: latent-variable/pi-auto-continue
    npm: "@latent-variable/pi-auto-continue"
    role: in-process-agent-end
    notes: "~50 LOC. agent_end → sendUserMessage('continue'). Hard cap 100."
---

# Pi Loop and Ralph Extensions

Comparative survey of Pi extensions implementing autonomous agent loops,
deterministic iteration patterns, and Ralph Wiggum-style coding campaigns.

14 distinct projects across 7 architectural variants.

## What this page is for

Architectural and feature comparison across the 14 implementations.
The structure here (variants A–G, hook-surface usage, recommendation
matrix by goal) doesn't decay — it's about *how* each extension solves
the loop problem, not *how popular* it is right now.

## The two front-runners

**`davebcn87/pi-autoresearch`** is the most adopted deterministic-loop
project in the Pi ecosystem. A Karpathy-inspired autoresearch harness:

```
loop:
  try idea → benchmark → if metric improved → keep + commit
                       → if regressed       → revert
  → repeat
```

Used for test speed, bundle size, LLM training, build times, Lighthouse
scores. Differs from Ralph because it has a first-class metric that gates
whether each iteration is kept. State persists in `autoresearch.md` +
`autoresearch.jsonl`. Resumable across context resets and `/compact`.
Status widget always visible. `Ctrl+Shift+T` / `Ctrl+Shift+F` for
inline/fullscreen dashboard. Confidence scoring (after 3+ runs, shows how
the best improvement compares to noise floor).

Recent versions added compaction-aware behavior: `session_compact`
re-prompts the agent to re-read `autoresearch.md` and continue, handling
Pi's auto-compaction without stopping the loop.

**`mitsuhiko/agent-stuff`** is Armin Ronacher's personal collection.
Contains the canonical "agent-end loop with `signal_loop_success`
breakout tool" in `extensions/loop.ts` — every later implementation
either copies or independently re-derives this pattern.

Note on bundle effects: `mitsupi` ships ~25 different extensions; npm
download counts reflect the entire bundle, not the loop extension
specifically.

## Architectural variants — 7 distinct approaches

### Variant A — In-process, LLM-driven via breakout tool

The LLM calls a tool (`signal_loop_success` / `ralph_done`) to advance or
break. Extension queues next iteration as `pi.sendUserMessage` or
`pi.sendMessage` with `triggerTurn:true`. Same session throughout —
context window persists across iterations until `/compact`.

| Implementation | Originator | Pattern signature |
|---|---|---|
| **mitsuhiko/agent-stuff `loop.ts`** | Armin Ronacher (Flask/Sentry creator) | `/loop tests \| custom <cond> \| self`; LLM calls `signal_loop_success`; `pi.sendMessage({...}, {deliverAs:"followUp", triggerTurn:true})` on `agent_end`; `session_before_compact` preserves loop state; condition summarized via Haiku for status widget |
| **@tmustier/pi-ralph-wiggum** | Thomas Mustier | LLM calls `ralph_done` advance tool; text marker `<promise>COMPLETE</promise>` for completion; reflection cadence; multiple parallel loops in one repo |
| **kostyay/agent-stuff `loop.ts`** | Konstantin Yegupov | Independent reimplementation of mitsuhiko's pattern; same `signal_loop_success` shape |
| **jayshah5696/pi-agent-extensions** | Jay Shah | Adapts mitsuhiko's `loop.ts` directly (with attribution) |

### Variant B — In-process, `agent_end`-driven (no LLM tool)

Extension fires next iteration on every `agent_end`, no LLM tool required.

| Implementation | Pattern signature |
|---|---|
| **latent-variable/pi-auto-continue** | ~50 LOC. `agent_end` → `pi.sendUserMessage("continue")`. Hard cap of 100 iterations. Disables on user input or abort. Use case: overnight autoresearch. |

### Variant C — Subprocess + RPC + custom rendering

Each iteration spawns `pi --mode rpc` as child; parent re-renders RPC
events with Pi's exported components. Iterations are independent processes
(clean cold start per iteration).

| Implementation | Pattern signature |
|---|---|
| **lnilluv/pi-ralph-loop** (`ralph-loop-pi`) | Most production-feature-complete. RALPH.md + YAML frontmatter (commands, guardrails, completion_promise, required_outputs, block_commands, protected_files). 4 presets (fix-tests, migration, research-report, security-audit). `/ralph-pause` (SIGSTOP), `/ralph-resume` (SIGCONT), `/ralph-steer`, `/ralph-follow`, `/ralph-stop`, `/ralph-status`. ~1300 LOC. |

### Variant D — Branched session per iteration (no RPC, no subprocess)

Extension waits for parent agent idle, branches new session per iteration,
sends prompt as user message via session APIs.

| Implementation | Pattern signature |
|---|---|
| **rahulmutt/pi-ralph** | Minimalist. `/ralph <prompt-file> [iterations]`; each iteration starts in fresh session branched from original. Progress in `.ralph/<YYYY>/<MM>/<DD>/RALPH-*.md` files. Closest to Huntley's "fresh context every iteration" Ralph original — but Pi-native (no `pi --print` overhead). |

### Variant E — PTY-embedded external runtime

Extension wraps an external Ralph runtime (separate CLI tool) and embeds
its TUI in a PTY. Pi acts as a launcher and inspector, not the loop driver.

| Implementation | Wraps | Notes |
|---|---|---|
| **mikeyobrien/pi-ralph** (`@rhobot-dev/pi-ralph`) | `ralph` CLI v2.4.4 | Status widget below editor; `/ralph` overlay; `ralph_loop()` LLM tool; PTY embedding; keybindings `s` stop, `m` merge, `d` discard, `r` retry, `H` history, `D` diff, `a` attach shell |
| **mikeyobrien/pi-autoloop** | `autoloop` CLI | Presets: autocode/autoqa/autotest/autofix/autoreview/autosec/autospec; `/loop:run`, `/loop:list`, `/loop:status`, `/loop:stop`, `/loop:inspect`, `/loop:presets`. EventEmitter-based for reactive UI. |

### Variant F — Hat-based multi-agent orchestration

Specialized agent "hats" (Planner, Builder, Reviewer, etc.) hand off work
via published events. Closer to a workflow engine than the original Ralph.

| Implementation | Pattern signature |
|---|---|
| **samfoy/pi-ralph** | YAML preset defines hats with `triggers`/`publishes`; agent emits `>>> EVENT: <name>` to advance. Built-in presets: feature, code-assist, spec-driven, debug, refactor, review. Includes `/plan` for PDD (Prompt-Driven Development) sessions. |

### Variant G — Cron-style scheduled loop

Recurring interval-based — closer to Claude Code's `/loop` than to Ralph.

| Implementation | Pattern signature |
|---|---|
| **emanuelcasco/pi-mono-extensions/loop** | `/loop [interval] <prompt>`. Trailing "every" clause supported. 7-day expiry. `/loop stop` to cancel. |

### Special cases — autoresearch and self-improving

Deterministic agent loops that don't fit the Ralph mold:

| Implementation | Approach |
|---|---|
| **davebcn87/pi-autoresearch** | Karpathy-inspired autoresearch with metric-gated keep/revert; explicit benchmark backpressure |
| **akijain2000/hermes-loop** | Self-improving runtime: creates skills from experience, iterative context compression, persistent memory; runs on Pi or Claude Code |
| **nicobailon/pi-review-loop** | Specialized for code review: iterates until "no issues found"; auto-trigger on phrases like "implement the plan"; smart exit detection |

## Code quality observations

These are structural notes from inspecting each codebase. They aren't
quality scores — they're features and patterns you can verify quickly.
For a current evaluation framework see
[How to Evaluate a Pi Extension](../references/evaluation.md).

| Extension | Notes |
|---|---|
| **pi-autoresearch** | CI/CD via GitHub Actions, npm OIDC trusted publishing, multiple contributors, regular tagged releases, comprehensive CHANGELOG. TypeBox for schemas; cleanly split extension/skill. Compaction-aware (v1.2+). Dashboard config supports user shortcut overrides. The most production-grade extension in this niche. |
| **mitsuhiko/agent-stuff `loop.ts`** | Concise (~250 LOC), TypeBox, structured for clarity. Clean state-machine model. Hooks `session_before_compact` to preserve loop intent across compaction (the only extension surveyed that does this). Uses Haiku for the status-widget condition summary. Idiomatic TypeScript. |
| **@tmustier/pi-ralph-wiggum** | ~700 LOC. State persisted to `.ralph/<name>.state.json` + `.ralph/<name>.md`. Survives reload via `session_start` rehydration. `<promise>COMPLETE</promise>` text marker. `migrateState()` for backwards-compat. Production-grade for the use case. |
| **pi-review-loop** | ~250 LOC main extension. Configurable patterns (trigger, exit, prompt). Smart exit detection (won't be fooled by "Fixed N issues. No further issues found."). "Fresh context" mode strips prior review iterations from context. |
| **ralph-loop-pi** (lnilluv) | ~1300 LOC. Heavy: full RPC parent/child plumbing, signal handling, response correlation with timeout. Tasks-folder workflow. YAML frontmatter with rich validation. Goal-continuation audits per iteration. Test parity harness for iteration determinism. Most feature-complete; also most surface area to maintain. |
| **rahulmutt/pi-ralph** | Minimalist (~few hundred LOC). Cleanly written. `.ralph/<YYYY>/<MM>/<DD>/RALPH-*.md` progress hierarchy. Branches new session per iteration via session APIs. No subprocess. Closest to Huntley's original. |
| **samfoy/pi-ralph** | Medium-sized. YAML-driven preset system. Six built-in presets covering common workflows. `/plan` PDD workflow saves artifacts to `specs/<task-name>/`. Single contributor. |
| **mikeyobrien/pi-ralph** (PTY) | Small wrapper. Delegates real work to external `ralph` CLI. Status widget + overlay + LLM tool. If the external CLI changes, the wrapper needs updates. |
| **emanuelcasco/pi-mono-extensions/loop** | Small. Smart input parsing (leading token vs trailing "every" clause vs default). 7-day auto-expiry. Clean cleanup on session shutdown. |
| **latent-variable/pi-auto-continue** | ~50 LOC. The minimalist choice. `setTimeout(...,0)` defer trick to let agent settle into idle. User-input counter reset. Aborted-turn detection. |
| **kostyay/agent-stuff `loop.ts`** | Independent reimplementation of mitsuhiko's pattern; ~250 LOC; similar shape with `signal_loop_success`. Author has 25+ other Pi extensions. |
| **akijain2000/hermes-loop** | Combines pi-mono + hermes-agent + Skill Factory. Self-improving (creates skills from experience), iterative context compression, persistent memory. Mostly research-grade. |

## Hook-surface usage matrix

| API | Used by |
|---|---|
| `pi.on("agent_end", ...)` | All in-process variants — drives next iteration |
| `pi.on("before_agent_start", ...)` | mitsuhiko, tmustier, pi-autoresearch (inject loop context into system prompt or messages) |
| `pi.on("session_start", ...)` | mitsuhiko, tmustier, pi-autoresearch (rehydrate state on reload/fork/resume) |
| `pi.on("session_before_compact", ...)` | mitsuhiko only (preserve loop state across `/compact` — most extensions miss this) |
| `pi.on("input", ...)` | latent-variable, pi-autoresearch (reset counters on user typing) |
| `pi.sendUserMessage(text)` | tmustier, latent-variable, rahulmutt |
| `pi.sendMessage(msg, {triggerTurn:true, deliverAs:"followUp"})` | mitsuhiko, kostyay |
| `pi.registerTool(...)` | All — `signal_loop_success`, `ralph_done`, `ralph_loop`, `autoloop`, `init_experiment`, etc. |
| `pi.registerCommand(...)` | All — `/ralph`, `/ralph-stop`, `/loop`, `/autoresearch`, `/review-start`, etc. |
| `pi.appendEntry(type, data)` | mitsuhiko, samfoy, pi-autoresearch (persist state in session JSONL) |
| `ctx.sessionManager.getBranch()` | tmustier (rehydrate from tool result `details` for branch correctness) |
| `ctx.signal?.aborted` on `agent_end` | latent-variable, mitsuhiko (abort detection) |
| `ctx.hasPendingMessages()` | tmustier (don't double-fire if steering already queued) |
| `spawn("pi", ["--mode", "rpc", ...])` | lnilluv (subprocess pattern) |
| RPC commands (`prompt`, `steer`, `follow_up`, `abort`, `get_state`) | lnilluv |
| `spawn` external process in PTY | mikeyobrien (both extensions) |

Only `mitsuhiko/agent-stuff loop.ts` uses `session_before_compact` to
preserve loop state across compaction. Every other in-process loop will
"forget" it's in a loop after `/compact` fires.

## Recommendation matrix

| Goal | Best extension | Why |
|---|---|---|
| Deterministic improvement loops with metrics (test speed, bundle size, LLM training) | **pi-autoresearch** | Most adopted in this niche; production-grade; compaction-aware; confidence scoring; dashboard |
| Single-context loop (visible iterations, compaction-safe) | **mitsuhiko/agent-stuff `loop.ts`** | The canonical pattern. Compaction-safe via `session_before_compact`. |
| Closest to Huntley's Ralph (fresh context every iteration, prompt file based) | **rahulmutt/pi-ralph** | Branches new session per iter; clean cold start; minimal LOC; closest to bash `while :; do cat PROMPT.md \| pi -p; done` semantics |
| Production autonomous campaigns (guardrails, presets, completion gating, pause/resume, RALPH.md) | **lnilluv/pi-ralph-loop** | Most complete: RALPH.md frontmatter, completion_gate, required_outputs, block_commands, protected_files, signal-based pause/resume, RPC subprocess architecture |
| Just want autocontinue overnight | **latent-variable/pi-auto-continue** | 50 LOC, hard cap of 100, abort-aware. Simplest possible thing. |
| TODO/PRD/feature-list driven loops with reflection | **@tmustier/pi-ralph-wiggum** | LLM-driven via `ralph_done` tool; reflection cadence; multiple parallel loops in one repo |
| Multi-role workflow (Planner → Builder → Reviewer, TDD pipelines) | **samfoy/pi-ralph** | Hat-based with built-in presets (TDD, spec-driven, debug, refactor) |
| External Ralph CLI integration | **mikeyobrien/pi-ralph** (for `ralph`) or **mikeyobrien/pi-autoloop** (for `autoloop`) | If you already use these external runtimes, Pi becomes a launcher/inspector |
| Cron-style scheduled prompts | **emanuelcasco/pi-mono-extensions/loop** | Closest to Claude Code's `/loop` semantics |
| Code-review-only loop | **nicobailon/pi-review-loop** | Specialized for review-until-clean; smart exit detection; auto-trigger on phrases |
| Self-improving (creates skills from experience) | **akijain2000/hermes-loop** | Research-grade; combines hermes-agent's learning loop with pi-mono. |

## Convergence signal

At least 6 different authors (mitsuhiko, kostyay, tmustier, lnilluv,
samfoy, emanuelcasco) independently converged on essentially the same
in-session pattern: `pi.on("agent_end", ...)` → `pi.sendMessage({triggerTurn:true})`,
with optional LLM-tool breakout. The hook surface
(`agent_end`, `before_agent_start`, `session_before_compact`,
`session_start`, `sendMessage(triggerTurn:true)`, `registerTool`,
`appendEntry`) already exists in pi-mono — no fork or core PR needed.

## See also

- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs, maintenance signals, and code-quality recipes
- [Ghuntley — Ralph Wiggum as a software engineer](https://ghuntley.com/ralph/) — the article that popularized the pattern
- [Karpathy — autoresearch idea](https://x.com/karpathy/status/1827143768459637044) — origin of the autoresearch shape
