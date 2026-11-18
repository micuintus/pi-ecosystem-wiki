---
title: Pi Figma Extensions
type: ecosystem
updated: 2026-11-18
sources:
  - pi-figma-kit
  - pi-figma-mcp
  - pi-figma-remote-auth
  - pi-mono-figma
  - runkids-figlens
tags: [extension, figma, design, mcp]
entries:
  - id: pi-figma-kit
    name: pi-figma-kit
    repo: sorinirimies/pi-figma-kit
    npm: pi-figma-kit
    role: figma-pick
    notes: "Code-read. 35 figma_* tools plus /figma: file exploration, CSS-annotated design trees, renders, asset and token export, HTML/React/Tailwind/Compose scaffolds. REST-direct, no server process; optional desktop bridge for live selection. 13 test files including fuzz, security audit workflow. Installed and verified: tools register in a fresh session."
  - id: pi-figma-mcp
    name: pi-figma-mcp
    repo: Semjuel19/figma-mcp-pi
    npm: pi-figma-mcp
    role: figma-shim
    notes: "Catalog-level, not code-read. Connects Pi to the Figma desktop MCP server. 0 stars, untouched since April, no tests."
  - id: pi-figma-remote-auth
    name: pi-figma-remote-auth
    repo: DianP/pi-figma-remote-auth
    npm: pi-figma-remote-auth
    role: figma-shim
    notes: "Catalog-level, not code-read. OAuth and config for Figma's hosted remote MCP, used with pi-mcp-adapter. No tests."
  - id: runkids-figlens
    name: "@runkids/figlens"
    repo: runkids/figlens
    npm: "@runkids/figlens"
    role: figma-offline
    notes: "Code-read (adapters only). Builds screens from a saved .fig, offline: no Dev Mode seat, login or quota. Rust core with integration tests, Pi/OpenCode adapters with JS tests. Different tool from the live-file pick: no live access."
  - id: pi-mono-figma
    name: pi-mono-figma
    npm: pi-mono-figma
    role: superseded
    notes: "Repository deleted (404); npm tarball from May remains. Do not install."
---

# Pi Figma Extensions

Five packages in three shapes: live-file tools, MCP shims, and one
offline builder. No dedicated page existed because Figma access used
to mean the MCP server; `pi-figma-kit` changed that by talking to the
REST API directly.

## The pick

`pi-figma-kit` for anything against a live file: 35 tools, design
trees, renders, tokens, scaffolds. Verified in a fresh session here
(`figma_compare`, `figma_desktop_selection` and siblings register).
Scope its personal access token to view-only on the files you need:
file contents flow through model context.

## The rest

MCP shims (`pi-figma-mcp` for the desktop server,
`pi-figma-remote-auth` for the hosted one) are glue, not picks: thin,
untested, barely starred. `@runkids/figlens` is the offline
alternative when there is no API access at all. `pi-mono-figma` is
dead, repo gone.
