# Roadmap

Where slideshow-master goes next. Items are ordered; checked items shipped.

## Shipped

- [x] Hybrid Engine Router (reveal.js / Slidev / Marp) + routing workflow
- [x] 5 narrative modes, 10 visual styles, 12 layout templates
- [x] Data-graphics pack (charts, tables, diagrams — pure HTML/CSS/SVG)
- [x] Workflow stages (research, image-review, visual-review, refine, export-verify)
- [x] Governance: failure-recovery catalog
- [x] Scripts: scaffold, image verify, per-engine export
- [x] 3 full starter decks + gallery + verify checklist (16 gates)

## Next

- [ ] Engine version watch: re-pin reveal.js / Slidev / Marp quarterly in
  `references/engines.md` (current pins noted per engine file)
- [ ] More visual styles: high-contrast print theme, academic-poster style
- [ ] More layout templates: agenda, team-roster, pricing, appendix
- [ ] `scripts/verify-deck.py`: link checker + contrast spot-check to
  complement `verify-images.py`
- [ ] Rendered screenshot gallery (CI-rendered PNGs of the three starters)
- [ ] i18n note: RTL + CJK font-pair guidance in `references/colors.md`

## Non-goals

- Native PPTX authoring (use ppt-master for that — this skill is HTML-first)
- A visual slide editor or hosted builder
- Chart libraries (observable-plot, chart.js) — pure CSS/SVG keeps decks
  dependency-free and printable
