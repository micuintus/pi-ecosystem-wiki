---
title: How to Evaluate a Pi Extension
type: reference
updated: 2026-05-08
sources:
  - pi-dev-packages
  - qualisero-awesome-pi-agent
tags: [reference, evaluation, quality, methodology]
---

# How to Evaluate a Pi Extension

This wiki deliberately does **not** bake live numbers into pages —
they go stale within weeks. Instead, every survey page lists each
extension with stable machine-readable identifiers (`repo:`, `npm:`)
in its frontmatter so you (or an agent) can query the signals you
care about at the moment you care about them.

This page defines the signals and gives copy-pasteable recipes.

## Three tiers of signal

| Tier | Cost | What it tells you | When to run |
|---|---|---|---|
| **Vital signs** | Two API calls (~1s) | Is it alive? Is anyone using it? | Always, before considering an extension |
| **Maintenance signals** | A few API calls + light reading (~1min) | Is it likely to keep working as Pi evolves? | When narrowing 2–3 candidates |
| **Code quality signals** | Clone + inspect (~5–15min) | Is it safe to install? Will it break things? | Before installing into a real workflow |

Match the depth to the stakes. Don't audit a one-off TODO widget the way you'd audit something that intercepts every tool call.

## Tier 1 — Vital signs

The bare minimum. Cheap, scriptable.

| Signal | Why it matters | Source |
|---|---|---|
| **Last commit / push date** | Pi's internal API moves fast; extensions break on Pi updates. >6 months stale on a moving target = assume broken. **Single most important filter.** | `gh api repos/<owner>/<repo> --jq .pushed_at` |
| **GitHub stars** | Hype-biased and lagging, but useful as a tie-breaker between two similar options | same call, `.stargazers_count` |
| **Weekly npm downloads** | Real adoption signal. Beware: bundle packages (e.g., mitsupi) report combined downloads | `curl -s https://api.npmjs.org/downloads/point/last-week/<pkg> \| jq .downloads` |
| **Contributors** | Bus factor. 1 contributor = single point of failure | `gh api repos/<owner>/<repo>/contributors --jq 'length'` |

### Maturity tag (derived from last push)

| Tag | Meaning |
|---|---|
| `[active]` | Commit within the last month |
| `[stable]` | Commit within ~6 months, no recent activity |
| `[experimental]` | Single-author, no releases, recent commits |
| `[stale]` | No commits in >6 months — assume broken on current Pi |
| `[fork-of-X]` | Soft-forked from another extension — check whether the parent is more active |

### Fast recipe

```bash
# Vital signs for one extension
REPO=owner/name
PKG=npm-package-name

gh api repos/$REPO --jq '{stars:.stargazers_count, pushed:.pushed_at, forks:.forks_count}'
curl -s https://api.npmjs.org/downloads/point/last-week/$PKG | jq .downloads
```

## Tier 2 — Maintenance signals

Once you've filtered to a shortlist, check whether the project is built to last.

| Signal | What "good" looks like | Source |
|---|---|---|
| **Release discipline** | Tagged releases with semver, CHANGELOG present | `gh api repos/$REPO/releases` |
| **Open vs closed issues ratio** | Closed > open, recent issues responded to | `gh issue list --state all --json state` |
| **Maintainer response time on issues** | Days, not months | Manual scan |
| **Featured in `qualisero/awesome-pi-agent`** | Curated list = peer-reviewed quality filter | `gh search code --repo qualisero/awesome-pi-agent <name>` |
| **Pi version compatibility stated** | README mentions which `@earendil-works/pi-coding-agent` versions it targets | README scan |

A project with 1k⭐ but no releases tagged in a year is a worse bet than a 30⭐ project with monthly tagged releases and a CHANGELOG.

## Tier 3 — Code quality signals

Run only when you're about to install into a real workflow, especially
for extensions that:

- Intercept every tool call (rendering, footer, hashline extensions)
- Run as subagents or spawn subprocesses
- Read or write outside the working directory
- Touch credentials, env vars, or auth state

### Static signals (read-only inspection)

| Signal | Look for | Why |
|---|---|---|
| **License** | MIT / Apache-2.0 in `LICENSE` | Some "open" repos are unlicensed = not safe to fork |
| **TypeScript strict mode** | `"strict": true` in `tsconfig.json` | Strict TS catches a class of bugs that ship in lax projects |
| **Tests present and run in CI** | `test/` or `*.test.ts` + a `.github/workflows/*.yml` that runs them | Untested extensions break silently on Pi upgrades |
| **README has install + config docs** | Concrete install command, config keys explained | A bare README is a smell |
| **`package.json` hygiene** | `repository`, `bugs`, `homepage`, `keywords` filled; `engines` field if Node-version-sensitive | Signals professional packaging |
| **Pinned vs ranged dependencies** | Pinned for tools, ranged for libraries — match expectation | Loose pinning on dev tools is fine; loose pinning on `@earendil-works/pi-coding-agent` itself is a warning |
| **Dependency footprint** | Reasonable size relative to feature set | A "rendering" extension pulling 200 deps is suspicious |
| **No bundled binaries / postinstall scripts** | Inspect `package.json` `scripts` for `postinstall` | Postinstall is a known supply-chain attack vector |

### Dynamic signals (require running)

| Signal | How |
|---|---|
| **Builds cleanly** | `npm install && npm run build` (or whatever the project's build command is) |
| **Tests pass on your Node version** | `npm test` |
| **Bundle size sanity** | `du -sh node_modules` after install — outliers suggest dependency creep |
| **Runs without runtime errors against current Pi** | `pi install <repo>` then run a typical session and watch for `pi.on(...)` failures |

### Recipe — quick code-quality scan

```bash
git clone --depth 1 https://github.com/$REPO /tmp/audit && cd /tmp/audit

# Fast static checks
cat LICENSE 2>/dev/null | head -1
jq '.license, .repository, .scripts.postinstall' package.json
jq '.compilerOptions.strict' tsconfig.json 2>/dev/null
ls test/ tests/ __tests__/ 2>/dev/null
ls .github/workflows/ 2>/dev/null
wc -l README.md
```

## What this wiki does and doesn't promise

**Does:**

- Group extensions by use case so you have a meaningful shortlist
- Capture stable identifiers (`repo:`, `npm:`) in frontmatter so signal-querying is one command
- Editorialize on architectural patterns and trade-offs that don't decay (e.g., "PTY-embed external CLI" vs "in-process iteration")
- Flag known-stale or known-broken entries when discovered

**Does not:**

- Pretend to have current download/star numbers — those are queries, not facts
- Pre-run code-quality audits across the whole catalog — that's per-reader, per-stake
- Replace the upstream catalogs ([catalogs.md](catalogs.md)) for raw discovery

## See also

- [Pi Ecosystem Catalogs and Awesome-Lists](catalogs.md) — where the entries come from in the first place
- [SCHEMA.md](../SCHEMA.md) — the `entries:` frontmatter convention
