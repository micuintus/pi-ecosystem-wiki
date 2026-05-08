---
title: Pi Subagent Extensions
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
entries:
  - id: pi-mono-subagent-example
    name: "pi-mono examples/extensions"
    repo: badlogic/pi-mono
    role: subprocess-reference
    notes: "Reference subprocess-spawn implementation. JSON-mode output. Single, parallel, chain modes."
  - id: mjakl-pi-subagent
    name: pi-subagent (mjakl)
    repo: mjakl/pi-subagent
    role: subprocess-spawn
    notes: "Single (spawn or fork), parallel. Configurable spawn/fork context modes."
  - id: aleclarson-pi-subagent
    name: pi-subagent (aleclarson)
    repo: aleclarson/pi-subagent
    role: subprocess-fork
    notes: "Fork of mjakl/pi-subagent."
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
    notes: "Most workflow-rich. Hierarchical agent trees; agents spawn and message each other; pool-based dispatch."
  - id: pi-fast-subagent
    name: pi-fast-subagent
    repo: tuansondinh/pi-fast-subagent
    npm: pi-fast-subagent
    role: in-process
    notes: "createAgentSession() in same process — no subprocess cold-start. Single, parallel, background modes."
  - id: pi-subagents
    name: pi-subagents
    repo: nicobailon/pi-subagents
    npm: pi-subagents
    role: async-artifact
    notes: "Largest single-author subagent extension. Async delegation with truncation, artifacts, and session sharing."
  - id: noahsaso-interactive-subagents
    name: pi-interactive-subagents
    repo: noahsaso/my-pi
    role: async-multiplexer
    notes: "Subagents in multiplexer panes for interactive orchestration. Bundled in noahsaso's Pi collection."
  - id: pi-delegate
    name: pi-delegate
    repo: drsh4dow/pi-delegate
    npm: pi-delegate
    role: minimal
    notes: "One delegate tool. Fresh child, runs task, returns result. 'Small by design.'"
  - id: cmf-pi-subagent
    name: "@cmf/pi-subagent"
    repo: cmf/pi-subagent
    npm: "@cmf/pi-subagent"
    role: library
    notes: "Library exporting invokeAgentWithUI and registerSubagentRenderer for other extensions. Direction RFC #552 explores."
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

| Extension | Modes | Notes |
|---|---|---|
| **`badlogic/pi-mono` example** | single, parallel, chain | Reference implementation. JSON-mode output. Spawns a `pi` process per call. |
| **`mjakl/pi-subagent`** | single (spawn or fork), parallel | Configurable `spawn` / `fork` context modes. Lightweight. |
| **`aleclarson/pi-subagent`** | spawn / fork | Fork of mjakl's; same architecture. |
| **`jamwil/pi-subagent`** | as upstream | Fork of mjakl's. |
| **`espennilsen/pi/extensions/pi-subagent`** (`@e9n/pi-subagent`) | single, parallel, chain, orchestrator, pool | Most workflow-rich. Hierarchical agent trees, agents can spawn and message each other, pool-based dispatch. |

### In-process

| Extension | Approach |
|---|---|
| **`tuansondinh/pi-fast-subagent`** (`pi-fast-subagent`) | `createAgentSession()` in same process. No subprocess cold-start, reuses Pi auth/model registry. Single, parallel, background (fire-and-forget with poll/cancel) modes. Slash commands for background job status. |

### Async / artifact-oriented

| Extension | Approach |
|---|---|
| **`nicobailon/pi-subagents`** | Largest single-author subagent extension. Async delegation with truncation, artifacts, and session sharing. Use cases: code review, scouting, parallel audits, saved workflows, background jobs. |
| **`noahsaso/pi-interactive-subagents`** (in `noahsaso/my-pi`) | Subagents in multiplexer panes; interactive orchestration. Bundled in noahsaso's Pi extension collection. |

### Minimal

| Extension | Approach |
|---|---|
| **`drsh4dow/pi-delegate`** | One tool: `delegate`. Fresh child agent, runs task, returns only the useful result. No workflow engine, no background jobs, no dashboard. Stated philosophy: "small by design." |

### Library / infrastructure

| Extension | Approach |
|---|---|
| **`cmf/pi-subagent`** (`@cmf/pi-subagent`) | Library, not a standalone extension. Exports `invokeAgentWithUI` and `registerSubagentRenderer` for other extensions to build on top of. The "extract subagent execution into a library" direction RFC #552 is exploring. |

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

## See also

- [How to Evaluate a Pi Extension](../references/evaluation.md) — vital signs and code-quality recipes for picking among these variants
- [Loop and Ralph Extensions](loop-extensions.md) — related iteration-pattern surveys
