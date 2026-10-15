# Pastel collage — blobs behind rotated plates, copy on white

> From Chikiwaa. The warm community section: pastel ground, freeform blob + arch outline behind plain `rect` photos rotated ±3–6° (rotation BAKED in PIL), copy on a white rounded card — contrast by surface, never by scrim.

```python
slide = new_slide()
solid_bg(slide, "#BBE6F7")                                        # pastel ramp stop, never repeats twice running
deco_blob(slide, "cloud-a", cx=3.0, cy=3.4, w=6.2, h=4.4, color="#FFEFC8")
deco_ring(slide, "arch", cx=11.0, cy=2.2, d=3.6, color="#E2EFFB")  # outline arch, behind plate
rect_pic(slide, "plate", "assets/09_kids_reading.jpg", x=2.7, y=1.2, w=5.8, h=4.4, rot=-4)
round_rect(slide, "card", x=8.6, y=2.3, w=4.0, h=2.9, fill="#FFFFFF")
pill(slide, "STEP 3", x=8.9, y=2.55, w=1.1, fill="#BBFFC8", color="#1F2328")
title(slide, "Every child gets a shelf.", x=8.9, y=2.95, w=3.4, size=28, color="#1F2328")
body(slide, "Self-built wooden shelves, donated books, 12,000đ each.",
     x=8.9, y=4.1, w=3.4, size=14, color="#1F2328")
```

Ramp walk per slide: `#BBE6F7 → #FFEFC8 → #FFE8F4 → #E2EFFB → #FFFDE4 → #BBFFC8`, one saturated break (`#4EA72E`) per section max. Alternate plate tilt `-4 / +3 / -5` and card side left/right.

## Slide spec

```
Slide N — <Title>                      bg: pastel-<stop>
  Text runs:  pill {11pt} ; title {28pt} ; body {≤3 lines 14pt} on white card
  Z-order:    ground → cloud-a → arch → plate → card → pill → copy
  Entrances:  none (blob drift + tilt change carry the motion)
  Anchors:    card pinned or mirrored ; cloud-a drifts one step
  Images:     plate (+ optional second small plate) = 1–2 rasters
  Done when:  pastel ≠ previous slide; white card holds all type; plate tilt ±3–6°.
```

## Don't

- Don't mask the photo into blobs, don't scrim pastels, don't rotate the text card — only plates and decor move. No audio: Chikiwaa's MP3s are a Canva export artifact.
