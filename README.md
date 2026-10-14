# slideshow-master

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/skill-universal-blue.svg)](skills/slideshow/SKILL.md)
[![Stack](https://img.shields.io/badge/python--pptx_%2B_PowerPoint_COM-green.svg)](skills/slideshow/references/engines.md)

Universal agent skill for building **real, animated .pptx decks** —
editable text, embedded photos, PowerPoint Morph transitions, fade
entrances, speaker notes — not HTML exports, not rasterized slides.

**How it works:** the agent runs an 11-phase workflow (Intake → Design
Read → Style lock → **Research (artifact)** → **Outline + Visual Plan
(artifacts)** → Scaffold → Images+PIL prep → Build → Motion → Verify →
Ship). Geometry and content are authored with python-pptx; motion and
renders go through real PowerPoint COM; `scripts/verify-pptx.py`
asserts the OOXML and the builder's own eyes assert the renders.

## Contents

```
skills/slideshow/
├── SKILL.md                    # lean router: stack, route table, discipline
├── workflows/
│   └── generate-pptx.md        # full 11-phase procedure + quick-build path
├── references/
│   ├── modes/                  # 5 narrative arcs: tech-talk, pitch, tutorial, showcase, narrative
│   ├── visual-styles/          # 13 palettes (STRONG default + SOFT explicit) + picker + styles_index.json
│   ├── layout-templates/       # 8 python-pptx recipes (photo-collage … annotation-stage) + picker + templates_index.json
│   ├── data-graphics/          # diagrams, charts, tables (native shapes) + picker + graphics_index.json
│   ├── media/                  # images + icons guides + picker + media_index.json
│   ├── pptx-motion-language.md # 12-section craft law: anchors, Morph contract, stagger, ramp, type scale
│   ├── engines.md              # the one engine: python-pptx + PowerPoint 365 COM, enums, hygiene
│   ├── animations.md           # transition/entrance snippets, rebuild-clean rule, stagger table
│   ├── layouts.md              # inches grid, stations, ceilings, section patterns, z-order
│   ├── decorations.md          # one organic device per deck, rings, pills, glow
│   ├── tokens.md               # palette shape, type tiers, spacing in inches
│   └── verify-checklist.md     # 15 gates: notes, raster floor, contrast on renders, motion budget, continuity
├── scripts/
│   ├── scaffold.py             # scaffold a deck project: build.py + motion.py + verify_extra.py
│   ├── verify-images.py        # check build.py refs resolve + CREDITS.md covers them + budgets
│   ├── verify-pptx.py          # OOXML asserts: canvas, notes, rasters, transitions, fx budget, continuity
│   └── render.py               # generic COM pass: Morph/fade + manual advance + PNG renders
```

Repo-level: `docs/` (getting-started, gallery, faq, roadmap),
`CONTRIBUTING.md` (add a style / palette / template / mode).

## Install (one skill, every harness)

- **opencode:** copy `skills/slideshow/` → `.config/opencode/skills/slideshow/`
- **Antigravity IDE:** copy `skills/slideshow/` → `.gemini/config/skills/slideshow/`
  (the only IDE-scanned global path)
- **Claude Code / Codex:** copy `skills/slideshow/` → the harness's
  global skills dir

No dependencies for the skill itself. Each *deck build* needs
`python-pptx`, `Pillow`, `pywin32` (`python -m pip install …`) and
desktop PowerPoint 2019+/365 for the motion pass — without PowerPoint,
motion is blocked and the skill says so.

## Workflow (what the agent does)

1. **Route** — request → `workflows/generate-pptx.md` + ONE mode
2. **Intake & Design Read** — questions, one-line Design Read, dials
3. **Style lock** — ONE palette, shape contract (3–8 vocabulary + moving
   object), one organic device, value ramp, type tiers, template, ONE
   transition
4. **Research (artifact)** — `research-notes.md` (4–8 bullets/slide,
   2-source log, ship-blocking)
5. **Outline + Visual Plan (artifacts)** — `bg:` tags, depth rule
   (≥1.5x topics), per-slide spec blocks with `Done when:`, hard image
   counts, nod
6. **Scaffold + Images** — `python scripts/scaffold.py`, source photos to
   `assets/` + `CREDITS.md`, PIL prep (plates, crops, baked rotation)
7. **Build** — `build.py`: blank 13.333×7.5in slides, template recipes
   verbatim, `name=` morph identities, notes; NO transitions in build.py
8. **Motion** — `motion.py` via COM: Morph-byObject default, fade
   exceptions, ≤3 fade entrances/slide, manual advance, PNG renders
9. **Verify + Ship** — 15 gates, repair at owning layer, read every
   render by eye, ship .pptx + renders/ (+ handout PDF)

Details: `skills/slideshow/SKILL.md` + `skills/slideshow/workflows/`.

## Anti-slop contract

Every deck must pass: **explicit palette (no theme-slot defaults)**,
contrast read on renders, **value ramp** (max 2 consecutive same-bg),
**content density** (research-notes.md), **photo floor** (≥1 raster/slide,
total ≥ half the slides, on ≥60% of slides), **one organic device**,
morph-name discipline (exact `name=` matches, parked shapes never
"fixed"), one transition for the deck, entrance budget (≤3 fade/slide),
speaker notes on every slide, zero placeholders. Enforced by
`references/verify-checklist.md` (15 gates) + `scripts/verify-pptx.py`.

## New deck in 30 seconds

```powershell
python skills/slideshow/scripts/scaffold.py my-talk
cd my-talk
# fill build.py from visual-plan.md, source assets/, then:
python build.py
python motion.py
python ..\skills\slideshow\scripts\verify-pptx.py deck.pptx
python ..\skills\slideshow\scripts\verify-images.py .
```
