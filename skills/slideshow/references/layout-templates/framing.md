# Framing — open / divide / close

> Tokens in [tokens.md](../tokens.md). One slide per pattern. This file owns framing; body patterns live in `references/layouts.md`, diagrams in `references/data-graphics/diagrams.md`. Helpers (`solid_bg`, `kicker`, `title`, `body`, `circle_pic`, `rect_pic`, `set_notes`) ship in the scaffold's `build.py` — same signatures in every deck.

## Open (title hero)

```python
slide = new_slide()
solid_bg(slide, BG)
kicker(slide, "ACME CORP · Q3 ENGINEERING REVIEW · OCT 2026", x=0.65, y=1.9, color=ACCENT)
title(slide, "Ship calmly.", x=0.65, y=2.3, w=8.0, size=54, accent="calmly.", accent_color=ACCENT)
body(slide, "How preview deploys took p95 from 412ms to 243ms in six weeks — and ended Friday fear.",
     x=0.65, y=3.6, w=7.5)
circle_pic(slide, "speaker", "assets/ada.jpg", cx=1.15, cy=5.5, d=0.7)
body(slide, "Ada Okafor · Platform Lead, Acme", x=1.75, y=5.35, w=5.0, size=14)
set_notes(slide, "Open with the Friday-fear story; land the 412→243 number before advancing.")
```

## Divide (numbered + number-free)

```python
slide = new_slide()
solid_bg(slide, BG)
title(slide, "02", x=0.65, y=1.6, w=3.0, size=96, color=MUTED)          # ghost number
kicker(slide, "PART TWO — EVIDENCE", x=0.65, y=3.1, color=ACCENT)
title(slide, "The pipeline recovered", x=0.65, y=3.5, w=9.0, size=44)
body(slide, "Three changes, six weeks, p95 down 41%.", x=0.65, y=4.6, w=8.0)
```

Number-free variant: drop the ghost number, keep kicker + title + one lead line.

## Close (ask + QR)

```python
slide = new_slide()
solid_bg(slide, BG)
kicker(slide, "TRY IT TONIGHT", x=0.65, y=2.0, color=ACCENT)
title(slide, "One-command deploys.", x=0.65, y=2.4, w=7.0, size=44)
body(slide, "npx acme-deploy --preview", x=0.65, y=4.2, w=7.0, size=20, mono=True)
body(slide, "Slides plus demo: acme.dev/talks/q3 · ada@acme.dev", x=0.65, y=4.9, w=7.0, size=14, color=MUTED)
set_notes(slide, "Close on the ask: ship your next deploy in one command, tonight.")
```

QR variant: copy column narrows to `w=6.5`; QR goes right:

```python
rect_pic(slide, "qr", "assets/qr.png", x=10.3, y=2.5, w=2.4, h=2.4)    # real QR, never drawn
```

## Slide spec

```
Slide N — <Title>                      bg: <solid|photo>
  Text runs:  kicker {11pt ACCENT} ; title {44–54pt} ; body {≤3 lines 16pt}
  Z-order:    bg → <photos> → copy → logo
  Entrances:  none (framing slides land whole; motion lives in body sections)
  Anchors:    kicker slot reused from previous section
  Images:     assets/<NN>_<name>.jpg (avatar or QR only)
  Done when:  ask is headlined, chapters numbered, QR is a real raster.
```

## Don't

- Don't headline the close "Thank you" and don't ship a divider without a number — headline the ask, number the chapters.
