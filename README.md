# pi-ecosystem-wiki

A [Karpathy-style LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
about the [Pi coding agent](https://pi.dev/) ecosystem — extensions,
skills, packages, themes, providers. Survey pages by use case, each
comparing options so you can choose.

**Use this via Pi, not by browsing it manually.** The wiki is designed
to be queried by an LLM. Point Pi at this repo and ask things like
*"what loop extension should I use for overnight autoresearch?"* or
*"which subagent extension does in-process delegation?"*. The
recommended way is the [`micuintus/llm-wiki`](https://github.com/micuintus/llm-wiki)
skill — it handles ingest, query, and lint following the page
conventions this wiki already uses. Disclosure: same author maintains
both.

Manual browsing works too — the "I want to…" table below is the fast
lane — but the design assumes an LLM is doing the synthesis. This is
**not** a flat awesome-list. For exhaustive coverage see
[`qualisero/awesome-pi-agent`](https://github.com/qualisero/awesome-pi-agent),
[`awesome-pi.site`](https://awesome-pi.site/), and
[`pi.dev/packages`](https://pi.dev/packages) — all referenced in
[references/catalogs.md](references/catalogs.md). Every claim here
cites a source; see [`SCHEMA.md`](SCHEMA.md).

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

## Quick picks — author's minimal Pi setup

Pi is deliberately minimal. Stay minimal yourself; grab more later as
real needs surface. This is the author's actual install list, not a
"top downloads" list:

**Extensions (install these first):**

1. **[`nicobailon/pi-powerline-footer`](ecosystem/footer-extensions.md#pi-powerline-footer-nicobailon)** — at-a-glance status bar (model, cost, branch, dir). The footer you stop noticing because it's right.
2. **[`MasuRii/pi-tool-display`](ecosystem/tool-rendering-extensions.md)** — compact tool-call rendering. Stops tool output from burying the conversation.
3. **[`nicobailon/pi-web-access`](ecosystem/web-search-extensions.md)** — web search + content fetch. Single tool, sensible defaults.

**Skills (workflow-dependent — install only what you'll use):**

- **GitHub skill** from [`mitsuhiko/agent-stuff`](references/catalogs.md#curated-extension-collections) — `gh` CLI workflows
- *Optional:* **[Google Workspace skill](ecosystem/google-workspace.md)** — only if you live in Gmail/Docs/Calendar
- *Optional:* **[Jira skill](https://github.com/netresearch/jira-skill)** — only if your tickets are in Jira

Everything else in this wiki is "grab when you actually need it" —
loops, subagents, todos, evolve, MCP. Don't pre-install for the
hypothetical workflow you might want.

---

## Full browse

For the complete list of pages organized by category, see
**[index.md](index.md)**. The "I want to…" table above covers the
most common entry points; `index.md` covers everything.

---

## Contributing

Open a PR. New page = new entry in `raw-sources/index.md` and `index.md`,
plus a line in `log.md`.

## License

MIT.
