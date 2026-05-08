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
├── concepts/            # what things are
├── comparisons/         # X vs Y
├── ecosystem/           # per-package reference pages
└── references/          # pointers to upstream docs and lists
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

## Page types

- **concept** — what a thing is. Skills, extensions, packages, hooks, etc.
- **comparison** — X vs Y vs Z, with axes and tradeoffs.
- **reference** — flat reference material (this file, schema docs).
- **ecosystem** — one page per notable package or project.
- **synthesis** — opinionated rollup across multiple concepts.
- **stub** — registered but not yet compiled.

## Source rules

- Every claim cites a source listed in `raw-sources/index.md`.
- Stable public URLs are referenced, not copied.
- Mutable or auth-walled sources are copied into
  `raw-sources/<bucket>/YYYY-MM-DD-slug.md`.
- Code references use permalinks (commit SHA), not `main` URLs.

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
