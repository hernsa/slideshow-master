# Stage: visual-review — render-by-eye walkthrough

> Runs inside `generate-pptx.md` phase 10, after `verify-pptx.py`
> passes. Output is a fix list executed in `build.py` (never in the
> .pptx). Authority: Gates 4, 10, 15.9.

## Procedure

1. Open every `renders/sN.png` at full size, in order. Check: copy
   matches the visual-plan spec block, anchors sit where named, no
   collisions (rings vs kickers, pills vs body, discs vs edges).
2. Scale each render to 960px wide. Body copy must still read —
   otherwise cut words or darken the plate, never shrink type.
3. Check the `Done when:` line of every spec block literally against
   the render. A line that isn't true is a fix item.
4. Read every visible string aloud (titles, kickers, pills, labels,
   captions): flag broken grammar, unclear referents, and fake-precise
   numbers with no source. Rewrite or cut on the spot.
5. Fix in `build.py`, rebuild clean, re-run motion once, re-read the
   affected renders. Never diagnose from XML dumps.

## Handoff

`Visual done: N/N renders read, M fixes applied + re-read — ship may
proceed.`
