import json
import glob
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

errors = []

# 1. SKILL.md frontmatter
head = open("skills/slideshow/SKILL.md", encoding="utf-8").read(2000)
m = re.match(r"^---\n(.*?)\n---", head, re.S)
if not m:
    errors.append("SKILL.md missing YAML frontmatter")
else:
    fm = m.group(1)
    if not re.search(r"^name:\s*slideshow\s*$", fm, re.M):
        errors.append("frontmatter name must be 'slideshow'")
    if not re.search(r"^description:\s*.+", fm, re.M):
        errors.append("frontmatter description required")

# 2. index JSONs parse
files = glob.glob("skills/slideshow/**/*_index.json", recursive=True)
if not files:
    errors.append("no index JSONs found")
for f in files:
    try:
        json.load(open(f, encoding="utf-8"))
    except Exception as e:
        errors.append("%s: %s" % (f, e))

# 3. Gate 6: no placeholders in shipped content
# (docs/superpowers/ holds internal planning notes, not shipped content)
import os
pat = re.compile(r"lorem ipsum|todo:|tbd|fixme", re.I)
roots = ["skills"]
root_files = ["README.md", "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md",
              "SECURITY.md", "CODE_OF_CONDUCT.md", "CHANGELOG.md",
              "docs/getting-started.md", "docs/faq.md",
              "docs/why-html-slides.md", "docs/gallery.md",
              "docs/roadmap.md"]
targets = [f for f in root_files if os.path.exists(f)]
for base in roots:
    for dp, _, fns in os.walk(base):
        if "__pycache__" in dp:
            continue
        for fn in fns:
            if fn.endswith((".md", ".html")):
                targets.append(os.path.join(dp, fn))
hits = []
for t in targets:
    try:
        text = open(t, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    for i, line in enumerate(text.splitlines(), 1):
        # Skip lines that only document the gate's own grep patterns
        if line.lstrip().startswith("grep ") or "grep -r" in line:
            continue
        if pat.search(line):
            hits.append("%s:%d:%s" % (t, i, line.strip()[:100]))
if hits:
    errors.append("placeholders found: %s" % hits[:5])

if errors:
    print("FAIL")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("ALL CHECKS OK (%d index JSONs)" % len(files))
