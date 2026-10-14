# Modes Index — PPTX Deck Arcs

> All modes live in `references/modes/`. The route table in `SKILL.md`
> selects one mode per deck. Never blend two arcs in one deck.

## Mode table

| Mode | File | Goal | Arc | Slides |
|---|---|---|---|---|
| Tech Talk | `tech-talk.md` | Persuade engineers with a live demo | Problem → Demo → Code → Takeaways | 10 |
| Pitch | `pitch.md` | Win a yes: funding, approval, headcount | Hook → Problem → Solution → Traction → Ask | 8 |
| Tutorial | `tutorial.md` | Teach a skill the audience can repeat hands-on | Goal → Steps → Pitfalls → Exercise | 8 |
| Showcase | `showcase.md` | Prove range with visual evidence | Gallery sweep | 6 |
| Narrative | `narrative.md` | Move a mixed audience with a story | Hero → Tension → Turn → Resolution | 8 |

## How to pick (in order)

1. **Is there a live demo or runnable code?** If yes → `tech-talk.md`.
2. **Is there an ask with a deadline?** Funding, hiring, migration
   approval, conference acceptance. If yes → `pitch.md`, even if the
   topic is technical.
3. **Must the audience reproduce steps tomorrow?** Install, configure,
   ship. If yes → `tutorial.md`. Tutorial decks ship a handout PDF.
4. **Is the proof mostly screenshots and shipped work?** Redesigns,
   past talks, shipped product. If yes → `showcase.md`.
5. **Otherwise → `narrative.md`.** Keynotes, openers, vision talks,
   anything where feeling carries further than a diff.

## Tie-breakers

- Code + story both present: pick by the closing slide. Ends with a
  diff or benchmark → tech talk. Ends with a line the audience quotes
  → narrative.
- Pitch vs showcase: pitch ends with an ask slide (amount, date,
  contact). Showcase ends with a contact strip, no ask number.
- Tutorial vs tech talk: tutorial has numbered steps the audience
  follows along with. Tech talk has one hero demo the speaker drives.
- Time-boxed to 5 minutes: prefer showcase (6 slides) or pitch
  (8 slides, drop slide 6 detail to notes).

## Design dials per mode

| Mode | DESIGN_VARIANCE | MOTION_INTENSITY | VISUAL_DENSITY | Palette default |
|---|---|---|---|---|
| tech-talk | 7 | 6 | 5 | Midnight SaaS dark + mono |
| pitch | 5 | 3 | 3 | Teal Serenity |
| tutorial | 4 | 4 | 6 | Botanical Warm (on request) else Forest Ink |
| showcase | 8 | 5 | 2 | Midnight SaaS dark, one accent per project |
| narrative | 9 | 6 | 2 | Crimson Bold or Forest Ink, warm accent |

Dials are set in the Design Read and drive layout choices from
`references/layouts.md` and motion from `references/animations.md`.

## File contract (every mode file)

Each file in this directory follows the same contract:

1. Arc description (purpose + slide count).
2. Per-slide outline: slide number + title + template recipe from
   `references/layout-templates/` + beat notes.
3. PPTX notes: moving object, raster needs, entrance exceptions.
4. Mode-specific guidance, concrete, no generic advice.

## Outline approval gate

Write the per-slide outline (title + point + visual, one line per
slide) plus `visual-plan.md` spec blocks before building anything, per
`workflows/generate-pptx.md` phase 5. Paste outline + research-notes +
visual-plan together, get a nod, then build. Outlines are cheap;
rebuilt decks are not.

## Verify pointer

All modes converge on `references/verify-checklist.md` gates,
`scripts/verify-pptx.py`, `scripts/verify-images.py`, and the
renders-by-eye review. Mode choice never skips verification.
