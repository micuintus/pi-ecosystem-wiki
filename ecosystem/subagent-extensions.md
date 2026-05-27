---
title: Pi Subagent Extensions
type: ecosystem
updated: 2026-05-27
sources:
  - pi-subagent-example
  - mjakl-pi-subagent
  - aleclarson-pi-subagent
  - jamwil-pi-subagent
  - espennilsen-pi-subagent
  - nicobailon-pi-subagents
  - tuansondinh-pi-fast-subagent
  - cmf-pi-subagent
  - drsh4dow-pi-delegate
  - noahsaso-my-pi
  - pi-rfc-552
  - obra-superpowers
  - tintinweb-pi-subagents
  - hazat-pi-interactive-subagents
  - ifi-pi-extension-subagents
  - edxeth-pi-subagents
  - masta-g3-pi-tmux-subagents
  - hamdimaz-pi-sub-agent
  - jerryan-pi-subagent-lite
  - tintinweb-pi-subagents-issue-75
tags: [extension, subagent]
entries:
  - id: pi-mono-subagent-example
    name: "pi-mono examples/extensions/subagent"
    repo: earendil-works/pi-mono
    role: subprocess-reference
    notes: "~990 LOC. Reference subprocess-spawn implementation. spawn('pi --mode json -p --no-session'). Re-renders child Message[] inline using Pi's exported components. Single, parallel, chain modes."
  - id: tintinweb-pi-subagents
    name: pi-subagents (tintinweb)
    repo: tintinweb/pi-subagents
    npm: "@tintinweb/pi-subagents"
    version: "0.7.3 (2026-05-14)"
    role: in-process-gold-standard
    notes: "~6,000 LOC. createAgentSession + ConversationViewer modal (live session.subscribe re-render) + agent-tree widget (Braille spinners, live tool activity, token counts) + cross-extension pi.events RPC + .pi/agents/*.md discovery + memory + group-join + steering + worktree. Idiomatic Claude Code tool names: Task, get_subagent_result, steer_subagent — LLM training-known shape. **Known issue:** built-in default agents declare `tools: all` (or omit the field), which silently breaks tool-calling on some models — child reports status:completed, tool_uses:0, no output. See issue #75, fix PR #74 open since 2026-05-14. Workaround: override `~/.pi/agent/agents/general-purpose.md` with an explicit tools list. Note: Hopsken/pi-subagents is a stale private mirror of this package, not a separate project."
  - id: hazat-pi-interactive-subagents
    name: pi-interactive-subagents (HazAT)
    repo: HazAT/pi-interactive-subagents
    npm: pi-interactive-subagents
    role: multiplexer-pane
    notes: "~8,200 LOC (incl. tests). Each subagent runs in its own multiplexer pane (cmux/tmux/zellij/wezterm). Async non-blocking — subagent() returns immediately. Status from child-written runtime snapshots (4 phases: starting/active/waiting/done). caller_ping (child→parent help request). /plan and /iterate workflows. subagent_interrupt for turn-level cancel. The first Pi extension to support true side-by-side parallel inspection."
  - id: edxeth-pi-subagents
    name: pi-subagents (edxeth)
    repo: edxeth/pi-subagents
    npm: pi-subagents
    version: "2.1.0 (2026-05-26)"
    role: mux-plus-subprocess-hybrid
    notes: "~10,622 LOC across 55+ files — the largest subagent runtime in the ecosystem. Forked from HazAT/pi-interactive-subagents then radically diverged. **Hybrid Pattern 4+1**: interactive mode runs each child in a multiplexer pane (cmux/tmux/zellij/wezterm via PI_SUBAGENT_MUX), background mode spawns `pi -p` headless via child_process. Tools: subagent / subagent_resume / subagent_kill / set_tab_title (parent-side); caller_ping / subagent_done / set_tab_title auto-injected into every child. /subagents TUI overlay. **Distinctive**: orchestrator mode (PI_ORCHESTRATOR_MODE=1) replaces system prompt and strips read/bash/edit/write/grep/find from parent, leaving only delegation tools — modeled on Claude Code COORDINATOR_MODE. Ambient awareness (hidden custom message listing available agents + isolation labels). Three session modes (lineage-only / standalone / fork). Rich agent frontmatter: mode, async, cwd, tools, extensions, skills, inject-skills, no-context-files, no-session, auto-exit, system-prompt, session-mode, env, spawning, parent-close-policy, allow-model-override. Skill allowlist + injection. Mixed sync/async batch barrier (race-safe). Token roll-up partner of pi-tasks. Custom snake_case tool namespace — NOT idiomatic Claude Code Task/get_subagent_result/steer_subagent shape."
  - id: masta-g3-pi-tmux-subagents
    name: pi-tmux-subagents (masta-g3)
    repo: masta-g3/pi-tmux-subagents
    npm: pi-tmux-subagents
    role: multiplexer-pane-minimal
    notes: "~1,387 LOC. Pattern 4 (mux pane) but **tmux-only** (no cmux/zellij/wezterm). Single `tmux_subagent` tool with rich action verbs: run / list / get / send / wait / status / stop / cancel. Ships scout (gpt-5.4-mini), worker (gpt-5.5), delegate (inherits parent model). Auto-stops cleanly-completed children to keep tmux/dashboards uncluttered (override with autoStopOnComplete:false). Persistent children support multi-turn follow-up via action:send (pasted into live child) and action:wait with timeoutMs. Numbered turn results under jobs/<id>/turns/. Optional pi-agent-hub integration when PI_AGENT_HUB_DIR is set. Tighter, more opinionated than HazAT's mux runtime."
  - id: hamdimaz-pi-sub-agent
    name: pi-sub-agent (HamdiMaz)
    repo: HamdiMaz/pi-sub-agent
    npm: pi-sub-agent
    version: "0.1.5 (2026-05-18)"
    role: subprocess-with-9-agents
    notes: "~1,537 LOC. Pattern 1 (subprocess+JSON) spawning `pi --mode json -p --no-session`. Single subagent tool with three modes: single / parallel (max 8 tasks, 4 concurrent) / chain (max 8 steps, {previous} placeholder). **Distinctive**: 9 bundled agents (scout, planner, worker, reviewer, debugger, verifier, security-auditor, docs-writer, refactorer) — most of any subprocess option. Per-agent tools allowlist with discovery from user (~/.pi/agent/agents/*.md) and project (.pi/agents/*.md) with explicit confirmation before running project agents. /sub-agent-settings slash command for runtime model/thinking edits. Prompt sent via stdin (not args). Output truncated to Pi defaults (2k lines / 50KB) with full text spilled to temp file. Self-disables `subagent` tool inside children — no recursive nesting."
  - id: jerryan-pi-subagent-lite
    name: pi-subagent-lite (JerryAZR)
    repo: JerryAZR/pi-subagent-lite
    npm: "@jerryan/pi-subagent-lite"
    version: "0.1.4 (2026-04-23)"
    role: subprocess-zero-config
    notes: "245 LOC (single index.ts). Pattern 1 subprocess. Single `subagent` tool with only **two params**: task + skills. **Distinctive**: zero setup. No agent definitions, no .md files, no model param, no cwd param. Specialization mechanism is **pi skills** (passed via --skill flags), not agent personas. Auto-spills tasks >4000 chars to temp file to dodge CLI length limits. Self-unregisters inside children — no recursive nesting. Minimum viable subagent extension if you want delegation without agent-management surface area."
  - id: tintinweb-pi-subagents-issue-75
    name: "tintinweb/pi-subagents issue #75: tools:all silently breaks tool-calling"
    repo: tintinweb/pi-subagents
    role: known-issue
    notes: "Open since 2026-05-15. When an agent definition uses `tools: all` (or omits the field, which is the default for built-in `general-purpose`), the spawned subagent reports status:completed, tool_uses:0, no output. Model is alive but cannot invoke tools — either returns nothing or emits tool calls as raw XML text. PR #74 is the candidate fix (open). Workaround: create `~/.pi/agent/agents/general-purpose.md` overriding the default with explicit tools list."
  - id: nicobailon-pi-subagents
    name: pi-subagents (nicobailon)
    repo: nicobailon/pi-subagents
    npm: pi-subagents
    version: "0.25.0 (2026-05-21)"
    role: subprocess-kitchen-sink
    notes: "~20,500 LOC (+ ~17,800 LOC tests). **Dominant subagent extension by every measurable signal** — 1,581 stars, 232 forks, 24,118 weekly npm downloads, 25 releases, 9+ external contributors including HazAT and tmustier. ~10× the downloads of the next contender. Subprocess-based with truncation, JSONL artifacts, git worktree, true async with result-watcher polling, /run-status slash command. verbose:true mode preserves full transcripts to disk. v0.25.0 added nested subagent fanout. **Known issue #80**: sync subagent returning large results after a long session can crash the parent agent — relevant for evolve-style workflows producing big diffs."
  - id: ifi-pi-extension-subagents
    name: "@ifi/pi-extension-subagents"
    repo: ifiokjr/pi-extension-subagents
    npm: "@ifi/pi-extension-subagents"
    role: tui-overlay
    notes: "Fork of nicobailon adding Agents Manager TUI overlay (Ctrl+Shift+A or /agents) — multi-screen List/Detail/Edit/ChainDetail/ParallelBuilder/TaskInput/NewAgent. Per-agent run history, GitHub Gist export, .chain.md files, multi-select chain/parallel building."
  - id: aleclarson-pi-subagent
    name: pi-subagent (aleclarson)
    repo: aleclarson/pi-subagent
    role: subprocess-minimalist
    notes: "1,786 LOC. spawn (fresh) / fork (session snapshot via --session <jsonl>) modes. No widget. Configurable depth limit. Fork of mjakl/pi-subagent."
  - id: jamwil-pi-subagent
    name: pi-subagent (jamwil)
    repo: jamwil/pi-subagent
    role: subprocess-fork
    notes: "Fork of mjakl/pi-subagent."
  - id: e9n-pi-subagent
    name: "@e9n/pi-subagent"
    repo: espennilsen/pi
    npm: "@e9n/pi-subagent"
    role: subprocess-orchestration
    notes: "5 modes: single, parallel, chain, orchestrator (hierarchical agent trees), pool (long-lived persistent agents). Most workflow-rich subprocess option."
  - id: pi-fast-subagent
    name: pi-fast-subagent
    repo: tuansondinh/pi-fast-subagent
    npm: pi-fast-subagent
    role: in-process-minimal
    notes: "createAgentSession() in same process — no subprocess cold-start, reuses Pi auth/model registry. Single, parallel, background modes."
  - id: noahsaso-interactive-subagents
    name: pi-interactive-subagents (noahsaso)
    repo: noahsaso/my-pi
    role: bundle-multiplexer
    notes: "Multiplexer-pane subagents bundled in noahsaso's Pi collection. Distinct from HazAT despite the similar name."
  - id: elpapi42-pi-minimal-subagent
    name: pi-minimal-subagent
    repo: elpapi42/pi-minimal-subagent
    role: subprocess-minimalist
    notes: "1,144 LOC. One tool. Env-injection escape hatch for env-configured extensions. Tri-state extensions config (null/[]/whitelist)."
  - id: pi-delegate
    name: pi-delegate
    repo: drsh4dow/pi-delegate
    npm: pi-delegate
    role: minimal
    notes: "~150 LOC. One delegate tool. Fresh child, runs task, returns result. 'Small by design.'"
  - id: cmf-pi-subagent
    name: "@cmf/pi-subagent"
    repo: cmf/pi-subagent
    npm: "@cmf/pi-subagent"
    role: experimental
    notes: "1,331 LOC. Single-commit experiment (2026-01-08), 0 stars, 0 forks, never published to npm. Pattern reference (recursive step composition, tree progress UI) — not a production dependency target. RFC #552 explores extracting subagent execution into a library; this is the closest existing prototype."
---

# Pi Subagent Extensions

## Contents

- [The four architectural patterns](#the-four-architectural-patterns)
- [Cross-pattern comparison](#cross-pattern-comparison)
- [Idiomatic LLM-known tool shapes](#idiomatic-llm-known-tool-shapes)
- [ConversationViewer](#conversationviewer-tintinwebhopsken-capabilities-and-limits)
- [Comparison with other agents](#comparison-with-other-agents)
- [Picking a subagent extension](#picking-a-subagent-extension)
- [Caveats](#caveats)
- [See also](#see-also)

Pi extensions that delegate tasks to child agents with isolated
context windows. Pattern: parent calls a `delegate` / `subagent` /
`Task` tool → child agent runs the task → result returns to parent
without polluting the parent's context.

**Short answer for most readers:** `nicobailon/pi-subagents` is the
dominant choice by raw popularity — ~10× the weekly downloads of the
next contender, 4× the stars, 9+ external contributors. Use it if you
want the most-adopted subprocess option with worktree, JSONL artifacts,
async polling, and a steady release cadence. `tintinweb/pi-subagents`
remains the polished in-process option with idiomatic Claude Code tool
names (`Task`, `get_subagent_result`, `steer_subagent`), at the cost
of less process isolation and a known tool-calling bug (issue #75).
`HazAT/pi-interactive-subagents` if you want each child in its own
visible terminal pane. Everything below maps the 4 architectural
patterns and 16+ extensions onto specific goals.

There is no built-in subagent in Pi (unlike Claude Code's `Task` tool
or opencode2's first-class `subtask` part type). The community has
filled the gap with **four distinct architectural patterns** spread
across 12+ extensions.
[RFC #552](https://github.com/earendil-works/pi-mono/issues/552) tracks
discussion of extracting subagent execution into a reusable library.

## The four architectural patterns

Capabilities (parallel, chain, orchestrator, pool) are orthogonal —
most patterns can support most capabilities. What changes between
patterns is **where the child runs, how the parent observes it, and
how output flows back**.

| Pattern | Where child runs | Parent observes via | Used by |
|---|---|---|---|
| **1. Subprocess + JSON event stream** | `spawn('pi --mode json -p')` | parse stdout `Message[]` events | in-tree reference, aleclarson, jamwil, elpapi42, e9n, nicobailon, @ifi, drsh4dow, HamdiMaz, jerryan-lite |
| **2. Subprocess + RPC over stdin/stdout** | `spawn('pi --mode rpc')` | JSON-RPC notifications + bidirectional commands | (no generic subagent extension; only ralph drivers like `lnilluv/pi-ralph-loop`) |
| **3. In-process via `createAgentSession` SDK** | same process, separate session | direct `session.subscribe(...)` callback | tintinweb/pi-subagents, tuansondinh/pi-fast-subagent |
| **4. Multiplexer pane per subagent** | each child = own cmux/tmux/zellij/wezterm pane | child-written runtime snapshot file + the pane itself | HazAT/pi-interactive-subagents, noahsaso (in `my-pi`), masta-g3 (tmux-only) |
| **4+1 hybrid** | mux pane for interactive, headless `pi -p` for background | both | **edxeth/pi-subagents** |

### Pattern 1 — Subprocess + line-delimited JSON event stream

```ts
const proc = spawn("pi", [
  "--mode", "json", "-p", task,
  "--no-session",  // or --session <jsonl-path> to inherit parent context
], { cwd, stdio: ["ignore", "pipe", "pipe"] });

proc.stdout.on("data", chunk => {
  for (const line of buffer.split("\n")) {
    const event = JSON.parse(line);
    if (event.type === "message_end") messages.push(event.message);
    if (event.type === "tool_result_end") toolResults.set(event.id, event.result);
  }
});
await once(proc, "exit");
return { messages, finalOutput, usage, exitCode };
```

**Wins:** full process isolation (crashes contained), clean context
separation by default, optional context inheritance via
`--session <jsonl>`, re-renderable transcripts, cheap parallelism.

**Trades:** ~200–500ms spawn cost per child; no mid-flight steering
(SIGTERM only); result is a *log* not a *living view*; tool registration
in child is whatever the child's pi config does.

**Best for:** stateless one-shot delegations, parallel fan-out,
hard isolation guarantees.

### Pattern 2 — Subprocess + JSON-RPC

`pi --mode rpc` exposes a bidirectional RPC channel for `session.start`,
`session.steer`, `session.abort`, `turn_end`/`message_update`/`tool_*`
notifications. Long-lived child amortizes spawn cost across many
turns. ~5× the LOC of Pattern 1 because of RPC framing, request
correlation, notification dispatch, timeout handling. Coupling to Pi's
RPC schema adds semver risk.

No generic subagent extension uses this pattern today —
`lnilluv/pi-ralph-loop` uses it for steerable ralph loops. Pattern 1
covers most one-shot needs more cheaply; Pattern 3 covers steering
needs in-process with zero subprocess overhead.

### Pattern 3 — In-process via `createAgentSession` SDK

```ts
import { createAgentSession, SessionManager, SettingsManager } from "@earendil-works/pi-coding-agent";

const { session } = await createAgentSession({
  cwd,
  sessionManager: SessionManager.inMemory(cwd),
  settingsManager: SettingsManager.create(),
  modelRegistry: ctx.modelRegistry,   // share parent's auth + cache
  model: "claude-opus-4-7",
  tools: parentTools,
});
session.setActiveToolsByName(["bash", "read", "edit"]);
await session.bindExtensions({ onError: (err) => log(err) });

session.subscribe(event => {
  if (event.type === "turn_end") onComplete(event);
  if (event.type === "message_update") render(event);
});
await session.sendMessage({ content: task, triggerTurn: true });

session.steer("Wrap up immediately");   // direct method call
session.abort();
```

**Wins:** zero subprocess overhead, full event subscription matching
Pi's own InteractiveMode, direct steering and abort, shared
`ModelRegistry` (no re-login per child), the richest UI surface
(Hopsken's `ConversationViewer` and agent-tree widget are only viable
in this pattern).

**Trades:** no process isolation (child crash takes parent down),
memory accumulation in long-running parents, tool conflicts unless
filtered, **highest SDK semver risk** — `createAgentSession` is the
most internals-exposing surface and not yet documented as semver-stable.

**Best for:** live oversight where the user actively watches and
steers; frequent short tasks where spawn cost would dominate; shared
auth/quota.

### Pattern 4 — Multiplexer pane per subagent

```ts
const mux: MuxBackend = detectMux();   // cmux | tmux | zellij | wezterm | none
const paneId = await mux.createPane({
  command: ["pi", "-p", task, "--session", sessionPath],
  title: `subagent: ${name}`,
  splitDirection: "right",
});

// Child writes runtime state file: { phase: "starting"|"active"|"waiting"|"done", ... }
// Parent polls + correlates to widget. Result steered back via deliverAs:"followUp".
```

**Wins:** each subagent is a real, full Pi session in a real terminal
pane — full TUI, full transcript, **fully interactive (you can type
into the child)**. **True parallel inspection** via mux split — N
children visible simultaneously. No truncation anywhere. Async
non-blocking by default. Native multiplexer keybinds the user already
knows.

**Trades:** hard dependency on a multiplexer (degrades without one),
pane lifecycle is the user's problem, no automatic re-rendering inside
parent's TUI (status widget shows phase, content lives in the other
pane), each child is still a separate `pi` subprocess.

**Best for:** multi-candidate comparison, users who already live in
cmux/tmux, when children need full interactivity for steering.

## Cross-pattern comparison

| Dimension | Pattern 1 (subprocess+JSON) | Pattern 2 (subprocess+RPC) | Pattern 3 (in-process) | Pattern 4 (mux pane) |
|---|---|---|---|---|
| Spawn cost | ~200–500ms | ~200–500ms | ~0 | ~200–500ms + mux pane |
| Process isolation | full | full | none | full |
| Mid-run steer/abort | no (SIGTERM only) | yes (RPC) | yes (method call) | yes (write to pane) |
| Live event stream | poll stdout | RPC notifications | `session.subscribe` | runtime snapshot file + pane |
| **Parallel inspection** | no | no | no (modal) | **yes (mux split)** |
| **User-interactive child** | no | no | no | **yes** |
| Tool result truncation in viewer | extension's choice | extension's choice | tintinweb truncates 500ch | none (real pane) |
| LOC for minimum viable | ~150 | ~1,300 | ~3,000 | ~5,000 |
| LOC for production-grade | ~20,000 (nicobailon) | n/a | ~6,000 (tintinweb) | ~8,200 (HazAT) |
| SDK semver risk | low | medium | **high** | low |

## Adoption signals (2026-05-27)

Hard popularity and activity data across the major subagent extensions.
Numbers pulled from GitHub and npm APIs on 2026-05-27. The picture is
lopsided: nicobailon dominates raw adoption by an order of magnitude,
but several mid-tier options are healthy production choices for
specific use cases.

| Extension | Stars | Forks | Open issues | npm wk dl | Releases | Latest | Last push |
|---|---:|---:|---:|---:|---:|---|---|
| **`nicobailon/pi-subagents`** | **1,581** | **232** | **65** | **24,118** | 25 | v0.25.0 | 2026-05-21 |
| `HazAT/pi-interactive-subagents` | 483 | 85 | 17 | n/a (not on npm) | — | — | 2026-05-12 |
| `tintinweb/pi-subagents` | 380 | 74 | 17 | 2,555 | 11 | v0.7.3 | 2026-05-26 |
| `mjakl/pi-subagent` | 47 | 12 | 0 | 340 | 10 | v1.4.1 | 2026-05-22 |
| `edxeth/pi-subagents` | 28 | 3 | 1 | shares `pi-subagents` slug | 2 | v2.1.0 | 2026-05-26 |
| `tuansondinh/pi-fast-subagent` | 15 | 5 | 1 | 56 | — | v0.9.3 | 2026-04-28 |
| `drsh4dow/pi-delegate` | 2 | 1 | 0 | 468 | — | — | 2026-05-23 |
| `HamdiMaz/pi-sub-agent` | 0 | 0 | 0 | 103 | — | v0.1.5 | 2026-05-18 |
| `masta-g3/pi-tmux-subagents` | 0 | 0 | 0 | 12 | — | — | 2026-05-24 |
| `JerryAZR/pi-subagent-lite` | 1 | 0 | 0 | 153 | — | v0.1.4 | 2026-04-16 |
| `aleclarson/pi-subagent` | 0 | 0 | 0 | n/a | — | — | 2026-03-03 |

### Observations

- **nicobailon dominates adoption by ~10×**: 24,118 weekly downloads
  vs 2,555 for tintinweb (second-place on npm) and 468 for pi-delegate.
  Star count is ~4× next-largest. Forks ~3×.
- **Cross-pollination signals maturity**: HazAT (author of
  pi-interactive-subagents) and tmustier (author of multiple loop
  extensions) both contribute commits to nicobailon — ecosystem leaders
  treat it as the canonical subprocess option. Tintinweb's contributor
  graph is much flatter (one author, others ≤2 commits each).
- **High open-issue counts mean active triage, not neglect** — 65 open
  issues on nicobailon is the signature of an extension lots of people
  actually run. Compare to repos with 0 open issues that simply have
  no users.
- **Release cadence**: nicobailon ships ~25 tagged releases vs
  tintinweb's 11; both push to main frequently.
- **Slug collision warning**: nicobailon and edxeth both publish to
  `pi-subagents` on npm. Disambiguate by repo URL when installing.
  HazAT's `pi-interactive-subagents` is not on npm at all — install
  via git URL.

### Picking from this table

| If you want… | Pick |
|---|---|
| Battle-tested default with the most users | **nicobailon** (subprocess, no live UI) |
| Live in-process inspection with Claude-Code tool names | **tintinweb** (mind issue #75) |
| Side-by-side parallel panes | **HazAT** (mux, requires cmux/tmux/zellij/wezterm) |
| Smallest viable subprocess | **drsh4dow/pi-delegate** or **JerryAZR/pi-subagent-lite** |
| Opinionated multi-agent runtime with orchestrator mode | **edxeth** (Pattern 4+1 hybrid, ~10.6k LOC) |

## Idiomatic LLM-known tool shapes

Same principle as TODO extensions: matching a training-known tool
shape lets the LLM use the extension correctly with zero
system-prompt fine-tuning.

| Shape | Origin | Pi extension that mirrors it |
|---|---|---|
| `Task`, `get_subagent_result`, `steer_subagent` | Claude Code | **`tintinweb/pi-subagents`** — verbatim |
| Custom (`delegate`, `subagent`, `spawn`, etc.) | bespoke | most others |

This is one reason `tintinweb/pi-subagents` punches above its star
count for production use — Anthropic-tuned models hit it with strong
priors out of the box.

## Inspection: nicobailon artifacts vs tintinweb ConversationViewer

The two extensions take opposite approaches to inspecting child runs.
`tintinweb/pi-subagents` puts everything in a live modal viewer with
in-memory truncation; `nicobailon/pi-subagents` writes everything to
disk and lets you `status`/`interrupt`/`resume` against persistent
artifacts. The choice is between *live show* and *post-mortem replay*.

### nicobailon inspection surface

Live:
- Compact async widget in parent TUI — per-agent progress, parallel
  groups stay grouped, nested children render as a tree
- `subagent({ action: "status" })` lists active runs;
  `action: "status", id: "..."` drills into one (resolves exact ids,
  top-level async, nested, then prefix-match)
- Foreground runs stream directly into the conversation
- Completion notifications for background runs
- Stall detection with next-action suggestions

On disk — `{sessionDir}/subagent-artifacts/<run-id>/`:

| File | Content |
|---|---|
| `status.json` | Powers the widget and `status` action |
| `events.jsonl` | **Full Pi JSON event stream** (message_end, tool_call, tool_result_end, …) annotated with run/step metadata. Replayable. |
| `output-<n>.log` | Live human-readable tail per step |
| chain dir | Per-step pinned outputs (`output=context.md` style) |
| patch files | Full diffs from worktree parallel steps |

Mid-flight control:
- `action: "interrupt"` aborts a running child (nested too)
- `action: "resume"` restarts a paused/interrupted run
- `action: "doctor"` for read-only setup diagnostics
- Optional `pi-intercom` companion lets the child call
  `contact_supervisor` for blocking decisions or progress updates —
  true bidirectional steering

### Side-by-side comparison

| Feature | nicobailon | tintinweb ConversationViewer |
|---|---|---|
| Live tool calls visible | yes (widget + foreground stream) | yes (modal `session.subscribe`) |
| Modal full-transcript view | no (uses log files) | yes (k/j/PgUp/PgDn nav) |
| Tool result truncation | **none** (full `events.jsonl` on disk) | 500 chars in modal |
| Bash output truncation | **none** | 500 chars in modal |
| Post-mortem after session ends | **yes** (persistent files) | no (modal closes, no replay) |
| Side-by-side parallel inspection | partial (widget tree) | no (one agent, modal-blocking) |
| Mid-flight steering | `interrupt` + intercom `contact_supervisor` | none from viewer |

For long-running pipelines and evolve-style workflows where the value
is in *post-hoc auditing*, nicobailon's `events.jsonl` wins decisively.
For live coaching/oversight where you actively watch the child unfold,
tintinweb's modal is more immediate.

## ConversationViewer (tintinweb/Hopsken) — capabilities and limits

The `tintinweb/pi-subagents` modal viewer is the most polished
in-process inspection UI in the ecosystem. Verified by reading the
source on 2026-05-08:

| What it does | What it doesn't do |
|---|---|
| Modal overlay (`ctx.ui.custom`) with own keyboard handling | No keybind switch between agents (Esc → re-open via `/agents`) |
| Live updates via `session.subscribe(() => tui.requestRender())` | Modal blocks parent view — can't see parent agent while open |
| Full message log scroll (k/j/PgUp/PgDn/Home/End) | **Tool results truncated to 500 chars** |
| Streaming indicator at bottom (`▍ describeActivity(...)`) | **Bash output truncated to 500 chars** |
| Header with status icon, duration, token count, tool count | Read-only — can't type, inject, steer from viewer |
| ANSI-aware width adaptation (`wrapTextWithAnsi`) | One agent at a time — no side-by-side comparison |

The 500-char truncation is the practical reason to reach for
`HazAT/pi-interactive-subagents` (full pane, no truncation) or
`nicobailon/pi-subagents` (`verbose:true` mode preserves full JSONL
transcripts to disk) for evolve-grade post-mortem inspection.

## Comparison with other agents

- **Claude Code** ships a built-in `Task` tool with a `subagent_type`
  parameter. Provider-side dispatch.
- **opencode2** has `subtask` as a first-class message part type
  handled in `runLoop()` itself. Post-PR #14814 it cycles between
  full-screen sessions via `<leader>+down` / arrows, but **has no
  tabs/panes** ([open FR](https://github.com/anomalyco/opencode/issues/5826)).
- **Pi** delegates this to extensions, which is why the variant
  landscape exists at all. For parallel inspection,
  `HazAT/pi-interactive-subagents` is **strictly more capable than
  opencode** — multiplexer split puts N candidates on screen
  simultaneously where opencode forces full-screen cycling.

## Picking a subagent extension

Updated 2026-05-27 with the four new entries.

| Goal | Best choice | Why |
|---|---|---|
| **Default in-process delegation** (idiomatic, Claude Code-tuned) | **`tintinweb/pi-subagents`** | 271 stars, 27 releases, 8 contributors. Idiomatic `Task`/`get_subagent_result`/`steer_subagent` tool names. Live ConversationViewer. Cross-extension RPC. |
| **Side-by-side parallel inspection** (compare N candidates live) | **`HazAT/pi-interactive-subagents`** | The only Pi extension that supports true parallel inspection. Requires user already in cmux/tmux/zellij/wezterm. |
| **Default subprocess option, most-adopted, most-active** | **`nicobailon/pi-subagents`** | **1,581 stars, 24k weekly downloads, 25 releases, 9+ external contributors (incl. HazAT and tmustier from other ecosystem packages)**. Subprocess kitchen-sink with worktree, JSONL artifacts, async polling, nested fanout (v0.25). Default recommendation for production workloads unless you specifically need in-process steering or interactive panes. |
| **TUI overlay for browse/edit/launch** | `@ifi/pi-extension-subagents` | nicobailon fork with Agents Manager multi-screen UI. |
| **Hierarchical agent trees, pools** | `@e9n/pi-subagent` | Five modes: single, parallel, chain, orchestrator, pool. |
| **In-process, minimal** | `tuansondinh/pi-fast-subagent` | `createAgentSession` only, no extra UI. |
| **Subprocess, minimal** | `aleclarson/pi-subagent` or `drsh4dow/pi-delegate` | Smallest production options. aleclarson's spawn/fork modes are useful. |
| **Reference for building your own** | `pi-mono/examples/extensions/subagent` | Re-renders child Message[] inline using Pi's exported components. |
| **Skill complement** (when/how to spawn, not the mechanism) | `obra/superpowers` | Cross-agent skills `subagent-driven-development`, `dispatching-parallel-agents`, `executing-plans`. Compatible with whichever extension is installed. |
| **Opinionated multi-agent runtime** (orchestrator mode, ambient awareness, mux+background hybrid) | **`edxeth/pi-subagents`** | 10k LOC. Hybrid Pattern 4+1. Orchestrator mode strips parent's edit tools so it can only delegate. Skill injection, three session modes, rich frontmatter. Closest thing to a production multi-agent framework on Pi. Pairs with edxeth/pi-tasks for token accounting. |
| **tmux-only mux** (simpler than HazAT if you only use tmux) | **`masta-g3/pi-tmux-subagents`** | ~1.4k LOC. Single `tmux_subagent` tool with run/send/wait/status verbs. Auto-stops cleanly-completed children. Multi-turn follow-up via action:send. Optional pi-agent-hub integration. |
| **Subprocess with bundled experts** (scout/planner/worker/reviewer/debugger/verifier/security-auditor/docs-writer/refactorer) | **`HamdiMaz/pi-sub-agent`** | ~1.5k LOC. Pattern 1. Most bundled agents of any subprocess option. Confirmation gate for project agents. /sub-agent-settings for runtime model edits. |
| **Zero-config minimum-viable subagent** (skills instead of agent files) | **`@jerryan/pi-subagent-lite`** | 245 LOC. Single `subagent` tool, only `task` + `skills` params. No agent .md files anywhere. Specialization via pi skills. Auto-spills long tasks. Smallest production option that's still useful. |

## Caveats

- **`Hopsken/pi-subagents` is a stale private mirror of
  `@tintinweb/pi-subagents`**, not a separate project. Earlier
  community comparisons treating them as two packages were
  conflating versions.
- **`@cmf/pi-subagent` is experimental, not production** —
  single-commit, never published to npm. The recursive step
  composition pattern is interesting as a reference but not a
  dependency target.
- `noahsaso/pi-interactive-subagents` (in the `my-pi` collection)
  shares a name with HazAT's package but is a different
  implementation. Confirm which one you're installing.
- **`tintinweb/pi-subagents` issue #75 (open since 2026-05-15)** —
  the built-in `general-purpose` agent declares `tools: all` (no
  explicit list), which silently breaks tool-calling on some models.
  Child reports `status: completed`, `tool_uses: 0`, no output. PR #74
  is the candidate fix (open). Until merged, override
  `~/.pi/agent/agents/general-purpose.md` with an explicit tools list:

  ```yaml
  ---
  description: General-purpose agent for complex, multi-step tasks
  display_name: Agent
  tools: read, bash, edit, write, grep, find, ls
  prompt_mode: append
  ---
  ```

  Confirmed in the wild: in-session hangs at 0 tool uses, plus a
  separate failure mode at ~20 tool retries in <5% context (the same
  bug expressed against partially-trained model behavior).
- **edxeth/pi-subagents NPM name collides** with `nicobailon/pi-subagents`
  on the bare `pi-subagents` slug. Disambiguate by repo when installing.
  HamdiMaz/pi-sub-agent uses the singular `pi-sub-agent` and does not collide.

## See also

- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes for picking among these
- [Loop and Ralph Extensions](loop-extensions.md) — companion survey; loop drivers often use subagents
- [TODO List Extensions](todo-extensions.md) — companion survey
