---
title: SCHEMA
type: reference
updated: 2026-05-08
sources: []
---

# Schema

Conventions for this wiki. Public-tuned variant of the
[Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern.

## Layout

```
pi-ecosystem-wiki/
├── README.md            # human entry
├── SCHEMA.md            # this file
├── index.md             # catalog of compiled pages
├── log.md               # append-only ingest log
├── raw-sources/
│   └── index.md         # registry of every source
├── ecosystem/           # surveys of extensions by use case
└── references/          # pointers to upstream docs and lists,
                         # plus evaluation/methodology pages
```

## Page frontmatter (mandatory)

```yaml
---
title: <human-readable title>
type: concept | comparison | reference | ecosystem | synthesis | stub
updated: YYYY-MM-DD
sources: [<id from raw-sources/index.md>, ...]
---
```

Optional: `tags: [tag1, tag2]`.

### Survey-page entries (recommended for `type: ecosystem`)

Survey pages list multiple extensions. To keep numbers from going stale,
put extension identifiers in frontmatter as machine-readable entries
and **do not** inline live numbers (stars, downloads, last-commit dates)
in the body. Readers and agents query those at read-time using the
recipes in [`references/evaluation.md`](references/evaluation.md).

```yaml
entries:
  - id: pi-autoresearch                     # short stable slug
    name: pi-autoresearch                   # display name
    repo: davebcn87/pi-autoresearch         # GitHub owner/repo
    npm: pi-autoresearch                    # npm package name (optional)
    role: evolve-driver                     # one-word categorical tag
    notes: "Karpathy-inspired autoresearch harness"
```

Body prose may make qualitative claims ("dominates", "single-author")
backed by a `# (live: gh api ...)` recipe link, but should not name a
specific star count, download number, or commit date. Architectural
and feature comparisons are timeless and stay inline.

### `role:` is page-local, not a global taxonomy

The `role:` field on each entry is a **page-local categorical label**
used to group entries inside that one survey (e.g. `subprocess-spawn`
vs `in-process` on the subagent page; `footer-default` vs
`footer-event-driven` on the footer page). It is not a controlled
vocabulary and is not expected to be consistent across pages.
Readers and agents looking for a global classification should rely on
`tags:`, not `role:`.

## Page types

- **ecosystem** — covers an extension, a family of extensions (survey),
  or an integration target. Lives under `ecosystem/`. Survey pages
  carry an `entries:` block; integration-reference pages do not.
- **reference** — flat reference / methodology material. Lives under
  `references/` (or at the root for `index.md` / `SCHEMA.md`).

The distinction between *survey* and *integration-reference* inside
`type: ecosystem` is implicit and visible from the presence of an
`entries:` block. Survey pages also typically include a
`## Recommendation matrix`.

## Source rules

Sources in this wiki must be **canonical, external, and public**. Allowed kinds:

- **GitHub repos / files / issues / PRs** (use commit-pinned permalinks for files)
- **Project home pages** (pi.dev, etc.)
- **npm package listings**
- **Other Pi extension collections / awesome-lists**
- **Articles / gists** (Karpathy, Huntley, etc.)

Not allowed: local file paths, private session dumps, internal investigation
notes, links into a developer's local clone. If the source can't be opened
by anyone in the world from a fresh browser, it doesn't belong in
`raw-sources/index.md`.

Every claim cites a source id from `raw-sources/index.md`. Code references
use permalinks (commit SHA), not `main` URLs.

## Public-use deltas vs private LLM Wiki

- No `decision/`, `bug/`, `open-question/` directories — those belong in
  a private wiki, not a public one.
- Voice is neutral and third-person. No "I think", no insider shorthand.
- Every package page links to: repo, npm (if any), official docs (if any),
  the upstream catalog entry, and at least one independent source.

## Ingest

1. **Register** the source in `raw-sources/index.md` with a stable id.
2. **Compile** into pages in the right directory. Merge with targeted
   edits, append to `sources:`, bump `updated:`.
3. **Log** the operation in `log.md`.
