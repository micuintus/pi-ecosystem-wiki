---
title: Index
type: reference
updated: 2026-05-31
sources: []
---

# Pi Ecosystem Wiki

The full browse. Each survey page covers one niche, names the options,
compares them, and links upstream.

If you can't find what you need here, see
[references/catalogs.md](references/catalogs.md) for the broader
catalogs (`pi.dev/packages`, `qualisero/awesome-pi-agent`,
`awesome-pi.site`) — this wiki sits on top of them, not in place of
them.

## Browse by use case

### 🔁 Loops, agents, and iteration

- [Loop and Ralph Extensions](ecosystem/loop-extensions.md) — 7 architectural variants for "keep iterating until done"
- [Evolve / Code-Optimization Extensions](ecosystem/evolve-extensions.md) — `pi-autoresearch` and the broader research landscape (try variant → benchmark → keep/discard)
- [Subagent Extensions](ecosystem/subagent-extensions.md) — Four execution patterns (subprocess, in-process, mux-pane) plus the team/swarm orchestration class; with a full-view inspection guide and picking table
- [Claude Code `/loop`](ecosystem/claude-code-loop.md) — Cross-tool reference: how Claude Code's cron-scheduled loop differs from Pi Ralph

### ✅ Task tracking and planning

- [TODO List Extensions](ecosystem/todo-extensions.md) — Tool-only, rendered widget, and external-file TODO patterns

### ✏️ Prompt: input, templates, queue, cache

- [Prompt Extensions](ecosystem/prompt-extensions.md) — floating editor (`pi-sticky-prompt`), Ctrl+R history search, template authoring (`pi-prompt-composer`, `pi-prompt-template-model`), hidden/`ask_user`-driven queues, dual cache-breakpoint fix, cache-hit observability

### 🗜️ Compaction and memory

- [Compaction Extensions](ecosystem/compaction-extensions.md) — Algorithmic, observation-ledger, agentic-VFS, tool-output-pruning, large-context-subprocess, and grounded LLM compaction patterns; `pi-blackhole` = `pi-vcc` + `pi-observational-memory`

### 🎨 TUI customization

- [Themes](ecosystem/theme-extensions.md) — 5 strategies for theming Pi (terminal-ANSI inheritance, single-port, curated bundle, distinct-UI, personal-collection)
- [Footer / Powerline Extensions](ecosystem/footer-extensions.md) — Status bars and powerline-style segments
- [Tool-Call Rendering Extensions](ecosystem/tool-rendering-extensions.md) — Compact rendering and richer diff visualization (OpenCode-style)
- [Working / Thinking Indicator Extensions](ecosystem/working-indicator-extensions.md) — Animated busy spinners and shimmering status verbs (Claude Code / Crush style); per-state animations
- [Slash-Command Discovery & Palette Extensions](ecosystem/slash-command-extensions.md) — Favorite/reorder the `/` dropdown, leader-key palette, command cheat-sheet; organizing a crowded command surface

### 🔧 Tool behavior

- [Hashline Edit Extensions](ecosystem/hashline-edit-extensions.md) — Hash-anchored `read`/`edit` replacements that fail loudly on stale context

### 🌐 Web search and information retrieval

- [Web Search Extensions](ecosystem/web-search-extensions.md) — Pi web search extensions and skills, side-by-side
- [Web Search Providers](references/web-search-providers.md) — What backend powers search in major AI products (reference)
- [LLM Chat Ingestion](ecosystem/llm-chat-ingestion.md) — Importing web LLM conversations (Claude.ai, ChatGPT, Gemini, Le Chat) when share links are unavailable

### 🧠 Knowledge and skills

- [LLM Wiki Skills](ecosystem/llm-wiki-skills.md) — Karpathy LLM Wiki implementations across agents

### 📱 Remote and browser access

- [Web UI and Remote/Mobile Access](ecosystem/web-ui-and-remote-access.md) — Embedded library and remote-terminal options

### 🔌 Providers and model access

- [Provider Extensions](ecosystem/provider-extensions.md) — OpenCode Zen/Go, Nebius Token Factory, and EU/privacy-forward open-weight model providers

**Claude Pro/Max subscription in Pi** — start with the survey; it names the pick. The other three pages are the foundation and the deep dives.

- [Claude Pro/Max Subscription Extensions](ecosystem/claude-subscription-extensions.md) — **start here.** Survey of three shapes: Shape A payload patchers (`pi-claude-code-use`, `pi-anthropic-auth`), Shape B provider proxies (`pi-claude-bridge`), Shape C provider replacement (`pi-anthropic-oauth`), with a picking guide
- [Anthropic Auth & Billing in Pi](ecosystem/anthropic-auth-and-billing.md) — platform baseline beneath the survey: OAuth / API key / Foundry routes, billing, and why third-party tools can't reach the main subscription budget
- [claude-agent-sdk-pi](ecosystem/claude-agent-sdk-pi.md) — deep dive: the original Shape B bridge to Anthropic's Agent SDK; thinking-mode mapping
- [pi-claude-bridge](ecosystem/pi-claude-bridge.md) — deep dive: the dominant Shape B; Claude Code as a Pi provider + AskClaude sub-agent, and what you can/can't shut off

### 🧩 Integrations

- [MCP Integration](ecosystem/mcp-integration.md) — Model Context Protocol adapters; when MCP makes sense and when CLI skills are leaner
- [Google Workspace Integration](ecosystem/google-workspace.md) — `gws` CLI, OAuth, GCP prerequisites, command shapes

## 📋 References and catalogs

- [How to Evaluate a Pi Extension](references/evaluation.md) — vital signs, maintenance signals, code-quality recipes (the framework this wiki uses instead of stale numbers)
- [Pi Ecosystem Catalogs and Awesome-Lists](references/catalogs.md) — Where to look when this wiki doesn't cover your need
- [Web Search Providers](references/web-search-providers.md) — Backends behind the major AI products

## 🚧 Niches not yet surveyed

Extensions exist and are actively used but no survey page has been compiled yet.
Use [`qualisero/awesome-pi-agent`](https://github.com/qualisero/awesome-pi-agent),
[`awesome-pi.site`](https://awesome-pi.site/), and
[`pi.dev/packages`](https://pi.dev/packages) to find candidates.

| Niche | Notable entries (starting points for a future survey) |
|---|---|
| **Security, guardrails, and sandboxing** | `michalvavra/agents` (filter-output, security), `kcosr/toolwatch`, `prateekmedia/pi-hooks` permission, `@aliou/pi-guardrails`, `shitty-extensions` plan-mode, `gondolin` (earendil-works sandbox), `nono` (Landlock/Seatbelt) |
| **Notifications** | `pi-notification-extension`, `pi-notify-pp`, `ferologics/pi-notify`, `qualisero/rhubarb-pi` background-notify |
| **Cost tracking and usage monitoring** | `shitty-extensions` cost-tracker/usage-bar, `tmustier` usage-extension, `mrexodia/pi-cost-dashboard`, `pi-sub` |
| **Session management and checkpoints** | `nicobailon/pi-rewind-hook`, `prateekmedia/pi-hooks` checkpoint, `shitty-extensions` branch-sessions/handoff |
| **Process and task orchestration** | `juanibiapina/gob`, `patleeman/task-factory`, `taskplane`, `lsj5031/PiSwarm` |
| **Memory and persistent context** | `noahsaso/my-pi` memory.ts, `shitty-extensions` memory-mode, `@0xkobold/pi-learn` (project-memory-layer and observation-ledger patterns covered in [Compaction Extensions](ecosystem/compaction-extensions.md)) |
| **SSH remote access** | `cv/pi-ssh-remote` (redirects all file ops to a remote host) |
