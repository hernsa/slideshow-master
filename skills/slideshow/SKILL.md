---
name: slideshow
description: Build real animated .pptx decks via python-pptx + PowerPoint COM (Morph transitions, entrances, staged renders). Use when the user asks for a PowerPoint deck, pptx, slide deck, presentation, keynote-style talk, or demo talk.
---

# Slideshow Skill — Real .pptx Builder

You build real, animated `.pptx` decks: editable text, embedded photos,
Morph transitions, entrance animations, speaker notes. No HTML, no Marp, no
reveal.js, no rasterized slides. The output file is the deck.

Stack: `python-pptx` 1.0.2 (geometry + content) plus PowerPoint COM
(transitions, entrances, PNG renders). Motion authoring and render
verification require Windows + desktop PowerPoint; content and OOXML asserts
run anywhere. Install with `python -m pip` (never the `pip.exe` wrapper).

## Route (read this table, then load ONE workflow only)

| Request | Workflow | Mode |
|---|---|---|
| Tech talk, demo, API walkthrough | `workflows/generate-pptx.md` | `references/modes/tech-talk.md` |
| Fundraising / sales pitch | `workflows/generate-pptx.md` | `references/modes/pitch.md` |
| Workshop, how-to, handout | `workflows/generate-pptx.md` | `references/modes/tutorial.md` |
| Portfolio, gallery, launch | `workflows/generate-pptx.md` | `references/modes/showcase.md` |
| Story-driven keynote | `workflows/generate-pptx.md` | `references/modes/narrative.md` |
| "Fast", "quick", "draft", "15 minutes" | `workflows/generate-pptx.md` §quick-build | any (fixed style) |

PowerPoint versions + COM setup: `references/engines.md`. Stage
procedures (research, image review, visual review, refine, export):
`workflows/stages/`, `workflows/governance/failure-recovery.md`.

**Hard rule — selected authority only.** Load the ONE routed workflow and its
ONE mode. Do not mix procedures across modes. Supporting documents (styles,
templates, motion) refine the route; they never compete with it.

## Vocabulary

| Term | Meaning |
|---|---|
| Mode | Narrative arc: tech-talk, pitch, tutorial, showcase, narrative |
| Engine | PowerPoint 365 via python-pptx + COM. No other engines |
| Visual style | One locked palette + type pair from `references/visual-styles/` |
| Layout template | Copy-paste python-pptx recipe from `references/layout-templates/` |
| Design Read | One-line read + 3 dials before any building |
| Dials | DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY |
| Gate | Numbered ship-blocker in `references/verify-checklist.md` |
| Device | The deck's one organic device (tile cluster / blob-behind / arch) |
| Morph | p159 byObject transition between exact-name shapes |
| Anchor | Named shape (`data` = `cNvPr` name) continuing across slides |
| Render | COM-exported slide PNG, inspected by eye before shipping |

## Execution Discipline

1. Execute serially: intake → design read → style lock → research → outline +
   visual-plan → assets → build → motion → verify → ship. Never skip ahead.
2. Blocking means stop. No outline nod, no build. No renders inspected, no ship.
3. `python -m pip` for every install. The `pip.exe` wrapper is corrupt.
4. python-pptx owns geometry and content; COM owns transitions, entrances,
   renders. Never hand-edit the `.pptx` zip by hand when an API exists.
5. COM hygiene: kill stray `POWERPNT.EXE` before opening, rebuild the file
   clean (delete first, COM doubles effects on re-run), open with
   `WithWindow=False`, `DisplayAlerts=0`.
6. Verify the OOXML (`scripts/verify-pptx.py`) before spending COM time.
7. A render not inspected is a render not done. Read every exported PNG.
8. Act at the owning layer; no speculative execution, no invented APIs.

## Communication Rules

- Open with a one-line Design Read: `Reading this as: <mode> for <audience>,
  <vibe>, <dial values>.`
- Defaults: mixed-tech audience, 8 slides, dark photographic section +
  one showcase break, EN display + VI gloss only when asked, `.pptx` + PNG
  renders shipped.
- Match the user's language (Vietnamese deck → Vietnamese replies).
- State the phase on entry (`Phase 4/11 — research`) and what blocks next.

## Reference Map

- Modes live in `references/modes/` (+ `_index.md` picker).
- Engines: `references/engines.md` (PowerPoint versions, COM setup, enums).
- Styles: `references/visual-styles/` (+ `styles_index.json`).
- Craft grammar: `references/pptx-motion-language.md` (12 sections — the law).
- Motion mechanics: `references/animations.md` (COM transitions + entrances).
- Layouts: `references/layouts.md` (inches grid) + `references/layout-templates/`
  (+ `templates_index.json`) — copy the recipe, never improvise the geometry.
- Media: `references/media/images.md` (sourcing + PIL prep + raster floor),
  `references/media/icons.md`.
- Data: `references/data-graphics/` (charts via python-pptx, tables, diagrams).
- Tokens: `references/tokens.md` (spacing, radius, type tiers in pt).
- Gates 1–15 → `references/verify-checklist.md`.
- Scripts: `scripts/scaffold.py`, `scripts/verify-images.py`,
  `scripts/verify-pptx.py`, `scripts/render.py`.
