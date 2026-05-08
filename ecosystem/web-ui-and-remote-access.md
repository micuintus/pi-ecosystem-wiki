---
title: Pi Web UI and Remote Access Extensions
type: ecosystem
updated: 2026-05-08
sources:
  - pi-web-ui-package
  - qroy-pi-remote
  - noahsaso-pi-remote
  - VVander-pi-remote-web-ui
  - sleepingrobots-pi-web-ui
tags: [extension, web-ui, remote, mobile]
entries:
  - id: pi-web-ui
    name: "@mariozechner/pi-web-ui"
    repo: badlogic/pi-mono
    npm: "@mariozechner/pi-web-ui"
    role: library
    notes: "Library of Lit web components for AI chat UIs. Lives in pi-mono itself. Build on it; not installable as an extension."
  - id: qroy-pi-remote
    name: "@q.roy/pi-remote"
    repo: ruanqisevik/pi-mono-extensions
    npm: "@q.roy/pi-remote"
    role: remote-terminal-original
    notes: "The original WebSocket+browser remote terminal. Eclipsed by noahsaso fork for active use."
  - id: noahsaso-pi-remote
    name: "@noahsaso/pi-remote"
    repo: noahsaso/pi-remote
    npm: "@noahsaso/pi-remote"
    role: remote-terminal-tailscale
    notes: "Active fork of @q.roy/pi-remote with Tailscale HTTPS, per-session routes, token auth, mobile-friendly UI."
  - id: pi-remote-web-ui
    name: pi-remote-web-ui
    repo: VVander/pi-remote-web-ui
    role: remote-terminal-ssh
    notes: "SSH-tunnel-only remote terminal. Server binds 127.0.0.1; reach via existing SSH. Single in-process AgentSession shared across tabs."
  - id: sleepingrobots-pi-web-ui-showcase
    name: Pi Web UI by Sleeping Robots
    repo: sleepingrobots
    role: showcase
    notes: "Full-stack showcase wiring pi-web-ui components to a Node server; reference implementation for the embedded library."
---

# Web UI and Remote/Mobile Access

Options for accessing Pi from a browser or mobile device. Pi is
primarily a TUI; "use Pi from a phone" or "open Pi like opencode in a
browser" requires either an upstream package or a community remote
extension.

Two distinct shapes:

1. **Embedded library** — components for building your own Pi-powered
   chat UI in a web app.
2. **Remote terminal** — run Pi on a server, attach a browser as a
   remote terminal.

## Embedded: `@mariozechner/pi-web-ui`

Lives inside `pi-mono` itself at
[`packages/web-ui`](https://github.com/badlogic/pi-mono/tree/main/packages/web-ui).
**Not** an extension — a publishable npm library of reusable web UI
components for AI chat interfaces.

- Lit-based web components, Tailwind CSS v4
- Powered by `@mariozechner/pi-ai` and `@mariozechner/pi-agent-core`
- Features: chat UI with history/streaming/tool execution, JS REPL,
  document extraction, artifacts (HTML/SVG/Markdown), file
  attachments (PDF, DOCX, XLSX, PPTX, images)
- Direct Mode (browser → LLM) or Server Mode (browser → your server →
  LLM)

This is what you build *with*, not what you install. A community
showcase using it is
[Pi Web UI by Sleeping Robots](https://sleepingrobots.com/dreams/pi-web-ui/) —
a full-stack web app wiring `pi-web-ui` components to a Node server
that runs `createAgentSession()` with system tools, exposed via
WebSocket.

## Remote terminal: WebSocket + browser

Run Pi as a process on a server (or your laptop) and attach via a
browser. Two community options:

### `@q.roy/pi-remote` (`ruanqisevik/pi-mono-extensions`)

The original. Remote terminal access for Pi via WebSocket and
browser. Single repo, simple binding model.

### `@noahsaso/pi-remote`

Active fork of `@q.roy/pi-remote` with hardening:

- **Tailscale HTTPS** serving with per-session `/pi/{id}/` routes —
  no need to expose ports to the public internet
- **Token auth enforcement** — every connection authenticated
- **Discovery service** at `/pi/` for switching between active
  sessions
- **Mobile-friendly browser UI** — explicitly designed for phone use
- UI improvements over the upstream

### `VVander/pi-remote-web-ui`

Different architecture: SSH-tunnel-only. The server **only binds to
`127.0.0.1`** and is never reachable directly from the internet. You
expose it through your existing SSH connection.

```
Browser tabs (localhost:8080)
  │
  │ SSH tunnel
  └─► pi-remote-web-ui server (127.0.0.1:8080) ← binds here only
        │
        ├─► AgentSession (in-process, shared across all tabs)
              Uses Pi SDK directly (createAgentSession)
```

This trades Tailscale's mesh model for "if you trust SSH you trust
this." Single in-process `AgentSession` shared across all browser
tabs — different from `@noahsaso/pi-remote`'s per-session routes.

## Comparison

| Project | Type | Architecture | Auth model | Mobile UX |
|---|---|---|---|---|
| `@mariozechner/pi-web-ui` | Library | Components only | Your responsibility | Your responsibility |
| `@q.roy/pi-remote` | Remote terminal | WebSocket | None / minimal | Basic |
| `@noahsaso/pi-remote` | Remote terminal | WebSocket + Tailscale | Token auth + Tailscale ACLs | Designed for it |
| `VVander/pi-remote-web-ui` | Remote terminal | SSH tunnel + 127.0.0.1 bind | Trust SSH | Phone via SSH-capable client |

## Where this differs from opencode

OpenCode's web/mobile story is built into the project itself —
running `opencode serve` exposes a browser-runnable session by default.
Pi's web/mobile story is **library + community extensions**: Pi ships
the components and the SDK; the community ships the deployable remote
servers.

This means more variation but also more responsibility on the user
side: there is no single "open Pi in your phone browser" command.
Pick `@noahsaso/pi-remote` if you want Tailscale,
`VVander/pi-remote-web-ui` if you want SSH-only, or build on
`@mariozechner/pi-web-ui` if you need full UX control.

## See also

- [`pi.dev/packages`](https://pi.dev/packages) — the official Pi
  package catalog includes other browser-adjacent projects (e.g.
  `pi-studio` two-pane prompt/response workspace,
  `pi-agent-browser-native` for browser automation).
