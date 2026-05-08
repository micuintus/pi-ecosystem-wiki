---
title: LLM Wiki Skills and Pi-native Implementations
type: ecosystem
updated: 2026-05-08
sources:
  - karpathy-llm-wiki
  - astro-han-llm-wiki
  - praneybehl-llm-wiki-plugin
  - aaronoah-llm-wiki-skill
  - iRonin-pi-llm-wiki
  - atomicmemory-llm-wiki-compiler
  - lucasastorian-llmwiki
tags: [skill, llm-wiki]
---

# LLM Wiki Skills and Pi-native Implementations

Community implementations of [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
The space is fragmented — no clear winner — but several viable options
with different trade-offs.

## Landscape

The gist itself is at 5,000+ stars / 4,400+ forks, but the
implementation space is fragmented. Most people share their own
adaptations in comments rather than rallying behind one repo. The gist
explicitly says "your agent will build out the specifics with you," so
fragmentation may be by design.

| Project | Type | Stars | Notes |
|---|---|---|---|
| **`Astro-Han/karpathy-llm-wiki`** | Multi-agent skill | ~638 | Most established. Faithful "thin wrapper": three layers, three ops, index + log, templates. No bundled scripts, slash commands, or graph layer. `npx add-skill`. Works with Claude Code, Cursor, Codex. |
| **`praneybehl/llm-wiki-plugin`** | Claude Code plugin | ~12 | Most engineered. Seven slash commands (`/wiki:init`, `/wiki:ingest`, …), BM25 search, SQLite graph layer, scaling playbook, file-back-into-wiki workflow. Multi-agent (Claude, Codex, Cursor, Gemini, OpenCode, Pi). Newer, less battle-tested. |
| **`aaronoah/llm-wiki-skill`** | CLI-first skill | small | Lean. Python 3.10, three scripts (`data.py`, `ingest.py`, `links.py`). Roadmap honestly flags gaps (self-correction, multimedia, embeddings absent). |
| **`iRonin/pi-llm-wiki`** | Pi-native package | small | Pi extension + skill bundle, npm-installable. Four logical layers: raw capture packets, wiki pages, generated JSON metadata (registry, backlinks, events), schema. Guardrails block direct raw/meta edits. Uses Obsidian wikilinks. Source-page intermediate layer mandatory. |
| **`atomicmemory/llm-wiki-compiler`** | Skill | unknown | Surfaced in landscape; not deeply analyzed. |
| **`lucasastorian/llmwiki`** | Skill | unknown | Surfaced in landscape; not deeply analyzed. |

## Fidelity scorecard (vs Karpathy gist)

| Dimension | Astro-Han | praneybehl | aaronoah | iRonin |
|---|---|---|---|---|
| Three layers | ✅ | ✅ (+graph) | ✅ | ✅ |
| Ingest/Query/Lint | ✅ | ✅ (+extras) | ✅ | ✅ |
| `index.md` + `log.md` | ✅ | ✅ | unclear | ✅ (generated) |
| Citations / wikilinks | ✅ | ✅ | unclear | ✅ (source IDs) |
| Query-as-page recompound | unclear | ✅ explicit | ❌ | ✅ |
| Schema co-evolution | implicit | explicit `SCHEMA.md` + `/wiki:upgrade` | implicit | `WIKI_SCHEMA.md` + `config.json` |
| Optional search engine | ❌ | ✅ BM25 + graph | scripts only | `wiki_search` tool |
| Multi-agent install | ✅ broad | ✅ broadest | ✅ via `npx skills` | Pi-native only |
| Departures from gist | none | graph + ontology | thin coverage | extension guardrails, JSON meta |

## Recommendation matrix

| Goal | Best choice | Why |
|---|---|---|
| Faithful gist, multi-agent | **Astro-Han/karpathy-llm-wiki** | Most established, thin wrapper, broad agent support |
| Claude Code, full features | **praneybehl/llm-wiki-plugin** | Slash commands, BM25, graph layer, scaling docs |
| Minimal CLI | **aaronoah/llm-wiki-skill** | Three Python scripts, no overhead |
| Pi-native, npm-installable | **iRonin/pi-llm-wiki** | Pi extension + skill bundle, deterministic guardrails |
| Build your own | Karpathy gist directly | The gist explicitly invites collaboration with your agent |

## Note on the pattern

Karpathy's gist frames the wiki as something the LLM compiles and
maintains, with a human curator. Three layers (raw sources → compiled
pages → query results), three operations (ingest, query, lint), and an
explicit `index.md` + `log.md`. Implementations diverge mostly on
whether to add a search/graph engine on top, and on how strict to be
about file-shape conventions.
