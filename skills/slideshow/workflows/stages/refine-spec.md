# Stage: refine-spec — revision rounds without rebuild churn

> Runs when feedback arrives after a nod. Classify first, re-run only
> affected phases. Never edit the .pptx by hand.

## Procedure

1. Classify each note: copy (phase 4/5 wording), visual (phase 5 spec
   block + phase 8 geometry), motion (phase 9), asset (phase 7).
2. Copy notes: edit `research-notes.md` + the spec block, rebuild,
   re-verify notes gate only.
3. Visual notes: edit the spec block first, then `build.py`. A visual
   note with no spec change is a guess — write the spec.
4. Motion notes: edit `motion.py` (add the slide to FADE_SLIDES or
   adjust entrances), rebuild clean first (COM doubles effects), run
   once, re-read renders.
5. A note that adds a section (new pillar, new audience) is not a
   revision — re-run phases 4–5 for the new slides, then build.

## Handoff

`Refine done: N notes classified (C copy / V visual / M motion),
affected gates re-passed — ship may proceed.`
