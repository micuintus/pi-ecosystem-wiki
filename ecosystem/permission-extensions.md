---
title: Pi Permission and Guard Extensions
type: ecosystem
updated: 2026-08-21
sources:
  - masurii-pi-permission-system
  - gotgenes-pi-permission-system
  - jdiamond-pi-guard
  - pi-permission-suite
  - inobit-pi-permission
  - diegopetrucci-pi-extensions
  - composio-top-pi-extensions
  - pi-extensions-docs
tags: [extension, permissions, safety, guards, approval]
entries:
  - id: masurii-pi-permission-system
    name: pi-permission-system (MasuRii)
    repo: MasuRii/pi-permission-system
    role: category-leader
    notes: "Centralized, deterministic permission gates across tool, bash, MCP, skill and 'special' operations. Strongest adoption in the category. Ships explicit guidance for people arriving from OpenCode, including which OpenCode-specific permissions (`webfetch`, `websearch`, `question`, `lsp`, `todowrite`) have no Pi equivalent — a useful map of where Pi's tool surface genuinely differs."
  - id: gotgenes-pi-permission-system
    name: "@gotgenes/pi-permission-system"
    repo: gotgenes/pi-permission-system
    npm: "@gotgenes/pi-permission-system"
    role: divergent-fork
    notes: "Full fork of MasuRii, self-declared as substantially diverged in config format, internal architecture and permission model. Treat as a separate product, not a version — config is not portable."
  - id: jdiamond-pi-guard
    name: pi-guard
    repo: jdiamond/pi-guard
    npm: pi-guard
    role: bash-ast-matcher
    notes: "Distinctive for parsing shell commands with a real **AST parser**, so pipes and subshells are matched properly rather than by regex — the failure mode that makes naive bash allowlists trivially bypassable (`sh -c '...'`, backticks, `$( )`). Pattern-based permissions for bash, file access and custom tools, with safe defaults."
  - id: pi-permission-suite
    name: pi-permission-suite
    npm: pi-permission-suite
    role: approval-modes
    notes: "Four approval modes (Act / Auto / Ask / Plan) plus command-level restrictions and a rule engine — the closest thing to Claude Code's mode switch. Notably includes **subagent auto-approval**, which matters once delegation is in play: without it every child blocks on prompts nobody is watching."
  - id: inobit-pi-permission
    name: "@inobit/pi-permission"
    role: lightweight-guard
    notes: "Lighter enforcement: sensitive-file guard, read/write-aware project boundary, dangerous-operation confirmation, and a plan/build read-only mode."
---

# Pi Permission and Guard Extensions

## Why this category exists

Pi ships **no approval prompts and no permission layer**. The model gets
`read`, `write`, `edit` and `bash`, and `bash` means bash. That is a deliberate
core decision, and it is the single most common reason people bounce off Pi
coming from Claude Code or OpenCode, where gating is built in.

So the ecosystem built it. This category is where "minimal core" is most
visibly a trade rather than a free win: the functionality is genuinely
necessary for many users, and getting it means picking a third-party package
that sits in the hot path of every tool call.

## The shapes

| Shape | What it gates | Options |
|---|---|---|
| **Centralized gate** | tool, bash, MCP, skill, special ops — one rule set | `MasuRii/pi-permission-system`, `@gotgenes/...` fork |
| **Pattern matcher** | bash commands (AST-parsed), file paths, custom tools | `jdiamond/pi-guard` |
| **Mode switch** | approval *posture* (Act/Auto/Ask/Plan) + rules | `pi-permission-suite` |
| **Targeted guard** | sensitive files, project boundary, destructive ops | `@inobit/pi-permission`, `diegopetrucci`'s `confirm-destructive` |

## What to actually check before installing

This is the one category where the wiki's usual "pick by features" advice is
insufficient, because a permission layer is only as good as its worst bypass.

1. **How does it parse bash?** Regex allowlists over shell strings are
   defeated by `sh -c`, backticks, `$( )`, pipes and `;`. `pi-guard`'s AST
   parsing is the honest answer to this; anything doing substring matching
   should be assumed bypassable by a model that is not even trying to evade it.
2. **Does it gate subagents?** Delegation multiplies the problem: children run
   their own tools, and a prompt in an unwatched pane is a hang, not a gate.
   `pi-permission-suite` addresses this explicitly; check the others.
3. **Does it fail closed?** An extension that errors and silently stops
   enforcing is worse than no extension, because you believe you are covered.
4. **Is the config portable?** It usually is not. The `gotgenes` fork of
   `MasuRii` has deliberately incompatible config, so "the same extension" can
   mean two different rule languages.

## Picking guide

| Goal | Pick |
|---|---|
| One comprehensive rule set across everything | `MasuRii/pi-permission-system` |
| Trustworthy bash gating specifically | `jdiamond/pi-guard` (AST-based) |
| Claude-Code-style mode switching, plus subagent handling | `pi-permission-suite` |
| Just stop the obvious disasters | `@inobit/pi-permission` or `confirm-destructive` |
| Read-only exploration phase | a plan/build mode from the suite or `@inobit` |

## Caveats

- **Do not stack them.** Two enforcement layers over the same tool calls
  produce double prompts at best and contradictory verdicts at worst.
- **A permission extension is maximally trusted code.** It sees every tool
  call and every bash command, in-process. Apply
  [evaluation](../references/evaluation.md) more strictly here than anywhere
  else in this wiki, and prefer packages with readable source over npm-only
  drops.
- **Gating is not sandboxing.** None of these contain a compromised process;
  they decide whether a call happens. For real isolation use a container or VM.
- **Expect friction with autonomy.** Approval gates and
  [loop extensions](loop-extensions.md) pull in opposite directions; decide
  per session which you want rather than running both and fighting it.

## See also

- [Human-in-the-Loop Extensions](human-in-the-loop-extensions.md) — asking a
  question is not the same as gating an action
- [How to Evaluate a Pi Extension](../references/evaluation.md) — the vetting
  framework, which matters most for in-path code
- [Subagent Extensions](subagent-extensions.md) — why delegation complicates
  approval
