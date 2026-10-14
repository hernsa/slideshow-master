# Media — Picker Index

> Images + icons: the two things that separate a deck from a document.
> Photos are embedded rasters (never hotlinks); icons are native
> shapes (never emoji, never icon fonts).

## Picker — which media for which story

| Story you tell | Media to use | File | Max per deck |
|---|---|---|---|
| Proof it exists (screenshot, photo) | Framed raster, white 1pt outline | `images.md` | 1 per slide |
| Immersion (place, mood, scale) | Full-bleed plate + scrim 60–70% | `images.md` | 1 per section |
| Brand tint on a photo | Darkened plate (PIL brightness + desat) | `images.md` | 2 |
| Person behind a quote | Avatar `circle_pic` tile | `images.md` | 1 per quote |
| Text vs visual, 50/50 | Split: copy column + feature `rect_pic` | `images.md` | 3 |
| Action, status, direction | Native-shape icon (2–4 shapes) | `icons.md` | unlimited, 1 style |
| 3 features at a glance | Pills with labels | `icons.md` | 1 row per deck |
| Sequence with owners | Flow pills + fork connectors | `icons.md` | 2 |
| The one takeaway | Leader callout (line + dot + label) | `icons.md` | 1 per slide max |

## File pointers

- `images.md` — raster floor, sourcing ladder, PIL prep, placement
  grammar, budgets. Attribution format matches
  `scripts/verify-images.py` (`assets/CREDITS.md`).
- `icons.md` — native-shape-only system, leader callouts, pills,
  failures + fixes.

## Global rules (all media)

- Offline-safe: no icon fonts, no hotlinked images — everything
  embedded, so the .pptx travels whole.
- Notes carry narration; captions live under feature photos at 11pt
  muted where the plan calls for one.
- Explicit RGB everywhere, never theme slots.
- Type floor: gloss 11pt minimum, never below.

## Anti-slop rules (the two rules)

- No 3 consecutive text-only slides — every 3rd slide changes surface
  (tinted divider, plate, accent band, dark stage).
- Zero emoji-as-icons. Ever.
