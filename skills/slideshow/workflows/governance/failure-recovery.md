# Failure Recovery — Failure Catalog

> Fix at the shallowest layer that owns the fault: slide → outline → style →
> tooling (SKILL.md discipline 7). Never silently downgrade a required artifact.
> Every recovery below ends at a named re-verify gate — recovery without
> re-verification is just a second failure with confidence.

## Owning layers

- slide: one file, one image, one snippet — fix and re-run the slide's gates.
- outline: structure, order, count — fix, get a fresh outline nod, rebuild affected slides.
- style: tokens, fonts, palettes, motion — fix, re-measure, rebuild affected slides.
- tooling: installs, versions, export binaries — fix the environment, re-export everything.

How to tell: change one file and the symptom moves → slide. Change one file
and nothing moves → the layer is deeper. Change a token and five slides shift →
style. Reinstall and the export works → tooling. Cut two slides and the talk
lands → outline was the fault all along.

## Triage before the catalog

1. Reproduce from the final commit: re-run the exact failing command or re-open the exact slide — never diagnose from memory of the failure.
2. Isolate to one layer: one broken image is slide; every image broken is tooling; washed text everywhere is style; a sagging middle is outline.
3. Check the delivery note for the routing slip, outline version, and last green gate — recovery starts from the last known good state.
4. Pick the catalog entry below by symptom, not by guess; apply its fix, then its re-verify gates.
5. Timebox to 20 minutes per failure; at the cap, escalate one layer up instead of repeating step 4.

Log every recovery in the delivery note:

```text
Failure: contrast trio 4.2:1 on muted/surface (visual-review §4)
Layer: style — fix: .fix-muted, re-measured 15.8/6.1/4.9
Re-verify: Gate 4 green, 390px re-walk clean — resume export-verify.
```

If no entry matches, treat it as a style-layer defect first (most visual
surprises live there), then outline, then tooling — and write the new entry
into this catalog when it resolves.

## 1. Empty asset dir

Symptom: `scripts/verify-images.py` reports `missing file` for every image; the served deck shows broken-image icons. Owning layer: slide. Fix in `stages/image-review.md` §§4–6 (local paths, per-file license records, CREDITS entries), then re-run the verify script to exit 0. Re-verify: Gate 3 (images & media) and Gate 12 (no 404s).

## 2. Broken CDN pin

Symptom: fonts swap to fallback serif on venue Wi-Fi; console shows `Reveal is not defined` or a failed stylesheet fetch. Owning layer: tooling. Fix per `references/engines.md` pins (never float `latest`), vendor the runtime locally, confirm a system fallback stack with Wi-Fi off. Re-verify: Gates 6 (style tokens), 7 (code slides render), and 12 (zero console errors).

## 3. Contrast failure

Symptom: the trio reads `fg/bg 15.8:1, muted/bg 6.1:1, muted/surface 4.2:1` — the third pair fails; body copy in teal measures 3.9:1; the projector wash makes it worse. Owning layer: style. Promote the failing muted without redesigning (`.fix-muted`), re-measure all three pairs (fixing one often shifts another), hold projector body to ≥7:1 with never gradient body text (Gate 6 bans it), re-check code blocks at ≥7:1 with Shiki themes tracking the toggle. Re-verify: Gate 4 (trio recorded, all pass) plus a 390px re-walk for the changed slides.

## 4. Placeholder leak

Symptom: a grepped marker or an `src="http…"` hotlink survives into the built deck. Owning layer: slide. Run the four Gate 5 greps from the deck root, replace every hit with real content or delete the slide, vendor hotlinked `src` into `assets/` with license records, re-run greps to zero. Re-verify: Gate 5 (placeholder scan) and Gate 12 (no 404s from the replaced sources).

## 5. Export tool missing

Symptom: Slidev PDF export hangs at Chromium; `slidev: command not found`; decktape writes a correct page count of white pages; Marp reports no Chrome. Owning layer: tooling. Most-hit fixes: missing Chromium (Slidev and Marp PDF/PPTX both drive headless Chrome) → `npx playwright install chromium`, re-run with `--timeout 60000` if it still stalls; blank decktape PDF → open `http://localhost:8000/?print-pdf` in a browser first, then `npx decktape reveal --load-pause 2000` against it; Marp images missing → re-run raw with `--allow-local-files` (`stages/export-verify.md` §3 + `references/engines.md` raw flags). Re-verify: Gate 11 (page count, no clipping, PPTX spot-check) and Gate 12 (clean console).

## 6. Oversized images

Symptom: a `lab-4MB.png` sits in `assets/`; transitions hitch; the PDF balloons. Owning layer: slide. Re-export each offender at max 1920px wide (parallax 3000px allowed, still ≤400KB) until it fits, update `assets/CREDITS.md` sizes, re-run the verify script and reload for blur/shift. Re-verify: Gate 3 (sizes in budget, alt intact) and Gate 10 (mobile still clean).

## Visual defect catalog (moved from `stages/visual-review.md` — single source)

Act at the shallowest layer that owns the fault (SKILL.md discipline 7):
slide → outline → style → tooling. Never silently downgrade a required artifact.

| Defect | Owning layer | Fix |
|---|---|---|
| Stretched logo or pillarboxed portrait | slide | set `aspect-ratio` + `object-fit: cover`, re-export at 16/9 |
| Two heavy-text halves side by side | outline | split into two slides; grids imply equality, not order |
| Muted-on-surface measures 4.2:1 | style | apply `.fix-muted`, re-measure the trio (Gate 4) |
| Gradient headline or 4 competing gradients | style | keep the single hero wash, delete the rest (Gate 6) |
| 28-line code dump at 11px | slide → outline | cut to ≤12 discussed lines, link the repo in notes (Gate 7) |
| Missing `alt` or `alt="image"` | slide | conclusion-bearing alt per Gate 3, `alt=""` if decorative |
| `v-motion` invisible under reduced motion | style/tooling | Gate 8 static fallback CSS + JS guard |
| 4-column bento unreadable at 390px | style | 520px single-column collapse from `layouts.md` (Gate 10) |
| Third body font sneaking in via a component | style | cut back to 2 families + mono (Gate 6) |
| Iframe demo blocked by X-Frame-Options | slide | screenshot into `assets/demo-shot.png` + link, keep live URL in notes |
| QR code under 120px, unscannable past row 3 | slide | re-export at ≥180px in a 16px bordered box (`layouts.md` §9) |
| Stat cards mixing $, %, ms with no unit labels | slide | label every unit explicitly (Gate 2 honesty rule) |
| Divider between every slide, count doubled | outline | keep max 3 dividers; merge the rest into section headers |
| Teal body copy at 3.9:1 shipped as paragraphs | style | swap body to fg, reserve teal for accents ≥18pt (Gate 4) |
| Appendix with no notes and no `NO-NOTES` mark | slide | write the 3-part note or mark `NO-NOTES` explicitly (Gate 9) |
| Auto-Animate dead from mismatched `data-id` casing | slide | match `data-id` strings exactly across adjacent sections (Gate 15) |

Worked defect log (Acme Q3, 12 slides):

```text
slide 2 — contrast — muted caption on surface 4.1:1 → style, .fix-muted
slide 4 — overflow — 14-line snippet at 13px → slide, cut to 9 lines + repo link
slide 5 — notes — NRR provenance missing → slide, add billing-export line
slide 7 — motion — two morph pairs in one section → style, keep bar growth only
slide 9 — alignment — bento 4-col crushed at 390px → style, 520px collapse
```

Five defects, three at slide layer, two at style. Fix in layer order (slide
first, style second), then re-walk neighbors — never fix mid-walk.

## Escalation

Three failed recoveries on one failure means the layer is wrong: escalate one
layer up (slide → outline → style → tooling) and state the new hypothesis in the
delivery note. A red lite gate on the fast path that survives one recovery is an
upgrade trigger — switch to `workflows/generate-deck.md`, do not sprint around it.

Worked escalation: the muted trio fails twice after `.fix-muted` (style, 20 min
each). The third attempt escalates to outline — the deck carries muted statistics
on six consecutive slides, so the fault is density, not color. Two stat slides
merge into one bento, muted labels drop to captions only, trio re-measures
`15.8/6.1/5.2` green. The layer was wrong; the catalog steps were right.

## After every recovery

- [ ] Named re-verify gates recorded green with evidence in the delivery note.
- [ ] `assets/CREDITS.md` and license records match the files on disk.
- [ ] Outline version bumped when structure changed, with a fresh approval nod.

Handoff line: `Recovery done: <failure> fixed at <layer>, gates <n> green — resume <stage>.`
