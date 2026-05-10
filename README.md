# pi-ecosystem-wiki

A compiled, interlinked knowledge base about the [Pi coding agent](https://pi.dev/)
ecosystem — extensions, skills, packages, prompt templates, themes,
providers, and the people building them.

Pi itself is deliberately minimal. The ecosystem around it is not.
This wiki helps you **pick the right extensions for your Pi setup**
without trawling 1000+ entries in the flat catalogs.

---

## I want to…

| Goal | Go here |
|---|---|
| **Make Pi work autonomously** (iterate until done, run overnight) | [Loop and Ralph Extensions](ecosystem/loop-extensions.md) — 7 architectural variants compared |
| **Delegate tasks to child agents** (subagents, parallel work) | [Subagent Extensions](ecosystem/subagent-extensions.md) — 4 patterns, 12 extensions, with tradeoff matrix |
| **Track what my agent is doing** (TODO lists, task progress) | [TODO List Extensions](ecosystem/todo-extensions.md) — idiomatic tool shapes, widget stack, picking guide |
| **Search the web from Pi** | [Web Search Extensions](ecosystem/web-search-extensions.md) — extensions and skills side-by-side |
| **Customize how Pi looks** (themes, status bar, tool output) | [Themes](ecosystem/theme-extensions.md) · [Footer / Powerline](ecosystem/footer-extensions.md) · [Tool Rendering](ecosystem/tool-rendering-extensions.md) |
| **Connect Pi to other services** (Google Workspace, Claude SDK, auth) | [Google Workspace](ecosystem/google-workspace.md) · [Anthropic Auth](ecosystem/anthropic-subscription-auth.md) · [Claude Agent SDK Bridge](ecosystem/claude-agent-sdk-pi.md) |
| **Evaluate whether an extension is worth installing** | [How to Evaluate a Pi Extension](references/evaluation.md) — vital signs, maintenance signals, code-quality recipes |
| **Browse all surveyed pages** | [index.md](index.md) — full browse organized by category |
| **Find extensions not yet surveyed here** | [Pi Ecosystem Catalogs](references/catalogs.md) — `pi.dev/packages`, `awesome-pi.site`, curated collections |

---

## Quick picks

**Just installed Pi?** Three safe starting points used by multiple curators:

1. **[`tintinweb/pi-manage-todo-list`](ecosystem/todo-extensions.md)** — minimal TODO tool that LLMs already know how to use (mirrors GitHub Copilot's `manage_todo_list` shape). Branch-safe, polished widget.
2. **[`davebcn87/pi-autoresearch`](ecosystem/evolve-extensions.md)** — the most adopted code-optimization loop. Confidence scoring, dashboard, compaction-aware.
3. **[`tintinweb/pi-subagents`](ecosystem/subagent-extensions.md)** — in-process subagent delegation with idiomatic Claude Code tool names. Live modal viewer, cross-extension RPC.

---

## Full browse

For the complete list of pages organized by category, see
**[index.md](index.md)**. The "I want to…" table above covers the
most common entry points; `index.md` covers everything.

---

## What this is — and is not

**Is:** an LLM-maintained markdown wiki following the
[Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern. Survey pages by *use case*, each comparing options so you can choose.

**Is not:** another flat awesome-list. Those exist and do their job —
see [references/catalogs.md](references/catalogs.md) for `qualisero/awesome-pi-agent`,
[`awesome-pi.site`](https://awesome-pi.site/), and [`pi.dev/packages`](https://pi.dev/packages).

Every claim cites a source. See [`SCHEMA.md`](SCHEMA.md) for conventions.

---

## Contributing

Open a PR. New page = new entry in `raw-sources/index.md` and `index.md`,
plus a line in `log.md`.

## License

MIT.
