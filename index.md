---
title: Index
type: reference
updated: 2026-05-10
sources: []
---

# Pi Ecosystem Wiki

A use-case-organized guide to picking extensions for your Pi setup.
Each survey page covers one niche, compares the available options, and
links upstream.

If you can't find what you need here, see
[references/catalogs.md](references/catalogs.md) for the broader
catalogs (`pi.dev/packages`, `qualisero/awesome-pi-agent`,
`awesome-pi.site`) — this wiki sits on top of them, not in place of
them.

## Browse by use case

### 🔁 Loops, agents, and iteration

- [Loop and Ralph Extensions](ecosystem/loop-extensions.md) — 7 architectural variants for "keep iterating until done"
- [Evolve / Code-Optimization Extensions](ecosystem/evolve-extensions.md) — `pi-autoresearch` and the broader research landscape (try variant → benchmark → keep/discard)
- [Subagent Extensions](ecosystem/subagent-extensions.md) — Subprocess, in-process, fork, and async patterns for delegating tasks to child agents
- [Claude Code `/loop`](ecosystem/claude-code-loop.md) — Cross-tool reference: how Claude Code's cron-scheduled loop differs from Pi Ralph

### ✅ Task tracking and planning

- [TODO List Extensions](ecosystem/todo-extensions.md) — Tool-only, rendered widget, and external-file TODO patterns

### 🎨 TUI customization

- [Themes](ecosystem/theme-extensions.md) — 5 strategies for theming Pi (terminal-ANSI inheritance, single-port, curated bundle, distinct-UI, personal-collection)
- [Footer / Powerline Extensions](ecosystem/footer-extensions.md) — Status bars and powerline-style segments
- [Tool-Call Rendering Extensions](ecosystem/tool-rendering-extensions.md) — Compact rendering and richer diff visualization (OpenCode-style)

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

### 🔌 Integrations and providers

- [MCP Integration](ecosystem/mcp-integration.md) — Model Context Protocol adapters; when MCP makes sense and when CLI skills are leaner
- [Anthropic Subscription Auth in Pi](ecosystem/anthropic-subscription-auth.md) — OAuth, API key, Foundry; why third-party tools can't reach the main subscription budget
- [claude-agent-sdk-pi](ecosystem/claude-agent-sdk-pi.md) — Bridge between Pi and Anthropic's Agent SDK; thinking-mode mapping
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
| **Memory and persistent context** | `noahsaso/my-pi` memory.ts, `shitty-extensions` memory-mode, `@0xkobold/pi-learn` |
| **SSH remote access** | `cv/pi-ssh-remote` (redirects all file ops to a remote host) |
