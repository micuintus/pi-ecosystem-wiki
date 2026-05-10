---
title: How to Evaluate a Pi Extension
type: reference
updated: 2026-05-08
sources:
  - pi-dev-packages
  - qualisero-awesome-pi-agent
  - github-rest-api
  - npm-downloads-api
tags: [reference, evaluation, quality, methodology]
---

# How to Evaluate a Pi Extension

## Contents

- [Three tiers of signal](#three-tiers-of-signal)
- [Tier 1 — Project health](#tier-1--project-health-highest-priority)
- [Tier 2 — Community sentiment](#tier-2--community-sentiment)
- [Tier 3 — Code quality signals](#tier-3--code-quality-signals)
- [What this wiki does and doesn't promise](#what-this-wiki-does-and-doesnt-promise)
- [See also](#see-also)

This wiki deliberately does **not** bake live numbers into pages —
they go stale within weeks. Instead, every survey page lists each
extension with stable machine-readable identifiers (`repo:`, `npm:`)
in its frontmatter so you (or an agent) can query the signals you
care about at the moment you care about them.

This page defines the signals and gives copy-pasteable recipes.

## Three tiers of signal

| Tier | Cost | What it tells you | When to run |
|---|---|---|---|
| **Project health** | Two API calls (~1s) per source | Is it alive? Is anyone using it? Will it still work next month? | Always, before considering an extension |
| **Community sentiment** | A few searches + light reading (~5min) | What do real users say? Is the maintainer responsive? | When narrowing 2–3 candidates |
| **Code quality** | Clone + inspect (~5–15min) | Is it safe to install? Will it break things? | Before installing into a real workflow |

Each underlying source (issues, commits, releases, README) is named in
exactly one tier. Tier 2 doesn't re-count what Tier 1 already counts —
it tells you what to *read* from sources that Tier 1 might also touch.

Match the depth to the stakes. Don't audit a one-off TODO widget the way you'd audit something that intercepts every tool call.

## Tier 1 — Project health (highest priority)

The first filter. Pi's internal API moves fast; an extension that
hasn't kept up is broken regardless of how popular it once was. All
signals here are quantitative — counts, dates, ratios — runnable in
seconds with no judgement calls.

Ranked by signal strength:

| Priority | Signal | Why it matters | Source |
|---|---|---|---|
| ★★★ | **Last commit / push date** | Single most important filter. >6 months stale on a moving target like Pi = assume broken. | `gh api repos/<owner>/<repo> --jq .pushed_at` |
| ★★★ | **Weekly npm downloads** | Real adoption. Beware: bundle packages (e.g. mitsupi) report combined counts | `curl -s https://api.npmjs.org/downloads/point/last-week/<pkg> \| jq .downloads` |
| ★★★ | **Contributors count** | Bus factor. 1 contributor = single point of failure when they lose interest | `gh api repos/<owner>/<repo>/contributors --jq 'length'` |
| ★★ | **Release count and last release date** | Tagged releases with semver indicate published-package discipline vs scratch repo | `gh api repos/<owner>/<repo>/releases --jq '[length, .[0].published_at]'` |
| ★★ | **Commit frequency over last 90 days** | One stale commit at the cutoff is worse than steady weekly pushes. Catches "abandoned with one cleanup commit". | `gh api repos/<owner>/<repo>/commits --jq 'length'` (use `since` param) |
| ★★ | **Open issues count + closed-recently count** | Simple ratio. Many open + few closed-recently = warning. Reading the issues is Tier 2. | `gh issue list --state all --json state,closedAt` |
| ★★ | **Archived flag** | GitHub's explicit "don't use this" signal | `gh api repos/<owner>/<repo> --jq .archived` |
| ★ | **GitHub stars** | Hype-biased and lagging. Useful as tie-breaker between two similar extensions, not a primary filter. | `gh api repos/<owner>/<repo> --jq .stargazers_count` |
| ★ | **Forks count** | Forks signal real use (someone wanted to modify it). Also signals fragmentation if many forks have diverged. | `gh api repos/<owner>/<repo> --jq .forks_count` |
| ★ | **Pi version compatibility stated** | README mentions which `@earendil-works/pi-coding-agent` versions it targets | README scan |

### Maturity tag (derived from last push + commit frequency)

| Tag | Meaning |
|---|---|
| `[active]` | Commit within the last month and >1 commit in the last 90 days |
| `[stable]` | Commit within ~6 months, low recent activity, but tagged releases |
| `[experimental]` | Single-author, no releases, recent commits |
| `[stale]` | No commits in >6 months — assume broken on current Pi |
| `[abandoned]` | No commits in >12 months, open issues unanswered |
| `[fork-of-X]` | Soft-forked from another extension — check whether the parent is more active |

### Fast recipe

```bash
# Project-health one-liner for one extension
REPO=owner/name
PKG=npm-package-name

gh api "repos/$REPO" --jq '{
  stars: .stargazers_count,
  forks: .forks_count,
  pushed: .pushed_at,
  open_issues: .open_issues_count,
  archived: .archived
}'
gh api "repos/$REPO/contributors" --jq 'length'
gh api "repos/$REPO/releases" --jq '[length, .[0].published_at]'
gh api "repos/$REPO/commits?since=$(date -v-90d -u +%Y-%m-%dT%H:%M:%SZ)" --jq 'length'
curl -s "https://api.npmjs.org/downloads/point/last-week/$PKG" | jq .downloads
```

## Tier 2 — Community sentiment

Stars and downloads measure adoption, not satisfaction. A project can
be popular and broken at the same time. Tier 2 reads the same sources
Tier 1 counted, plus external community channels.

Use already-aggregated sources first. Resist generic web searches for
opinions — that path leads to reviewer hallucination.

| Source | What to extract | Cost |
|---|---|---|
| **GitHub Issues** (already counted in Tier 1) | Read the recent ones. Maintainer response style and time-to-first-comment. Whether closed issues are actually resolved or just abandoned. Recurring complaints. | `gh issue list --repo $REPO --state all --limit 30` and scan |
| **Pi Discord `#extensions` channel** | Where most user reports land. Already scraped by `qualisero/awesome-pi-agent`'s automation | Discord search, ~30s |
| **Inclusion in curated collections** | Named practitioners vouching for an extension with their own workflow on the line. See weighting table below. | `gh search code "<name>" --repo <collection>` per row |
| **Mentions in other extensions' READMEs** | Peer signal. "Based on X", "fork of X", "inspired by X" = extension authors picking each other | `gh search code "<name>" --filename README.md` |
| **HN / Reddit / X mentions** | High noise, occasional gold. Time-box and weight low. | Web search, time-boxed to 5min |

### Curated-collection inclusion weights

Each collection below is maintained by a named practitioner who uses Pi
daily. Inclusion means they evaluated it and kept it in their setup —
a stronger signal than a star or an awesome-list entry.

| Collection | Curator | Inclusion means | Weight |
|---|---|---|---|
| [`mitsuhiko/agent-stuff`](https://github.com/mitsuhiko/agent-stuff) | Pi maintainer | Ships in the reference Pi setup and used in real projects | Highest — maintainer-grade endorsement |
| [`qualisero/awesome-pi-agent`](https://github.com/qualisero/awesome-pi-agent) | qualisero (list maintainer) | Passed PR review + Discord-sentiment filter | High — community quality gate |
| [`noahsaso/my-pi`](https://github.com/noahsaso/my-pi) | noahsaso | Used in production subagent/orchestration workflows | High — active, opinionated setup |
| [`hjanuschka/shitty-extensions`](https://github.com/hjanuschka/shitty-extensions) | hjanuschka | Bundled and shipped on npm; maintained alongside | Medium-high — active bundle maintainer |
| [`kcosr/pi-extensions`](https://github.com/kcosr/pi-extensions) | kcosr | Semver-tagged, CI; each extension individually justified | Medium-high — engineering-quality bar |
| [`aliou/pi-extensions`](https://github.com/aliou/pi-extensions) | aliou | Used across a coherent large-scale extension set | Medium |
| [`ben-vargas/pi-packages`](https://github.com/ben-vargas/pi-packages) | ben-vargas | CI, individual tests, separately published | Medium — good engineering signal |
| [`tmustier/pi-extensions`](https://github.com/tmustier/pi-extensions) | tmustier | Active personal bundle, qualisero-listed | Medium |

**Convergence signal:** if an extension appears in 3+ curated collections
independently, treat that as strong evidence of broad utility regardless
of download count. Use the recipe above to check each collection.

What **not** to do: don't run open-ended sentiment-analysis prompts
("is this extension well-liked?"). The model will confabulate. Stick
to concrete sources above.

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
