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
entries:
  - id: karpathy-llm-wiki
    name: karpathy/llm-wiki gist
    repo: karpathy/llm-wiki
    role: source-of-truth
    notes: "The original gist. Specification rather than implementation."
  - id: astro-han-llm-wiki
    name: karpathy-llm-wiki (Astro-Han)
    repo: Astro-Han/karpathy-llm-wiki
    role: multi-agent-skill
    notes: "Most established faithful 'thin wrapper'. Three layers, three ops, index + log, templates. No bundled scripts. Works with Claude Code, Cursor, Codex via npx add-skill."
  - id: praneybehl-llm-wiki-plugin
    name: llm-wiki-plugin
    repo: praneybehl/llm-wiki-plugin
    role: claude-plugin
    notes: "Most engineered. Seven slash commands, BM25 search, SQLite graph, scaling playbook. Multi-agent (Claude, Codex, Cursor, Gemini, OpenCode, Pi)."
  - id: aaronoah-llm-wiki-skill
    name: llm-wiki-skill
    repo: aaronoah/llm-wiki-skill
    role: cli-skill
    notes: "Lean. Python 3.10, three scripts (data.py, ingest.py, links.py). Roadmap honestly flags absent self-correction/multimedia/embeddings."
  - id: ironin-pi-llm-wiki
    name: pi-llm-wiki
    repo: iRonin/pi-llm-wiki
    role: pi-native
    notes: "Pi extension+skill bundle, npm-installable. Four logical layers: raw packets, wiki pages, generated JSON metadata, schema. Guardrails block direct raw/meta edits. Obsidian wikilinks."
  - id: atomicmemory-llm-wiki-compiler
    name: llm-wiki-compiler
    repo: atomicmemory/llm-wiki-compiler
    role: skill
    notes: "Surfaced in landscape; not deeply analyzed."
  - id: lucasastorian-llmwiki
    name: llmwiki
    repo: lucasastorian/llmwiki
    role: skill
    notes: "Surfaced in landscape; not deeply analyzed."
---

# LLM Wiki Skills and Pi-native Implementations

Community implementations of [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
The space is fragmented — no clear winner — but several viable options
with different trade-offs.

## Landscape

The gist itself attracts substantial attention, but the
implementation space is fragmented. Most people share their own
adaptations in comments rather than rallying behind one repo. The gist
explicitly says "your agent will build out the specifics with you," so
fragmentation may be by design.

| Project | Type | Notes |
|---|---|---|
| **`Astro-Han/karpathy-llm-wiki`** | Multi-agent skill | Most established. Faithful "thin wrapper": three layers, three ops, index + log, templates. No bundled scripts, slash commands, or graph layer. `npx add-skill`. Works with Claude Code, Cursor, Codex. |
| **`praneybehl/llm-wiki-plugin`** | Claude Code plugin | Most engineered. Seven slash commands (`/wiki:init`, `/wiki:ingest`, …), BM25 search, SQLite graph layer, scaling playbook, file-back-into-wiki workflow. Multi-agent (Claude, Codex, Cursor, Gemini, OpenCode, Pi). Newer, less battle-tested. |
| **`aaronoah/llm-wiki-skill`** | CLI-first skill | Lean. Python 3.10, three scripts (`data.py`, `ingest.py`, `links.py`). Roadmap honestly flags gaps (self-correction, multimedia, embeddings absent). |
| **`iRonin/pi-llm-wiki`** | Pi-native package | Pi extension + skill bundle, npm-installable. Four logical layers: raw capture packets, wiki pages, generated JSON metadata (registry, backlinks, events), schema. Guardrails block direct raw/meta edits. Uses Obsidian wikilinks. Source-page intermediate layer mandatory. |
| **`atomicmemory/llm-wiki-compiler`** | Skill | Surfaced in landscape; not deeply analyzed. |
| **`lucasastorian/llmwiki`** | Skill | Surfaced in landscape; not deeply analyzed. |

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
