# Log

Append-only. Newest at top.

## [2026-05-19] research | Berlin providers: Kimi/GLM availability and GPU access

**`ecosystem/provider-extensions.md`** — expanded Berlin-based providers section:
- Added Kimi 2.6 and GLM availability columns to the Berlin providers table.
- **Finding: only AKI.IO offers GLM** (GLM 4.7 358B). **None of the nine
  Berlin providers offer Kimi 2.6** as a managed API.
- Added GPU access column. **GPU providers:** exalsius (K8s-native),
  Polarise (NVIDIA B200/GB200/GB300 NVL72 bare metal), Vective (H100/A100
  bare metal), basebox (self-hosted K8s + GPU Operator), Xydra Labs
  (on-prem/VPC), Nervur (your own hardware). **API-only (no GPU rental):**
  AKI.IO and Langdock.
- New subsection "GPU access compared to Scaleway" — Polarise and Vective
  are the closest German equivalents to Scaleway's GPU offerings.
- Updated recommendation matrix with three new rows: GLM via Berlin
  provider, Kimi 2.6 via Berlin provider, German bare-metal GPU.
- Registered 4 new sources: `aki-io-models`, `polarise-baremetal`,
  `basebox-llm-recommendations`, `nervur-architecture`.
- Source graph: 186/186. No broken links.

## [2026-05-19] feat | Add provider extensions survey; EU/privacy-forward open-weight providers

**New page: `ecosystem/provider-extensions.md`**
- 6 entries in frontmatter: `awtotty/pi-opencode` (static provider),
  `mdsitton/pi-opencode-provider` (runtime discovery, npm/pi.dev only),
  `lnilluv/pi-opencode-go-rotation` (reactive key rotation + watchdog),
  `mosquito/tokenfactory-pi` (runtime Nebius catalog discovery),
  `pi-model-router` (generic model routing), `pi-provider-litellm`
  (LiteLLM proxy adapter — closest thing to a universal EU-provider
  extension in Pi today).
- Comparison matrix: static vs runtime discovery vs key-rotation.
- Built-in vs extension gaps table — when each extension is actually
  needed vs using Pi core providers.
- Expanded EU / privacy-forward provider landscape: 9 general providers
  plus StackIT, Scaleway, AKI.IO. Deep-dive sections on:
  - **EUrouter** — unfunded Amsterdam router; AWS Bedrock controversy;
    sovereignty-washing criticism from HN.
  - **LLMbase** — Eyloo GmbH (German); consumer + API hybrid.
  - **Tensorix** — Tensorix Ltd (Irish reg 796387); zero-retention claim.
  - **Juice Factory** — Swedish startup (org 559382-2942); founders
    Misisca and Fallström; defense-grade dedicated instances.
  - **Infomaniak** — Swiss employee-owned B Corp; owned data centers;
    strongest sovereignty profile surveyed.
- **Berlin-based providers** table: AKI.IO, Langdock, Xydra Labs,
  exalsius, Berlin AI Labs, Polarise, Vective, basebox, Nervur.
- **Sovereignty washing** section: CISPE open letter (24 EU cloud CEOs),
  AWS European Sovereign Cloud critique, Microsoft EU Data Boundary
  "smoke and mirrors," Google Cloud EU Data Boundary limitations;
  red-flag vs green-flag checklist.
- **Pi extensions for EU providers** — documented the gap: no dedicated
  extensions exist. Generic OpenAI provider, `pi-provider-litellm`,
  or custom 50-line extension are the current paths.

**`index.md`** — added Provider Extensions to "Integrations and providers".

**`raw-sources/index.md`** — registered 30 new sources (4 extensions,
  2 built-in issues, 2 fork PRs, 9 EU providers, 1 model reference,
  4 major EU cloud providers, 4 provider deep-dive sources, 9 Berlin
  providers, 3 sovereignty-washing articles, 2 Pi extension proxies).

Source graph: 182/182. No broken links.

## [2026-05-10] feat | Reframe README; honest Quick picks; surface llm-wiki skill

**README.md**
- Merged intro and "What this is — and is not" into one opening that
  leads with the actual use case: **query this wiki via Pi using an
  LLM wiki skill**, manual browsing as the fallback fast lane. Names
  `micuintus/llm-wiki` as the recommended skill (with disclosure that
  same author maintains both). Trimmed redundant framing.
- **Quick picks rewritten.** Was: "three safe starting points used by
  multiple curators" (mostly TODO/loop/subagent — premature for a
  fresh install). Now: author's actual minimal-first setup:
  `pi-powerline-footer`, `pi-tool-display`, `pi-web-access`,
  GitHub skill (mitsuhiko/agent-stuff), optionally GWS/Jira skills if
  workflow demands. Explicit philosophy: stay minimal, grab more
  later.

**ecosystem/llm-wiki-skills.md**
- Added `micuintus/llm-wiki` to entries, landscape table, and
  recommendation matrix (slot: "querying pi-ecosystem-wiki"). Was
  missing despite being the maintained skill for this wiki.

Source `micuintus-llm-wiki` registered. Graph: 140/140.

## [2026-05-10] cleanup | Apply tightened TOC rule

Removed `## Contents` from `ecosystem/mcp-integration.md` (149 lines).
The new skill rule drops the "or >6 H2s" alternative threshold — line
count alone is sufficient. mcp-integration had 7 H2s but is short
enough to scroll without a TOC.


## [2026-05-10] polish | TL;DR ledes on two longest survey pages

`loop-extensions.md` (340 lines) and `subagent-extensions.md` (347 lines)
now open with a 2–3 sentence "short answer for most readers" punchline
naming the top picks, before diving into the variant taxonomy. Readers
who just want a recommendation get one without scrolling.

Also dropped `## What this page is for` from `loop-extensions.md` — it
was defensive meta-commentary ("the structure doesn't decay…") that
added no information for the reader.

No new pages, no new sources. 139/139.

## [2026-05-10] refactor | Walk back duplication; fix broken TOC anchors

**README.md trimmed 114 → 67 lines.** Removed the full browse-by-use-case
section that duplicated `index.md`. README now contains: identity,
"I want to…" decision table, Quick picks, pointer to `index.md` for
full browse, what-this-is/is-not, contributing. One canonical browse
location.

**TOC anchor fixes (9 broken).** Em-dash headings (`Tier 1 — Project
Health`) slugify to single-dash (`tier-1-project-health`), not double.
Manual TOCs across 6 pages had `--` where GitHub generates `-`. Fixed
in: loop-extensions, web-search-extensions (×2), subagent-extensions,
mcp-integration, evaluation (×3), web-search-providers (×1).

**Validation upgraded.** Anchor verifier added (Python script in this
log entry's session): walks all `.md` files, slugifies headings,
checks every `](#anchor)` and `](file.md#anchor)` resolves. Run
alongside the existing source-graph and link checks.

Source graph: 139/139.

## [2026-05-10] feat | Add MCP integration survey; complete ## See also coverage

**New page: `ecosystem/mcp-integration.md`**
- 4 entries: `nicobailon/pi-mcp-adapter` (608 stars, 23.7K weekly downloads,
  proxy pattern ~200 tokens), `steimbyte/pi-mcp-extension` (Zod conflict
  fix), `mitsuhiko/pi-codemode-mcp` (experimental sandbox), `spences10/my-pi`
  (bundle with MCP + LSP + chains).
- Opinionated caveat lede: Mario Zechner's stance that CLI skills are
  leaner than MCP servers for most tasks. Design tension surfaced as
  first-class content, not suppressed.
- Comparison table: when MCP makes sense (databases, browsers,
  third-party APIs) vs when CLI skills are better (file ops, custom
  tools, long-running services).
- Proxy pattern explained: how nicobailon's adapter avoids 10k+ token
  registration cost.

**`references/web-search-providers.md`** — added `## See also`
**`references/catalogs.md`** — added `## See also`

**`index.md`** — added MCP to "Integrations and providers" category;
removed from "Niches not yet surveyed"; updated date.

**Inline TOCs added** to:
- `ecosystem/theme-extensions.md`
- `ecosystem/footer-extensions.md`
- `references/evaluation.md`

Sources registered: 7 new (nicobailon-pi-mcp-adapter, jordyvd-pi-mcp-adapter,
steimbyte-pi-mcp-extension, mitsuhiko-pi-codemode-mcp, mariozechner-mcp-vs-cli,
mariozechner-what-if-no-mcp, pi-mcp-adapter-docs, spences10-my-pi).

Source graph: 139/139.

## [2026-05-10] feat | Improve human navigation: README portal, inline TOCs, visual anchors

**README.md** — complete rewrite as a landing page:
- "I want to…" decision table mapping 8 common goals to the right page
- "Quick picks" section — 3 safe starting points for new Pi users
- Full browse-by-use-case with emoji category markers and inline descriptions
- Moved `index.md` content into README so GitHub visitors don't bounce

**Inline TOCs added** to the 4 longest pages:
- `ecosystem/subagent-extensions.md` — 8 section anchors
- `ecosystem/loop-extensions.md` — 9 section anchors
- `ecosystem/todo-extensions.md` — 9 section anchors
- `ecosystem/web-search-extensions.md` — 9 section anchors

**index.md** — emoji visual anchors on all category headers (🔁 ✅ 🎨 🔧 🌐 🧠 📱 🔌 📋 🚧)

Source graph: 131/131. No broken links.

## [2026-05-10] feat | Ingest substantial updates from upstream private llm-wiki

Pulled in new public-relevant content from the private source wiki. Stripped internal-project framing, investigation tone, and pi-evolve confabulation; kept objective ecosystem analysis.

**`ecosystem/todo-extensions.md`** — major expansion (5 → 9 entries):
- Added `tintinweb/pi-manage-todo-list` (506 LOC, verbatim Copilot `manage_todo_list` shape, branch-safe). The "minimal idiomatic" recommendation.
- Added `edxeth/pi-tasks` (~1,100 LOC, verbatim Claude Code `Task*` shape, DAG, stats, file-backed). The "full task experience" recommendation.
- Added `tintinweb/pi-tasks` (2,061 LOC, 7 tools, DAG).
- Added `Soleone/pi-tasks` (3,566 LOC, pluggable backends).
- New section "Idiomatic LLM-known TODO tool shapes" — Claude Code `TodoWrite` vs VSCode Copilot `manage_todo_list` field-by-field comparison; explains which Pi extension mirrors which.
- New section "The four-layer widget stack" — L1 renderResult, L2 setWidget factory form, L3 registerMessageRenderer (the unrealized polish opportunity, no production extension uses it), L4 modal viewer.
- New section on `popododo0720/pi-stuff/workflow-extension` as proof-of-pattern for state-machine + transition-guards on top of TODOs.
- Replaced old "Polish gap vs TodoWrite" section with structural explanation.

**`ecosystem/subagent-extensions.md`** — major restructure (10 → 12 entries):
- Added `tintinweb/pi-subagents` as the in-process gold standard (verbatim Claude Code `Task`/`get_subagent_result`/`steer_subagent` tool names; ConversationViewer modal; agent-tree widget; cross-extension `pi.events` RPC).
- Added `HazAT/pi-interactive-subagents` (~8,200 LOC, 442 stars) — Pattern 4 (multiplexer pane per subagent). The only Pi extension supporting true side-by-side parallel inspection.
- Added `@ifi/pi-extension-subagents` (nicobailon fork with Agents Manager TUI overlay).
- Added `elpapi42/pi-minimal-subagent` (1,144 LOC, env-injection escape hatch).
- Restructured around four architectural patterns (was three): added Pattern 4 (multiplexer pane) with full code sketch and tradeoff analysis.
- New "Cross-pattern comparison" matrix covering spawn cost, isolation, parallel inspection, LOC, SDK semver risk.
- New "Idiomatic LLM-known tool shapes" section.
- New "ConversationViewer — capabilities and limits" section documenting the 500-char truncation in tintinweb's modal.
- Updated opencode comparison: post-PR #14814 opencode also has no tabs/panes, so HazAT (mux split) is strictly more capable than opencode for parallel inspection.
- Added Caveats section: Hopsken/pi-subagents = stale private mirror of tintinweb/pi-subagents (not a separate project); cmf/pi-subagent = experimental not production.

**`ecosystem/loop-extensions.md`** — small addition:
- New "Source-path notes" subsection correcting common citation errors (mitsuhiko's `loop.ts` lives at `extensions/`, not `pi-extensions/`; tmustier's at `pi-ralph-wiggum/index.ts`; pi-autoresearch at `extensions/pi-autoresearch/index.ts`; lnilluv ships as `ralph-loop-pi` on npm).

**Sources registered** (8 new): `tintinweb-pi-manage-todo-list`, `tintinweb-pi-tasks`, `edxeth-pi-tasks`, `soleone-pi-tasks`, `popododo-pi-stuff`, `tintinweb-pi-subagents`, `hazat-pi-interactive-subagents`, `ifi-pi-extension-subagents`.

Source graph: 131/131. No broken markdown links.

## [2026-05-08] feat | Ingest personal collections; expand evaluation Tier 2

**Survey page updates (ingestion seeds from the 6 newly catalogued collections):**

- `ecosystem/footer-extensions.md`: added `aliou-chrome` (two-component TUI chrome: header + footer, part of `aliou/pi-extensions`) and `hjanuschka-status-widget` (provider status indicator, part of `shitty-extensions`). Both entries and body sections.
- `ecosystem/todo-extensions.md`: added `mitsuhiko-todos` (file-backed, dependency tracking, TUI viewer — the most feature-complete TODO extension from the maintainer's own setup).
- `ecosystem/web-search-extensions.md`: added `@benvargas/pi-exa-mcp` (Exa via MCP, tested), `@benvargas/pi-firecrawl` (structured scraping, tested), `native-web-search` skill (no API key, uses model's native search). Updated both "What each does" table and recommendation matrix.
- `ecosystem/anthropic-subscription-auth.md`: added `@benvargas/pi-claude-code-use` to the Practical answer routing table as an extension-level OAuth compatibility option (lighter-weight than oh-my-pi fork).
- `ecosystem/subagent-extensions.md`: added `## Skill complement — obra/superpowers` section documenting the skill-side workflow complement to the extension-side subagent tools.

**`references/evaluation.md` Tier 2 update (non-redundant central quality assessment):**

- Replaced single `qualisero/awesome-pi-agent` row with a broader "Inclusion in curated collections" row.
- Added weighting table naming 8 curated collections with curator identity, inclusion meaning, and relative weight (Pi maintainer > qualisero > other active collections).
- Added convergence-signal rule: 3+ independent collections = strong utility evidence regardless of download count.
- Methodology stays central; survey pages do not repeat it.

Source graph: 123/123.

## [2026-05-08] feat | Add missing personal collections; stub uncovered niches

Research pass against `qualisero/awesome-pi-agent` and `shaftoe/awesome-pi-coding-agent`.

Added to `references/catalogs.md` — curated collections:
- `mitsuhiko/agent-stuff` (mitsupi) — Pi maintainer's own bundle; was cited in loop survey but not listed as a collection.
- `hjanuschka/shitty-extensions` — oracle, plan-mode, memory-mode, branch-sessions, cost-tracker, usage-bar, clipboard, handoff, status-widget.
- `tmustier/pi-extensions` — tab-status, arcade, usage-extension, agent-guidance + ralph-wiggum (was cited for ralph-wiggum only).
- `aliou/pi-extensions` — breadcrumbs, providers manager, chrome header/footer, git-branch-autocomplete, session-name, models-overrides.
- `ben-vargas/pi-packages` — CI/tested monorepo: Synthetic provider, Exa MCP, Firecrawl, Antigravity image gen, Claude Code OAuth patch.
- `obra/superpowers` — cross-agent workflow skills (TDD, systematic-debugging, subagent-driven-development, brainstorming). In Claude Code official marketplace.

Added to `index.md` — "Niches not yet surveyed" table covering 8 uncovered niches: MCP integration, security/guardrails/sandboxing, notifications, cost tracking, session management, process orchestration, memory/persistent context, SSH remote.

Registered 4 new sources: `hjanuschka-shitty-extensions`, `aliou-pi-extensions`, `ben-vargas-pi-packages`, `obra-superpowers`.

Source graph: 123 cited, 123 registered, zero unmatched.

## [2026-05-08] refactor | Centralize Live signals; document section conventions

- Removed `## Live signals` boilerplate section from `ecosystem/loop-extensions.md` (pure methodology pointer; now covered centrally in `references/evaluation.md`).
- Trimmed `ecosystem/theme-extensions.md`'s `## Live signals` section to a `## Theme-specific quality signal` block that retains only the domain-specific point (theme dependency footprint should be ~zero); removed the boilerplate methodology pointer.
- Updated `SCHEMA.md`: documented decision-support section name as **page-local** (no fixed header taxonomy — `## Recommendation matrix`, `## Picking a <thing> strategy`, `## Tradeoffs`, `## Comparison`, `## Discriminator: <axis>` are all valid). Documented that **Live signals methodology stays central** in `references/evaluation.md`; surveys may include only domain-specific signals not covered there.

## [2026-05-08] refactor | Source graph cleanup + title sweep

- Registered 3 missing sources: `bruclan-pi-hashline-edit`, `kcosr-codemap`, `whamp-pi-read-map` (cited from hashline-edit-extensions.md but absent from the registry).
- Removed duplicate / alias source IDs: `awesome-pi-agent` (alias of `qualisero-awesome-pi-agent`), `awesome-pi-coding-agent` (alias of `shaftoe-awesome-pi-coding-agent`), and the literal duplicate rows for `awesome-pi-site` and `pi-dev-packages` and `tomsej-pi-ext`.
- Pruned 13 orphan source IDs (cited nowhere): the dropped opencode-* family, `pi-agent-loop`, `pi-agent-session`, `vercel-ai-sdk`, `anthropic-sdk-typescript`, `pi-dev`, `pi-dev-docs-extensions`, `pi-dev-docs-packages`, `pi-dev-docs-skills`, `pi-mono-extension-examples`, `opencode-pr-20074`.
- Cited `github-rest-api` and `npm-downloads-api` from `references/evaluation.md` (both are referenced from the recipe code blocks).
- URL sweep: `badlogic/pi-mono` → `earendil-works/pi-mono` across all `pi-*` source rows that pointed at the old org (post-rename canonical home).
- Renamed 3 survey titles to the `Pi <Topic> Extensions` convention: `subagent-extensions.md`, `tool-rendering-extensions.md`, `web-ui-and-remote-access.md`.

After the pass: source graph is complete and orphan-free — 119 cited IDs, 119 registered IDs, zero unmatched on either side.

## [2026-05-08] refactor | Wiki-wide consistency pass

- Stripped stale numbers from `README.md` and `references/catalogs.md` (counts of stars and entries decay; only shape descriptions remain).
- Added `## See also` to `claude-agent-sdk-pi`, `llm-chat-ingestion`, `llm-wiki-skills`, `tool-rendering-extensions`, `anthropic-subscription-auth`, `google-workspace`.
- Renamed `ecosystem/themes.md` → `ecosystem/theme-extensions.md` to match the survey-page naming convention; updated cross-links.
- Replaced `## Open questions` sections in `anthropic-subscription-auth.md` and `google-workspace.md` with `## Caveats` prose (avoids private-investigation tone).
- Trimmed unused page types (`concept`, `comparison`, `synthesis`, `stub`) from `SCHEMA.md`; documented the implicit *survey* vs *integration-reference* split inside `type: ecosystem`.
- Documented `role:` as page-local, not a global taxonomy, in `SCHEMA.md`.
- Moved "one tool, internal routing" guidance from `references/web-search-providers.md` to `ecosystem/web-search-extensions.md` so the reference page stays a clean backend reference. Cross-link kept.
- Reshaped `ecosystem/evolve-extensions.md` to integration-reference style (dropped the single-entry `entries:` block; the page is explicitly a category-of-one).
- Dropped "14 projects" / "10 web search extensions" stale counts from `index.md`.

## [2026-05-08] refactor | Split footer + hashline surveys

- Split `ecosystem/footer-and-hashline-extensions.md` (legacy lump from the private wiki) into two orthogonal pages: `ecosystem/footer-extensions.md` (visual status-bar layer) and `ecosystem/hashline-edit-extensions.md` (hash-anchored read/edit replacements).
- The two niches share no design surface; only `oh-my-pi` (a fork) ships both. Cross-referenced from each.
- Updated `index.md` (added "Tool behavior" section), `ecosystem/tool-rendering-extensions.md`, `ecosystem/themes.md` cross-links.

## [2026-05-08] refactor | Roll entries-frontmatter to remaining surveys; backfill

- Rolled the `entries:` frontmatter convention to subagent-extensions, web-ui-and-remote-access, llm-wiki-skills, web-search-extensions, footer-and-hashline-extensions. Stripped inline metric numbers in favor of pointers to `references/evaluation.md`.
- Backfilled `pi-powerline-footer` `/vibe` and `workingVibeMode` detail (file vs ai modes; the openai-codex provider-binding gotcha).
- Added entries for `bruclan/pi-hashline-edit`, `kcosr/codemap`, `Whamp/pi-read-map` to the hashline survey.
- Folded "one tool, internal routing" guidance from the private `decisions/web-search-provider-strategy.md` into `references/web-search-providers.md`.

## [2026-05-08] feat | Themes survey

- Added `ecosystem/themes.md`: 5-strategy survey (terminal-ANSI inheritance, single-port, curated bundle, distinct-UI, personal-collection) with 13 entries in frontmatter. Names the canonical implementation for each strategy rather than enumerating all 131 themes the catalogs index.
- Registered: pi-themes-docs, leblancfg-pi-ansi-themes, juanibiapina-pi-tokyonight, danielcherubini-pi-dracula, dracula-pi-coding-agent, joelhooks-pi-theme-catppuccin-mocha, otahontas-pi-coding-agent-catppuccin, victor-pi-curated-themes, ironin-pi-curated-themes, hasit-pi-community-themes, vinyroli-pi-codex-theme, tomsej-pi-ext, astrofoundry-pi-astro.

## [2026-05-08] expand | Project health prioritized + community sentiment tier

- Reframed `references/evaluation.md`. Tier 1 is now "Project Health" with priority-ranked metrics (★★★ last commit, npm downloads, contributors; ★★ release cadence, 90-day commit frequency, issue ratio; ★ stars, forks, version compatibility).
- Added Tier 2 "Community Sentiment" with concrete cheap sources (Pi Discord, awesome-list inclusion, GitHub Issues tone, README cross-mentions). Explicitly warns against generic web-search sentiment prompts.
- Added `[abandoned]` maturity tag (>12mo no commits, unanswered issues).
- Expanded fast recipe to cover all health signals in one block.

## [2026-05-08] structure | Evaluation framework + entries-frontmatter convention

- Added `references/evaluation.md`: three-tier framework (vital signs / maintenance / code quality) with copy-pasteable `gh` and `npm` recipes. Wiki captures stable identifiers (`repo:`, `npm:`); readers query live data on demand.
- Updated `SCHEMA.md`: added `entries:` frontmatter convention for `type: ecosystem` survey pages. Inline numeric values (stars, downloads, last-commit) are explicitly disallowed in body prose.
- Pilot rewrite of `ecosystem/loop-extensions.md` to the new convention: stripped headline-metrics table and inline star/download counts; added 14 entries with stable IDs to frontmatter; preserved all architectural variant descriptions, hook-surface matrix, and recommendation matrix (timeless content).
- Registered: github-rest-api, npm-downloads-api as methodology sources.

## [2026-05-08] restructure | Use-case landing + catalogs reference

- Reframed wiki around "pick the right extension for your Pi setup" persona.
- Rewrote index.md as use-case landing page (loops/iteration, task tracking, TUI customization, web search, remote access, integrations).
- Added references/catalogs.md surveying pi.dev/packages, qualisero/awesome-pi-agent, shaftoe/awesome-pi-coding-agent, plus curated single-author collections (rhubarb-pi, kcosr/pi-extensions, noahsaso/my-pi, oh-my-pi).
- Updated README.md to point to catalogs.md and drop concepts/comparisons section references (out of scope).
- Registered: 9 sources (qualisero-awesome-pi-agent, shaftoe-awesome-pi-coding-agent, awesome-pi-site, pi-dev-packages, qualisero-rhubarb-pi, kcosr-pi-extensions, oh-my-pi-collection, pi-packages-docs; noahsaso-my-pi already registered).

## [2026-05-08] ingest | Subagents, tool rendering, web/remote access

- Registered: 14 sources (pi-subagent-example, mjakl-pi-subagent, aleclarson-pi-subagent, jamwil-pi-subagent, espennilsen-pi-subagent, nicobailon-pi-subagents, tuansondinh-pi-fast-subagent, cmf-pi-subagent, drsh4dow-pi-delegate, noahsaso-my-pi, pi-rfc-552, MasuRii-pi-tool-display, vinyroli-pi-tool-view, danielmlevans-pi-tool-display, tynanbe-pi-tool-display, pi-built-in-tool-renderer, pi-minimal-mode, pi-diff-extension, pi-issue-851, qroy-pi-remote, noahsaso-pi-remote, VVander-pi-remote-web-ui, pi-web-ui-package, sleepingrobots-pi-web-ui).
- Compiled: ecosystem/subagent-extensions.md, ecosystem/tool-rendering-extensions.md, ecosystem/web-ui-and-remote-access.md.
- Fresh research; not ported from private wiki (which had only stubs for these three topics).
- Updated: index.md.

## [2026-05-08] ingest | Anthropic + Google integrations

- Registered: 9 sources (claude-agent-sdk-pi, claude-agent-sdk-pi-pr-8, claude-agent-sdk-pi-pr-10, anthropic-claude-agent-sdk, pi-pr-3286, pi-issue-3299, opus-47-adaptive, googleworkspace-cli, anthropic-third-party-end).
- Compiled: ecosystem/llm-chat-ingestion.md, ecosystem/claude-code-loop.md, ecosystem/anthropic-subscription-auth.md, ecosystem/claude-agent-sdk-pi.md, ecosystem/google-workspace.md, references/web-search-providers.md.
- Updated: index.md.

## [2026-05-08] ingest | LLM Wiki Skills

- Registered: 6 sources (astro-han-llm-wiki, praneybehl-llm-wiki-plugin, aaronoah-llm-wiki-skill, iRonin-pi-llm-wiki, atomicmemory-llm-wiki-compiler, lucasastorian-llmwiki).
- Compiled: ecosystem/llm-wiki-skills.md.
- Updated: index.md.

## [2026-05-08] ingest | Pi Evolve / Code-Optimization Extensions

- Registered: 3 sources (karpathy-autoresearch, openevolve, shinkaevolve).
- Compiled: ecosystem/evolve-extensions.md (stripped internal-project framing; kept pi-autoresearch deep-dive and research-landscape context).
- Updated: index.md.

## [2026-05-08] ingest | Pi TODO List Extensions

- Registered: 3 sources (pi-todo-md, patriceckhart-pi-todo, pi-mono-todo-example).
- Compiled: ecosystem/todo-extensions.md (stripped internal loop sketch).
- Skipped: subagents.md (too thin), web-mobile-access.md, tool-rendering.md (mostly open questions).
- Updated: index.md.

## [2026-05-08] ingest | Pi Footer, Powerline and Hashline Extensions

- Registered: 9 sources (pi-powerline-footer, pi-fancy-footer, pi-powerbar, pi-vitals, diegopetrucci-pi-extensions, tomsej-pi-ext, pi-hashline-edit, pi-hashline-readmap, oh-my-pi).
- Compiled: ecosystem/footer-and-hashline-extensions.md (consolidates footer-themes.md and pi-hashline-edit-tools.md from private wiki). Later split into footer-extensions.md and hashline-edit-extensions.md — see 2026-05-08 refactor entry above.
- Updated: index.md.

## [2026-05-08] ingest | Pi Web Search Extensions

- Registered: 11 sources (pi-web-access, pi-codex-web-search, pi-free-web-search, pi-web-extension, pi-exa-gh-web-tools, pi-web-utils, aemonculaba-pi-search, pi-skills, pi-skills-brave-search, joemccann-pi-exa, pi-exa-search).
- Compiled: ecosystem/web-search-extensions.md (rewritten from private wiki, internal cross-refs stripped).
- Updated: index.md.

## [2026-05-08] docs | tighten source rules

- SCHEMA.md: sources must be canonical and externally accessible (GitHub, project pages, npm, awesome-lists, articles). No local paths or private session dumps.

## [2026-05-08] ingest | Pi Loop and Ralph Extensions

- Registered: 16 sources (pi-autoresearch, mitsuhiko-agent-stuff, tmustier-pi-extensions, pi-ralph-wiggum, pi-review-loop, jayshah-pi-agent-extensions, samfoy-pi-ralph, kostyay-agent-stuff, mikeyobrien-pi-ralph, emanuelcasco-pi-mono-extensions, lnilluv-pi-ralph-loop, rahulmutt-pi-ralph, mikeyobrien-pi-autoloop, akijain-hermes-loop, latent-variable-pi-auto-continue, ghuntley-ralph).
- Compiled: ecosystem/loop-extensions.md (rewritten from private wiki, internal-project refs stripped).
- Updated: index.md.

## [2026-05-08] init

- Bootstrap: README, SCHEMA, index, log, raw-sources/index, LICENSE, .gitignore.

## [2026-05-25] ingest | pi-claude-bridge

- Registered: 1 source (pi-claude-bridge).
- Compiled: ecosystem/pi-claude-bridge.md — dedicated page covering the
  two integration modes (provider + AskClaude tool), the structural
  reason it can reach the Claude Max/Pro subscription budget (real CC
  binary launched via Agent SDK, so Anthropic's prompt-content
  detector sees Claude Code), the AskClaude per-mode tool blocklists,
  and a feature matrix of what users can and cannot shut off
  (notably: `claude_code` SDK preset is not exposed as a config knob,
  so CC's personality + native-tool descriptions persist in the
  system prompt even when memory and Pi-side append are disabled).
- Updated: ecosystem/anthropic-subscription-auth.md (added route row +
  See also link), ecosystem/claude-agent-sdk-pi.md (cross-link to
  downstream fork), index.md (catalog entry).

## [2026-05-25] update | pi-claude-bridge recommendation matrix

- ecosystem/pi-claude-bridge.md: added "Picking between claude-agent-sdk-pi
  and pi-claude-bridge" section with capability matrix and explicit
  subscription-route recommendation (pi-claude-bridge for day-to-day;
  upstream only if smaller-surface tradeoff is acceptable). Notes that
  neither route lets you drop the claude_code SDK preset — direct
  ANTHROPIC_API_KEY is the right path for "no CC personality" use cases.
- Extended with a "Token cost" subsection: upstream leaks the default CC
  tool catalog + filesystem/cloud MCP descriptions into the prompt and
  has no session-resume, so prompt-cache hits are lost each turn and
  double-compact thrashing can occur; pi-claude-bridge passes `tools: []`,
  `--strict-mcp-config`, `ENABLE_CLAUDEAI_MCP_SERVERS=0`,
  `DISABLE_AUTO_COMPACT=1`, and preserves sessionId across turns.

## [2026-05-25] deepen | pi-claude-bridge token-cost section

- ecosystem/pi-claude-bridge.md: expanded the "Token cost" subsection
  with the structural mechanism — upstream declares CC's native tools
  (`DEFAULT_TOOLS = ["Read","Write","Edit","Bash","Grep","Glob"]`) to
  the model and then refuses execution via `canUseTool: deny`, so the
  model emits native tool calls, receives a denial as `tool_result`,
  re-plans, and tries again. pi-claude-bridge passes `tools: []` so
  the native schemas are never declared and no denial loop occurs.
  Added a concrete per-turn worked example and order-of-magnitude
  estimates (2–5× higher upstream cost in multi-turn sessions;
  ~10–30% in single-shot queries; widens with session length).

## [2026-05-27] expand | new subagent + task systems, tintinweb #75 caveat

Triggered by in-session observation of tintinweb/pi-subagents subagents
hanging at 0 tool uses (mirrors the failure mode the user saw earlier
in scriabin-waveform-qt). Live verification at
`~/.pi/agent/npm/node_modules/@tintinweb/pi-subagents/src/default-agents.ts`
confirmed: the built-in `general-purpose` agent omits `builtinToolNames`,
which means "all available tools" — the trigger for issue #75.

- ecosystem/subagent-extensions.md: added four entries —
  - **edxeth/pi-subagents** (Pattern 4+1 hybrid, ~10,622 LOC, orchestrator
    mode, ambient awareness, rich frontmatter, skill injection, the
    closest thing to a production multi-agent framework on Pi)
  - **masta-g3/pi-tmux-subagents** (~1,387 LOC, tmux-only mux, single
    rich-action tool, auto-stop, pi-agent-hub integration)
  - **HamdiMaz/pi-sub-agent** (~1,537 LOC, Pattern 1, 9 bundled agents
    incl. security-auditor, /sub-agent-settings, single/parallel/chain
    modes, prompt via stdin, self-disables in children)
  - **JerryAZR/pi-subagent-lite** (245 LOC, Pattern 1 minimal, no agent
    .md files at all — specialization via pi skills)
  - New "4+1 hybrid" row in the pattern table for edxeth.
  - New caveat documenting tintinweb #75 with the override-file workaround;
    notes PR #74 in flight (open since 2026-05-14) as the candidate fix.
  - Refreshed tintinweb/pi-subagents entry to v0.7.3 and embedded the
    known-issue notice.
- ecosystem/todo-extensions.md: added three entries —
  - **eleqtrizit/pi-tasks** ("Pi TaskGraph", npm `pi-taskgraph`, 6 tools
    incl. **get_batch_of_tasks** for parallel-ready unblocked tasks —
    first-class fan-out API)
  - **code-yeongyu/pi-todotools** (extracted from senpi-mono, 2 tools,
    **built-in auto-continuation** when incomplete todos remain — disable
    via `pi --disable-todo-continuation`)
  - **JerryAZR/pi-task-tree** (hierarchical, 7 tools, focus mode; author's
    own README warns about context cost — recommends NOT installing
    globally)
  - Refreshed edxeth/pi-tasks to v1.1.3, ~1,840 LOC; noted the token
    roll-up integration with edxeth/pi-subagents and the `pi-tasks` npm
    slug collision (Soleone, tintinweb, edxeth all publish under it).
- raw-sources/index.md: registered 9 new sources (4 subagent repos +
  3 task-system repos + 1 issue + 1 re-registration for the tintinweb
  bug-tracker).

## [2026-05-27] add | Adoption-signals section + nicobailon dominance

Pulled fresh GitHub stars/forks/issues and npm weekly-download numbers
across 11 subagent extensions on 2026-05-27 to settle the question of
which extension is most mature.

Findings (full table in ecosystem/subagent-extensions.md):

- nicobailon/pi-subagents dominates by ~10× weekly downloads (24,118
  vs tintinweb's 2,555), 4× stars (1,581 vs 380), 3× forks (232 vs 74).
- Cross-pollination signal: HazAT (pi-interactive-subagents author)
  and tmustier (multiple loop extensions) both contribute commits to
  nicobailon — ecosystem-mature project.
- High open-issue count (65) is healthy triage activity, not neglect.
- nicobailon released v0.25.0 on 2026-05-21 adding nested subagent
  fanout.
- Surfaced nicobailon issue #80: sync subagent returning large results
  after long sessions can crash parent — flagged in entry as relevant
  to evolve-style workflows.

Updates:
- New "Adoption signals (2026-05-27)" section with hard-data table,
  observations, and a sharpened picking-guide.
- Rewrote the "Short answer for most readers" lead to surface
  nicobailon as the dominant default (was tintinweb-led).
- Refreshed nicobailon entry: v0.25.0, full popularity numbers,
  issue #80 caveat.
- Updated the picking-guide "Heavy async pipelines" row to "Default
  subprocess option, most-adopted, most-active" with bolded numbers.

## [2026-05-27] expand | nicobailon inspection surface, pi-claude-bridge empirical note

- ecosystem/subagent-extensions.md: new "Inspection: nicobailon
  artifacts vs tintinweb ConversationViewer" section detailing
  nicobailon's events.jsonl/status.json/output-*.log layout,
  status/interrupt/resume actions, and pi-intercom contact_supervisor
  steering. Adds a side-by-side feature table making the
  *live-show vs post-mortem-replay* tradeoff explicit. Frames
  nicobailon as the decisive winner for long-running pipelines where
  the value is post-hoc auditing.
- ecosystem/pi-claude-bridge.md: added "Empirical observation
  (2026-05-27)" line under Order-of-magnitude. Real-world usage
  confirms the structural analysis — noticeable per-session token-burn
  reduction against the same subscription quota relative to the SDK
  route. Effect size consistent with the predicted multi-turn 2–5×
  gap, suggesting denial-loop + prompt-cache-miss dominate in practice.

## [2026-05-28] new survey | compaction extensions (pi-blackhole and its predecessors)

Ingested `k0valik/pi-blackhole` as the entry point and traced both
predecessors (`sting8k/pi-vcc`, `elpapi42/pi-observational-memory`),
then ran an Exa search across the broader compaction landscape on
pi.dev / npm / GitHub.

New page: ecosystem/compaction-extensions.md surveys 15 entries
across 6 strategies + 1 adjacent (project-memory):

1. Algorithmic / extractive — pi-vcc
2. Observation ledger — pi-observational-memory (+ GitHubFoxy fork)
3. Combined — pi-blackhole (vcc in compact slot, OM in memory slot,
   shared hook, unified config, per-worker model fallback chains,
   persisted cooldowns, manual-flush `noAutoCompact` mode, lockstep
   audit skill tracking both upstreams)
4. Tool-output pruning — pi-dcp, pi-context-prune,
   @complexthings/pi-dynamic-context-pruning
5. Agentic compaction (subagent + shell tools over VFS) —
   pi-agentic-compaction (Whamp & salemsayed variants),
   pi-omni-compact (large-context subprocess)
6. Grounded LLM compaction with files-touched index —
   pi-grounded-compaction
7. Adjacent: pi-memctx (durable Markdown project memory)

Frankenmerge lineage spelled out: pi-blackhole credits sting8k and
elpapi42; both upstreams hooked the same compaction path and were
not co-installable until k0valik resolved the conflict. Also noted
alpertarhan/pi-smart-compact's "Kamradt-style chunking" framing.

Updates:
- raw-sources/index.md: +15 source rows, bumped updated date
- index.md: new "Compaction and memory" section
- README.md: new I-want-to row for compaction

## [2026-05-28] new survey | prompt extensions (input UX, templates, queue, cache)

Entry point: ingested `alonmartin2222/pi-sticky-prompt` (macOS
floating-HUD prompt bar over UDS, fixes the "scroll terminal = lose
editor" problem of pi running outside alternate-screen mode). Then
ran Exa searches on prompt input / prompt-template / prompt-cache /
queue extensions.

New page: ecosystem/prompt-extensions.md surveys 9 entries across
four layers of "the prompt":

1. Prompt input UX — pi-sticky-prompt (out-of-TUI floating editor,
   macOS NSPanel + UDS), pi-prompt-history (Ctrl+R reverse search
   over user prompts, SQLite-indexed, Local/Global cwd scopes,
   fork-from-prompt action)
2. Prompt-template authoring — pi-prompt-composer (Markdown→slash
   commands with Liquid templating, grouped dirs, missing-arg
   collection), pi-prompt-template-model (model/skill/thinking
   frontmatter, auto-restore previous model after turn)
3. Prompt queueing — true-queue (`+`-prefixed hidden queue,
   sequential isolation, counter-pattern to steering since LLMs
   anchor on completion when they see future tasks), pi-copilot-queue
   (TaskSync-style `ask_user` tool + system-prompt loop policy +
   forced tool_choice, provider-gated to github-copilot by default)
4. Prompt-cache layer — pi-better-messages-cache (dual cache_control
   markers on assistant tool_use + user msg, matches OpenCode / Kilo
   Code / Roo Code; reported MiniMax/Kimi cache hit lift near-zero →
   80%+; implements pi-mono#1737, declined upstream; also fixes
   control-char-in-tool-call-JSON streaming crash), pi-cache-graph
   (/cache graph|stats|export, three TUI views, CSV export)

Updates:
- raw-sources/index.md: +9 source rows
- index.md: new "Prompt: input, templates, queue, cache" section
- README.md: new I-want-to row

## [2026-05-28] sharpen | compaction picking-guide; pi-vcc license caveat; pi-custom-compactor

User-driven refinement after working through the "I just want
/compact, but better" question against live tier-1 / tier-3 signals.

Findings:
- pi-vcc is the right answer for "drop-in better /compact" — not
  pi-blackhole. Blackhole's ledger machinery is orthogonal complexity
  for that use case.
- pi-vcc has a real packaging-hygiene gap: no LICENSE file in the
  repo, `"license": null` in package.json. Hard blocker for commercial
  or policy-gated installs until fixed. Durable, non-numeric fact —
  belongs in the wiki body.
- pi-observational-memory carries the strongest adoption signal in
  the niche (highest stars, downloads, forks) but is the wrong answer
  for "make /compact better" — its value is durable cross-compaction
  memory, not the compaction step itself.
- pi-blackhole's engineering bar (lockstep audit skill, 41 tests,
  strict TS, MIT license, manual-flush mode) is the highest of the
  three, but it's 4 days old — adoption signal is thin. Install it
  when you want vcc *and* the ledger, not just sharper compaction.
- New entry surfaced via web search: `davidorex/pi-custom-compactor`
  — YAML-declared extraction passes (mechanical or LLM-based per
  extract), JSON artifacts on disk, multiple specs per work mode.
  Same bracketed-section family as pi-vcc but configuration-driven.

Updates:
- ecosystem/compaction-extensions.md: added "Picking the right
  layer" decision table up front, mapping "what you actually want"
  → extension. The downstream strategy taxonomy stays as the deep
  dive.
- ecosystem/compaction-extensions.md: added LICENSE-hygiene caveat
  to the pi-vcc entry note.
- ecosystem/compaction-extensions.md: added pi-custom-compactor as
  a new entry in the same algorithmic-family bucket as pi-vcc.
- raw-sources/index.md: +1 row (pi-custom-compactor).

## [2026-05-28] expand | prompt-history niche has three players, not one

Initial prompt-extensions survey treated this niche as solved by
pi-prompt-history. Re-search surfaced two siblings:

- `mrshu/pi-readline-search` — Readline Ctrl+R + ! bash history,
  current-branch scope only, tiny single-file. Stale (no commits in
  90+d as of 2026-05-28).
- `samfoy/pi-session-search` — FTS5 keyword search + optional
  semantic embeddings (hybrid via Reciprocal Rank Fusion), indexes
  whole session content not just prompts. Dominant adoption signal
  in the niche (highest npm DL, multi-contributor, semver-tagged,
  CI + MIT). Browse-and-read rather than copy-into-editor.

The three don't replace each other — different mechanisms, scopes,
and primary actions. pi-prompt-history's unique-value action is
**fork-from-prompt** (resume a session, fork at the chosen user
message, pre-fill the prompt text).

Also tightened the pi-prompt-history entry with the WTFPL +
package.json license-mismatch caveat (durable non-numeric fact).

Updates:
- ecosystem/prompt-extensions.md: section title changed from
  "pi-prompt-history — Ctrl+R over past prompts" to "Searching past
  prompts and sessions"; replaced the single-tool prose with a
  three-row comparison table and per-extension prose. Added
  pi-session-search to the recommendation matrix.
- raw-sources/index.md: +2 rows.

## [2026-05-28] new survey | Claude Pro/Max subscription extensions

Code-deep review across the niche after user asked: "which is closest
to 'using my Claude subscription in Pi', has least token waste, is
least error-prone for CC feature leakage." Cloned and read the four
serious candidates (pi-claude-code-use, pi-claude-bridge,
claude-agent-sdk-pi, pi-claude-cli) plus surveyed adjacent niches.

Key structural finding: the niche splits into TWO shapes that are
trivially confusable but solve different problems:

- **Shape A — payload patcher** (`pi-claude-code-use`,
  `pi-anthropic-auth`): hooks `before_provider_request`, rewrites
  outbound payload to dodge Anthropic's third-party fingerprinting.
  Stays on Pi's built-in Anthropic OAuth transport. No subprocess,
  no SDK, no CC at all. Zero structural per-turn overhead. CC
  feature leakage surface structurally zero because CC is never
  invoked.
- **Shape B — provider proxy** (`pi-claude-bridge`,
  `claude-agent-sdk-pi`, `pi-claude-cli`): registers a new provider
  that routes LLM calls to CC SDK or CLI subprocess. Pi still
  executes tools. CC's `claude_code` preset system prompt is paid
  on every cold-start session. Mitigation surface (strict-mcp-config,
  cloud-MCP suppression, autocompact disable, session resume) is
  real and well-engineered in pi-claude-bridge.

Code-read empirical findings worth recording (durable, non-numeric):

- `claude-agent-sdk-pi` (prateekmedia, the original) has **no session
  resume** — searched the 1,258-line single file for `resume`,
  `sessionId`, `sharedSession`; found only Pi-side session
  bookkeeping. Every turn sends full history to a fresh `query()`,
  CC re-prefixes its full system prompt, no cache reuse. Strictly
  worse token economics than the elidickinson fork on any multi-turn
  session.
- `pi-claude-bridge` (elidickinson fork) added: session resume via
  `cc-session-io` (`resume: resumeSessionId`), `--strict-mcp-config`,
  `ENABLE_CLAUDEAI_MCP_SERVERS=0`, `DISABLE_AUTO_COMPACT=1`. Each
  one a meaningful correctness/cost win the upstream lacks.
- `pi-claude-code-use` (Vargas): pure-function pipeline, 779 LOC
  src + 1,298 LOC tests (1.67× ratio). Notable empirical claim in
  README: Anthropic OAuth fingerprints tool *names* — `web_search_exa`
  rejected in live testing, `mcp__exa__web_search` accepted.
- `pi-claude-cli` (rchern): highest test ratio in the niche (2.78×).
  Stale (no commits in 90+ days).

Updates:
- ecosystem/claude-subscription-extensions.md NEW — full survey
  (10 entries) with two-shapes structural distinction, picking
  guide, three-axis comparison.
- ecosystem/anthropic-subscription-auth.md — promoted to platform-
  level integration-reference; routes the "extensions" question to
  the new survey. Cleaned up the practical-answer table. Resolved
  the "open thread" caveat about Discussion #2950 (it's now solved
  in practice by both shapes).
- ecosystem/claude-agent-sdk-pi.md and pi-claude-bridge.md: added
  See-also links to the new survey. The agent-sdk-pi entry now
  explicitly notes the missing-resume → token-waste consequence
  vs the elidickinson fork.
- index.md, README.md: added survey entry.
- raw-sources/index.md: +6 rows.

## [2026-05-29] new survey | working/thinking indicator extensions

Triggered by "I want a Crush-style busy widget." Brave + gh research
across the busy-indicator niche; compared with the evaluation.md tiers.

New page: ecosystem/working-indicator-extensions.md (6 entries).

Niche boundary drawn explicitly: transient *busy* indicator only.
Distinct from footer-extensions (persistent status bar) and
tool-rendering-extensions (tool output + thinking-step content, where
fluxgear/pi-thinking-steps belongs).

Findings:
- @dustydonkey/pi-spinner (HarshalRathore) — the truest Crush/Claude
  Code match: rotating verbs + per-char shimmer, idle-aware, 187 CC
  verbs, auditable, highest npm pull (339/mo) despite 1 star. Fresh
  (2026-05). [experimental] but the recommended default for the
  shimmer-verb aesthetic.
- arpagon/pi-animations — maximalist: 21 animations incl. a `crush`
  scrambler, only one with 3 states (thinking/working/tool) and
  per-state assignment. Most stars (15), 2 releases, MIT — but
  feature-frozen since creation day 2026-03-20 (staleness watch).
  Needs true-color + Nerd Font.
- pi-fancy-loader (unitdhda) — 50+ sequences, HSL palette jitter,
  100+ verbs, picker. MIT but **npm-only, no public repo** →
  unauditable; flagged per evaluation Tier-3.
- shitty-extensions/ultrathink — novelty rainbow toggle, not a real
  indicator. Noted for completeness.
- Platform primitive: ctx.ui.setWorkingIndicator()/setWorkingMessage()
  /setWorkingVisible() (pi-mono #3413) + working-indicator.ts /
  titlebar-spinner.ts examples — the build-your-own path.

Updates:
- index.md: added under "TUI customization".
- raw-sources/index.md: +5 rows (incl. pi-fancy-loader as npm-only
  docs source).

## [2026-05-29] refine | working-indicator survey with code-read discriminators

Read the actual source of both leading entries (not just READMEs) to
settle a switch decision. Durable findings folded into the page:

- pi-spinner is genuinely idle-aware (`if (ctx.isIdle()) return` pauses
  the shimmer during sub-agent/user waits); gentle 200ms/3s cadence;
  uses both setWorkingIndicator + setWorkingMessage; clean teardown.
- pi-animations has NO idle/sub-agent guard — its 40–100ms multi-line
  render loop keeps firing during nested work (flicker + terminal-write
  pressure). CI is `tsc … || true` (cannot fail), 0 tests, hard
  true-color + Nerd Font requirement, feature-frozen since 2026-03-20.
- Disambiguated "Crush style": pi-animations ships a literal `crush`
  scramble animation (Charm Crush effect) vs pi-spinner's shimmer-verb
  line (Claude Code effect). New "Two senses of Crush style" section.
- Rewrote the picking-guide rows around the real discriminator: idle-
  awareness + terminal capability + which effect you actually mean,
  rather than "aesthetic match."

## [2026-05-30] new survey | slash-command discovery & palette extensions

Ingested alonmartin2222/pi-favorites-commands; searched the niche.

New page: ecosystem/slash-command-extensions.md (5 entries). Niche =
organizing/navigating a crowded `/` command surface, distinct from
authoring commands (prompt-extensions).

Three shapes + adjacent fix:
- reorder native dropdown — pi-favorites-commands (star+reorder, ★,
  persisted to ~/.pi/agent/data/slash-favorites.json; most-adopted)
- modal palette/launcher — leader-key palette in tomsej/pi-ext (Ctrl+X,
  which-key style; most-starred via the collection)
- cheat-sheet widget — pi-command-center (toggleable list above editor)
- adjacent UX fix — datspike/pi-inline-slash-extension (slash fires
  mid-text/2nd line; absolute-path submit bypass)

Code-read note worth recording: pi has NO public autocomplete-
contribution API (open issue earendil-works/pi#2983 for the @ analog),
so pi-favorites-commands wraps the editor + CombinedAutocompleteProvider
and shadows setAutocompleteProvider. Consequences: mirrors the built-in
command list locally (new built-in needs a bump) and bypasses
per-command argument autocomplete. Documented as the niche's structural
caveat.

Updates: index.md (TUI customization); raw-sources +4 rows.

## [2026-05-31] ingest | Claude OAuth cluster: code-read pi-anthropic-auth/-oauth, add Shape C, tidy nav

Re-characterised `pi-anthropic-auth` from inference to a source read of
`gotgenes/pi-anthropic-auth` (src/request-shaping.ts,
system-prompt-shaping.ts, docs/comparison-to-similar-projects.md).

**Correction.** The prior entry framed pi-anthropic-auth as
"pi-claude-code-use minus the tool-aliasing layer" — a subset. That is
wrong. Both are Shape A payload patchers that never invoke Claude Code,
but they bet on *different* Anthropic fingerprint signals:
- pi-claude-code-use targets tool **names** (MCP-style aliasing).
- pi-anthropic-auth targets the billing **header** — it forges Claude
  Code's `x-anthropic-billing-header` (cc_version / cc_entrypoint / cch
  = truncated sha256 of the first user message + sampled-char salt),
  does anchor-based minimal system-prompt de-fingerprinting, fixes
  assistant text-after-tool_use ordering, and hardens OAuth refresh.
  No tool aliasing.
They are complementary and combinable, not big-vs-small.

Nav tidy (cut the two-layer hop to the survey):
- Updated: claude-subscription-extensions.md — added a short-answer
  lede (per survey-lede rule); reframed Shape A as "different
  fingerprint axes"; rewrote the pi-anthropic-auth entry + picking-guide
  rows; folded pi-anthropic-auth into the three-axis rankings.
- Updated + renamed: anthropic-auth-and-billing.md (was
  anthropic-subscription-auth.md — the old name collided with the
  survey and ignored that the page also covers API key + Foundry).
  Deduped its practical table; the survey is the single source of
  extension picks; all inbound links updated.
- Updated: index.md — Providers section gets a "start here → survey"
  lede + reorder; auth baseline and the two SDK/bridge pages flagged as
  foundation / deep dives.

Follow-up in the same investigation:
- New source: `leohenon/pi-anthropic-oauth` (code-read). A third
  architectural shape the survey was missing — a **full provider
  replacement** (own OAuth + own `streamSimple` transport to
  api.anthropic.com + own conversion, bundles `@anthropic-ai/sdk`,
  adds Opus 4.8, symlinks `~/.Claude Code` → `~/.pi`). Openly targets
  the *main* Pro/Max budget; self-warns on ToS; no in-repo tests.
  Added as Shape C across the survey, the auth-baseline practical
  table, index.md, and raw-sources.
- Survey taxonomy: "two shapes" → "three shapes".
- Added a Shape A head-to-head (minimal / Pi-grain / razor-sharp /
  capability / adoption). Finding: pi-anthropic-auth is the cleaner,
  leaner, zero-dep, more Pi-idiomatic build; pi-claude-code-use wins
  only on capability (tool-name aliasing, via a jiti runtime dep).
- Adoption correction: dropped the implied pi-claude-code-use
  "dominance". npm installs currently favour pi-anthropic-auth; the
  higher star count is the pi-packages monorepo, a confounded signal.
  Live numbers kept out of pages per SCHEMA; pointed at evaluation.md.
- Clarified the easy-to-misread tool behaviour: pi-anthropic-auth
  passes all Pi tools through unchanged; pi-claude-code-use is the one
  that filters the model's tool view.
- Full-source re-read corrected the Shape A head-to-head: pi-claude-
  code-use uses **four** lifecycle hooks and mutates the active-tools
  list (not a 2-hook pure payload patch) and detects OAuth via Pi's
  official isUsingOAuth API; pi-anthropic-auth also owns a thin oauth
  override and sniffs OAuth from system-block markers. Both are high
  quality — pi-claude-code-use is v1.0 stable and well-engineered for
  its complexity; framing now says "larger surface, not sloppier".

Note: log.md has a stale "Newest at top" header but recent entries
append at the bottom — left as-is, not in scope here.

## [2026-05-31] docs | README looks-row + extension-agnostic goal table

The "Customize how Pi looks" entry-point row linked themes, footer, and
tool rendering but omitted the busy-indicator niche; added it as the
fourth facet (pi-animations and the other spinners are surveyed in
working-indicator-extensions.md). Also made the "I want to…" table route
by goal only — dropped the inline extension names (pi-animations,
pi-blackhole) so it doesn't pre-empt the surveys' recommendations.

## [2026-05-31] research+restructure | subagent survey: razor-sharp layout, orchestration class, full-view

Wide gh+npm discovery sweep (100+ repos). Reworked subagent-extensions.md:
- Decision-first short answer; two-axis orientation (observation pattern +
  delegation-vs-orchestration); single picking table at the end (dropped two
  redundant mid-page picking blocks).
- NEW "Delegation vs orchestration: teams and swarms" section for the
  emerging multi-agent class — tmustier/pi-agent-teams, melihmucuk/pi-crew,
  Tiziano-AI/pi-multiagent, messense/pi-parallel-agents, pi-zerg-swarm,
  @llblab/pi-actors, teelicht/pi-superagents, MasuRii/pi-agent-router.
- Sharpened "Inspecting a subagent: the full-view problem" — mux pane vs
  in-process+JSONL vs subprocess-persisted vs tintinweb's truncated modal.
  Added ross-jill-ws/pi-subagent-in-memory (in-process, persona-free, full
  events.jsonl) and a "running two systems at once" note.
- Fixed stale facts: tintinweb #75 FIXED (PR #74, v0.8+ line); nicobailon
  #80 and RFC #552 are closed, not live. Stripped volatile
  star/download/version numbers (kept LOC as a structural signal); adoption
  is now qualitative tiers + evaluation.md pointer.
- Added gotgenes/pi-subagents (tintinweb fork).
Sources +7; index + README descriptions synced.

Verification pass (source-read of nicobailon, tintinweb v0.10, HazAT,
pi-subagent-in-memory, aleclarson) corrected two claims:
- tintinweb's spawn tool is `Agent` (+ get_subagent_result / steer_subagent),
  NOT Claude Code's `Task`. Recast the tool-naming section and dropped the
  "verbatim / strong-priors" overclaim. tintinweb is in-process +
  `SessionManager.inMemory`, so its children are not resumable sessions.
- nicobailon runs children as real `pi --session <file>` (pi-args.ts), so
  per-child sessions are genuine RESUMABLE Pi sessions, not just an
  events.jsonl log — corrected the entry and the inspection table.
Also softened aleclarson's fork claim (the --session snapshot feeds context
in; the child's own session persistence is unconfirmed).
- Second pass: corrected LOC drift (HazAT entry ~8k→~5k src; tintinweb
  ~6k→~7k); added amosblomqvist/pi-subagents (★107, a coverage gap —
  minimal Pattern 1 subprocess) and jwangkun/Pi-Multi-Agent to orchestration;
  pinned the `cmux` backend to craigsc/cmux. Lint clean; no private leak.
