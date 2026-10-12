# Visual Review — Self-Review Pass on the Built Deck

> Review the built deck, not the plan. Open the actual slides in a browser,
> walk every slide in order, and write down each defect with its owning layer
> before fixing anything. Review first, repair second.

## 1. When this stage runs

- Full path: `generate-deck.md` step 10, on the finished build, before any export.
- Fast path: sprint 0:08–0:12 lite subset — images, contrast eyeball, placeholders.
- Re-entry: `stages/refine-spec.md` routes visual feedback here after the owning fix lands.

## 2. Setup

1. Serve or build per engine: reveal.js via `npx serve .` (open `http://localhost:3000/`); Slidev via `npx slidev slides.md` (open `localhost:3030`); Marp HTML via `npx marp slides.md -o deck.html --allow-local-files` and open the file.
2. Open Chromium and Firefox side by side with DevTools ready (contrast picker, Rendering → emulate `prefers-reduced-motion`, device toolbar at 390×844).
3. Keep `references/verify-checklist.md` open — this walkthrough feeds Gates 4–12.

## 3. Walkthrough procedure — per slide, in order

For each slide, top to bottom, run these five checks and log failures as
`slide N — check — symptom` before moving on:

1. Contrast spot-check: read the three pairs (§4) with the DevTools picker — never eyeball the close calls.
2. Alignment: grid gaps even, text column left edges share one line, images bordered with 16px radius, nothing touching the viewport edge.
3. Overflow: no horizontal scroll at desktop or 390px, code within its box, footer/QR clear of content.
4. Motion: fragments advance in narration order, the one morph moment morphs, everything else is static.
5. Notes present: the slide's say-line, transition line, and stat provenance exist in `<aside class="notes">`, Slidev `<!-- -->`, or the Marp presenter comment.

Log format — one line per defect, layer assigned at log time:

```text
slide 4 — overflow — 14-line snippet at 13px → layer: slide
slide 7 — motion — two morph pairs in one section → layer: style
```

## 4. Contrast — Gate 4, plus the projector delta

Measure the trio per Gate 4. Delta: venue projectors wash out mid-tones — hold body copy to ≥7:1 on projection-flagged decks; re-measure under the actual projector when possible.

## 5. Alignment — deltas only (no dedicated gate)

8pt scale (`8 / 16 / 24 / 32 / 48 / 64`), bento gap 16px with hero padding 32px, split gap 32px. Two heavy-text halves on one slide is an outline defect, not a CSS defect — split the slide. Responsive collapse feeds Gate 10: bento to 1–2 columns, stat cards to one column at 390px, tap targets ≥44px.

## 6. Overflow — Gates 7 + 10 deltas

Code ≤12 lines at ≥14px per Gate 7; bento cells hold one line plus one metric — a cell needing two sentences becomes its own slide. Delta: Slidev `v-click` steps become extra PDF pages, which is expected, not a bug.

## 7. Motion — Gate 8 only

One morph moment per section max; fragments advance in narration order and all resolve visible. Emulate `prefers-reduced-motion: reduce`: cuts, visible fragments, static parallax, nothing over 3Hz. A `v-motion` hero stuck at `opacity: 0` under emulation is a blocking defect — Gate 8 fix.

## 8. Notes — Gate 9 only

Ratio 1:1 with say/then/provenance. A title note saying "intro myself" with no name, title, or timecheck fails.

## 9. Common visual defects — single source is the failure-recovery catalog

Defect table + worked log moved to `workflows/governance/failure-recovery.md` (visual entries). Log defects here as `slide N — check — symptom → layer`, then look the fix up there.

## 10. Re-walk rule

Re-walk only the fixed slides plus their immediate neighbors — morph pairs and
transitions cross slide boundaries. A style-layer token fix means re-walking the
whole deck; tokens have no neighbors. Log the re-walk as one line:
`Re-walk: slides 2, 4–5, 7, 9 green, neighbors clean.`

## 11. Sign-off checklist before export

- [ ] Contrast trio recorded, all pairs pass (Gate 4).
- [ ] Placeholder greps 1–3 return nothing; grep 4 only intentional demo URLs (Gate 5).
- [ ] Fonts ≤2 + mono, gradients ≤1 (Gate 6); code max 12 lines, Shiki dual-theme (Gate 7).
- [ ] Fragment budget + reduced-motion cuts + keyboard walk pass (Gate 8).
- [ ] Notes 1:1 with say/then/provenance (Gate 9).
- [ ] 390px swipe passes, zero horizontal scroll (Gate 10).

## 12. Handoff

Paste one line: `Visual review done: 12/12 slides walked, 3 defects fixed at slide/style layers, sign-off 6/6 — export may proceed.` Keep the defect log in the delivery note for the exporter.
