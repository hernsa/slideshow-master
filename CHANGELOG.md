# Changelog

All notable changes to this project are documented here. Format follows
Keep a Changelog; versions follow SemVer.

## [1.0.0] - 2026-10-14

### Changed (rewrite: pure PPTX, HTML engines retired)

- Skill now authors **real .pptx decks**: python-pptx geometry/content +
  PowerPoint COM transitions/entrances/renders. reveal.js / Slidev / Marp
  engines, `generate-deck.md`, `routing.md`, `quick-generate.md`, and the
  three HTML demo decks are deleted.
- `workflows/generate-pptx.md`: 11 phases + quick-build path, both
  `research-notes.md` and `visual-plan.md` ship-blocking.
- `references/engines.md`, `animations.md`, `layouts.md`: rewritten
  PPTX-native (COM enums, rebuild-clean rule, inches grid, stagger table).
- `references/layout-templates/`: all 8 files converted to python-pptx
  recipes against the scaffold Helper API contract (`templates_index.json`
  v4); `references/modes/`: all 5 arcs rewritten PPTX-native.
- `references/media/images.md`, `media/icons.md`, `decorations.md`,
  `data-graphics/`, `tokens.md`: rewritten PPTX-native (raster floor, PIL
  prep, native-shape icons/diagrams/charts, inches tokens).
- `scripts/`: new `scaffold.py`, `verify-pptx.py` (OOXML asserts: canvas,
  notes, rasters, transitions, fx budget, continuity), `render.py`;
  `verify-images.py` rewritten for `build.py` refs + CREDITS.md.
  Retired `verify-deck.py`, `export-deck.sh`, `new-deck-scaffold.sh`.
- `references/verify-checklist.md`: 15 gates rewritten (raster floor,
  contrast on renders, back-row legibility, COM hygiene, morph-name
  discipline); new 5-step pre-ship run ending in eye review of renders.
- `README.md` rewritten; `AGENTS.md` commands updated.

## [0.2.0] - 2026-10-08

### Added

- `workflows/stages/` — five stage procedures (topic-research, image-review,
  visual-review, refine-spec, export-verify) plus `workflows/governance/`
  failure-recovery.
- `references/data-graphics/` — charts, tables, diagrams guides (pure
  HTML/CSS/SVG, no chart libs).
- Machine-readable index JSONs for visual-styles, layout-templates, and
  data-graphics.
- `docs/gallery.md` starter gallery, `docs/roadmap.md`.
- Repo-level files: LICENSE (MIT), AGENTS.md, CLAUDE.md, SECURITY.md,
  CODE_OF_CONDUCT.md, `.editorconfig`, `.gitattributes`, CI validate
  workflow, issue/PR templates, Claude plugin manifests.

### Fixed

- `export-deck.sh` marp path now passes `--allow-local-files` so local
  images render in exported decks.

## [0.1.0] - 2026-10-08

### Added

- Initial release: `slideshow` skill with hybrid engine router
  (reveal.js 6 / Slidev 52 / Marp 4).
- `references/` deep guides: animations, colors, layouts, engines,
  verify-checklist.
- `references/visual-styles/` (10 styles), `references/layout-templates/`
  (12 types), `references/modes/` (5 deck arcs).
- `workflows/` routing, generate-deck, quick-generate.
- `scripts/`: verify-images.py, export-deck.sh, new-deck-scaffold.sh.
- Three full 10-slide demo decks (reveal / Slidev / Marp).
- Docs: getting-started, faq, why-html-slides; CONTRIBUTING.md.
