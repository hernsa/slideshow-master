# Getting started

Build a real .pptx deck with the slideshow skill in five commands.
Requires Python 3.12+, `python -m pip install python-pptx Pillow
pywin32`, and desktop PowerPoint 2019+/365 (Windows) for motion.

## 1. Route

Read `skills/slideshow/SKILL.md`, then load `workflows/generate-pptx.md`
plus the ONE mode file your request maps to (`references/modes/`).

## 2. Lock the design

Answer Intake, write the one-line Design Read, lock the style: ONE
palette, 3–8 shape vocabulary + one moving object, one organic device,
3–4-stop value ramp, type tiers, section template, ONE transition.

## 3. Research + plan (both ship-blocking)

Write `research-notes.md` (4–8 bullets + 2-source log per slide) and
`visual-plan.md` (one spec block per slide in z-order with `Done
when:`). Get the nod on all three artifacts before building.

## 4. Scaffold + build

```powershell
python skills/slideshow/scripts/scaffold.py my-talk
cd my-talk
# fill build.py from visual-plan.md, source photos to assets/ + CREDITS.md
python build.py
python motion.py
python ..\skills\slideshow\scripts\verify-pptx.py deck.pptx
python ..\skills\slideshow\scripts\verify-images.py .
```

## 5. Verify + ship

Run the 5-step pre-ship run (`references/verify-checklist.md` bottom):
structure, assets, deck asserts, read every render by eye, COM hygiene.
Ship `deck.pptx` + `renders/` (+ handout PDF on request) with the
filled ship record.
