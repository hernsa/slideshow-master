# Diagrams — duo boxes, forks, flows (PPTX-native)

> Diagrams are native shapes + textboxes, drawn by build.py. No SmartArt
> (unscriptable), no screenshots of diagrams (uneditable), no inline SVG.

## 1. The three workhorses

- **Duo boxes**: two rounded rects side by side, one per accent (jade/gold),
  each with a 20–24pt head + 2-line 14pt body. The pillar pattern. Widths
  equal, gap 0.3in, vertically centered in the live zone.
- **Fork**: one kicker/headline top-center, two arrows (straight connectors
  with triangle heads) splitting to two boxes. Used for pillar splits,
  before/after, cause/effect. Draw with
  `connect(slide, name, x1, y1, x2, y2, arrow=True)`.
- **Flow pills**: 3–4 stadium pills in a row with `→` separators (text runs,
  not shapes), e.g. SCHOOLS → AI+SEA LABS → GUARDIANS. 14–16pt semibold,
  solid fills, alternating accent tints. One flow per slide max.

## 2. Construction rules

- All boxes: `ROUNDED_RECTANGLE`, radius via `adjustments[0] ≈ 0.12–0.18`.
- Fills solid (accent or tint); lines 1pt accent-dark or none. Contrast
  first: white 16pt on solid jade passes; muted-on-tint often doesn't —
  check renders.
- Arrows: `STRAIGHT` connectors + `end_arrowhead`; never draw arrowheads
  as separate triangles (they detach on nudge). `connect()` bakes the
  `a:tailEnd` triangle for you.
- Every diagram box gets a name (`pillar-a`, `flow-1`) — diagrams persist
  across slides as morph anchors.

## 3. Don'ts

- Max one diagram per slide. Two diagrams = two slides.
- No org-chart sprawl (max 5 nodes), no 3D bevels, no gradient fills in
  diagram boxes (flat only — gradients fight the value ramp).
