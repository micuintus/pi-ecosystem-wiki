# pi-ecosystem-wiki

A compiled, interlinked knowledge base about the [Pi coding agent](https://pi.dev/)
ecosystem — extensions, skills, packages, prompt templates, themes,
sandboxes, providers, and the people building them.

Pi itself is deliberately minimal. The ecosystem around it is not.
This wiki tries to make that ecosystem navigable for both humans and LLMs.

## What this is — and is not

**Is:** an LLM-maintained markdown wiki following the
[Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern. Concept pages, comparison pages, per-package reference pages,
all linked, all backed by `raw-sources/`.

**Is not:** another flat awesome-list. Those exist and do their job:

- [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) — hand-curated
- [shaftoe/awesome-pi-coding-agent](https://github.com/shaftoe/awesome-pi-coding-agent) / [awesome-pi.site](https://awesome-pi.site/) — auto-aggregated
- [pi.dev/packages](https://pi.dev/packages) — official catalog

This wiki sits *on top of* those: it synthesizes, compares, and
explains, instead of just listing.

## Browse

- [`index.md`](index.md) — catalog of compiled pages
- [`concepts/`](concepts/) — what skills, extensions, packages, hooks etc. actually are
- [`comparisons/`](comparisons/) — package vs. package, approach vs. approach
- [`ecosystem/`](ecosystem/) — per-package reference pages
- [`references/`](references/) — pointers to upstream docs and lists
- [`raw-sources/`](raw-sources/) — registry of every ingested source

## Conventions

See [`SCHEMA.md`](SCHEMA.md). Every page has frontmatter
(`title`, `type`, `updated`, `sources`). Every claim cites a source.

## Contributing

Open a PR. New page = new entry in `raw-sources/index.md` and `index.md`,
plus a line in `log.md`.

## License

MIT.
