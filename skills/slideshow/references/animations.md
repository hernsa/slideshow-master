# Motion — COM transitions + entrances (mechanics)

> The grammar (ONE transition, stagger cadence, morph contract) lives in
> `pptx-motion-language.md` §§2–4. This file is the COM mechanics: constants,
> call shapes, budgets, hygiene. Craft stays in the craft file.

## Transition map (the only pattern)

```python
FADE = 1793          # ppEffectFade
MORPH_OBJECT = 3954  # ppEffectMorphByObject
FADE_SLIDES = {1, 6}  # named exceptions from style lock, max ~2 per deck

for i, slide in enumerate(pres.Slides, start=1):
    t = slide.SlideShowTransition
    t.EntryEffect = FADE if i in FADE_SLIDES else MORPH_OBJECT
    t.AdvanceOnTime = 0  # manual advance, always
```

Default every slide to Morph-byObject; exceptions are named at style lock,
never improvised at motion time. One `zoom` showcase or one `fade` break per
deck — never both, never more.

## Entrance budget (≤3 per slide, shared with stagger)

```python
FADE_FX, AFTER_PREV = 10, 3  # msoAnimEffectFade, triggerAfterPrevious
seq = slide.TimeLine.MainSequence
for shape, delay_ms in plan:  # max 3 entries, 100–150ms apart
    fx = seq.AddEffect(shape, FADE_FX)
    fx.Timing.TriggerType = AFTER_PREV
    fx.Timing.TriggerDelayTime = delay_ms / 1000
```

Rules: entrances are fade-only, after-previous chains, paragraphs whole
(`animateLevelNone`). Reading order: kicker → headline → body → visual.
Zero click-reveals unless the visual-plan explicitly buys them (`trigger 1`
is a smell — grep the plan for `click` before motion). Morph-only sections
carry NO entrances: the flying anchor is the animation.

## Rebuild-clean rule (non-negotiable)

COM **doubles** effects on re-run. The pipeline is:

```
delete deck.pptx → run build.py → run motion.py → render → inspect
```

`build.py` output is disposable; the scripts are truth. Never re-run
`motion.py` on an already-motioned file. Never hand-tweak in the GUI and
call it a build — re-encode the tweak into `build.py`.

## COM hygiene checklist (every motion run)

1. `taskkill /F /IM POWERPNT.EXE` — zombies lock files and reject calls.
2. Open `WithWindow=False`, `DisplayAlerts=0`.
3. `AdvanceOnTime=0` on every slide (manual advance is the default state).
4. Export renders in the same session: `slide.Export(path, "PNG", 1920, 1080)`.
5. `pres.Close()`, `app.Quit()` — then verify the process is actually gone.
6. PDF handout (on request only): `pres.ExportAsFixedFormat(pdf, 2)`
   (`ppFixedFormatTypePDF = 2`).

## Stagger delays (the cadence table)

| Entrance | Delay | Duration |
|---|---|---|
| 1st (kicker/headline) | 100ms | 300ms |
| 2nd (body/visual) | 220ms | 300ms |
| 3rd (visual/accent) | 340ms | 300ms |

Total ≤ 640ms. `transform + opacity` has no COM equivalent to set — fade
covers it; never reach for fly/swirl/boomerang presets. If a 4th element
wants attention, it is already visible — cut the entrance, not the budget.

## What COM cannot do (don't try)

- Transition `Speed`: no enum in the typelib — accept the default.
- Shape rotation on custom-geometry pictures: renders a white wedge even via
  GUI — bake tilt into pixels in PIL (see `media/images.md`).
- Reliable headless operation with a visible window open: always
  `WithWindow=False`.
- Automation without desktop PowerPoint installed: BLOCKED — say so loudly,
  ship content-only with morph/entrance plan documented, never fake the XML.
