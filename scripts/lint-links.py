import re, pathlib, unicodedata
root = pathlib.Path.home() / "devel/AI/pi-ecosystem-wiki"
def slug(h):
    h = h.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)   # drop punctuation except - and _
    return h.replace(" ", "-")
anchors = {}
for f in root.rglob("*.md"):
    raw = re.sub(r"```.*?```", "", f.read_text(), flags=re.S)
    t = re.sub(r"`[^`\n]+`", "", raw)
    anchors[f] = {slug(m) for m in re.findall(r"^#{1,6} (.+)$", raw, re.M)}
    anchors[f] |= set(re.findall(r'<a id="([^"]+)"', t))
import sys
touched = sys.argv[1:] or [str(f.relative_to(root)) for f in sorted(root.rglob("*.md"))]
bad = 0
for rel in touched:
    f = root / rel
    t = re.sub(r"```.*?```", "", f.read_text(), flags=re.S)
    t = re.sub(r"`[^`\n]+`", "", t)
    for target in re.findall(r"\]\(([^)\s]+)\)", t):
        if target.startswith(("http://", "https://", "mailto:")): continue
        path, _, anchor = target.partition("#")
        dest = (f.parent / path).resolve() if path else f
        if path and not dest.exists():
            print("MISSING FILE", rel, "->", target); bad += 1; continue
        if anchor and dest.suffix == ".md" and anchor not in anchors.get(dest, set()):
            print("BAD ANCHOR", rel, "->", target); bad += 1
print("link problems in touched pages:", bad)
