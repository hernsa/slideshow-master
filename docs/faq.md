# FAQ

## 1. Why .pptx instead of HTML?

The file that presents is the file the builder verified: editable
text, embedded photos, real Morph, speaker notes. No export step
between the authoring surface and the stage, so nothing silently drops
(styles, backgrounds, SVGs) on the way out.

## 2. Where does motion come from?

PowerPoint COM (`motion.py` / `scripts/render.py`): Morph-byObject as
the deck default, fade exceptions, ≤3 fade entrances per slide, manual
advance. python-pptx owns geometry, content, and notes; COM owns motion
and renders. Scripts are the truth — never hand-edit the .pptx.

## 3. What if I have no desktop PowerPoint?

Motion is blocked: say so, ship the static .pptx with a motion plan
(Fade/Morph map + entrance lines) the user can apply in two minutes.
Never fake transitions by hand-writing XML.

## 4. Why did my Morph not carry a shape?

The `name=` values drifted between slides, or the parked shape got
"fixed" back on-canvas. Names match exactly or Morph sees two different
shapes. Off-canvas parking (`x=14.5`) is intentional.

## 5. Why is there a white wedge on my rotated photo?

`shape.rotation` on custom-geometry pictures renders a white wedge.
Bake the tilt into pixels (`diamond_pic(..., content_rot=N)`) and keep
shape rotation at 0.

## 6. How many photos per slide?

At least one raster per slide; narrative sections run 3–6. A deck with
zero rasters fails Gate 3. `verify-pptx.py` prints the `Rasters:` line;
`verify-images.py` checks every `build.py` ref resolves and CREDITS.md
covers it.

## 7. `Call was rejected by callee`?

A zombie POWERPNT.EXE holds the file. Taskkill it, rebuild clean
(COM doubles effects on re-run), run motion once.

## 8. Do I still write speaker notes?

Yes — 1:1, every slide. Notes are the talk; `verify-pptx.py` fails
empty ones. Appendix slides may carry `NO-NOTES`.
