---
title: Pi Subagent Extensions
type: ecosystem
updated: 2026-05-10
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
    role: in-process-gold-standard
    notes: "~6,000 LOC. createAgentSession + ConversationViewer modal (live session.subscribe re-render) + agent-tree widget (Braille spinners, live tool activity, token counts) + cross-extension pi.events RPC + .pi/agents/*.md discovery + memory + group-join + steering + worktree. Idiomatic Claude Code tool names: Task, get_subagent_result, steer_subagent — LLM training-known shape. Note: Hopsken/pi-subagents is a stale private mirror of this package, not a separate project."
  - id: hazat-pi-interactive-subagents
    name: pi-interactive-subagents (HazAT)
    repo: HazAT/pi-interactive-subagents
    npm: pi-interactive-subagents
    role: multiplexer-pane
    notes: "~8,200 LOC (incl. tests). Each subagent runs in its own multiplexer pane (cmux/tmux/zellij/wezterm). Async non-blocking — subagent() returns immediately. Status from child-written runtime snapshots (4 phases: starting/active/waiting/done). caller_ping (child→parent help request). /plan and /iterate workflows. subagent_interrupt for turn-level cancel. The only Pi extension that supports true side-by-side parallel inspection."
  - id: nicobailon-pi-subagents
    name: pi-subagents (nicobailon)
    repo: nicobailon/pi-subagents
    npm: pi-subagents
    role: subprocess-kitchen-sink
    notes: "~20,500 LOC (+ ~17,800 LOC tests). Most popular subagent extension. Subprocess-based with truncation, JSONL artifacts, git worktree, true async with result-watcher polling, /run-status slash command. verbose:true mode preserves full transcripts to disk."
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

Pi extensions that delegate tasks to child agents with isolated
context windows. Pattern: parent calls a `delegate` / `subagent` /
`Task` tool → child agent runs the task → result returns to parent
without polluting the parent's context.

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
| **1. Subprocess + JSON event stream** | `spawn('pi --mode json -p')` | parse stdout `Message[]` events | in-tree reference, aleclarson, jamwil, elpapi42, e9n, nicobailon, @ifi, drsh4dow |
| **2. Subprocess + RPC over stdin/stdout** | `spawn('pi --mode rpc')` | JSON-RPC notifications + bidirectional commands | (no generic subagent extension; only ralph drivers like `lnilluv/pi-ralph-loop`) |
| **3. In-process via `createAgentSession` SDK** | same process, separate session | direct `session.subscribe(...)` callback | tintinweb/pi-subagents, tuansondinh/pi-fast-subagent |
| **4. Multiplexer pane per subagent** | each child = own cmux/tmux/zellij/wezterm pane | child-written runtime snapshot file + the pane itself | HazAT/pi-interactive-subagents, noahsaso (in `my-pi`) |

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

| Goal | Best choice | Why |
|---|---|---|
| **Default in-process delegation** (idiomatic, Claude Code-tuned) | **`tintinweb/pi-subagents`** | 271 stars, 27 releases, 8 contributors. Idiomatic `Task`/`get_subagent_result`/`steer_subagent` tool names. Live ConversationViewer. Cross-extension RPC. |
| **Side-by-side parallel inspection** (compare N candidates live) | **`HazAT/pi-interactive-subagents`** | The only Pi extension that supports true parallel inspection. Requires user already in cmux/tmux/zellij/wezterm. |
| **Heavy async pipelines, JSONL artifacts, worktrees** | `nicobailon/pi-subagents` | 1.3k stars, the popular kitchen-sink. `verbose:true` preserves full transcripts. |
| **TUI overlay for browse/edit/launch** | `@ifi/pi-extension-subagents` | nicobailon fork with Agents Manager multi-screen UI. |
| **Hierarchical agent trees, pools** | `@e9n/pi-subagent` | Five modes: single, parallel, chain, orchestrator, pool. |
| **In-process, minimal** | `tuansondinh/pi-fast-subagent` | `createAgentSession` only, no extra UI. |
| **Subprocess, minimal** | `aleclarson/pi-subagent` or `drsh4dow/pi-delegate` | Smallest production options. aleclarson's spawn/fork modes are useful. |
| **Reference for building your own** | `pi-mono/examples/extensions/subagent` | Re-renders child Message[] inline using Pi's exported components. |
| **Skill complement** (when/how to spawn, not the mechanism) | `obra/superpowers` | Cross-agent skills `subagent-driven-development`, `dispatching-parallel-agents`, `executing-plans`. Compatible with whichever extension is installed. |

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

## See also

- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes for picking among these
- [Loop and Ralph Extensions](loop-extensions.md) — companion survey; loop drivers often use subagents
- [TODO List Extensions](todo-extensions.md) — companion survey
