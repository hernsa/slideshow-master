# Workflow — generate-pptx

> 11 phases. Serial execution. A phase's exit artifact is the next phase's
> entry ticket — no ticket, no advance. `§quick-build` at the bottom is the
> only sanctioned shortcut.

## 1. Intake (7 questions, then proceed)

1. Topic + one-line thesis?
2. Audience (who sits in the room)?
3. Slide count (default 8)?
4. Palette family: dark photographic / pastel community / black showcase?
5. Real photos available, or source them (Commons/Pexels/Unsplash)?
6. Motion level: full morph / morph-lite (transitions only) / static?
7. Deliverables: `.pptx` always; +PNG renders always; +PDF handout on request?

If the user says "defaults": mixed-tech audience, 8 slides, dark photographic
+ one showcase break, morph-lite minimum, `.pptx` + renders.

## 2. Design Read (one line + 3 dials)

Emit: `Reading this as: <mode> for <audience>, <vibe>, VAR <n> / MOT <n> /
DEN <n>.` Then set `DESIGN_VARIANCE` (1 symmetric – 10 chaos),
`MOTION_INTENSITY` (1 static – 10 cinematic), `VISUAL_DENSITY` (1 airy –
10 packed). Defaults `7 / 6 / 4`.

## 3. Style lock (ONE palette, ONE contract)

- ONE palette: name 4–6 hexes (bg, ink, accent, accent-2, muted, card).
  Never invent new hexes per slide.
- **Deck shape contract** (`pptx-motion-language.md` §§0–1): list the deck's
  3–8 shape vocabulary AND its one moving object. Write both into the
  Design Read message.
- ONE organic device for the deck (§6): tile cluster / blob-behind / arch.
- 3–4-stop value ramp derived from the accent (§7); longest identical-bg
  run ≤ 2.
- Named type tiers in pt: `--t-hero` (54–96) / `--t-title` (40–44) /
  `--t-head` (28–32) / `--t-label` (18–20) / `--t-body` (14–16). Zero
  letter-spacing drift; one accent word per slide max.
- Section template per section from `layout-templates/_index.md` (photo-collage
  / pastel-collage / annotation-stage are the PPTX-transcribed defaults).
- ONE transition for the whole deck (§3); per-slide exceptions named now
  (max one `zoom` showcase or one `fade` break section).

## 4. Research — REQUIRED ship-blocking `research-notes.md`

One section per planned slide: 4–8 content bullets + a 2-source log. Fewer
than ~60 words of distinct facts per slide = redo. APIs/specs verified live;
anything unverified is marked `[unverified]`. Named stats ship with sources
(Gate 2). Hand the file to the user with the outline nod.

## 5. Outline + visual-plan (BOTH ship-blocking)

Outline: one line per slide with a MANDATORY `bg:` tag (plate / surface /
black / pastel-N). DEPTH RULE: 2–3 slides per major topic, outline ≥ 1.5×
topic count. Demo-universe titles stay concrete.

`visual-plan.md`: one block per slide, in z-order, using the §9 grammar:

```
Slide 3 — Pillars                      bg: surface
  Template: photo-collage
  Text runs:   hero "Two pillars, one city" {--t-title} ; body 2 lines {--t-body}
  Z-order:     bg → duo-boxes → feature-photo → parked-disc → copy
  Images:      assets/cuavan.jpg (feature) · assets/disc.jpg (parked, off-canvas)
  Entrances:   none (morph-only section)
  Anchors:     scrim-left (static) ; parked-disc flies 14.5in → 7.7in
  Done when:   duo boxes jade/gold, disc parked off-canvas, copy ≤ 3 lines.
```

**The plan's hard counts:** ≥1 raster per slide (narrative/photo sections
3–6); ≥1 shape-drawn diagram per 2 content slides; 1–2 deco primitives per
slide; entrances ≤3 per slide sharing one budget; ≥2 named anchors per
section, exactly one moving per step. Paste outline + research-notes +
visual-plan together for the nod.

## 6. Scaffold

`python scripts/scaffold.py <deck-dir>`: creates `build.py`, `motion.py`,
`verify_extra.py` (deck-specific asserts), `assets/`, `renders/`,
`research-notes.md`, `visual-plan.md` stubs. Never build inside the skill
repo — always a fresh deck folder.

## 7. Images + PIL prep — REQUIRED artifact

Execute `visual-plan.md` line by line, in z-order. Every planned raster lands
in `assets/` with a `CREDITS.md` line (filename + source + license). Never
hotlink. Prep in PIL, not in PowerPoint:
- Plates: darken to the plan's brightness (`.70` narrative / `.45–.55`
  under white text) + slight blur; cache per brightness.
- Tiles/discs: center-crop squares FIRST (`add_picture` stretches).
- Tilt: bake rotation into pixels (shape-level rotation on custom-geometry
  pictures renders a white wedge).
- Logos: key out white → transparent; keep the keyed PNG.
A plan line with no matching file in `assets/` stops the build — fix the
plan, not the slide. Closing check: every slide ≥1 raster, ratio matches
phase 5, organic device matches phase 3.

## 8. Build (`build.py`: python-pptx owns geometry + content)

- Blank layout, 13.333×7.5in. Copy the section's template recipe verbatim;
  swap copy for real content. Geometries, rotations, z-order are load-bearing.
- 3–8 distinct shapes reused across every slide; names set via `shape.name`
  (that name IS the morph identity — exact match, `!!` prefixes kept).
- Parked shapes wait off-canvas (`left=14.5in`), never `display:none`.
- Text: tier sizes from phase 3, Segoe UI or the locked pair; Vietnamese
  diacritics verified in the render.
- Notes: full speech per slide via `notes_slide.placeholders[1]`.
- No transitions, no timing in `build.py` — motion is phase 9's job.
- Anti-slop smell-check: no three-equal-box rows, no emoji, no raw rect
  photo under text, one accent word per slide.

## 9. Motion (`motion.py`: COM owns transitions + entrances + renders)

- Hygiene first: kill stray `POWERPNT.EXE`, delete nothing — but ALWAYS
  rebuild `build.py` output clean before re-running motion (COM doubles
  effects on re-run; the `.pptx` is disposable, the scripts are truth).
- Transitions map: slide → `ppEffectMorphByObject` (3954) default; named
  exceptions from phase 3 get `ppEffectFade` (1793). Open
  `WithWindow=False`, `DisplayAlerts=0` (`ppAlertsNone=1`).
- Entrances: ≤3 per slide, fade (`msoAnimEffectFade=10`), after-previous
  chain (`triggerAfterPrevious=3`), 100–150ms apart. Manual advance
  everywhere: `SlideShowTransition.AdvanceOnTime=0`. Zero click-reveals
  unless the plan explicitly buys them.
- Export PNGs: `Slide.Export(path, "PNG", 1920, 1080)` (positional args),
  into `renders/`. Read every one (phase 10).
- Enum table + serialization notes: `references/animations.md`.

## 10. Verify (three layers, in order)

1. OOXML asserts: `python scripts/verify-pptx.py <deck.pptx>` — slides,
   16:9, notes 1:1, raster floor (≥1/slide, ≥60% of slides), morph +
   fallback present, manual advance, entrance budget, anchor name
   continuity. Deck-specific asserts live in `verify_extra.py`.
2. Assets: `python scripts/verify-images.py <deck-dir>` — local files,
   size caps, CREDITS line per raster.
3. Renders: open every `renders/sN.png` and READ it — geometry collisions,
   contrast on plates, diacritics, wedge artifacts. Fix in `build.py`,
   rebuild clean, re-run motion, re-read. Uninspected renders = Gate fail.

## 11. Ship

- The `.pptx` (editable, notes embedded), the `renders/` PNGs, PDF handout
  via COM `ExportAsFixedFormat` only on request.
- Paste a ship log: palette, shape contract, transition map, entrance
  count, raster count, verifier outputs.
- Commit + push the SKILL change if any; reinstall both skill installs.

## §quick-build (the only shortcut)

Phases 1–3 compressed into one message (topic + palette pick + template
pick), research capped at 3 slides of notes, single-section deck (one
template, one transition, morph-lite). Phases 7/9/10/11 run FULL — no
shortcut ever skips assets, motion hygiene, render inspection, or gates.

## Don'ts for this workflow

1. Don't build before the outline + visual-plan nod.
2. Don't invent a fresh layout per slide — the morph contract (§2) forbids it.
3. Don't ship without `visual-plan.md` — ship-blocking, same as research-notes.
4. Don't let a slide reach the build with zero rasters; that's a phase-7
   plan failure, not a styling fix for phase 8.
5. Don't hand-edit the `.pptx` zip or click around in the GUI — scripts are
   truth, the `.pptx` is disposable output.
6. Don't re-run `motion.py` on the same file twice — rebuild clean first.
7. Don't diagnose motion from XML dumps; open the deck in PowerPoint and
   read the renders.
