---
name: slideshow
description: Create modern HTML slideshows via routed workflows (tech-talk, pitch, tutorial, showcase, narrative). Routes reveal.js / Slidev / Marp with visual styles, layout templates, animations, and verification gates. Use when the user asks for a slide deck, presentation, keynote-style page, or demo talk.
---

# Slideshow Skill — Hybrid Engine Router

You build conference-grade HTML slide decks. Never AI-slop (no purple-blue
gradients, no three-equal-cards, no centered-hero-over-mesh defaults).
Every deck gets: a routed mode + engine + visual style, verified images,
fragments/motion, speaker notes, reduced-motion fallback, and an export path.

## Route (read this table, then load ONE workflow only)

| Request | Workflow | Mode | Engine bias |
|---|---|---|---|
| Tech talk, demo, API walkthrough | `workflows/generate-deck.md` | `modes/tech-talk.md` | reveal.js / Slidev |
| Fundraising / sales pitch | `workflows/generate-deck.md` | `modes/pitch.md` | Marp / reveal.js |
| Workshop, how-to, handout | `workflows/generate-deck.md` | `modes/tutorial.md` | Slidev / Marp |
| Portfolio, gallery, launch | `workflows/generate-deck.md` | `modes/showcase.md` | reveal.js |
| Story-driven keynote | `workflows/generate-deck.md` | `modes/narrative.md` | reveal.js |
| "Fast", "quick", "15 minutes", "draft" | `workflows/quick-generate.md` | any (fixed style) | Marp first |

Full decision logic: `workflows/routing.md` (engine table, style picker,
mode picker). Engine versions + installs: `references/engines.md`.

**Hard rule — selected authority only.** Load the ONE routed workflow and
its ONE mode. Do not mix procedures across modes. Supporting documents
(styles, templates, animations) refine the route; they never compete with it.

## Vocabulary

One meaning per term across every file in this skill.

| Term | Meaning |
|---|---|
| **Mode** | Narrative arc (tech-talk, pitch, tutorial, showcase, narrative). Picks the slide outline, never the engine |
| **Engine** | Runtime: reveal.js (full HTML/JS control), Slidev (Markdown+Vue), Marp (Markdown→static) |
| **Visual style** | One named style from `visual-styles/` — tokens + fonts + code theme + gradient rule. One style per deck |
| **Layout template** | One slide-type sketch from `layout-templates/` (comparison, stats, quote, code-demo…). A starting sketch, freely adjusted |
| **Design Read** | The one-line declaration of deck kind + audience + vibe + engine/style/fonts, stated before building |
| **Dials** | `DESIGN_VARIANCE` / `MOTION_INTENSITY` / `VISUAL_DENSITY` (1–10 each). Drive layout, motion, density choices |
| **Gate** | One check in `verify-checklist.md`. `⛔ BLOCKING` gates stop and wait for the user; the rest auto-continue |
| **Device** | Everyday slide carrier — stat card, callout, KPI tile, divider, quote block, browser mock |
| **Morph** | Same-element continuity across slides: `data-id` (reveal.js), `view-transition-name` (Marp/Slidev), `data-flip-id` (GSAP) |

## Execution Discipline

1. **Serial execution** — follow the routed workflow's steps in order.
2. **Blocking means stop** — at every `⛔ BLOCKING` gate, wait for explicit
   user confirmation. Never decide on the user's behalf.
3. **Outline before slides** — one line per slide (title + point + visual);
   get a nod before writing slides. Cheap to change, expensive to redo.
4. **Markdown source first** — even for reveal.js (convert at the end).
   Markdown is diffable and reviewable. Ship it alongside the built deck.
5. **Research (2-source rule)** — every factual claim needs 2+ independent
   sources; APIs/flags/versions verified against current docs, never memory.
   Log sources per slide as a comment; single-source claims get `[unverified]`.
6. **Images (hybrid + verify, no exceptions)** — AI / stock (credited) /
   user-supplied; copied into `assets/`, never hotlinked; logged in
   `assets/CREDITS.md`; checked by `scripts/verify-images.py`.
7. **Act at the owning layer** — on failure, repair at the shallowest layer
   that owns the fault (slide → outline → style → tooling), then resume.
   Never silently downgrade a required artifact.
8. **No speculative execution** — do not prepare later-phase artifacts before
   their owning step.

## Communication Rules

- One-line Design Read before building:
  > Reading this as: \<deck kind> for \<audience>, with a \<vibe> language,
  > leaning toward \<engine + style + font pair>.
- If the user says "defaults": mixed-tech audience, 12 slides, Midnight SaaS
  dark, hybrid images + verify, HTML + PDF.
- Match the user's language. Keep file/field/enum names in English.
- Before switching phases, state the phase and what it needs.

## Reference Map

- Workflows → `workflows/routing.md`, `workflows/generate-deck.md`,
  `workflows/quick-generate.md`, `workflows/index.md`
- Stages → `workflows/stages/` (topic-research, image-review,
  visual-review, refine-spec, export-verify); governance →
  `workflows/governance/failure-recovery.md`
- Modes → `references/modes/` (+ `_index.md` picker)
- Visual styles → `references/visual-styles/` (+ `_index.md` picker,
  `styles_index.json`)
- Layout templates → `references/layout-templates/` (+ `_index.md` picker,
  `templates_index.json`)
- Data graphics → `references/data-graphics/` (charts, tables, diagrams
  + `graphics_index.json`)
- Engines + versions → `references/engines.md`
- Animations, morph, fragments → `references/animations.md`
- Palettes, fonts, code themes → `references/colors.md`
- Color deployment, rotation scripts → `references/color-usage.md`
- Layouts, boxes, image treatments → `references/layouts.md`
- Images, icons, media density → `references/media/`
- Gates 1–20 → `references/verify-checklist.md`
- Scripts → `scripts/verify-images.py`, `scripts/verify-deck.py`,
  `scripts/export-deck.sh`, `scripts/new-deck-scaffold.sh`
- Starters → `examples/reveal-demo/`, `examples/slidev-demo/`,
  `examples/marp-demo/`
- Contributor guide → repo `CONTRIBUTING.md`; first-deck guide → `docs/`
