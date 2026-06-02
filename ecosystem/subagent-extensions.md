---
title: Pi Subagent Extensions
type: ecosystem
updated: 2026-05-31
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
  - tintinweb-pi-subagents-pr-74
  - hazat-pi-interactive-subagents
  - ifi-pi-extension-subagents
  - edxeth-pi-subagents
  - masta-g3-pi-tmux-subagents
  - hamdimaz-pi-sub-agent
  - jerryan-pi-subagent-lite
  - ross-jill-ws-pi-subagent-in-memory
  - tmustier-pi-agent-teams
  - melihmucuk-pi-crew
  - tiziano-pi-multiagent
  - messense-pi-parallel-agents
  - gotgenes-pi-subagents
  - amosblomqvist-pi-subagents
tags: [extension, subagent, multiagent, orchestration]
entries:
  - id: nicobailon-pi-subagents
    name: pi-subagents (nicobailon)
    repo: nicobailon/pi-subagents
    npm: pi-subagents
    role: subprocess-default
    notes: "The dominant subagent extension by every adoption signal (downloads, stars, forks, external contributors including HazAT and tmustier) — roughly an order of magnitude ahead of the next contender. Pattern 1 (subprocess + JSON event stream). Each child runs as a real `pi --mode json -p --session <file>` process, so per-child session files are **genuine resumable Pi sessions** (`pi --session <file>`) — not just a log — alongside captured `events.jsonl` artifacts. Worktree isolation, true async with result-watcher polling, /run-status, nested fanout. `verbose:true` raises transcript verbosity. ~20k LOC src (+ ~18k tests) — the kitchen-sink option. Default for production unless you specifically need in-process steering, interactive panes, or a smaller surface."
  - id: tintinweb-pi-subagents
    name: pi-subagents (tintinweb)
    repo: tintinweb/pi-subagents
    npm: "@tintinweb/pi-subagents"
    role: in-process-claude-code-shape
    notes: "~7k LOC. Pattern 3 (in-process `createAgentSession` with `SessionManager.inMemory` — children are **not** persisted as resumable Pi sessions). Registers `Agent` / `get_subagent_result` / `steer_subagent` (a Claude-Code-*styled* async trio, not Claude Code's verbatim `Task` tool). Live ConversationViewer modal (`session.subscribe` re-render), an agent-tree widget, cross-extension `pi.events` RPC (`subagents:rpc:*`), `.pi/agents/*.md` discovery, memory, group-join, steering, worktree. The `tools: all` tool-calling bug (issue #75) is **fixed** — PR #74 merged, shipped from v0.8 (current line v0.10+); the fix was a breaking change to agent-definition tool/extension selectors (`extensions:`/`ext:`), so re-check agent files after upgrading. Inspection caveat: the modal truncates tool/bash output to 500 chars and has no post-mortem replay once closed."
  - id: hazat-pi-interactive-subagents
    name: pi-interactive-subagents (HazAT)
    repo: HazAT/pi-interactive-subagents
    role: mux-pane-full-view
    notes: "~5k LOC. Pattern 4 (multiplexer pane). Each subagent runs as a real, full Pi session in its own cmux/tmux/zellij/wezterm pane — full TUI, full transcript, no truncation, fully interactive (you can type into the child). The canonical **full-view** option. `subagent()` returns immediately (async, non-blocking); a live widget shows per-agent phase (starting/active/waiting/stalled), results steered back into the parent as async notifications. caller_ping (child→parent help), /plan and /iterate, subagent_interrupt. The first Pi extension with true side-by-side parallel inspection. Not on npm — install by git URL."
  - id: ross-jill-ws-pi-subagent-in-memory
    name: pi-subagent-in-memory (ross-jill-ws)
    repo: ross-jill-ws/pi-subagent-in-memory
    npm: pi-subagent-in-memory
    role: in-process-persona-free-logged
    notes: "Compact, zero-dependency Pattern 3 (in-process `createAgentSession`). Design principle: **adds nothing to the LLM context beyond the tool schema** — no system-prompt injection, no agent personas, no `.md` profiles. One tool, `subagent_create`. Full **`events.jsonl` + `result.md` per subagent** under `.pi/subagent-in-memory/<session>/subagent_N/` (no truncation, post-mortem replayable), plus live card widgets and a `Ctrl+N` detail overlay; `/saim-toggle-overlay off` or `--saim-no-tui` runs silently for headless fanout. Nested subagents supported. The cleanest match for full inspection without personas; in-process so no isolation (a child crash can take the parent down) and the usual `createAgentSession` semver risk."
  - id: tuansondinh-pi-fast-subagent
    name: pi-fast-subagent
    repo: tuansondinh/pi-fast-subagent
    npm: pi-fast-subagent
    role: in-process-lean-fanout
    notes: "Pattern 3 (in-process). single / parallel / background modes with poll+cancel, per-call model override, user+project agent discovery, max-depth guard, streamed prompt preview, chronological expanded view (Ctrl+O). Bundles only two light agents (`scout`, `general`). Tool: `subagent`. The lean in-process option for many short tasks where subprocess cold-start would dominate."
  - id: masta-g3-pi-tmux-subagents
    name: pi-tmux-subagents (masta-g3)
    repo: masta-g3/pi-tmux-subagents
    npm: pi-tmux-subagents
    role: mux-pane-tmux-only
    notes: "~1.4k LOC. Pattern 4 but **tmux-only** (no cmux/zellij/wezterm). Single `tmux_subagent` tool with action verbs run/list/get/send/wait/status/stop/cancel. Persistent children support multi-turn follow-up (action:send into the live child); numbered turn results under jobs/<id>/turns/ — a lighter, tmux-native full-view option than HazAT. Auto-stops cleanly-completed children. Ships scout/worker/delegate agents."
  - id: edxeth-pi-subagents
    name: pi-subagents (edxeth)
    repo: edxeth/pi-subagents
    npm: pi-subagents
    role: mux-plus-subprocess-hybrid
    notes: "~10k LOC across 55+ files — the largest single-runtime option. Hybrid **Pattern 4+1**: interactive children in a multiplexer pane, background children as headless `pi -p`. Orchestrator mode (PI_ORCHESTRATOR_MODE=1) strips read/bash/edit/write from the parent so it can only delegate (modeled on Claude Code COORDINATOR_MODE). Ambient awareness, three session modes (lineage/standalone/fork), rich agent frontmatter, skill allowlist+injection. Custom snake_case tool namespace — not the idiomatic Claude Code shape. NPM slug collides with nicobailon's `pi-subagents`; disambiguate by repo."
  - id: hamdimaz-pi-sub-agent
    name: pi-sub-agent (HamdiMaz)
    repo: HamdiMaz/pi-sub-agent
    npm: pi-sub-agent
    role: subprocess-bundled-experts
    notes: "~1.5k LOC. Pattern 1. single / parallel (max 8, 4 concurrent) / chain modes. Bundles 9 expert agents (scout, planner, worker, reviewer, debugger, verifier, security-auditor, docs-writer, refactorer) — most of any subprocess option. Per-agent tools allowlist, confirmation gate for project agents, /sub-agent-settings. Self-disables nesting. Uses singular `pi-sub-agent` slug (no collision)."
  - id: jerryan-pi-subagent-lite
    name: pi-subagent-lite (JerryAZR)
    repo: JerryAZR/pi-subagent-lite
    npm: "@jerryan/pi-subagent-lite"
    role: subprocess-zero-config
    notes: "~245 LOC single file. Pattern 1. One `subagent` tool with two params: task + skills. **No agent .md files, no personas** — specialization is via Pi skills passed as --skill flags. Auto-spills long tasks to temp. Self-unregisters inside children. The minimum-viable subprocess option that is still useful."
  - id: amosblomqvist-pi-subagents
    name: pi-subagents (amosblomqvist)
    repo: amosblomqvist/pi-subagents
    role: subprocess-minimal-popular
    notes: "'Minimal Subagents' — Pattern 1 subprocess registering a single `subagent` tool with a few small bundled agents (scout/haiku for recon, researcher/sonnet for web, plus a worker). Notably well-adopted for its size (one of the most-starred subagent extensions despite a tiny surface) — a compact alternative to nicobailon when you don't need worktrees/async artifacts. Registers the bare `subagent` tool (collides with other `subagent`-named extensions)."
  - id: e9n-pi-subagent
    name: "@e9n/pi-subagent"
    repo: espennilsen/pi
    npm: "@e9n/pi-subagent"
    role: subprocess-orchestration
    notes: "Pattern 1. Five modes: single, parallel, chain, orchestrator (hierarchical trees), pool (long-lived persistent agents). The most workflow-rich subprocess option."
  - id: aleclarson-pi-subagent
    name: pi-subagent (aleclarson)
    repo: aleclarson/pi-subagent
    role: subprocess-spawn-or-fork
    notes: "~1.8k LOC. spawn (fresh child) / fork (child seeded with a snapshot of the current session via `--session <jsonl>`) modes. Configurable depth limit, no widget. Fork of mjakl/pi-subagent. (The `--session` snapshot feeds parent context *in*; the child's own session persistence is not confirmed.)"
  - id: mjakl-pi-subagent
    name: pi-subagent (mjakl)
    repo: mjakl/pi-subagent
    npm: "@mjakl/pi-subagent"
    role: subprocess-lightweight
    notes: "Lightweight Pattern 1 subagent; the upstream that aleclarson/jamwil forked. Delegate tasks to specialized agents."
  - id: elpapi42-pi-minimal-subagent
    name: pi-minimal-subagent
    repo: elpapi42/pi-minimal-subagent
    role: subprocess-minimalist
    notes: "~1.1k LOC. One tool. Env-injection escape hatch for env-configured extensions. Tri-state extensions config (null/[]/whitelist)."
  - id: pi-delegate
    name: pi-delegate
    repo: drsh4dow/pi-delegate
    npm: pi-delegate
    role: subprocess-minimal
    notes: "~150 LOC. One `delegate` tool. Fresh child, runs task, returns result. No personas. 'Small by design' — the smallest production option."
  - id: pi-mono-subagent-example
    name: "pi-mono examples/extensions/subagent"
    repo: earendil-works/pi-mono
    role: subprocess-reference
    notes: "~990 LOC. The in-tree reference Pattern 1 implementation. `spawn('pi --mode json -p --no-session')`, re-renders child Message[] inline using Pi's exported components. single/parallel/chain. Fork this to build your own."
  - id: tmustier-pi-agent-teams
    name: pi-agent-teams (tmustier)
    repo: tmustier/pi-agent-teams
    role: orchestration-team-parity
    notes: "Brings Claude Code **agent teams** to Pi: a shared file-per-task list with three states and dependency tracking (blocked tasks wait for prerequisites), idle-teammate **auto-claim**, file-based mailboxes for direct messages and broadcast, and urgent messages that interrupt a teammate's turn via steering. Coordinates work across multiple Pi sessions rather than 1:1 delegation. Framework-scale, command-driven MVP + status widget."
  - id: melihmucuk-pi-crew
    name: pi-crew (melihmucuk)
    repo: melihmucuk/pi-crew
    npm: "@melihmucuk/pi-crew"
    role: orchestration-nonblocking
    notes: "Non-blocking subagent orchestration: spawn isolated agents that run in parallel while the spawning session stays interactive; results are delivered back as steering messages on completion. Mid-scale. (Distinct from the unrelated `pi-crew` npm slug published from baphuongna/pi-crew — disambiguate by repo.)"
  - id: tiziano-pi-multiagent
    name: pi-multiagent (Tiziano-AI)
    repo: Tiziano-AI/pi-multiagent
    npm: pi-multiagent
    role: orchestration-graph-isolated
    notes: "One tool, `agent_team`, plus a `/skill:pi-multiagent` guide and schema-checked graph cookbook (fan-out/fan-in DAGs). Strong isolation: children inherit neither the parent transcript, session, context files, prompt templates, themes, project SYSTEM.md, nor ambient skills; child output is treated as evidence, not instructions. Skill propagation is all-or-nothing and configurable. Framework-scale."
  - id: messense-pi-parallel-agents
    name: pi-parallel-agents (messense)
    repo: messense/pi-parallel-agents
    npm: pi-parallel-agents
    role: orchestration-model-race
    notes: "Five modes: single, parallel, sequential chain, **model race**, and team (DAG-based coordination with dependencies, roles, plan approval). Run the same task across different models in parallel; reuses existing agent definitions; auto-includes git branch/status/diff context. Works with or without predefined agent configs."
  - id: gotgenes-pi-subagents
    name: "@gotgenes/pi-subagents"
    repo: gotgenes/pi-packages
    npm: "@gotgenes/pi-subagents"
    role: tintinweb-fork
    notes: "Heavily-iterated 'friendly fork' of @tintinweb/pi-subagents (in-process, same Claude-Code-styled `Agent`/`get_subagent_result`/`steer_subagent` tool set). Worth evaluating against upstream tintinweb if you want the same tool shape with a different maintenance line; verify whether it preserves tintinweb's `subagents:rpc:*` cross-extension event contract before depending on that."
  - id: ifi-pi-extension-subagents
    name: "@ifi/pi-extension-subagents"
    repo: ifiokjr/pi-extension-subagents
    npm: "@ifi/pi-extension-subagents"
    role: nicobailon-fork-tui
    notes: "Fork of nicobailon adding an Agents Manager TUI overlay (List/Detail/Edit/ChainDetail/ParallelBuilder), per-agent run history, Gist export, .chain.md files."
  - id: noahsaso-interactive-subagents
    name: pi-interactive-subagents (noahsaso)
    repo: noahsaso/my-pi
    role: mux-pane-bundle
    notes: "Multiplexer-pane subagents bundled in noahsaso's Pi collection. Distinct implementation from HazAT despite the shared name."
  - id: jamwil-pi-subagent
    name: pi-subagent (jamwil)
    repo: jamwil/pi-subagent
    role: subprocess-fork
    notes: "Fork of mjakl/pi-subagent."
  - id: cmf-pi-subagent
    name: "@cmf/pi-subagent"
    repo: cmf/pi-subagent
    role: experimental-reference
    notes: "~1.3k LOC. Single-commit experiment, never published to npm. Pattern reference (recursive step composition, tree progress UI) — not a dependency target."
---

# Pi Subagent Extensions

**Short answer.** Pi ships no built-in subagent, so the community fills the
gap. For a battle-tested default, use **`nicobailon/pi-subagents`**
(subprocess, on-disk artifacts, the dominant choice by adoption). If your
priority is a **full, untruncated view of what the child did**, pick a
multiplexer-pane option — **`HazAT/pi-interactive-subagents`** (each child
is a real Pi session in its own terminal pane) — or, without a multiplexer,
**`ross-jill-ws/pi-subagent-in-memory`** (in-process, full `events.jsonl`
per child, no personas). For a **Claude-Code-styled tool set** use
**`tintinweb/pi-subagents`** (the `tools: all` bug is now fixed; in-process, not resumable). For
**low-latency fanout of many short children**, stay in-process
(`pi-subagent-in-memory` headless, or `pi-fast-subagent`). For
**coordinating a team or swarm** (shared task list, mailboxes, DAGs) rather
than 1:1 delegation, see the orchestration class
(**`tmustier/pi-agent-teams`**, **`melihmucuk/pi-crew`**).

## Contents

- [Two axes that decide everything](#two-axes-that-decide-everything)
- [The four execution patterns](#the-four-execution-patterns)
- [Cross-pattern comparison](#cross-pattern-comparison)
- [Delegation vs orchestration: teams and swarms](#delegation-vs-orchestration-teams-and-swarms)
- [Inspecting a subagent: the full-view problem](#inspecting-a-subagent-the-full-view-problem)
- [Tool naming: Claude-Code-styled vs bespoke](#tool-naming-claude-code-styled-vs-bespoke)
- [Adoption](#adoption)
- [Comparison with other agents](#comparison-with-other-agents)
- [Picking guide](#picking-guide)
- [Caveats](#caveats)
- [See also](#see-also)

The base pattern: parent calls a `delegate` / `subagent` / `Task` tool → a
child agent runs the task in an isolated context → the result returns to the
parent without polluting its window. There is no first-class subagent in Pi
(unlike Claude Code's `Task` tool or opencode's `subtask` part type);
[RFC #552](https://github.com/earendil-works/pi-mono/issues/552) proposed
extracting subagent execution into a reusable library but was closed without
landing one, so the variant landscape is the answer.

## Two axes that decide everything

Almost every choice reduces to two orthogonal questions. Capabilities
(parallel, chain, pool) are *not* an axis — most options support most of
them.

1. **How is the child observed and where does it run?** → the four
   execution patterns below. This decides spawn cost, isolation, steering,
   and how much of the child you can see.
2. **Is it 1:1 delegation or multi-agent orchestration?** → most extensions
   are "parent delegates one task to one child." A newer class coordinates a
   *team or swarm* with shared task lists, mailboxes, and DAGs. See
   [Delegation vs orchestration](#delegation-vs-orchestration-teams-and-swarms).

## The four execution patterns

What changes between patterns is **where the child runs, how the parent
observes it, and how output flows back**.

| Pattern | Where the child runs | Parent observes via | Examples |
|---|---|---|---|
| **1. Subprocess + JSON stream** | `spawn('pi --mode json -p')` | parse stdout `Message[]` events | in-tree reference, nicobailon, amosblomqvist, aleclarson, e9n, HamdiMaz, jerryan-lite, pi-delegate |
| **2. Subprocess + JSON-RPC** | `spawn('pi --mode rpc')` | JSON-RPC notifications + bidirectional commands | no generic extension; only ralph drivers (`lnilluv/pi-ralph-loop`) |
| **3. In-process (`createAgentSession`)** | same process, separate session | direct `session.subscribe(...)` | tintinweb, pi-subagent-in-memory, pi-fast-subagent |
| **4. Multiplexer pane per child** | each child = own cmux/tmux/zellij/wezterm pane | runtime snapshot file + the pane itself | HazAT, masta-g3 (tmux-only), noahsaso |
| **4+1 hybrid** | mux pane (interactive) + headless `pi -p` (background) | both | edxeth |

### Pattern 1 — subprocess + line-delimited JSON

```ts
const proc = spawn("pi", ["--mode", "json", "-p", task,
  "--no-session"],  // or --session <jsonl> to inherit parent context
  { cwd, stdio: ["ignore", "pipe", "pipe"] });
proc.stdout.on("data", chunk => {
  for (const line of buffer.split("\n")) {
    const event = JSON.parse(line);
    if (event.type === "message_end") messages.push(event.message);
  }
});
await once(proc, "exit");
```

**Wins:** full process isolation, clean context separation, optional
inheritance via `--session <jsonl>`, re-renderable transcripts, cheap
parallelism. **Trades:** ~200–500 ms spawn per child; no mid-flight steering
(SIGTERM only); the result is a *log*, not a *living view*. **Best for:**
stateless one-shot delegations, parallel fan-out, hard isolation.

### Pattern 2 — subprocess + JSON-RPC

`pi --mode rpc` exposes a bidirectional channel (`session.start`,
`session.steer`, `session.abort`, streaming notifications). A long-lived
child amortizes spawn cost across turns, at ~5× the LOC of Pattern 1 (RPC
framing, request correlation) and tighter coupling to Pi's RPC schema. No
generic subagent extension uses it; Pattern 1 covers one-shot needs more
cheaply and Pattern 3 covers steering in-process.

### Pattern 3 — in-process via `createAgentSession`

```ts
const { session } = await createAgentSession({
  cwd, sessionManager: SessionManager.inMemory(cwd),
  modelRegistry: ctx.modelRegistry,   // share parent auth + cache
  model: "claude-opus-4-7", tools: parentTools,
});
session.subscribe(event => { if (event.type === "turn_end") onComplete(event); });
await session.sendMessage({ content: task, triggerTurn: true });
session.steer("Wrap up");  session.abort();
```

**Wins:** ~zero spawn overhead (best for many short children), full event
subscription, direct steering/abort, shared `ModelRegistry` (no re-login per
child), the richest in-TUI surface. **Trades:** no isolation (a child crash
takes the parent down), memory accumulation in long parents, and the
**highest SDK semver risk** — `createAgentSession` is the most
internals-exposing surface and is not documented as semver-stable. **Best
for:** low-latency fanout, live oversight, shared auth/quota.

### Pattern 4 — multiplexer pane per child

```ts
const mux = detectMux();   // cmux | tmux | zellij | wezterm | none
await mux.createPane({ command: ["pi", "-p", task, "--session", sessionPath],
  title: `subagent: ${name}`, splitDirection: "right" });
// child writes { phase: "active"|"waiting"|"done", ... }; parent polls + widgets it
```

(`cmux` here is the agent-oriented "tmux for Claude Code" multiplexer
[`craigsc/cmux`](https://github.com/craigsc/cmux), detected via
`CMUX_SOCKET_PATH`; raw tmux, zellij, and wezterm work too.)

**Wins:** each child is a **real, full Pi session in a real pane** — full
TUI, full transcript, **no truncation, fully interactive** (you can type into
it). True parallel inspection: N children on screen at once. Async by
default. **Trades:** hard dependency on a multiplexer (degrades without one);
pane lifecycle is the user's problem; content lives in the other pane, not
re-rendered inside the parent. **Best for:** multi-candidate comparison,
users who live in cmux/tmux, children that need full interactivity.

## Cross-pattern comparison

| Dimension | P1 subprocess+JSON | P2 subprocess+RPC | P3 in-process | P4 mux pane |
|---|---|---|---|---|
| Spawn cost | ~200–500 ms | ~200–500 ms | **~0** | ~200–500 ms + pane |
| Process isolation | full | full | **none** | full |
| Mid-run steer/abort | no (SIGTERM) | yes | yes | yes (write to pane) |
| **Full untruncated view** | on disk (if persisted) | extension's choice | depends (in-memory: yes on disk) | **yes (real pane)** |
| **Parallel inspection** | no | no | modal/widget only | **yes (mux split)** |
| **User-interactive child** | no | no | no | **yes** |
| LOC, minimum viable | ~150 | ~1,300 | ~250 | ~1,400 |
| SDK semver risk | low | medium | **high** | low |

## Delegation vs orchestration: teams and swarms

Most extensions above are **1:1 delegation**: one parent hands one task to
one child and reads the result. A distinct, newer class is **multi-agent
orchestration** — coordinating a *team* of peers with shared state rather
than a parent/child tree. The mechanics are different (shared task lists,
mailboxes, DAGs, auto-claim) and so are the failure modes (deadlock,
duplicated work, mailbox races), so treat it as its own niche.

| Extension | Coordination model |
|---|---|
| **`tmustier/pi-agent-teams`** | Claude Code agent-teams parity: shared file-per-task list with dependency tracking, idle-teammate **auto-claim**, file mailboxes (direct + broadcast), steering interrupts across multiple Pi sessions. |
| **`messense/pi-parallel-agents`** | Five modes incl. **model race** (same task across models) and **team** (DAG with dependencies, roles, plan approval). |
| **`Tiziano-AI/pi-multiagent`** | One `agent_team` tool + schema-checked graph cookbook (fan-out/fan-in); strict child isolation; output treated as evidence, not instructions. |
| **`melihmucuk/pi-crew`** | Non-blocking: isolated agents run in parallel while your session stays interactive; results steered back on completion. |
| **`pi-zerg-swarm`**, **`@llblab/pi-actors`**, **`jwangkun/Pi-Multi-Agent`** | Heavier frameworks — native configurable agent teams with durable recovery; an actor-kernel model for many lightweight agents; a production-grade orchestration framework. |
| **`teelicht/pi-superagents`**, **`MasuRii/pi-agent-router`** | Workflow/routing layers on top of delegation (superpowers-pipeline role agents with model tiers; orchestrator-only active-agent routing). |

If you only want "run this one thing in a clean context," stay with 1:1
delegation — the orchestration runtimes add coordination surface you don't
need.

## Inspecting a subagent: the full-view problem

The single most common complaint is *"I can't reliably see what the child
did."* Three approaches give a genuinely **full** view; one popular option
truncates.

| Approach | Extension(s) | What you get |
|---|---|---|
| **Real pane** | HazAT, masta-g3, noahsaso | The child's entire live Pi session in a terminal pane — no truncation, scrollable, interactive. The most literal full view; needs a multiplexer. |
| **In-process + on-disk JSONL** | `pi-subagent-in-memory` | Per-child `events.jsonl` + `result.md` on disk (full stream, post-mortem replayable) plus a live `Ctrl+N` overlay. No multiplexer, no personas. |
| **Subprocess + persisted session** | nicobailon | Each child runs as a real `pi --session <file>` process, so its per-child session JSONL is a **genuine resumable Pi session** (`pi --session <file>`), with an `events.jsonl` artifact alongside. Post-mortem (and resumable), not live. |
| **Live modal (truncated)** | tintinweb ConversationViewer | Live `session.subscribe` modal with scroll — but **tool/bash output is truncated to 500 chars** and there is **no replay after the modal closes**. Great for live coaching, weak for auditing. |

**Rule of thumb:** for live, side-by-side oversight you can type into, use a
**mux pane** (HazAT). For audit-heavy or long pipelines where the value is
post-hoc, use **on-disk JSONL** (`pi-subagent-in-memory`, or nicobailon
`verbose:true`). Reach for tintinweb's modal only when you want to watch a
single child unfold live and don't need the full tail.

## Tool naming: Claude-Code-styled vs bespoke

No Pi extension replicates Claude Code's actual subagent tool — a single
`Task` tool with a `subagent_type` parameter and inline results.
`tintinweb/pi-subagents` (and its fork `@gotgenes/pi-subagents`) come
closest *in spirit*: they register `Agent` + `get_subagent_result` +
`steer_subagent` — a Claude-Code-*styled* async trio, **not** the verbatim
`Task` tool, so don't assume models carry strong out-of-the-box priors
for it. Everything else uses bespoke names (`subagent`, `delegate`,
`subagent_create`, `agent_team`, …). `pi-subagent-in-memory` is the
deliberate minimalist at the far end: one bespoke `subagent_create` and
**nothing** added to the prompt, letting the model decide from the
schema alone.

## Adoption

Adoption is lopsided and moves weekly, so this page does not inline live
counts — query them with the recipes in
[references/evaluation.md](../references/evaluation.md). The stable shape of
the field:

- **Tier 1 — `nicobailon/pi-subagents`** dominates by roughly an order of
  magnitude on downloads, with multiple external contributors (including the
  authors of other ecosystem packages). The default unless you have a
  specific reason.
- **Tier 2 — `tintinweb/pi-subagents`** (in-process, Claude-Code-styled) and
  **`HazAT/pi-interactive-subagents`** (the mux-pane leader, not on npm).
- **Long tail** — many small, single-author options and a wave of
  nicobailon clones/forks publishing to crowded `pi-subagent(s)` slugs.
  Disambiguate by repo URL, not npm name.

## Comparison with other agents

- **Claude Code** ships a built-in `Task` tool with `subagent_type`
  (provider-side dispatch) and first-class **agent teams**; `pi-agent-teams`
  ports the latter.
- **opencode** has `subtask` as a first-class message part handled in
  `runLoop()`; it cycles full-screen sessions but
  [has no tabs/panes](https://github.com/anomalyco/opencode/issues/5826).
  For parallel inspection, `HazAT/pi-interactive-subagents` is **strictly
  more capable** — a mux split puts N candidates on screen at once.
- **Pi** delegates this entirely to extensions, which is why the variant
  landscape exists.

## Picking guide

| Goal | Pick | Why |
|---|---|---|
| **Battle-tested default** | `nicobailon/pi-subagents` | Subprocess, on-disk artifacts, async polling, worktree, nested fanout; dominant adoption. |
| **Full live view you can type into** | `HazAT/pi-interactive-subagents` | Each child a real Pi session in a mux pane; no truncation; true side-by-side. Needs cmux/tmux/zellij/wezterm. |
| **Full view, no multiplexer, no personas** | `ross-jill-ws/pi-subagent-in-memory` | In-process; full `events.jsonl` per child on disk; adds nothing to the prompt. In-process = no isolation. |
| **tmux-only, lighter than HazAT** | `masta-g3/pi-tmux-subagents` | Single `tmux_subagent` tool; persistent children; turn artifacts on disk. |
| **Claude-Code-styled tool set** | `tintinweb/pi-subagents` | `Agent`/`get_subagent_result`/`steer_subagent`; live modal; cross-extension RPC. `tools: all` bug now fixed (PR #74). In-process (not resumable). |
| **Low-latency fanout of many short children** | `pi-subagent-in-memory` (headless) or `pi-fast-subagent` | In-process = ~0 spawn cost and shared auth; cap concurrency (provider limits, RAM). |
| **Coordinate a team / swarm** | `tmustier/pi-agent-teams`, `melihmucuk/pi-crew`, `messense/pi-parallel-agents` | Shared task list / mailboxes / DAGs / model races — orchestration, not 1:1 delegation. |
| **Smallest viable** | `drsh4dow/pi-delegate` or `@jerryan/pi-subagent-lite` | ~150–245 LOC, one tool, no personas. |
| **Opinionated multi-agent runtime** | `edxeth/pi-subagents` | Hybrid 4+1, orchestrator mode strips the parent's edit tools, rich frontmatter. |
| **Subprocess with bundled experts** | `HamdiMaz/pi-sub-agent` | 9 bundled expert agents; confirmation gate for project agents. |
| **Skill complement** (when/how, not the mechanism) | `obra/superpowers` | Cross-agent skills (`subagent-driven-development`, `dispatching-parallel-agents`); works with whichever extension you install. |
| **Reference for building your own** | `pi-mono/examples/extensions/subagent` | Re-renders child `Message[]` inline using Pi's exported components. |

### Running two systems at once

Because Pi loads many extensions, you can run two subagent systems in
parallel (e.g. an in-process fanout engine plus a mux-pane viewer) **as long
as their tool names and `pi.events` namespaces are disjoint**. Tool-name
collisions are the trap: several options register a bare `subagent` tool, so
pairing two of those breaks. Pairs like `tintinweb` (`Agent` + `subagents:*`
events), `pi-subagent-in-memory` (`subagent_create`), and `pi-fast-subagent`
(`subagent`) coexist cleanly. The remaining concern is the model seeing two
delegation tools — scope active tools per workflow rather than exposing both.

## Caveats

- **tintinweb issue #75 is fixed.** The `tools: all` agent definition that
  silently broke tool-calling (child reports `status: completed`,
  `tool_uses: 0`) was resolved by PR #74; upgrade to the v0.8+ line. The fix
  changed agent-definition tool/extension selectors — re-check your agent
  files after upgrading.
- **`pi-subagents` npm slug is contested.** `nicobailon` and `edxeth` both
  publish to bare `pi-subagents`, and there is a wave of clones. Install by
  repo URL. `HamdiMaz/pi-sub-agent` (singular) and `@scope/...` packages do
  not collide.
- **In-process (Pattern 3) has no isolation and the highest semver risk** —
  a child crash can take the parent down, and `createAgentSession` is not a
  documented-stable surface. Pin versions.
- **`HazAT/pi-interactive-subagents` is not on npm** — install by git URL,
  and it degrades without a multiplexer.
- **`noahsaso/pi-interactive-subagents` (in `my-pi`)** shares HazAT's name
  but is a different implementation. **`Hopsken/pi-subagents`** is a stale
  mirror of tintinweb, not a separate project.
- **`@cmf/pi-subagent` is experimental** (single commit, never published) —
  a pattern reference, not a dependency.

## See also

- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes; the source of live adoption numbers
- [Loop and Ralph Extensions](loop-extensions.md) — loop drivers often delegate to subagents
- [TODO List Extensions](todo-extensions.md) — companion survey; teams share a task list
