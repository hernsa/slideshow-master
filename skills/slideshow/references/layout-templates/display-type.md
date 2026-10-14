# Display type — giant statement

> Tokens in [tokens.md](../tokens.md). One line, one claim, type does the work. Pastel rotation allowed (`BBE6F7 → FFFDE4 → E2EFFB`, saturation ≤35%, near-black `#1F2328` type).

```python
slide = new_slide()
solid_bg(slide, BG)
kicker(slide, "ACME CORP · THESIS", x=0.65, y=1.9, color=ACCENT)
title(slide, "Ship calmly.", x=0.65, y=2.3, w=12.0, size=96, accent="calmly.", accent_color=ACCENT)
body(slide, "Preview deploys took p95 from 412ms to 243ms.", x=0.65, y=5.3, w=9.0, size=20)
```

Pastel variant: `solid_bg(slide, "#FFFDE4")`, hero in `#1F2328`, e.g. `title(slide, "41% faster.", ..., size=96)`.

Scale rule: hero 72–96pt on the 13.333in canvas (the AirPods tier). One accent word max; zero letter-spacing.

## Slide spec

```
Slide N — <Claim>                      bg: <solid|pastel>
  Text runs:  kicker {11pt} ; hero {72–96pt ≤2 lines} ; lead {20pt, one sentence}
  Z-order:    bg → copy
  Entrances:  none (the reveal IS the slide change; Morph carries it)
  Anchors:    none required
  Images:     none (this is the one sanctioned text-only pattern — record why)
  Done when:  hero fits ≤2 lines at ≥72pt on the render; one lead sentence, then stop.
```

## Don't

- Don't stack a paragraph under giant type — one lead sentence, then stop.
