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
---

# Pi Loop and Ralph Extensions

Comparative survey of Pi extensions implementing autonomous agent loops,
deterministic iteration patterns, and Ralph Wiggum-style coding campaigns.

14 distinct projects across 7 architectural variants.

## Headline metrics (2026-05-06)

Sorted by GitHub stars. Weekly npm downloads as of 2026-04-29 to 2026-05-05.

| Rank | Extension | Repo | ⭐ Stars | 🍴 Forks | 👥 Contrib | 📦 Weekly DL | Last push | Approach |
|------|-----------|------|--------:|--------:|----------:|------------:|-----------|----------|
| 1 | **pi-autoresearch** | davebcn87/pi-autoresearch | **6,443** | 375 | **14** | **943** | 2026-05-06 | Autoresearch (try → measure → keep/revert) |
| 2 | **mitsupi (`loop.ts`)** | mitsuhiko/agent-stuff | **2,275** | 167 | 4 | 168 | 2026-04-29 | LLM-tool breakout (`signal_loop_success`) — canonical pattern |
| 3 | **@tmustier/pi-ralph-wiggum** | tmustier/pi-extensions | 291 | 19 | 4 | **927** | 2026-04-28 | LLM-tool advance (`ralph_done`) |
| 4 | **pi-review-loop** | nicobailon/pi-review-loop | 75 | 12 | 2 | 133 | 2026-04-15 | Code review loop until "no issues found" |
| 5 | **emanuelcasco/pi-mono-extensions** | emanuelcasco/pi-mono-extensions | 37 | 5 | 1 | 27 | 2026-05-06 | Cron-style `/loop [interval]` |
| 6 | **jayshah5696/pi-agent-extensions** | jayshah5696/pi-agent-extensions | 24 | 2 | 3 | 208 | 2026-04-28 | Adapts mitsuhiko's `loop.ts` |
| 7 | **samfoy/pi-ralph** | samfoy/pi-ralph | 11 | 1 | 1 | 25 | 2026-04-21 | Hat-based multi-agent orchestration |
| 8 | **kostyay/agent-stuff** | kostyay/agent-stuff | 8 | 1 | 1 | (in-repo) | 2026-05-03 | LLM-tool breakout (`signal_loop_success`, separate from mitsuhiko's) |
| 9 | **mikeyobrien/pi-ralph** | mikeyobrien/pi-ralph (`@rhobot-dev/pi-ralph`) | 7 | 0 | 1 | 8 | 2026-02-07 | PTY-embed external `ralph` CLI |
| 10 | **ralph-loop-pi** | lnilluv/pi-ralph-loop | 2 | 1 | 2 | 21 | 2026-05-04 | Subprocess + RPC + custom rendering; RALPH.md |
| 11 | **mikeyobrien/pi-autoloop** | mikeyobrien/pi-autoloop | 2 | 0 | 1 | (not on npm) | 2026-04-17 | PTY-embed external `autoloop` CLI |
| 12 | **@rahulmutt/pi-ralph** | rahulmutt/pi-ralph | 2 | 0 | 1 | 32 | 2026-04-22 | Branched session per iteration |
| 13 | **akijain2000/hermes-loop** | akijain2000/hermes-loop | 1 | 1 | 1 | (not on npm) | 2026-04-06 | Self-improving (skill creation, context compression) |
| 14 | **@latent-variable/pi-auto-continue** | latent-variable/pi-auto-continue | 1 | 0 | 1 | 10 | 2026-04-11 | `agent_end` → `pi.sendUserMessage("continue")` |

Notes:
- `pi-autoresearch` dominates by stars and downloads, but is not a Ralph
  loop in the strict sense — it is a Karpathy-inspired autoresearch harness
  combining agent iteration with explicit benchmark-and-keep/revert
  decisions. Listed here because it implements deterministic agent loops.
- `mitsupi` (mitsuhiko/agent-stuff) hosts ~25 different extensions; download
  counts reflect the entire bundle.
- `jayshah5696/pi-agent-extensions` explicitly credits and adapts
  mitsuhiko's `loop.ts`.

## Two stars dominate

**`davebcn87/pi-autoresearch`** (6,443 ⭐, 14 contributors) is the most
adopted deterministic-loop project in the Pi ecosystem. A Karpathy-inspired
autoresearch harness:

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

**`mitsuhiko/agent-stuff`** (2,275 ⭐) is Armin Ronacher's personal
collection. Contains the canonical "agent-end loop with `signal_loop_success`
breakout tool" in `extensions/loop.ts` — every later implementation either
copies or independently re-derives this pattern.

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

| Implementation | Approach | Stars |
|---|---|---|
| **davebcn87/pi-autoresearch** | Karpathy-inspired autoresearch with metric-gated keep/revert; explicit benchmark backpressure | 6,443 |
| **akijain2000/hermes-loop** | Self-improving runtime: creates skills from experience, iterative context compression, persistent memory; runs on Pi or Claude Code | 1 |
| **nicobailon/pi-review-loop** | Specialized for code review: iterates until "no issues found"; auto-trigger on phrases like "implement the plan"; smart exit detection | 75 |

## Code quality observations

| Extension | Notes |
|---|---|
| **pi-autoresearch** | Well-tested (CI/CD via GitHub Actions, npm OIDC trusted publishing, 14 contributors, 16+ releases, comprehensive CHANGELOG). TypeBox for schemas; cleanly split extension/skill. Compaction-aware (v1.2+). Dashboard config supports user shortcut overrides. Production-grade. |
| **mitsuhiko/agent-stuff `loop.ts`** | Concise (~250 LOC), TypeBox, structured for clarity. Clean state-machine model. Hooks `session_before_compact` to preserve loop intent across compaction (the only extension surveyed that does this). Uses Haiku for the status-widget condition summary. Idiomatic TypeScript. |
| **@tmustier/pi-ralph-wiggum** | ~700 LOC. State persisted to `.ralph/<name>.state.json` + `.ralph/<name>.md`. Survives reload via `session_start` rehydration. `<promise>COMPLETE</promise>` text marker. `migrateState()` for backwards-compat. Production-grade for the use case. |
| **pi-review-loop** | ~250 LOC main extension. Configurable patterns (trigger, exit, prompt). Smart exit detection (won't be fooled by "Fixed N issues. No further issues found."). "Fresh context" mode strips prior review iterations from context. |
| **ralph-loop-pi** (lnilluv) | ~1300 LOC. Heavy: full RPC parent/child plumbing, signal handling, response correlation with timeout. Tasks-folder workflow. YAML frontmatter with rich validation. Goal-continuation audits per iteration. Test parity harness for iteration determinism. Most feature-complete; also most surface area to maintain. |
| **rahulmutt/pi-ralph** | Minimalist (~few hundred LOC). Cleanly written. `.ralph/<YYYY>/<MM>/<DD>/RALPH-*.md` progress hierarchy. Branches new session per iteration via session APIs. No subprocess. Closest to Huntley's original. |
| **samfoy/pi-ralph** | Medium-sized. YAML-driven preset system. Six built-in presets covering common workflows. `/plan` PDD workflow saves artifacts to `specs/<task-name>/`. Single contributor; 11 stars suggests modest adoption. |
| **mikeyobrien/pi-ralph** (PTY) | Small wrapper. Delegates real work to external `ralph` CLI. Status widget + overlay + LLM tool. If the external CLI changes, the wrapper needs updates. |
| **emanuelcasco/pi-mono-extensions/loop** | Small. Smart input parsing (leading token vs trailing "every" clause vs default). 7-day auto-expiry. Clean cleanup on session shutdown. |
| **latent-variable/pi-auto-continue** | ~50 LOC. The minimalist choice. `setTimeout(...,0)` defer trick to let agent settle into idle. User-input counter reset. Aborted-turn detection. |
| **kostyay/agent-stuff `loop.ts`** | Independent reimplementation of mitsuhiko's pattern; ~250 LOC; similar shape with `signal_loop_success`. Author has 25+ other Pi extensions. |
| **akijain2000/hermes-loop** | Combines pi-mono + hermes-agent + Skill Factory. Self-improving (creates skills from experience), iterative context compression, persistent memory. Mostly research-grade; 1 star, 1 contributor. |

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
| Deterministic improvement loops with metrics (test speed, bundle size, LLM training) | **pi-autoresearch** | 6.4k ⭐, 14 contributors, production-grade, compaction-aware, confidence scoring, dashboard. Standard for this niche. |
| Single-context loop (visible iterations, compaction-safe) | **mitsuhiko/agent-stuff `loop.ts`** | The canonical pattern. Compaction-safe via `session_before_compact`. |
| Closest to Huntley's Ralph (fresh context every iteration, prompt file based) | **rahulmutt/pi-ralph** | Branches new session per iter; clean cold start; minimal LOC; closest to bash `while :; do cat PROMPT.md \| pi -p; done` semantics |
| Production autonomous campaigns (guardrails, presets, completion gating, pause/resume, RALPH.md) | **lnilluv/pi-ralph-loop** | Most complete: RALPH.md frontmatter, completion_gate, required_outputs, block_commands, protected_files, signal-based pause/resume, RPC subprocess architecture |
| Just want autocontinue overnight | **latent-variable/pi-auto-continue** | 50 LOC, hard cap of 100, abort-aware. Simplest possible thing. |
| TODO/PRD/feature-list driven loops with reflection | **@tmustier/pi-ralph-wiggum** | LLM-driven via `ralph_done` tool; reflection cadence; multiple parallel loops in one repo; 927/wk downloads |
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

- [Ghuntley — Ralph Wiggum as a software engineer](https://ghuntley.com/ralph/) — the article that popularized the pattern
- [Karpathy — autoresearch idea](https://x.com/karpathy/status/1827143768459637044) — origin of the autoresearch shape
