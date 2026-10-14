# Photo collage — darkened plate + circular tiles + rotating disc

> From 23.4/28.3. The photographic narrative section: full-bleed darkened plate, 4 circular tiles stacked on the right, one diamond disc that rotates between slides, copy column pinned left and NEVER moving. 5–6 rasters per slide.

```python
slide = new_slide()
plate(slide, "assets/03_hanoi_1890.jpg", 0.70)                    # bg plate, darkened+blurred in PIL
circle_pic(slide, "tile-1", "assets/04_tile_gate.jpg",  cx=10.9, cy=1.9, d=1.9)
circle_pic(slide, "tile-2", "assets/05_tile_street.jpg", cx=11.5, cy=3.4, d=1.9)
circle_pic(slide, "tile-3", "assets/06_tile_river.jpg",  cx=10.9, cy=4.9, d=1.9)
circle_pic(slide, "tile-4", "assets/07_tile_market.jpg", cx=11.5, cy=6.2, d=1.6)
diamond_pic(slide, "disc", "assets/08_disc.jpg", cx=8.6, cy=4.0, d=3.2, rot=-89)  # rotation BAKED in PIL
kicker(slide, "HANOI · 1890", x=0.65, y=2.2, color=JADE, name="kicker")
title(slide, "The old gate at dawn.", x=0.65, y=2.6, w=4.9, size=40, name="sec-title")
body(slide, "Three mornings of archive scans; the fog always lifts by seven.",
     x=0.65, y=3.9, w=4.7)
```

Per-slide ramp (one value moves per step): slide 1 plate `.70` / disc `rot=0`; slide 2 plate `.85` / disc `rot=-89`; slide 3 plate `.70` / disc `rot=-178`; slide 4 plate `.85` / disc `rot=-267`.

## Slide spec

```
Slide N — <Title>                      bg: dark-photo
  Text runs:  kicker {11pt} ; title {40pt} ; body {≤3 lines 16pt}
  Z-order:    plate → tile-1..4 → disc → copy
  Entrances:  none (disc glide + plate ramp carry the motion)
  Anchors:    sec-title pinned ; disc rotates one step
  Images:     plate + 4 tiles + disc = 6 rasters
  Done when:  6 rasters present; copy column pixel-identical to previous slide; disc rotated one step.
```

## Don't

- Don't put body text over the plate without a scrim, don't rotate tiles, don't add a card behind the copy column.
