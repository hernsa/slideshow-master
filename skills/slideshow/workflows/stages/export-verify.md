# Stage: export-verify — renders + handout checks before shipping

> Runs inside `generate-pptx.md` phase 11. Output is the shippable set:
> `.pptx` + `renders/` (+ handout PDF on request). Authority: Gates 11, 12.

## Procedure

1. Renders exist for every slide at 1920×1080, exported in the same
   COM session as the motion pass, timestamps newer than the .pptx.
   Zero-byte PNGs fail the gate.
2. Handout PDF on request: `ExportAsFixedFormat` with
   `ppFixedFormatTypePDF=2` in that same COM session. Page count equals
   slide count.
3. COM hygiene: no `POWERPNT.EXE` remains, `DisplayAlerts` was 0, the
   .pptx saved after the motion pass (`pres.Save()` before `Close()`).
4. Ship record filled (checklist top block): outline nod, research +
   plan state, build size, motion map, verify lines, continuity
   anchors, deliverables list.

## Handoff

`Export done: N renders + handout (if requested), COM clean, ship
record filled — deck ships.`
