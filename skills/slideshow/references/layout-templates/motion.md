# Motion — anchor continuation across slides

> Tokens in [tokens.md](../tokens.md). Morph is a PowerPoint transition applied in `motion.py`, not content. This file owns the geometry contract that makes Morph possible: same `shape.name`, same slot, new text or photo — and the slide change reads as motion. Full grammar: `references/pptx-motion-language.md` §§1-3.

```python
# slide 1 — anchor headline pinned at its slot
title(slide1, "Hanoi · 1640", x=0.65, y=0.7, w=8.0, size=44, name="sec-title")

# slide 2 — SAME name, SAME slot, new text; photo swaps underneath
title(slide2, "Hue · 1776", x=0.65, y=0.7, w=8.0, size=44, name="sec-title")
```

(`title()`/`kicker()`/`circle_pic()` take an optional `name=` that sets `shape.name` = the morph identity. Parked shapes wait off-canvas: `rect_pic(..., x=14.5, ..., name="disc-next")` — Morph flies them in.)

Rules: 2 anchors per section (headline block + photo frame). Move one anchor per step, never both. ONE deck transition (Morph-byObject default; named `fade` exceptions). Entrances ≤3 fades, `100–150ms` stagger, `≤600ms` total. Body copy is never an anchor and never entrance-animated.

## Slide spec

```
Slide N — <Title>                      bg: <same as N-1>
  Text runs:  <same slots as N-1, new text>
  Z-order:    identical order to N-1
  Entrances:  ≤3, same slots as N-1
  Anchors:    <name> pinned ; <name> moves <dx,dy> (ONE moves)
  Done when:  verifier reports shared names with N-1; renders show the glide.
```

## Don't

- Don't invent a fresh layout per slide and don't "fix" parked off-canvas shapes back on-canvas — both kill the morph.
