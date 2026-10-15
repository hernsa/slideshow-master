# Annotation stage — black stage, baked glow, leader callouts

> From the AirPods deck. The showcase section: pure `#000` stage, spotlight BAKED into the product raster (left 40% pure black, alpha falling off — never a live gradient or shadow), 72–96pt hero, leader line + 0.16in dot callouts, size/comparison row. Max one section per deck.

```python
slide = new_slide()
solid_bg(slide, "#000000")
rect_pic(slide, "product", "assets/10_product_glow.png", x=4.4, y=0.6, w=4.5, h=6.3)
title(slide, "Sound without edges.", x=1.6, y=1.3, w=10.1, size=72, color="#F5F5F7",
      accent="edges.", accent_color="#02FF40", align="center", name="hero")
leader(slide, "leader-anc", x1=1.6, y1=4.2, x2=4.3, y2=4.2, label="Adaptive ANC · 2× quieter")
pill(slide, "XS", x=4.3, y=6.3, w=0.9, fill="#000000", color="#02FF40", outline="#02FF40")
pill(slide, "S",  x=5.5, y=6.3, w=0.9, fill="#000000", color="#02FF40", outline="#02FF40")
pill(slide, "M",  x=6.7, y=6.3, w=0.9, fill="#000000", color="#02FF40", outline="#02FF40")
pill(slide, "L",  x=7.9, y=6.3, w=0.9, fill="#000000", color="#02FF40", outline="#02FF40")
```

Product moves between slides (center → left → right) under the pinned hero; spec artboards wait parked at `x=14.5` and fly in via Morph. No baked raster? Substitute concentric `deco_ring` glows — never a card, never `#0A0A0A` ("near-black" kills the stage; depth comes from the raster).

## Slide spec

```
Slide N — <Title>                      bg: pure-black
  Text runs:  hero {72–96pt, one accent word} ; leader {18pt} ; size row {24pt}
  Z-order:    product → hero → leader → size-row
  Entrances:  hero .10s, product .22s, leader .34s (3 max)
  Anchors:    hero pinned ; product glides center→side
  Images:     product raster with baked glow (1 raster minimum)
  Done when:  bg is #000000; exactly one accent; no cards, no borders, no shadows.
```

## Don't

- Don't add cards, borders, radius, or drop-shadows on this stage — the raster carries all depth.
