---
title: Pi Compaction Extensions
type: ecosystem
updated: 2026-05-28
sources:
  - pi-mono
  - pi-mono-custom-compaction-example
  - pi-vcc
  - pi-observational-memory
  - pi-observational-memory-fork-githubfoxy
  - pi-blackhole
  - pi-smart-compact
  - pi-agentic-compaction-whamp
  - pi-agentic-compaction-salemsayed
  - pi-omni-compact
  - pi-dcp
  - pi-dynamic-context-pruning-complexthings
  - pi-context-prune
  - pi-grounded-compaction
  - pi-memctx
  - pi-custom-compactor
tags: [extension, compaction, memory, context-management]
entries:
  - id: pi-mono-custom-compaction
    name: "pi-mono examples/extensions/custom-compaction.ts"
    repo: earendil-works/pi-mono
    role: reference-impl
    notes: "Stock example. Replaces default with full-context summary, swaps in a cheaper model (e.g. Gemini Flash). Discards all old turns, keeps only summary. The default behavior baseline that every extension below diverges from."
  - id: pi-vcc
    name: pi-vcc
    repo: sting8k/pi-vcc
    npm: "@sting8k/pi-vcc"
    role: algorithmic-no-llm
    notes: "Inspired by lllyasviel/VCC (View-oriented Conversation Compiler). Zero LLM calls — extraction + formatting. Splits at last user message; everything after stays intact; older portion summarized into bracketed sections (Session Goal / Files And Changes / Commits / Outstanding Context / User Preferences) plus a rolling brief transcript with `(#N)` tool refs. Bounded merge across compactions: sticky sections (Goal, Preferences) carry forward, volatile sections (Outstanding Context) replace, accumulating sections (Files, Commits) union without duplicates, transcript rolls. Lossless `vcc_recall` tool reads raw JSONL; supports regex + BM25-style OR ranking; default scope=active lineage. `overrideDefaultCompaction` toggle routes Pi's `/compact` and auto-threshold paths through vcc too. `/pi-vcc` and `/pi-vcc-recall` slash commands. **Packaging-hygiene caveat:** no LICENSE file present in the repo and `"license"` is `null` in `package.json` — the README is open and the maintainer accepts PRs, but the missing license is a blocker for commercial/policy-gated installs until fixed."
  - id: pi-observational-memory
    name: pi-observational-memory
    repo: elpapi42/pi-observational-memory
    npm: pi-observational-memory
    role: observation-ledger
    notes: "V3 memory model. Continuously runs three background workers — observer (extracts timestamped events/decisions), reflector (distills durable reflections), dropper (prunes the active-observation pool under a token budget, coverage-aware). Memory work happens during the session so compaction is a fast render step, not a slow summarization. Session ledger survives compactions; observations and reflections carry hex ids; `recall` tool recovers source evidence by id. Coverage stewardship (none/partial/strong tiers) governs reflector support-id selection. Hooks Pi's compaction path."
  - id: pi-observational-memory-foxy
    name: pi-observational-memory (GitHubFoxy fork)
    repo: GitHubFoxy/pi-observational-memory
    role: observation-ledger-variant
    notes: "Fork. Directory extension, explicit command registration, fallback-safe hooks (default compaction stays available). Reflector GC runs when observation-block token estimate crosses threshold (~40k default). Preserves kept-tail. `/obs-memory-status` command."
  - id: pi-blackhole
    name: pi-blackhole
    repo: k0valik/pi-blackhole
    npm: pi-blackhole
    role: frankenmerge-vcc-plus-om
    notes: "Frankenmerge of pi-vcc and pi-observational-memory under unified config. Resolves the conflict where OM hooked default compaction and prevented vcc from running. Adds per-worker model fallback chains (observer/reflector/dropper each have ordered primary→fallback→session lists), persisted cooldowns at `~/.pi/agent/pi-blackhole/pi-blackhole-cooldown.json`, manual flush mode (`noAutoCompact: true` — observations spool to `pending.json`, compaction only fires on `/blackhole`), `/blackhole om-off` toggle, `PI_BLACKHOLE_PASSIVE=true` env kill-switch. Configuration presets for low (~32k) / medium (~128k) / high (~200k+) context budgets. Tracks both upstreams via a lockstep audit skill (`.pi/skills/lockstep/`) classifying each upstream commit as safe-to-port / modified / rewritten / orphan."
  - id: pi-smart-compact
    name: pi-smart-compact
    repo: alpertarhan/pi-smart-compact
    role: structured-pipeline
    notes: "Structured compaction pipeline preserving goal / modified files / unresolved errors / decisions / constraints / open follow-up loops. Cites 'agentic compaction' (let the system inspect and reason) and 'Kamradt-style chunking' (segment large conversations before synthesis) as design references."
  - id: pi-agentic-compaction-whamp
    name: pi-agentic-compaction (Whamp)
    repo: Whamp/pi-agentic-compaction
    role: agentic-virtual-fs
    notes: "Mounts the conversation as JSON at `/conversation.json` in a virtual filesystem. Spawns a summarizer subagent with sandboxed bash/jq/grep/head/tail tools. Summarizer follows a structured exploration strategy (e.g. inspect end window, find file ops, etc.) before producing the summary. Tool-driven exploration replaces one-shot prompting."
  - id: pi-agentic-compaction-salemsayed
    name: pi-agentic-compaction (salemsayed)
    repo: salemsayed/pi-agentic-compaction
    npm: pi-agentic-compaction
    role: agentic-virtual-fs
    notes: "npm-published variant of the same agentic-vfs pattern — virtual filesystem + shell-tool-driven summarizer subagent replacing pi's default compaction pass."
  - id: pi-omni-compact
    name: pi-omni-compact
    repo: Whamp/pi-omni-compact
    role: large-context-subprocess
    notes: "Replaces default compaction with a subprocess that spawns a separate pi instance using a *large-context* model that reads the entire conversation at once, producing higher-fidelity summaries than the active model could. settings.json configures which models to try."
  - id: pi-dcp
    name: pi-dcp (Dynamic Context Pruning)
    repo: PSU3D0/pi-dcp
    role: tool-output-pruning
    notes: "Aggressively (but safely) prunes stale, duplicate, and oversized tool outputs from the LLM context window without mutating local session history. Targets the bloat from huge file reads, bash stack traces, repeated `ls` calls. Pruning is a context-window-only operation; on-disk session is untouched."
  - id: complexthings-pi-dcp
    name: "@complexthings/pi-dynamic-context-pruning"
    npm: "@complexthings/pi-dynamic-context-pruning"
    role: compress-tool-plus-nudges
    notes: "LLM-callable `compress` tool that replaces stale conversation ranges with exhaustive technical summaries, preserving fidelity at fraction of the tokens. Plus context-nudge injections at configurable thresholds — soft housekeeping notices, strong emergency warnings — and dedup. Compression is *agent-driven* rather than hook-driven."
  - id: pi-context-prune
    name: pi-context-prune
    repo: championswimmer/pi-context-prune
    role: tool-call-tree-prune
    notes: "Summarizes completed tool-call batches and prunes raw tool outputs from future LLM context. Exposes a `context_tree_query` escape hatch so the agent can recover any original output on demand. Operates on tool-call trees rather than raw token sweep."
  - id: pi-custom-compactor
    name: pi-custom-compactor
    repo: davidorex/pi-custom-compactor
    role: yaml-declared-extraction
    notes: "Hooks `session_before_compact`. Compaction behavior is declared in YAML specs: each spec lists named **extracts**, each extract is either *mechanical* (regex / tool-call inspection, no LLM) or *llm-based* (via `complete()` from `@mariozechner/pi-ai`). Writes JSON artifacts to disk and composes them into the final summary. Multiple specs coexist for different work modes; falls back to default compaction on failure. Same family as pi-vcc (bracketed-sections shape) but with the section list and extraction logic moved out of code into config."
  - id: pi-grounded-compaction
    name: pi-grounded-compaction
    npm: pi-grounded-compaction
    role: model-presets-plus-files-touched
    notes: "Replaces Pi's compaction summarizer with configurable model presets and custom summarization prompt contracts. Distinctive: deterministic files-touched tracking covering Pi native tools, RepoPrompt, and bash-derived file operations. Augments `/tree` branch summarization with the same files-touched grounding."
  - id: pi-memctx
    name: pi-memctx
    npm: pi-memctx
    role: project-memory-layer
    notes: "Not a compactor — a local, durable, Markdown-native memory layer. Searches project memory before each prompt, injects only compact/relevant context, learns durable discoveries after turns. No DB server, no hosted memory vendor. Adjacent to compaction: reduces what *has* to live in the active context."
---

# Pi Compaction Extensions

Pi's default compaction asks an LLM to rewrite the older portion of
the conversation into a free-form prose summary. That works for one
or two cycles, but each subsequent compaction is summarizing a
summary — load-bearing details (why a decision was made, what was
already rejected, what the user clarified) erode away. The pause
while the summary is generated also breaks flow, especially on long
sessions.

The ecosystem has converged on a small handful of structural answers,
each replacing or augmenting a different part of the default path.

## Picking the right layer

Before reading the strategy taxonomy, decide which problem you
actually have. The strategies below solve different things and only
one of them is the answer to *"give me `/compact`, but better"*.

| What you actually want | Pick |
|---|---|
| **A drop-in better `/compact`** — same UX, sharper output, no new concepts to learn | [`pi-vcc`](https://github.com/sting8k/pi-vcc) with `overrideDefaultCompaction: true`. Algorithmic, deterministic, free, fast, and merges cleanly across repeated compactions. Mind the LICENSE caveat for commercial use. |
| **A drop-in better `/compact`, license hygiene must be clean** | [`pi-grounded-compaction`](https://www.npmjs.com/package/pi-grounded-compaction). Keeps the LLM path — lower payoff but properly packaged. |
| **Durable memory across many compactions and days** | [`pi-observational-memory`](https://github.com/elpapi42/pi-observational-memory). The observation ledger is the load-bearing piece. |
| **Both of the above in one extension** | [`pi-blackhole`](https://github.com/k0valik/pi-blackhole). The frankenmerge — don't install it just for sharper compaction, install it when you also want the ledger. |

The full strategy taxonomy and recommendation matrix below cover the
rest of the design space (tool-output pruning, agentic-VFS, large-context
subprocess, etc.).

## Strategies

Six recognizable patterns, ordered roughly from "least LLM" to "most
LLM":

1. **Algorithmic / extractive** — no LLM call. Regex extraction +
   formatting + rolling brief transcript. Deterministic, free, fast.
   Stays useful indefinitely but the rendered output is still a
   summary, so detail erodes if it's the *only* memory layer.
   `pi-vcc` is the canonical example.
2. **Observation ledger (work-ahead memory)** — capture observations
   and reflections in the background *while the session runs*, store
   them in a session ledger that survives compactions, surface them
   on next compaction as structured `[id]`-tagged bullets the agent
   can `recall`. Compaction itself becomes a fast render step.
   `pi-observational-memory` (and its Foxy fork) define the pattern.
3. **Combined (algorithmic compaction + observation ledger)** —
   `pi-vcc` in the compaction slot, `pi-observational-memory` in the
   memory layer, sharing one hook with conflict resolution and
   unified config. This is `pi-blackhole`.
4. **Tool-output pruning** — leave the conversation prose alone; just
   strip stale / duplicate / oversized *tool outputs* from the
   context window. The on-disk session is untouched; the agent gets a
   query hatch to recover originals on demand. `pi-dcp`,
   `pi-context-prune`, `@complexthings/pi-dynamic-context-pruning`.
5. **Agentic compaction (subagent with tools)** — spawn a summarizer
   subagent and give it shell tools (`jq`, `grep`, `head`, `tail`)
   over the conversation mounted as a virtual filesystem. The agent
   inspects before it summarizes. `pi-agentic-compaction` (both
   variants). A close cousin: route compaction to a *large-context*
   model in a subprocess that can read the whole conversation in one
   shot — `pi-omni-compact`.
6. **Configurable LLM compaction with grounding** — keep the default
   LLM path but pin the model, the prompt contract, and a
   deterministic files-touched index. `pi-grounded-compaction`.

A seventh pattern is adjacent rather than a compactor:
**project-memory layer** (`pi-memctx`) — keeps durable facts in
Markdown files outside the conversation and injects only what's
relevant per turn, reducing the volume of state that compaction has
to deal with at all.

## Recommendation matrix

| Situation | Default pick | Why |
|---|---|---|
| **Long multi-day sessions, want both speed and durable memory** | [`pi-blackhole`](https://github.com/k0valik/pi-blackhole) | Algorithmic compaction + observation ledger in one hook, with model fallback chains and a manual-flush mode. Two upstreams stitched together so they stop fighting over the compact hook. |
| **Predictable, free, deterministic compaction; recall is enough** | [`pi-vcc`](https://github.com/sting8k/pi-vcc) | No LLM call ever. ~99% reduction on long sessions, < 500ms. `vcc_recall` covers the "what did we decide three days ago" case. |
| **Long sessions but you want detail-preserving cross-compaction memory** | [`pi-observational-memory`](https://github.com/elpapi42/pi-observational-memory) | Observations/reflections + recall by id. Workers run during the session so compaction is fast. |
| **Conversation prose is fine; tool outputs are bloating context** | [`pi-dcp`](https://github.com/PSU3D0/pi-dcp), [`pi-context-prune`](https://github.com/championswimmer/pi-context-prune), or [`@complexthings/pi-dynamic-context-pruning`](https://www.npmjs.com/package/@complexthings/pi-dynamic-context-pruning) | Cheap, targets the actual bloat source on most sessions, keeps prose intact. |
| **Default compaction is fine in spirit, but the summary is sloppy or omits files** | [`pi-grounded-compaction`](https://www.npmjs.com/package/pi-grounded-compaction) | Pinned model + prompt contract + deterministic files-touched tracking. |
| **Default summary is sloppy because the model is too small for the conversation** | [`pi-omni-compact`](https://github.com/Whamp/pi-omni-compact) | Subprocesses a large-context model so the whole conversation fits in one shot. |
| **You want the summarizer to actually inspect before writing** | [`pi-agentic-compaction`](https://github.com/Whamp/pi-agentic-compaction) | Virtual filesystem + shell-tool-driven summarizer subagent. Slowest, but produces the most reasoned summary. |
| **You don't want compaction to be the memory layer at all** | [`pi-memctx`](https://www.npmjs.com/package/pi-memctx) | Durable Markdown memory outside the conversation; inject only what's relevant per turn. Stack with any of the above. |

## Lineage

`pi-blackhole` is explicit about being a merge:
[`pi-vcc`](https://github.com/sting8k/pi-vcc) (algorithmic
compaction) + [`pi-observational-memory`](https://github.com/elpapi42/pi-observational-memory)
(observation ledger). Both upstreams hooked Pi's default compaction
path and were not co-installable. `pi-blackhole` puts vcc in the
compaction slot and OM in the memory layer, shares the hook, and
adds the things both were missing: per-worker model fallback chains,
persisted cooldowns, a manual-flush mode (`noAutoCompact`), and an
OM kill-switch. It tracks both upstreams via a
[lockstep audit skill](https://github.com/k0valik/pi-blackhole/tree/lockstep/2026-05-27/.pi/skills/lockstep)
that classifies each upstream commit as safe-to-port / modified /
rewritten / orphan, so bugfixes flow downstream without blindly
overwriting deliberate divergences.

The Foxy fork of `pi-observational-memory` is a parallel evolution:
extension-only custom compaction, fallback-safe hooks (default
compaction stays available alongside it), and a `/obs-memory-status`
status command. It does not merge with vcc.

`pi-agentic-compaction` exists as two repos (`Whamp/` and
`salemsayed/`) implementing the same virtual-filesystem-plus-shell
pattern; the salemsayed variant is the npm-published one.

## What pi-blackhole's frankenmerge actually adds

Beyond stitching the two upstreams:

- **Per-worker model config** — observer / reflector / dropper each
  have their own primary model and ordered fallback list, so cheap
  models can do extraction while a stronger model does reflection.
- **Persisted cooldowns** — failed models (rate-limit, timeout, 5xx)
  are cooled down with expiry timestamps in
  `~/.pi/agent/pi-blackhole/pi-blackhole-cooldown.json`. Survives Pi
  restarts. The session model is always the last-resort and is
  never cooled.
- **Manual flush (`noAutoCompact: true`)** — workers still run, but
  observations spool to `pending.json` instead of being injected as
  conversation markers. Compaction only happens on `/blackhole`.
  Cleaner branch, deliberate schedule, the maintainer's own setup.
- **Bi-directional recall** — `#N` transcript expansion shows
  related OM observations/reflections, and OM hex-id recall shows
  the `#N` transcript-entry annotations.
- **Configuration presets** for low (~32k) / medium (~128k — the
  default) / high (~200k+) context budgets; the page rule of thumb
  is `compactAfterTokens` ≈ 60–70% of the model's window.

## See also

- [Loop and Ralph Extensions](loop-extensions.md) — long-running
  sessions are the main driver of compaction quality concerns.
- [Subagent Extensions](subagent-extensions.md) — agentic-compaction
  variants spawn a subagent inside the compactor; same machinery,
  different purpose.
- [References — How to Evaluate a Pi Extension](../references/evaluation.md)
  — for live popularity / maintenance signals on each entry above.
