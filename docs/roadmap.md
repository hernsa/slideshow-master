# Roadmap

Where slideshow-master goes next. Items are ordered; checked items shipped.

## Shipped

- [x] Pure-PPTX rewrite (v1.0.0): python-pptx + PowerPoint COM stack,
  `generate-pptx.md` 11-phase workflow, scaffold/verify/render scripts
- [x] 5 narrative modes, 13 visual styles, 8 python-pptx layout recipes
- [x] Data-graphics pack (diagrams, charts, tables — native shapes)
- [x] PPTX craft law (`pptx-motion-language.md`): anchors, Morph
  contract, stagger, value ramp, type scale, spec grammar
- [x] Governance: failure-recovery catalog
- [x] Verify checklist (15 PPTX-native gates) + `verify-pptx.py` OOXML
  asserts + renders-by-eye pre-ship run

## Next

- [ ] PowerPoint version watch: re-verify COM enums + p159
  serialization yearly against installed 365 (`references/engines.md`)
- [ ] More visual styles: high-contrast print theme, academic-poster style
- [ ] More layout recipes: agenda, team-roster, pricing, appendix
- [ ] `scripts/verify-pptx.py`: entrance-delay asserts (stagger timing
  from the timing tree, not just count + filter)
- [ ] Rendered PNG gallery (COM-exported renders of a sample deck)
- [ ] i18n note: RTL + CJK font-pair guidance in `references/tokens.md`

## Non-goals

- HTML slide engines (retired in v1.0.0 — this skill is PPTX-native)
- A visual slide editor or hosted builder
- Chart libraries — native shapes keep decks dependency-free and editable
