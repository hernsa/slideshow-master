# Verify checklist — Gates 1–15 (pure PPTX)

> Every gate states WHY + HOW + PASS + FAIL + fix. Fill the ship record
> at the bottom and keep it with the deck. Scripts truth, renders proof.

```
Deck: Acme Q3 — 8 slides — python-pptx + PowerPoint COM
Outline nod: 2026-10-14 09:40 UTC by boss
Research: research-notes.md, 8 sections, 2-source log each
Visual plan: visual-plan.md, 8 spec blocks, hard counts met
Build: python build.py -> deck.pptx (2.1MB)
Motion: python motion.py -> Morph 2-8, fade 1; renders/s1-8.png read
Verify: verify-pptx.py OK (Rasters: 17 across 8/8) · verify-images.py OK
Continuity: anchors hero/disc/scrim-left shared 1-8
Ship: deck.pptx + renders/ + handout.pdf
```

## Pre-condition — Content density

WHY: a thin deck with perfect motion is still a thin deck. A
`research-notes.md` with 2 bullets per slide means the slides will starve.

HOW: `research-notes.md` exists with one section per slide, 4–8 content
bullets + 2-source log each. Any slide section under ~60 words of distinct
facts gets redone before the outline nod.

## Gate 1 — Outline approved

WHY: building 8 slides twice costs a day; a nod costs a minute.

HOW: paste the outline + `research-notes.md` + `visual-plan.md` together
and get an explicit nod with a timestamp. Record it in the ship record.

- PASS: `Outline nod: 2026-10-14 09:40 UTC by boss`
- FAIL: "looks fine, go" with no timestamp, or a nod on the outline alone
  while `visual-plan.md` is still a vibe.

## Gate 2 — Two-source rule

WHY: one invented stat in front of a room kills credibility.

HOW: 100% of headline stats, dates, and proper nouns in
`research-notes.md` carry two independent sources. Mark anything single-
sourced `[unverified]` and keep it off headline slides.

## Gate 3 — Raster floor (photos are load-bearing)

WHY: a deck with no photographs is a slide sorter, not a deck. Every
reference deck carries rasters on every slide
(`references/pptx-motion-language.md` §5).

HOW:

1. `python scripts/verify-pptx.py deck.pptx` — the `Rasters:` line must
   clear the target (default: total ≥ slide count, on ≥60% of slides).
2. `python scripts/verify-images.py <deck-dir>` — every `ASSETS / "…"`
   ref and image literal in `build.py` resolves to a file, and
   `assets/CREDITS.md` names every source file with author + license.
3. Narrative/photo-collage sections run 3–6 rasters per slide.

- PASS: `Rasters: 17 across 8/8 slides (target >= 8)` + `OK: 12 image(s)
  verified`
- FAIL: zero rasters; a `CREDITS.md` line reading "No external raster
  images used in this deck" (a failure line, never a credit line); a deck
  of native shapes with no raster anywhere.
- Fix: source the photos (`references/media/images.md` §1 ladder), prep in
  PIL, rebuild. Text-only decks (type specimen, typography talk) pass
  `--allow-text-only` and record why in the ship record.

## Gate 4 — Contrast, measured on renders

WHY: scrims and plates shift under real rendering; numbers in build.py lie.

HOW: open `renders/sN.png` at full size. Body copy must read at arm's
length: light type on plates needs a scrim (`a:alpha` ≥ 60%) or a clear
side of frame. Muted gloss text (11pt) needs ≥4.5:1 against its surface —
eyeball it on the render, and bump the plate darkness (never shrink type)
when in doubt.

- PASS: every render reads cleanly; no white-on-daylight accidents.
- FAIL: daylight plate under white 16pt body; gold pills with thin dark
  text; gloss lines dissolving into the photo.
- Fix: darken the plate (`.85` → `.45`), widen the scrim, or move the
  copy column. Cut words, never point size.

## Gate 5 — Placeholder scan

WHY: "KICKER LINE" ships more often than anyone admits.

HOW: `verify-pptx.py` already fails on placeholder text (loremipsum,
unfinished markers, working titles) in shapes and notes. Also grep the
deck sources:

```powershell
Select-String -Path build.py,motion.py -Pattern "lorem|todo:|tbd|fixme|KICKER LINE|Slide one headline" -CaseSensitive:$false
```

- PASS: zero hits outside the scaffold's own comments.
- FAIL: any hit in a slide function. Fix the copy, rebuild.

## Gate 6 — Style tokens

WHY: one palette, one voice. Five grays and three blues is a default.

HOW: palette block in `build.py` is 4–6 hexes (BG/INK/ACCENT/ACCENT2/
MUTED/CARD), all fills use explicit RGB (never theme slots), `FONT` is one
family + Consolas for mono lines only. Zero emoji anywhere (see Gate 14).

## Gate 7 — Code and dense-text slides

WHY: a wall of 9pt code is a handout, not a slide.

HOW: code/mono textboxes hold ≤12 non-blank lines at ≥14pt. Anything
longer becomes 3–5 pills, a duo-box diagram, or moves to notes + handout.

## Gate 8 — Motion budget and manual advance

WHY: the clicker advances slides, never assembles them. A 20-step slide
is a demo that the speaker can't drive.

HOW: `verify-pptx.py` enforces it structurally — every slide's `fx`
count prints in the per-slide line; budget is ≤3 fade entrances per
slide, fade filter only. `AdvanceOnTime` is False on every slide
(`advTm` absent). Entrance delays stagger 100–150ms apart
(`references/animations.md` stagger table).

- PASS: per-slide lines show `fx=0..3`, no `auto-advance` failures.
- FAIL: `slide 4: 7 entrance effects (budget is 3)`; any `advTm present`
  failure; non-fade filters.
- Fix: cut entrances to the 3 that carry the point (kicker → headline →
  visual), move the rest to static. Rebuild clean, re-run motion once.

## Gate 9 — Speaker notes 1:1

WHY: notes are the talk. A slide without notes is a slide the speaker
wings.

HOW: `verify-pptx.py` fails any slide with empty notes. Every substantive
slide carries its full spoken beat in notes (the iSpeak deck shipped full
English speech as notes 8/8). Appendix slides may carry `NO-NOTES` as
their entire note text.

## Gate 10 — Back-row legibility (the projector test)

WHY: PPTX has no 390px viewport — it has a person 20 meters away.

HOW: open each render scaled to 960px wide. If the body copy isn't
readable there, it won't read in the room. Minimums: body 14–16pt, gloss
11pt only for asides, hero 54–96pt. When a render fails, cut words or
darken the plate — never shrink type.

## Gate 11 — Export smoke (renders for every slide)

WHY: renders are the proof. No renders, no review.

HOW: `renders/s1.png … sN.png` exist at 1920×1080, one per slide, exported
in the same COM session as the motion pass. PDF handout on request via
`ExportAsFixedFormat` (`ppFixedFormatTypePDF=2`) in that same session.

- PASS: N renders, N slides, each one actually looked at (Gate 10 + phase
  10 of the workflow).
- FAIL: missing renders, 0-byte PNGs, renders from a previous build
  (timestamps older than the .pptx).

## Gate 12 — Clean COM session

WHY: zombie PowerPoint locks files and rejects calls.

HOW: `motion.py` / `render.py` taskkill before opening, open with
`WithWindow=False`, `DisplayAlerts=0`, `Close()` + `Quit()` at the end.
After the run, no `POWERPNT.EXE` remains and the .pptx timestamp is fresh.
`Call was rejected by callee` means a zombie — taskkill, rebuild clean,
run once.

## Gate 13 — Theme ramp and rotation

WHY: eight identical backgrounds is a slideshow screensaver.

HOW: backgrounds walk the style-locked 3–4-stop value ramp
(`references/pptx-motion-language.md` §7); longest identical-bg run ≤2;
outline `bg:` tags match the built deck. One saturated break per section
max, never pastel + neon in one deck.

## Gate 14 — Icon and glyph discipline

WHY: emoji renders as color blobs on some projectors and as tofu on
others. Icon fonts don't travel with the file.

HOW: icons are native shapes only (2–4 shapes each,
`references/media/icons.md`); leaders are line + 12px dot + 18pt label.
Grep the sources for emoji:

```powershell
Select-String -Path build.py -Pattern "[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}]"
```

- PASS: zero hits. Fix: draw the glyph or delete it.

## Gate 15 — Composition and motion-language

WHY: this is the PPTX craft law — the difference between slides and a deck.

HOW (all vs `references/pptx-motion-language.md` + the template recipes):

1. `visual-plan.md` has one spec block per slide in z-order with
   `Template:` / `Text runs:` / `Z-order:` / `Images:` / `Entrances:` /
   `Anchors:` / `Done when:` — and the built slides match it.
2. Style lock named the 3–8 shape vocabulary AND the one moving object
   (§0, §1); the deck reuses them, no fresh layout per slide.
3. Anchors use exactly-matching `name=` values across slides; exactly one
   anchor moves per step (§2). Parked shapes (`x=14.5`) are never "fixed"
   back on-canvas.
4. ONE transition for the whole deck (Morph-byObject default), named
   exceptions only (§3).
5. Entrances ≤3 per slide, ≤640ms total, sharing the Gate 8 budget (§4).
6. Photos full-bleed-with-scrim or the deck's one organic device;
   copy column pinned outside moving groups (§5, §6).
7. Value ramp holds; bg run ≤2 (§7, Gate 13).
8. Display headline from the named tiers, one accent word per slide (§8).
9. The `Done when:` line of every spec block is literally true on the
   render.

- FAIL: no named vocabulary and no moving object; anchor `name=` drift
  between slides; off-canvas parked shapes "fixed"; body copy as a morph
  anchor; pastel + neon in one deck.
- Fix example — a photo-collage spec block that passed:

```
Slide 3 — Hà Nội · 1890        bg: plate .70
  Template: photo-collage
  Text runs:  hero "Hà Nội · 1890" 54pt bold ; sub 16pt 2 lines
  Z-order:    plate → tiles → disc → copy
  Images:     bay-bg plate + tile-1/2 + disc = 4 rasters
  Entrances:  hero .10s, sub .22s (2 only)
  Anchors:    disc rot 0 → -89 (baked) ; hero pinned identical
  Done when:  4 rasters embedded, hero glyph-identical to slide 2,
              disc visibly rotated on the render.
```

## Pre-ship run (20 minutes, in order)

1. Structure → `python scripts/verify-pptx.py deck.pptx` (expect `OK`,
   and a `Rasters:` line clearing the target).
2. Assets → `python scripts/verify-images.py <deck-dir>` (expect `OK`).
3. Deck asserts → `python verify_extra.py` (expect `OK`).
4. Eye → read every `renders/sN.png` at full size, then at 960px wide
   (Gates 4, 10, 15.9). Fix in `build.py`, rebuild clean, re-run motion,
   re-read. Never diagnose from XML dumps.
5. Motion hygiene → Gate 12 (no zombies, fresh timestamps), then ship the
   .pptx + renders/ (+ handout PDF on request) with the filled ship
   record.
