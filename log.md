# Log

Append-only. Newest at top.

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
- Compiled: ecosystem/evolve-extensions.md (stripped MATS/DACMICU framing; kept pi-autoresearch deep-dive and research-landscape context).
- Updated: index.md.

## [2026-05-08] ingest | Pi TODO List Extensions

- Registered: 3 sources (pi-todo-md, patriceckhart-pi-todo, pi-mono-todo-example).
- Compiled: ecosystem/todo-extensions.md (stripped DACMICU loop sketch).
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
- Compiled: ecosystem/loop-extensions.md (rewritten from private wiki, DACMICU/MetaHarness refs stripped).
- Updated: index.md.

## [2026-05-08] init

- Bootstrap: README, SCHEMA, index, log, raw-sources/index, LICENSE, .gitignore.
