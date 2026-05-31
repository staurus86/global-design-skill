"""One-off file-linkage audit. Finds .md files never referenced anywhere else.

Reachability model:
- corpus = all tracked text files (md/txt/yaml/yml/py/mdc/css/json/sh/toml)
- a target .md is "path-referenced" if its repo-relative posix path (or a suffix
  of it >= 2 segments) appears verbatim in any OTHER corpus file
- "name-referenced" if its basename appears in any other corpus file
- orphan = neither; weak = name-only (ambiguous / maybe coincidental)
"""
import subprocess
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent

TEXT_EXT = {".md", ".txt", ".yaml", ".yml", ".py", ".mdc", ".css", ".json", ".sh", ".toml", ".mjs", ".js"}

tracked = subprocess.run(
    ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
).stdout.splitlines()

corpus = {}
for rel in tracked:
    p = ROOT / rel
    if p.suffix.lower() in TEXT_EXT and p.exists():
        try:
            corpus[rel.replace("\\", "/")] = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            pass

md_files = sorted(f for f in corpus if f.endswith(".md"))

# Concatenate corpus per-file so we can exclude self when checking.
def referenced(target_rel):
    base = Path(target_rel).name
    # path suffixes of >=2 segments, e.g. "product-ui/microinteractions.md"
    segs = target_rel.split("/")
    suffixes = ["/".join(segs[i:]) for i in range(len(segs)) if len(segs) - i >= 2]
    path_hit = []
    name_hit = []
    for rel, text in corpus.items():
        if rel == target_rel:
            continue
        if any(s in text for s in suffixes):
            path_hit.append(rel)
        elif base in text:
            name_hit.append(rel)
    return path_hit, name_hit

orphans = []
weak = []
for m in md_files:
    path_hit, name_hit = referenced(m)
    if not path_hit and not name_hit:
        orphans.append(m)
    elif not path_hit:
        weak.append((m, name_hit))

def group(items):
    g = defaultdict(list)
    for it in items:
        rel = it if isinstance(it, str) else it[0]
        top = rel.split("/")[0] if "/" in rel else "(root)"
        g[top].append(it)
    return g

print(f"TOTAL .md files: {len(md_files)}\n")
print(f"=== TRUE ORPHANS (no path ref, no name ref anywhere): {len(orphans)} ===")
for top, items in sorted(group(orphans).items()):
    print(f"\n[{top}]")
    for it in items:
        print(f"  {it}")

print(f"\n\n=== WEAK (basename referenced but full path never linked): {len(weak)} ===")
for top, items in sorted(group(weak).items()):
    print(f"\n[{top}]  ({len(items)})")
    for rel, refs in items:
        src = ", ".join(sorted({r.split('/')[0] for r in refs}))
        print(f"  {rel}  <- via name in: {src}")
