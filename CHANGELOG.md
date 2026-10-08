# Changelog

All notable changes to this project are documented here. Format follows
Keep a Changelog; versions follow SemVer.

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
