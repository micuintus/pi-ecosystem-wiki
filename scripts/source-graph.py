import re, pathlib, yaml
root = pathlib.Path.home() / "devel/AI/pi-ecosystem-wiki"
reg = set(re.findall(r"^\| ([A-Za-z0-9._-]+) \|", (root / "raw-sources/index.md").read_text(), re.M)) - {"id"}
cited = {}
for f in list(root.glob("ecosystem/*.md")) + list(root.glob("references/*.md")) + [root / "index.md", root / "README.md"]:
    t = f.read_text()
    ids = set()
    if t.startswith("---"):
        head = t.split("\n---\n", 1)[0]
        try:
            fm = yaml.safe_load(head.lstrip("-\n")) or {}
            ids |= set(fm.get("sources") or [])
        except yaml.YAMLError as e:
            print("YAML-ERROR", f.name, str(e).splitlines()[-1][:80])
            m = re.search(r"^sources:\n((?:  - .*\n)+)", head + "\n", re.M)
            ids |= set(x.strip()[2:].strip() for x in m.group(1).splitlines()) if m else set()
        body = t.split("\n---\n", 1)[1]
    else:
        body = t
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    ids |= set(m for m in re.findall(r"(?<![!\]])\[([a-z0-9][A-Za-z0-9._-]+)\](?!\()", body) if "-" in m)
    for i in ids: cited.setdefault(i, set()).add(f.name)
missing = sorted(i for i in cited if i not in reg)
orphans = sorted(reg - set(cited))
print("registered:", len(reg), "cited:", len(cited))
print("MISSING:", len(missing)); [print("  ", i, sorted(cited[i])) for i in missing]
print("ORPHANS:", orphans)
