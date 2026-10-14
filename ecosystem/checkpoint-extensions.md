---
title: Pi Checkpoint, Rewind and Session-Branch Extensions
type: ecosystem
updated: 2026-10-14
sources:
  - pi-sessions-docs
  - claude-code-checkpointing
  - pi-coding-agent-changelog
  - nicobailon-pi-rewind-hook
  - prateekmedia-pi-hooks
  - hjanuschka-shitty-extensions
tags: [extension, checkpoint, rewind, sessions, branches]
entries:
  - id: nicobailon-pi-rewind-hook
    name: pi-rewind-hook
    repo: nicobailon/pi-rewind-hook
    role: file-checkpoint
    notes: "Catalog-level, not code-read. Per-prompt file checkpoints with rewind, from the author of the dominant MCP adapter and subagent extensions."
  - id: prateekmedia-pi-hooks
    name: pi-hooks checkpoint
    repo: prateekmedia/pi-hooks
    role: session-checkpoint
    notes: "Catalog-level, not code-read. Session checkpoint support inside a general hooks bundle, from the author of the original Claude SDK bridge. Last pushed May 2026."
  - id: shitty-branch-sessions
    name: branch-sessions and handoff
    repo: hjanuschka/shitty-extensions
    role: branch-workflow
    notes: "Catalog-level, not code-read. Branch-session and handoff workflows inside a novelty-plus-utility bundle."
---

# Pi Checkpoint, Rewind and Session-Branch Extensions

Pi branches conversations natively (`/tree`, `/fork`, `/clone`), but
it captures no file state; Claude Code captures both. The extensions
below close the file half. Entries marked catalog-level have not been
code-read; treat their notes as pointers, not findings.

## What Pi core does

Sessions are JSONL trees, and the model receives the active branch
only. `/tree` moves within the session file (selecting a user message
puts its text back in the editor; submitting forks the branch).
`/fork` starts a new session from an earlier user message. `/clone`
copies the active branch into a new session. Leaving a branch can
attach an LLM summary of the abandoned path ([pi-sessions-docs]).
What none of this restores is file state: checking out an old branch
does not undo edits made since. That is git's job, or an extension's.

## What Claude Code does

Claude Code takes a checkpoint at each user prompt and rewinds code,
conversation, or both with `/rewind` (aliases `/checkpoint`,
`/undo`, or Esc twice on an empty prompt). Since v2.1.191, `/rewind`
restores conversation from before `/clear` too
([claude-code-checkpointing]). What it does not capture: files changed
through Bash, most subagent edits, concurrent sessions and symlinks.
Snapshots older than about 30 days are swept.

## The gap in Pi terms

Conversation branching: Pi is ahead (a real tree with named
navigation; Claude Code rewinds a linear log). File restore: Pi has
nothing built in, and its extensions are thinner than Claude Code's
checkpoints. A full equivalent would snapshot tracked file edits per
prompt and restore them on branch switch.

## Picking a checkpoint strategy

| If you want | Use | Why |
|---|---|---|
| Undo exploration inside one session | `/tree` plus git | Core, no extension; git owns file state |
| A separate line of work from an old message | `/fork` or `/clone` | Core; fork shares history, clone copies it |
| Automatic per-prompt file checkpoints | `nicobailon/pi-rewind-hook` | Only dedicated file-checkpoint extension found; verify against Pi 1.2 before trusting it |
| Checkpoints inside a hooks bundle | `prateekmedia/pi-hooks` | Dormant since May 2026; check it loads on Pi 1.x first |

## See also

- [Compaction Extensions](compaction-extensions.md): branch summaries use the same summarizer as compaction
- [Model Routing Extensions](model-routing-extensions.md): router state follows the session tree
- [Claude Pro/Max Subscription Extensions](claude-subscription-extensions.md): the AskClaude path runs inside Claude Code's own checkpointing
- [How to Evaluate a Pi Extension](../references/evaluation.md): live signals for the catalog-level entries above
