# pi-ecosystem-wiki

A compiled, interlinked knowledge base about the [Pi coding agent](https://pi.dev/)
ecosystem — extensions, skills, packages, prompt templates, themes,
sandboxes, providers, and the people building them.

Pi itself is deliberately minimal. The ecosystem around it is not.
This wiki helps you **pick the right extensions for your Pi setup**
without trawling 1000+ entries in the flat catalogs.

## What this is — and is not

**Is:** an LLM-maintained markdown wiki following the
[Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern. Survey pages by *use case* (loops, todos, web search, footers,
subagents, tool rendering, remote access, …), each comparing the
extensions in that niche so you can choose.

**Is not:** another flat awesome-list. Those exist and do their job —
the wiki sits *on top of* them. See
[references/catalogs.md](references/catalogs.md) for the full set of
upstream catalogs and how they complement each other.

Quick links:

- [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) — hand-curated
- [shaftoe/awesome-pi-coding-agent](https://github.com/shaftoe/awesome-pi-coding-agent) / [awesome-pi.site](https://awesome-pi.site/) — auto-aggregated, daily updated
- [pi.dev/packages](https://pi.dev/packages) — official catalog

## Browse

- [`index.md`](index.md) — catalog of compiled pages, organized by use case
- [`ecosystem/`](ecosystem/) — surveys of extensions by niche
- [`references/`](references/) — pointers to upstream docs and catalogs
- [`raw-sources/`](raw-sources/) — registry of every ingested source

## Conventions

See [`SCHEMA.md`](SCHEMA.md). Every page has frontmatter
(`title`, `type`, `updated`, `sources`). Every claim cites a source.

## Contributing

Open a PR. New page = new entry in `raw-sources/index.md` and `index.md`,
plus a line in `log.md`.

## License

MIT.
