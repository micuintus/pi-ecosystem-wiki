---
title: Anthropic Subscription Auth in Pi
type: ecosystem
updated: 2026-05-25
sources:
  - pi-providers-docs
  - pi-issue-2751
  - pi-discussion-2950
  - pi-mono
  - oh-my-pi
  - anthropic-third-party-end
  - ben-vargas-pi-packages
  - pi-claude-bridge
tags: [auth, anthropic, oauth, billing]
---

# Anthropic Subscription Auth in Pi

Three routes to send requests to Anthropic from Pi, with very
different billing implications.

## Routes

1. **`/login` → Anthropic OAuth (subscription).** Browser OAuth flow,
   tokens in `~/.pi/agent/auth.json`, auto-refreshed. As of April 2026
   this routes to your Claude **extra-usage** add-on bundle, not the
   main Pro/Max/Team budget. Pi's interactive mode warns about this
   explicitly (per-token billing on top of the base subscription).
2. **`ANTHROPIC_API_KEY`.** Pay-as-you-go via the Anthropic Console.
   Pi prefers the env var over OAuth tokens if both are set — unset it
   before `/login` if you want subscription auth.
3. **Foundry (enterprise).** `CLAUDE_CODE_USE_FOUNDRY=1`,
   `FOUNDRY_BASE_URL`, `ANTHROPIC_FOUNDRY_API_KEY`. Anthropic's
   enterprise inference path.

## Why third-party tools can't reach the main subscription budget

On 2026-04-03 Anthropic terminated third-party access to the main
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

## Detection mechanism

Not header-based. Not TLS-fingerprint-based. Anthropic pattern-matches
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
| Use main Pro/Max/Team budget in Pi | Not possible in base Pi today. Use Claude Code directly, or a fork like oh-my-pi that wraps the Claude Code SDK. |
| Subscription auth in Pi at extra-usage rates | `/login` → Anthropic, accept the warning. Make sure `ANTHROPIC_API_KEY` is unset. |
| Pay-as-you-go API | Set `ANTHROPIC_API_KEY`. |
| Enterprise inference | Foundry env vars. |
| OAuth compatibility patching (without forking) | [`@benvargas/pi-claude-code-use`](https://github.com/ben-vargas/pi-packages) — extension-level OAuth compatibility patch; tracks Claude Code auth changes. Less invasive than oh-my-pi but also less capable. |
| Main-subscription budget without forking | [`pi-claude-bridge`](pi-claude-bridge.md) — runs the real Claude Code binary as a subprocess via Anthropic's Agent SDK; same structural trick as oh-my-pi, packaged as a Pi extension. |

## Caveats

The oh-my-pi main-budget route depends on Anthropic's third-party-tool
detection not catching it. Anthropic has tightened that detection at
least once already; the route may stop working at any time without
notice. Treat it as best-effort.

Whether a Pi *extension* (rather than a fork) could provide a
Claude-Code-SDK-based provider without forking is an open thread on
the Pi side. Discussion #2950 suggests no current path inside base Pi
— the SDK injection has historically required fork-level patches.

## See also

- [claude-agent-sdk-pi](claude-agent-sdk-pi.md) — the bridge extension to Anthropic's Agent SDK and the model/billing implications
- [pi-claude-bridge](pi-claude-bridge.md) — downstream extension that uses Claude Code as a Pi provider + AskClaude sub-agent (subscription route as extension, not fork)
- [Pi Ecosystem Catalogs](../references/catalogs.md) — where to find oh-my-pi and other forks
