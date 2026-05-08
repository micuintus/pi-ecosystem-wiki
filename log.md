# Log

Append-only. Newest at top.

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
- Compiled: ecosystem/footer-and-hashline-extensions.md (consolidates footer-themes.md and pi-hashline-edit-tools.md from private wiki).
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
