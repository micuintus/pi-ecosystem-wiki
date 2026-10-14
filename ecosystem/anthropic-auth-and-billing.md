---
title: Anthropic Auth & Billing in Pi
type: ecosystem
updated: 2026-10-13
sources:
  - pi-providers-docs
  - pi-models-docs
  - pi-anthropic-messages-ts
  - pi-interactive-mode-ts
  - support-monthly-api-credits
  - support-agent-sdk-plan
  - claude-code-legal
  - pi-anthropic-auth-architecture
  - gotgenes-pi-packages-issue-883
  - hermes-agent-issue-72171
  - pi-issue-2751
  - pi-discussion-2950
  - pi-mono
  - oh-my-pi
  - anthropic-third-party-end
  - ben-vargas-pi-packages
  - pi-claude-bridge
tags: [auth, anthropic, oauth, billing]
---

# Anthropic Auth & Billing in Pi

Three routes to send requests to Anthropic from Pi, with very
different billing implications.

## Routes

1. **`/login` → Anthropic OAuth (subscription).** Browser OAuth flow,
   tokens in `~/.pi/agent/auth.json`, auto-refreshed. As of April 2026
   this routes to your Claude **extra-usage** add-on bundle, not the
   main Pro/Max/Team budget. Pi's interactive mode warns about this
   explicitly (per-token billing on top of the base subscription).
2. **`ANTHROPIC_API_KEY`.** Pay-as-you-go via the Anthropic Console.
   Since 2026-10-07, Max plans include $100 (5x) or $200 (20x) and Team
   plans $20 or $100 per seat (pooled, capped at $500) of monthly API
   credits, spent through a key from the linked Console organization;
   Pro gets none ([support-monthly-api-credits], [support-agent-sdk-plan]).
3. **Foundry (enterprise).** `CLAUDE_CODE_USE_FOUNDRY=1`,
   `FOUNDRY_BASE_URL`, `ANTHROPIC_FOUNDRY_API_KEY`. Anthropic's
   enterprise inference path.

### Correction: a stored login wins over the env var

This page said Pi prefers `ANTHROPIC_API_KEY` over OAuth tokens. Pi's
credential order is a runtime `--api-key`, then a stored `auth.json`
credential, then `apiKey` from `models.json`, then environment
variables ([pi-models-docs]). To use the key while a login is stored,
run `/logout anthropic` first.

## Why third-party tools can't reach the main subscription budget

On 2026-04-03 Anthropic announced, effective 2026-04-04, the end of
third-party access to the main
Claude subscription budget. Their announcement: "Starting tomorrow at
12pm PT, Claude subscriptions will no longer cover usage on
third-party tools like OpenClaw. You can still use these tools with
your Claude login via extra usage bundles (now available at a
discount), or with a Claude API key."

Pre-April-2026, tools like opencode, OpenClaw, and oh-my-pi could
reverse-engineer the Claude Code OAuth flow and route requests through
the main budget at ~5–10× lower effective cost than pay-as-you-go API.
Anthropic patched the gateway and now issues clear errors to
unauthorized clients.

Later changes (the paused Agent SDK billing change, the legal-page
wording on subscription OAuth, and monthly API credits for Max and
Team) are dated in
[Status, October 2026](claude-subscription-extensions.md#status-october-2026).

## Detection mechanism

### Correction: the system prompt is one signal of several

The text below names system-prompt matching as the whole mechanism.
By October 2026, extension and harness authors had measured several
independent triggers of the third-party classification: a missing
Claude Code billing-header block in `system` (a 28 KB Pi prompt failed
without it and passed with it), a cumulative score over harness
vocabulary in `system` (two phrases of Pi's own `docs` line together
trip it), and tool names outside Claude Code's set. Separately, new
models refuse a `cc_version` below a per-model floor with
`claude_code_version_too_old` ([pi-anthropic-auth-architecture],
[gotgenes-pi-packages-issue-883], [hermes-agent-issue-72171]). Pi core
already sends Claude Code's transport identity for OAuth tokens
([pi-anthropic-messages-ts]). The full evidence table is in
[Claude Pro/Max Subscription Extensions](claude-subscription-extensions.md#status-october-2026).

The original analysis: not header-based. Not TLS-fingerprint-based. Anthropic pattern-matches
the **system prompt content** against Claude Code's known prompts.
Sending Claude Code's exact system prompt → routed to main budget;
sending a custom prompt → blocked or routed to extra-usage.

This is why user-agent and `anthropic-beta` header tricks don't work
on their own. Pi merged a user-agent fix (PR #1677) but requests still
land on extra-usage. The user-agent change is necessary but not
sufficient.

## How oh-my-pi appears to differ

Inferred from oh-my-pi's repo structure; confirmation requires reading
`packages/ai/src/providers/claude.ts` in that fork.

- Has a separate `./claude` provider module alongside `./anthropic`.
  Strong signal that it wraps the **Claude Code SDK** (`query()` /
  `claude -p` subprocess) rather than calling `api.anthropic.com`
  directly with an OAuth token. From Anthropic's perspective, that
  *is* Claude Code, so the main-budget path is legitimately open.
- Bundles a current Claude Code version.
- System prompt compatible with Claude Code's pattern (not directly
  verified — most load-bearing claim).

## Practical answer

| Goal | Route |
|---|---|
| Use main Pro/Max/Team budget in Pi | Not officially available to third-party tools since 2026-04-04. Unofficial routes: Claude Code directly, a fork like oh-my-pi that wraps the Claude Code SDK, or the Shape C extension [`pi-anthropic-oauth`](claude-subscription-extensions.md) (full provider replacement that impersonates CC). All are best-effort and may break or violate Anthropic's terms. |
| Subscription auth in Pi at extra-usage rates | `/login` → Anthropic, accept the warning. A stored login takes precedence over `ANTHROPIC_API_KEY` ([pi-models-docs]). |
| Pay-as-you-go API | Set `ANTHROPIC_API_KEY` (and `/logout anthropic` if a login is stored). |
| Max or Team plan, without the third-party classifier | Claim the monthly API credits into a Console organization and use a key from it. |
| Enterprise inference | Foundry env vars. |
| Use an extension instead of a raw route | See the [extension survey](claude-subscription-extensions.md): `pi-anthropic-auth` (Shape A, billing block plus prompt shaping on Pi's transport) for the smallest blast radius, `pi-claude-bridge` (Shape B) for Claude Code's own features, or Shape C providers that replace Pi's transport. |

For the full survey of extensions across all three shapes (payload-
patcher, provider-proxy, provider-replacement), with code-read
findings on token economics and leakage surface, see
[Claude Pro/Max Subscription Extensions](claude-subscription-extensions.md).

## Caveats

The oh-my-pi main-budget route depends on Anthropic's third-party-tool
detection not catching it. Anthropic has tightened that detection at
least once already; the route may stop working at any time without
notice. Treat it as best-effort.

Whether a Pi *extension* (rather than a fork) could provide a
Claude-Code-SDK-based provider without forking was once an open
thread on the Pi side (Discussion #2950). It's now resolved in
practice: `claude-agent-sdk-pi` and its dominant fork
`pi-claude-bridge` ship that path as a regular Pi provider via
`pi.registerProvider()` + `query()` from
`@anthropic-ai/claude-agent-sdk`. The payload-patcher route
(`pi-claude-code-use`) sidesteps the question entirely by staying on
Pi's native Anthropic transport.

## See also

- [Model Routing, Fallback and Usage-Limit Recovery Extensions](model-routing-extensions.md): what happens when the subscription limit hits
- [Claude Pro/Max Subscription Extensions](claude-subscription-extensions.md) — the full survey of extensions across all three shapes, with picking guide and code-read findings
- [claude-agent-sdk-pi](claude-agent-sdk-pi.md) — the bridge extension to Anthropic's Agent SDK and the model/billing implications
- [pi-claude-bridge](pi-claude-bridge.md) — downstream extension that uses Claude Code as a Pi provider + AskClaude sub-agent (subscription route as extension, not fork)
- [Pi Ecosystem Catalogs](../references/catalogs.md) — where to find oh-my-pi and other forks
