---
title: Claude Code `/loop` — Cron-Scheduled Task Repetition
type: ecosystem
updated: 2026-05-08
sources:
  - claude-code-scheduled-tasks
  - claude-code-agent-loop
tags: [claude-code, loop, cron, comparison]
---

# Claude Code `/loop`

Cross-tool reference for Pi users evaluating loop options. `/loop` in
Claude Code is **not** a tight tool-calling loop like Pi's Ralph
extensions ([loop-extensions](loop-extensions.md)). It is a
**session-scoped cron scheduler**. Different problem space, different
mechanics.

## What it does

`/loop` is a bundled skill (prompt-based, not hardcoded logic) that
schedules a prompt to re-run on an interval while the session stays
open.

| Invocation | Behavior |
|---|---|
| `/loop 5m check the deploy` | Runs prompt every 5 minutes (cron `*/5 * * * *`) |
| `/loop check the deploy` | Claude picks the interval (1m–1h) dynamically each iteration |
| `/loop` | Runs the built-in maintenance prompt at a dynamic interval, OR contents of `loop.md` if present |
| `/loop 20m /review-pr 1234` | Re-runs another packaged slash command on schedule |

Implemented via three tools: `CronCreate` (schedule), `CronList`,
`CronDelete`. Natural language scheduling also works (*"remind me at
3pm to push the release branch"* → one-shot).

## How tasks fire

- Scheduler checks every second; enqueues at low priority.
- Scheduled prompts fire **between turns**, never mid-response.
- Local timezone.
- **Jitter**: recurring tasks fire up to 30 minutes after scheduled
  time (deterministic offset from task ID); one-shot tasks at
  `:00`/`:30` fire up to 90s early.
- **7-day expiry**: recurring tasks auto-expire 7 days after creation.
- **No catch-up**: if Claude is busy past a scheduled time, fires once
  when idle, not once per missed interval.
- Session-scoped; restored on `claude --resume` / `--continue` if not
  yet expired.

## `loop.md` for bare `/loop`

Lookup order: `.claude/loop.md` (project) → `~/.claude/loop.md` (user)
→ built-in maintenance prompt. Plain Markdown, max 25KB. Edits take
effect on the next iteration.

## Stopping

- `Esc` while waiting → clears pending wakeup, loop ends.
- Tasks scheduled via natural language need explicit `CronDelete`.
- `CLAUDE_CODE_DISABLE_CRON=1` disables the scheduler entirely.

## How `/loop` differs from Pi Ralph extensions

| Aspect | Claude Code `/loop` | Pi Ralph extensions |
|---|---|---|
| Trigger | Cron (timed) | Event (`agent_end`) |
| Cadence | Minutes/hours | Immediate, back-to-back |
| Use case | Polling: deployment status, PR babysitting, periodic checks | Tight iteration: build → test → fix → repeat |
| Concurrent loops | Up to 50 per session | One per extension instance (typically) |
| Built-in? | Yes (bundled skill) | No (extension) |
| State persistence | Cron tasks restored on resume | Session entries / external files |
| Mid-iteration steering | N/A (waits for next interval) | Yes (`steer()` queue) in some variants |

They solve different problems. Pi's Ralph is for autonomous coding
campaigns. Claude Code's `/loop` is for monitoring and reactive task
scheduling.

## Could Pi implement `/loop`-style scheduling?

Yes, as an extension, but not yet built. Pi has `pi.on("agent_end", ...)`
but no built-in cron primitive. A `pi-cron` extension could use
`setInterval` / `node-cron`, register `/cron-create`, `/cron-list`,
`/cron-delete` commands, and call `pi.sendUserMessage(prompt)` on cron
tick (only when `ctx.isIdle()`). Persistence across restart would need
`pi.appendEntry` for cron state in the session JSONL. Jitter, expiry,
and missed-fire semantics would have to be re-implemented.

The two layers (timed vs immediate) are complementary, not equivalent.

## See also

- [Loop and Ralph Extensions](loop-extensions.md) — Pi's
  immediate/event-driven loop extensions
