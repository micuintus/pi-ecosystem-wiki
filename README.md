# pi-ecosystem-wiki

A [Karpathy-style LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
about the [Pi coding agent](https://pi.dev/) ecosystem — extensions,
skills, packages, themes, providers, grouped into categories.

Pi is minimal and stripped to its core. The extension ecosystem on the
other hand is sprawling and hard to keep track of. This LLM wiki makes
an attempt to map structure to this ecosystem: what extensions are out
there, what they do, how they compare to other extensions. PRs to this
repo are very welcome.

**Main use case is querying it with Pi** — this wiki is meant to be
read and written by an LLM. Point Pi at this repo (using the
[skill developed by the author](https://github.com/micuintus/llm-wiki)
or another [LLM-wiki skill](ecosystem/llm-wiki-skills.md)) and ask
things like *"What different categories of subagent systems exist and
which extension falls into which one? Please also specify the
community sentiment and popularity for each extension."*

This is **not** yet another awesome-extension list — it's a navigation
TOC with structure and comparisons. Awesome-lists like
[`qualisero/awesome-pi-agent`](https://github.com/qualisero/awesome-pi-agent),
[`awesome-pi.site`](https://awesome-pi.site/), and
[`pi.dev/packages`](https://pi.dev/packages) are referenced here in
[references/catalogs.md](references/catalogs.md).

---

## I want to…

| Goal | Go here |
|---|---|
| **Search the web from Pi** | [Web Search Extensions](ecosystem/web-search-extensions.md) — extensions and skills side-by-side |
| **Customize how Pi looks** (themes, status bar, tool output) | [Themes](ecosystem/theme-extensions.md) · [Footer / Powerline](ecosystem/footer-extensions.md) · [Tool Rendering](ecosystem/tool-rendering-extensions.md) |
| **Delegate tasks to child agents** (subagents, parallel work) | [Subagent Extensions](ecosystem/subagent-extensions.md) — 4 patterns, with tradeoff matrix |
| **Track what my agent is doing** (TODO lists, task progress) | [TODO List Extensions](ecosystem/todo-extensions.md) — idiomatic tool shapes, widget stack, picking guide |
| **Keep long sessions coherent across compactions** | [Compaction Extensions](ecosystem/compaction-extensions.md) — algorithmic vs observation-ledger vs agentic-VFS vs tool-output-pruning, with `pi-blackhole` as the combined default |
| **Tame the prompt** (floating editor, history search, templates, queues, cache) | [Prompt Extensions](ecosystem/prompt-extensions.md) — four layers (input UX, template authoring, queueing, provider cache) |
| **Make Pi work autonomously** (iterate until done, run overnight) | [Loop and Ralph Extensions](ecosystem/loop-extensions.md) — 7 architectural variants compared |
| **Connect Pi to other services** (Google Workspace) | [Google Workspace](ecosystem/google-workspace.md) — `gws` CLI, OAuth, command shapes |
| **Pick a provider or bring a Claude subscription** | [Providers and model access](index.md#-providers-and-model-access) — third-party providers, the EU gap, Anthropic auth routes, Claude Pro/Max in Pi, and the Claude Code bridges |

*Also: [evaluate an extension before installing](references/evaluation.md) · [browse everything by category](index.md) · [find what's not surveyed yet](references/catalogs.md).*

---

## Full browse

For the complete list of pages organized by category, see
**[index.md](index.md)**. The tables above cover the most common
entry points; `index.md` covers everything.

---

## How this wiki is organized

- **`ecosystem/`** — one page per niche. *Survey* pages name the
  options, compare them, and end in a "how to pick" section;
  *integration-reference* pages document a single integration target.
- **`references/`** — methodology and catalogs ([evaluation](references/evaluation.md),
  [catalogs](references/catalogs.md)).
- **No live numbers in prose.** Stars, downloads, and commit dates go
  stale in weeks, so pages carry stable `repo:`/`npm:` identifiers in
  frontmatter instead and you query the current figures at read-time
  with the recipes in [evaluation.md](references/evaluation.md).
  Architectural comparisons (which are timeless) stay inline.
- Conventions live in **[SCHEMA.md](SCHEMA.md)**; every source is
  registered in **[raw-sources/index.md](raw-sources/index.md)**.

---

## Author's opinionated minimal recommendations

**First gotos:**

1. **[`nicobailon/pi-web-access`](ecosystem/web-search-extensions.md)** — web search + content fetch. Single tool, sensible defaults.
2. **[`nicobailon/pi-powerline-footer`](ecosystem/footer-extensions.md#pi-powerline-footer-nicobailon)** — at-a-glance status bar (model, cost, branch, dir). The footer you stop noticing because it's right.
3. **[`MasuRii/pi-tool-display`](ecosystem/tool-rendering-extensions.md)** — compact tool-call rendering. Stops tool output from burying the conversation.

**Nice to have:**

- **[`tintinweb/pi-manage-todo-list`](ecosystem/todo-extensions.md)** — the moment you need to track what Pi is doing across multiple turns, you want this. It mirrors the Copilot `manage_todo_list` shape that LLMs already know.

**Environment-dependent:**

- **GitHub skill** from [`mitsuhiko/agent-stuff`](references/catalogs.md#curated-extension-collections) — `gh` CLI workflows
- *Optional:* **[Google Workspace skill](ecosystem/google-workspace.md)** — only if you live in Gmail/Docs/Calendar
- *Optional:* **[Jira skill](https://github.com/netresearch/jira-skill)** — only if your tickets are in Jira

## License

MIT.
