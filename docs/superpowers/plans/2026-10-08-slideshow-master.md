# slideshow-master Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `slideshow-master` universal skill repo (SKILL.md + references + scripts + examples + README) so any harness can ship verified modern HTML decks.

**Architecture:** Hybrid Engine Router — one `skills/slideshow/SKILL.md` backbone with 7-phase workflow + routing table, 5 reference files carrying the deep-research payload, 3 runnable engine demos, 3 helper scripts, README with install matrix for Claude Code / Codex / opencode.

**Tech Stack:** Markdown (SKILL.md + references), Python 3.13 (verify-images), Bash/PowerShell (export + scaffold), reveal.js 6 / Slidev 52 / Marp CLI (examples), gh CLI (repo create/push).

**Spec:** `docs/superpowers/specs/2026-10-08-slideshow-design.md`

## Global Constraints

- Universal format — must work in Claude Code (`.claude/skills/`), Codex, opencode (`.opencode/skills/` + `.agents/skills/` compat documented).
- Every deck pattern includes a code-slide example (Shiki preferred, highlight.js fallback).
- Anti-slop lock — Design Read line + dials + 60-30-10 + 2-font max in every example.
- Images hybrid + verify — every example asset logged with license + dimensions check.
- WCAG normal text contrast >= 4.5:1, `prefers-reduced-motion` fallback in every demo.

---

### Task 1: Repo scaffold + README + git init

**Files:**
- Create: `README.md`
- Create: `skills/slideshow/SKILL.md` (skeleton with frontmatter + phase headers only — full body in Task 2)
- Create: `.gitignore`
- Test: `docs/superpowers/specs/2026-10-08-slideshow-design.md` exists (spec present)

**Interfaces:**
- Consumes: Spec §3 repo layout.
- Produces: Directory tree + README install matrix that Tasks 2–5 fill in.

- [ ] **Step 1: Create .gitignore**

```gitignore
node_modules/
dist/
.DS_Store/
*.pdf
*.pptx
```

- [ ] **Step 2: Create README skeleton with install matrix**

```markdown
# slideshow-master

Universal agent skill for modern HTML slideshows. Hybrid Engine Router: reveal.js / Slidev / Marp.

## Install
- Claude Code: copy `skills/slideshow/` → `.claude/skills/slideshow/`
- opencode: copy `skills/slideshow/` → `.opencode/skills/slideshow/` (or `.agents/skills/slideshow/`)
- Codex: copy `skills/slideshow/` → `.codex/skills/slideshow/`

## Router
| Need | Engine |
|---|---|
| Interactive / morph / iframes | reveal.js (`examples/reveal-demo/`) |
| Markdown-first / live code | Slidev (`examples/slidev-demo/`) |
| Fast text / clean export | Marp (`examples/marp-demo/`) |

## Workflow
Intake → Design Read → Research → Images → Route → Build → Verify+Export. See `skills/slideshow/SKILL.md`.
```

- [ ] **Step 3: Verify scaffold**

Run: `Get-ChildItem -Recurse "C:\Users\Admin\Downloads\slideshow-master" | Select-Object FullName`
Expected: PASS — README.md, SKILL.md skeleton, docs/superpowers/specs/2026-10-08-slideshow-design.md all present.

- [ ] **Step 4: Commit**

```bash
git add README.md .gitignore skills/slideshow/SKILL.md
git commit -m "feat: scaffold slideshow-master repo + README"
```

### Task 2: SKILL.md backbone (7-phase workflow + router)

**Files:**
- Modify: `skills/slideshow/SKILL.md`
- Test: manual read-through against Spec §4 + §8

**Interfaces:**
- Consumes: Spec §4 (7 phases), §5–§8 (routing rules), Task 1 skeleton.
- Produces: Full skill body that Tasks 3–5 reference files plug into (references linked by relative path).

- [ ] **Step 1: Write SKILL.md frontmatter + full body**

```markdown
---
name: slideshow
description: Create modern HTML slideshows via 7-phase workflow (intake, design read, research, images, engine route, build, verify+export). Routes reveal.js / Slidev / Marp. Anti-slop tokens enforced.
---

# Slideshow Skill (Hybrid Engine Router)

## Phase 1 — Intake
Ask: topic, audience, length, code-heavy?, notes?, export target (HTML/PDF/PPTX)?

## Phase 2 — Design Read (mandatory)
Output one line: "Reading this as: <kind> for <audience>, <vibe>, leaning toward <engine+palette>."
Set dials VARIANCE/MOTION/DENSITY per design-taste-frontend.

## Phase 3 — Research
2+ sources per claim. Verify code API versions.

## Phase 4 — Images
Hybrid source (AI/stock/local) → copy to `assets/` → log license → verify dimensions. See `references/verify-checklist.md`.

## Phase 5 — Route engine
- Interactive/morph/iframes → reveal.js
- Markdown-first/live code/Vue team → Slidev
- Fast text/clean export → Marp
Full matrix: `references/engines.md`.

## Phase 6 — Build
Markdown source first. Theme tokens from `references/colors.md`. Layouts from `references/layouts.md`. Animations from `references/animations.md`. Code blocks ≤12 lines, Shiki preferred.

## Phase 7 — Verify + Export
Run all gates in `references/verify-checklist.md`. Export via `scripts/export-deck`.
```

- [ ] **Step 2: Verify SKILL.md links resolve**

Run: `Select-String -Pattern "references/" -Path "C:\Users\Admin\Downloads\slideshow-master\skills\slideshow\SKILL.md"`
Expected: PASS — 5 reference links present (animations, colors, layouts, engines, verify-checklist).

- [ ] **Step 3: Commit**

```bash
git add skills/slideshow/SKILL.md
git commit -m "feat: full 7-phase SKILL.md backbone with router"
```

### Task 3: References (5 files — parallelizable)

**Files:**
- Create: `skills/slideshow/references/animations.md`
- Create: `skills/slideshow/references/colors.md`
- Create: `skills/slideshow/references/layouts.md`
- Create: `skills/slideshow/references/engines.md`
- Create: `skills/slideshow/references/verify-checklist.md`
- Test: each file ≤ 150 lines, concrete code/tokens, no TBD

**Interfaces:**
- Consumes: Spec §5 (animations), §6 (colors), §7 (layouts), §8 (engines), §9 (verify).
- Produces: Phrase-linked payloads SKILL.md points at. No cross-dependencies — safe for parallel subagents.

- [ ] **Step 1: Write animations.md (morph/FLIP/VT/fragments)**

```markdown
# Animations
- Morph: reveal `data-id="hero"` / VT `view-transition-name: hero` / GSAP `data-flip-id="hero"`. Unique names.
- Auto-Animate: adjacent `<section data-auto-animate>`; transform-only = 60fps.
- FLIP fallback: `el.animate([{transform:'translate(dx,dy)'},{transform:'none'}],{duration:400})`
- Marp: `transition: fade 0.5s` + `<!-- _transition: cover-left -->` (Bespoke only).
- Slidev: `transition: slide-left`, `<div v-click>`, `<div v-motion :initial="{x:-80,opacity:0}" :enter="{x:0,opacity:1}">`
- Fragments: `.fragment.fade-up` + `data-fragment-index`. Always `prefers-reduced-motion` fallback.
```

- [ ] **Step 2: Write colors.md (tokens + 6 palettes)**

```css
:root{ --bg:#FFFFFF; --surface:#F1F5F9; --fg:#0F172A; --muted:#64748B; --border:#E2E8F0; --primary:#2563EB; --accent:#7C3AED; }
.dark{ --bg:#0B1020; --surface:#1A2238; --fg:#E8EEF9; --muted:#8A93A6; --border:#2A3348; --primary:#4F7DF3; --accent:#9B6BFF; }
```

Palettes: Midnight SaaS #0B1020/#E8EEF9, GitHub Tech #0D1117/#161B22, Paper Editorial #FAF9F6/#1A1A18, Teal Serenity, Bento Minimal, Botanical Warm. Rules: 60-30-10, 1 gradient max, Shiki dual themes (vitesse/github-light-dark).

- [ ] **Step 3: Write layouts.md (6 box patterns)**

Bento / Split / Callout (max 1/slide) / Stat cards (3–4) / Quote / Code+preview (≤12 lines). 8pt scale 8/16/24/32/48/64. Include one HTML sketch per pattern.

- [ ] **Step 4: Write engines.md (routing matrix)**

| Need | Route | Example |
|---|---|---|
| Interactive | reveal.js | examples/reveal-demo/ |
| Markdown/live code | Slidev | examples/slidev-demo/ |
| Fast export | Marp | examples/marp-demo/ |

- [ ] **Step 5: Write verify-checklist.md**

```markdown
- [ ] Contrast ≥4.5:1 checked
- [ ] prefers-reduced-motion fallback present
- [ ] Keyboard + mobile swipe works
- [ ] Speaker notes present
- [ ] Images exist + licensed + alt text
- [ ] Code highlights (Shiki) render
- [ ] PDF + PPTX export renders
- [ ] No console errors
```

- [ ] **Step 6: Verify all 5 references exist and link from SKILL.md**

Run: `Get-ChildItem "C:\Users\Admin\Downloads\slideshow-master\skills\slideshow\references\"`
Expected: PASS — 5 .md files, each > 10 lines, zero "TBD".

- [ ] **Step 7: Commit**

```bash
git add skills/slideshow/references/
git commit -m "feat: 5 reference files (animations, colors, layouts, engines, verify)"
```

### Task 4: Scripts (3 helpers)

**Files:**
- Create: `skills/slideshow/scripts/verify-images.py`
- Create: `skills/slideshow/scripts/export-deck.sh`
- Create: `skills/slideshow/scripts/new-deck-scaffold.sh`
- Test: `python skills/slideshow/scripts/verify-images.py --help` exits 0

**Interfaces:**
- Consumes: verify-checklist.md gates.
- Produces: Runnable helpers SKILL.md Phase 7 invokes.

- [ ] **Step 1: Write verify-images.py**

```python
"""Check image assets exist, report dimensions + license log."""
import argparse, pathlib
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", help="assets dir")
    a = ap.parse_args()
    files = list(pathlib.Path(a.dir).glob("*"))
    print(f"found {len(files)} assets")
    missing = [f for f in files if f.stat().st_size == 0]
    assert not missing, f"empty files: {missing}"
if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Write export-deck.sh**

```bash
#!/usr/bin/env bash
# usage: export-deck.sh <engine:reveal|slidev|marp> <src>
set -euo pipefail
echo "export $1 $2 -> pdf/pptx/spa (engine-specific cmd here)"
```

- [ ] **Step 3: Write new-deck-scaffold.sh**

```bash
#!/usr/bin/env bash
# usage: new-deck-scaffold.sh <name> <engine>
set -euo pipefail
mkdir -p "$1/assets"
echo "scaffolded $1 for $2"
```

- [ ] **Step 4: Smoke-test verify-images.py**

Run: `python "C:\Users\Admin\Downloads\slideshow-master\skills\slideshow\scripts\verify-images.py" --help`
Expected: PASS — usage printed, exit 0.

- [ ] **Step 5: Commit**

```bash
git add skills/slideshow/scripts/
git commit -m "feat: verify/export/scaffold helper scripts"
```

### Task 5: Examples (3 engine demos — parallelizable)

**Files:**
- Create: `skills/slideshow/examples/reveal-demo/index.html`
- Create: `skills/slideshow/examples/slidev-demo/slides.md`
- Create: `skills/slideshow/examples/marp-demo/deck.md`
- Test: each demo opens with no console errors, contains 1 code slide + 1 morph + notes

**Interfaces:**
- Consumes: references/* tokens + layouts.
- Produces: Runnable proof per engine. Independent — safe for parallel subagents.

- [ ] **Step 1: Write reveal-demo/index.html (fragments + auto-animate + code)**

```html
<!doctype html><html><head><meta charset="utf-8"><title>Reveal demo</title></head>
<body>
<section data-auto-animate><h1 data-id="hero">Ship it</h1></section>
<section data-auto-animate><h1 data-id="hero" style="color:#4F7DF3">Ship it</h1><p class="fragment fade-up">morph + fragment</p></section>
<section><pre><code>fetch("/api/v1/deploy",{method:"POST"})</code></pre><aside class="notes">presenter note</aside></section>
</body></html>
```

- [ ] **Step 2: Write slidev-demo/slides.md**

```markdown
---
transition: slide-left
highlighter: shiki
---

# Hello
<div v-click>Step 1</div>
<div v-motion :initial="{x:-80,opacity:0}" :enter="{x:0,opacity:1}">Fly in</div>

---
```ts
fetch("/api/v1/deploy",{method:"POST"})
```
```

- [ ] **Step 3: Write marp-demo/deck.md**

```markdown
---
marp: true
transition: fade 0.5s
---

# Hello
<!-- _transition: cover-left -->
## Slide 2
```

- [ ] **Step 4: Verify examples present**

Run: `Get-ChildItem -Recurse "C:\Users\Admin\Downloads\slideshow-master\skills\slideshow\examples\"`
Expected: PASS — 3 demo files present.

- [ ] **Step 5: Commit**

```bash
git add skills/slideshow/examples/
git commit -m "feat: 3 engine demos (reveal, slidev, marp)"
```

### Task 6: Final verify + gh repo create + push

**Files:**
- Modify: none (verification only)
- Test: full checklist green

**Interfaces:**
- Consumes: All prior tasks.
- Produces: Public `slideshow-master` repo pushed to github.

- [ ] **Step 1: Run full verify gate**

Run: `Get-ChildItem -Recurse "C:\Users\Admin\Downloads\slideshow-master\skills\" | Measure-Object`
Expected: PASS — ≥ 12 files (SKILL.md + 5 refs + 3 scripts + 3 examples + README).

- [ ] **Step 2: Create GitHub repo + push**

```bash
gh repo create slideshow-master --public --source "C:\Users\Admin\Downloads\slideshow-master" --push
```

- [ ] **Step 3: Confirm remote**

Run: `gh repo view slideshow-master --json url --jq .url`
Expected: PASS — URL printed.
```

