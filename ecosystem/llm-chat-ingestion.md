---
title: Web LLM Chat Ingestion (Claude.ai, ChatGPT, Gemini, Le Chat)
type: ecosystem
updated: 2026-05-08
sources:
  - ai-chat-exporter
  - chat-export
  - chatgpt-exporter
  - obsidian-clipper
  - rebrowser-playwright
  - playwright
tags: [tool, chat-export, browser-automation]
---

# Web LLM Chat Ingestion

How to import a single web LLM conversation (Claude.ai, ChatGPT,
Gemini, Le Chat) into a knowledge base when share links are
unavailable — e.g. business / enterprise tenants disable public
sharing.

## Constraint that shapes the design

Many corporate LLM tenants (Claude Business/Enterprise, ChatGPT
Business/Enterprise, Gemini for Workspace, Le Chat Enterprise) only
allow private or org-internal sharing — no public share URL. None
expose a programmatic "fetch my chat history" API for consumer
products. Anything that ingests a chat must therefore run **inside an
authenticated browser session**.

## Options surveyed

Three families:

### 1. User-triggered platform export

Claude/ChatGPT data export ZIPs, Google Takeout. Works but slow (email
link, hours), full-history only, overkill for a single chat.

### 2. Browser extension / userscript

Runs in your authenticated tab, reads the rendered DOM, writes a `.md`
file.

| Tool | License | Providers | Output | Notes |
|---|---|---|---|---|
| `obsidianmd/obsidian-clipper` | MIT | any (template-driven) | MD + frontmatter | ~4k stars, weekly releases. Universal fallback. |
| `revivalstack/ai-chat-exporter` | MIT | ChatGPT, Claude, Copilot, Gemini, Grok | MD with YAML+TOC | Userscript. Best multi-provider coverage. |
| `pionxzh/chatgpt-exporter` | MIT | ChatGPT only | MD/JSON/HTML | Mature, but reportedly broken on GPT Team workspaces (issue #220). |
| `Trifall/chat-export` | MIT | ChatGPT, Claude | MD/JSON/XML/HTML | Extension (not userscript). Bus factor 1. |

### 3. Browser automation

Drive a real authenticated browser programmatically. Suitable for
batch/CLI workflows where "give me a URL, get a markdown file" is the
target.

## Why automation over extensions for batch use

Extensions can't be triggered cleanly from outside the browser — you
end up clicking through a popup. Automation also opens the door to
batch ingestion of multiple URLs.

## CDP-against-real-Chrome vs Playwright-managed Chromium

`chromium.launchPersistentContext({channel: "chrome"})` with vanilla
`playwright-core` and even patched `rebrowser-playwright-core` (which
hides runtime-detection vectors) is reliably blocked by **Cloudflare
Turnstile on Claude.ai** — clicking the "Verify you are human"
checkbox loops back to the same state.

Working approach: launch a dedicated Chrome with
`--remote-debugging-port=9222 --user-data-dir=~/.chrome-llm-wiki`,
sign in once. Connect via
`chromium.connectOverCDP("http://localhost:9222")`. Real Chrome,
hardware-binding intact, Turnstile passes.

This is also the only path that reliably handles enterprise SSO with
device-trust attestation, since the IdP is checking against a Chrome
install Google itself signed.

## Output shape (typical)

One `.md` per chat under a `raw-sources/conversations/` directory,
with frontmatter:

```yaml
title: "<chat title>"
type: source
source_kind: web-chat
provider: claude
url: https://claude.ai/chat/<uuid>
conv_id: <uuid>
collected: YYYY-MM-DD
```

Body: `## User` / `## Assistant` headings per turn, HTML to Markdown
via Turndown. Claude's "thinking" and artifact blocks can be stripped
or kept depending on the use case.

## Limitations

- DOM selectors rot. `revivalstack` ships overhauls every few months;
  expect the same for any homegrown automation. Keep per-provider
  modules small (~50 LOC) so a fix is a one-line patch.
- One provider tends to be polished at a time; the others fall back to
  generic single-blob HTML extraction via Defuddle/Turndown.
- The dedicated Chrome window must be running when ingesting. Quitting
  it doesn't lose state — the profile persists in its `--user-data-dir`.
