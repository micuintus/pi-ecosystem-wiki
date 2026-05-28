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
