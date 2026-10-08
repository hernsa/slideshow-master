# Refine Spec — Revision-Round Procedure

> Revisions are surgery, not rebuilding. Classify each note, re-run only the
> phases it touches, and re-verify only the gates it can break.

## 1. When this stage runs

- Full path: after the user answers the outline approval gate or reviews the built deck.
- Fast path: only when an upgrade trigger fires; otherwise fix-forward inside the sprint.
- Output of this stage is always a re-run list plus a re-verify gate subset — never silent edits.

## 2. Collect user feedback in one batch

Ask for all notes in a single message, numbered against slide titles ("slide 4,
p95 slide: …"). Verbal drive-bys mid-build do not count — if it is not written
against a slide title, it is not a revision yet. Confirm the batch is complete
before classifying.

```markdown
Refine batch v4 (Acme Q3, from Jonas, 2026-10-07):
1. slide 5, NRR slide: caption should cite the billing export, not the dashboard.
2. deck-wide, style: muted stat labels wash out on the projector.
3. slide 3, lab photo: swap for the staging screenshot (Maria's capture).
Batch complete: yes — no further notes this round.
```

## 3. Classify — per-slide vs deck-wide

The test: a note touching more than two slides, or any token, font, palette, or
engine, is deck-wide. Everything else is per-slide. "Make slide 6 punchier" is
not a classification — send it back for one concrete change (new number, new
visual, or cut).

## 4. Deck-wide notes go to their owning layer

Route deck-wide changes to the shallowest layer that owns the fault: slide →
outline → style → tooling (SKILL.md discipline 7). A beveled-card request is
style; a "the story sags in the middle" request is outline; a "PDF renders blank"
request is tooling. Mislayered fixes return as second-round revisions — the
classic mislayer is treating washed-out projector text as a slide problem and
rewording captions for a week when one `.fix-muted` in the style layer ends it.
When two rounds fail at one layer, re-layer the note before running a third.

## 5. Re-run table — only affected phases

| Change | Re-run | Re-verify gates |
|---|---|---|
| Copy tweak on 1–2 slides | build the slides | placeholders (6), notes (11) |
| New slide inserted | outline delta + build | outline (1), notes (11), export (15) |
| Slides reordered | build + motion pass | keyboard (12), notes transitions (11) |
| Palette or font swap | style lock + build | contrast (5), fonts (7), gradients (9) |
| Layout pattern swap | build that slide | alignment via visual-review §5, mobile (13) |
| Image swap | `stages/image-review.md` §§4–6 | images (3), alt (4), console (16) |
| Stat correction | `stages/topic-research.md` §§3–5 | two-source (2), notes provenance (11) |
| Engine swap | full rebuild in the new engine | full `verify-checklist.md` — no subset |
| Motion-only change | motion pass on affected slides | reduced motion (10), keyboard (12) |
| Notes-only change | notes layer of affected slides | notes (11) |
| Appendix change | build the appendix slides | notes (11) if spoken, export (15) for page count |
| Contact strip / QR change | build the closing slide | placeholders (6), mobile (13) |
| Code snippet fix | re-run snippet + build the slide | two-source (2) if numbers, code (8/14) |

Structural changes (new, removed, or reordered slides) need a fresh outline nod:
version it (`Outline v4 — APPROVED 2026-10-07, Jonas`) and keep every version in
the delivery note. Engine swaps are rebuilds wearing a revision costume — say so.

## 6. Worked example — full path (Acme Q3 talk)

Jonas sends three notes: (a) slide 5 NRR caption should cite the billing export,
(b) the muted stat labels look washed on the projector, (c) swap the lab photo
for the staging screenshot. Classification: (a) per-slide copy → rebuild slide 5,
re-verify Gates 2 + 11; (b) deck-wide style → `.fix-muted` + re-measure the trio,
re-verify Gate 5; (c) image swap → full image-review §§4–6 on `shield-demo.png`,
re-verify Gates 3 + 4 + 16. Three notes, three lanes, no full rebuild.

## 7. Worked example — fast path (lightning talk, Marp)

Ada's 6-slide showcase draws one note: "add the shield hit-rate number to slide 5."
Classification: per-slide stat addition → re-source via topic-research §§3–5
(Maria's staging log plus the edge export), rebuild slide 5, re-verify Gates 2
+ 11. No upgrade trigger fires, so the note stays inside the fast path.

## 8. Subset procedure and rules

Run the re-verify subset in gate order and record each gate green with its
evidence (`contrast trio 15.8/6.1/4.9`, `placeholder greps 0 hits`). A subset
gate that turns red pulls its full stage back in — a red Gate 5 re-opens the
style lock, not just the one slide.

- Never silently downgrade a required artifact to close a revision (notes, credits, fallbacks).
- Never float `latest` or switch engines to dodge a style problem.
- Version every outline (`v1, v2, v3…` with date + approver) and keep all versions in the delivery note — the v3→v4 diff is the revision's scope proof.
- A note that adds a mode (investors appear, the lab becomes a pitch) is not a revision: re-route through `workflows/routing.md` and rebuild.
- Timebox a round to one working session; later notes open a new round, never reopen a closed one.
- Close the round with a handoff line: `Refine v4 done: 3 notes in 3 lanes, gates 2/5/3/4/11/16 green — export may proceed.`
