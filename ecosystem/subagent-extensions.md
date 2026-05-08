---
title: Subagent Extensions
type: ecosystem
updated: 2026-05-08
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
tags: [extension, subagent]
---

# Subagent Extensions

Pi extensions that delegate tasks to child agents with isolated
context windows. Pattern: parent calls a `delegate` / `subagent` /
`task` tool → child agent runs the task → result returns to parent
without polluting the parent's context.

There is no built-in subagent in Pi (unlike Claude Code's `Task` tool
or opencode2's first-class `subtask` part type). The community has
filled the gap with several variants.
[RFC #552](https://github.com/badlogic/pi-mono/issues/552) tracks
the discussion of extracting subagent execution into a reusable
library.

## Architecture variants

| Variant | How children run | Context | Use case |
|---|---|---|---|
| **Subprocess (fresh)** | `child_process.spawn('pi --print')` | Fresh, no parent state | Strong isolation, slow cold-start |
| **In-process** | `createAgentSession()` in same process | Fresh, but shares Pi auth/registry | Fast, max observability |
| **Fork** | Branched session inheriting parent context | Inherits parent transcript | Tasks needing parent's prior work |
| **Async / multiplexer** | Separate panes/processes, polled | Fresh or fork | Long-running parallel work |

## Extensions

### Subprocess-spawn family

| Extension | Stars | Modes | Notes |
|---|---|---|---|
| **`badlogic/pi-mono` example** | (in repo) | single, parallel, chain | Reference implementation. JSON-mode output. Spawns a `pi` process per call. |
| **`mjakl/pi-subagent`** | small | single (spawn or fork), parallel | Configurable `spawn` / `fork` context modes. Lightweight. |
| **`aleclarson/pi-subagent`** | fork | spawn / fork | Fork of mjakl's; same architecture. |
| **`jamwil/pi-subagent`** | fork | as upstream | Fork of mjakl's. |
| **`espennilsen/pi/extensions/pi-subagent`** (`@e9n/pi-subagent`) | small | single, parallel, chain, orchestrator, pool | Most workflow-rich. Hierarchical agent trees, agents can spawn and message each other, pool-based dispatch. |

### In-process

| Extension | Weekly downloads | Approach |
|---|---|---|
| **`tuansondinh/pi-fast-subagent`** (`pi-fast-subagent`) | 1.7K | `createAgentSession()` in same process. No subprocess cold-start, reuses Pi auth/model registry. Single, parallel, background (fire-and-forget with poll/cancel) modes. Slash commands for background job status. |

### Async / artifact-oriented

| Extension | Stars | Approach |
|---|---|---|
| **`nicobailon/pi-subagents`** | 1K | Largest single-author subagent extension. Async delegation with truncation, artifacts, and session sharing. Use cases: code review, scouting, parallel audits, saved workflows, background jobs. |
| **`noahsaso/pi-interactive-subagents`** | (in `noahsaso/my-pi`) | Subagents in multiplexer panes; interactive orchestration. Bundled in noahsaso's Pi extension collection. |

### Minimal

| Extension | Approach |
|---|---|
| **`drsh4dow/pi-delegate`** | One tool: `delegate`. Fresh child agent, runs task, returns only the useful result. No workflow engine, no background jobs, no dashboard. Stated philosophy: "small by design." |

### Library / infrastructure

| Extension | Stars | Approach |
|---|---|---|
| **`cmf/pi-subagent`** (`@cmf/pi-subagent`) | small | Library, not a standalone extension. Exports `invokeAgentWithUI` and `registerSubagentRenderer` for other extensions to build on top of. The "extract subagent execution into a library" direction RFC #552 is exploring. |

## Tradeoffs

| Concern | Subprocess (fresh) | In-process | Fork |
|---|---|---|---|
| Cold-start | High (~seconds) | Negligible | Negligible |
| Memory isolation | Strong (separate process) | Shared with parent | Shared with parent |
| Crash blast radius | Child only | Parent dies on child crash | Parent dies on child crash |
| Auth / model registry | Re-loaded per child | Shared | Shared |
| Observability | Stream stdout | Direct API access | Direct API access |
| Cancel | Kill process | Promise abort | Promise abort |

The **fast in-process** approach (`tuansondinh/pi-fast-subagent`) is
gaining traction for short tasks where cold-start dominates wall-clock
time. The **subprocess** approach is preferred when isolation matters
(e.g. running untrusted code in a child).

## Comparison with other agents

- **Claude Code** ships a built-in `Task` tool with a `subagent_type`
  parameter. Provider-side dispatch.
- **opencode2** has `subtask` as a first-class message part type
  handled in `runLoop()` itself.
- **Pi** delegates this to extensions, which is why the variant
  landscape exists at all. Different teams pick different tradeoffs.

See [Loop Architectures](../comparisons/loop-architectures.md) for the
broader framing.
