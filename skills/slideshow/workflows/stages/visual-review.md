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
3. Keep `references/verify-checklist.md` open — this walkthrough feeds Gates 5–16.

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

## 4. Contrast spot-check

Measure three pairs with the DevTools picker or WebAIM and record all three
numbers: `fg/bg`, `muted/bg`, `muted/surface`. Pass bars: normal text ≥4.5:1,
large text ≥3:1, code `fg/bg` ≥7:1, projector decks ≥7:1 for body. The classic
silent failure is muted-on-surface — `#64748B` on `#F1F5F9` reads fine and
measures 4.2:1. Promote without redesigning:

```css
.fix-muted { color: var(--fg); opacity: .82; }
```

Projector check: venue projectors wash out mid-tones, so hold body copy to
≥7:1 on any deck flagged for projection. Re-measure under the actual projector
when possible; otherwise the ≥7:1 bar plus the `.fix-muted` promotion above
is the ship standard.

## 5. Alignment

Check the 8pt scale (`8 / 16 / 24 / 32 / 48 / 64`), bento gap 16px with hero
padding 32px, split gap 32px. Two heavy-text halves on one slide is an outline
defect, not a CSS defect — split the slide. Confirm the responsive collapse:
bento to 1–2 columns and stat cards to one column at 390px, tap targets ≥44px.

## 6. Overflow

Code slides hold ≤12 lines at ≥14px (15px preferred) with horizontal scroll
intact where needed — a 28-line file dump at 11px gets split across two slides
or cut to the discussed lines with a repo link in notes. Bento cells hold one
line plus one metric; a cell needing two sentences becomes its own slide.
Preview the PDF pagination mentally: `v-click` steps in Slidev become extra
pages, which is expected, not a bug.

## 7. Motion

One morph moment per section max (`data-id`, `view-transition-name`, or GSAP
Flip — never two mechanisms on one pair). Fragments (`fragment` / `v-click` /
`_transition`) advance in narration order and all resolve visible. Emulate
`prefers-reduced-motion: reduce` in DevTools: every transition collapses to a
cut, every fragment is visible without clicks, parallax is static, nothing
flashes over 3Hz. A `v-motion` hero stuck at `opacity: 0` under emulation is a
blocking defect — add the static fallback from Gate 10.

## 8. Notes present

Notes-to-slides ratio 1:1 (appendix exempt only if marked `NO-NOTES`). Each note
holds three things: the one sentence to say, the transition line to the next
slide, and any stat provenance. `Say: p95 fell 41% in six weeks. Then: but July
was ugly — next slide. Timecheck: 2:00.` A title note saying "intro myself" with
no name, title, or timecheck fails.

## 9. Common visual defects — fix at the owning layer

Act at the shallowest layer that owns the fault (SKILL.md discipline 7):
slide → outline → style → tooling. Never silently downgrade a required artifact.

| Defect | Owning layer | Fix |
|---|---|---|
| Stretched logo or pillarboxed portrait | slide | set `aspect-ratio` + `object-fit: cover`, re-export at 16/9 |
| Two heavy-text halves side by side | outline | split into two slides; grids imply equality, not order |
| Muted-on-surface measures 4.2:1 | style | apply `.fix-muted`, re-measure the trio |
| Gradient headline or 4 competing gradients | style | keep the single hero wash, delete the rest (Gate 9) |
| 28-line code dump at 11px | slide → outline | cut to ≤12 discussed lines, link the repo in notes |
| Missing `alt` or `alt="image"` | slide | conclusion-bearing alt per Gate 4, `alt=""` if decorative |
| `v-motion` invisible under reduced motion | style/tooling | add the Gate 10 static fallback CSS + JS guard |
| 4-column bento unreadable at 390px | style | add the 520px single-column collapse from `layouts.md` |
| Third body font sneaking in via a component | style | cut back to 2 families + mono (Gate 7) |
| Iframe demo blocked by X-Frame-Options | slide | screenshot into `assets/demo-shot.png` + link, keep live URL in notes |
| QR code under 120px, unscannable past row 3 | slide | re-export at ≥180px in a 16px bordered box (`layouts.md` §9) |
| Stat cards mixing $, %, ms with no unit labels | slide | label every unit explicitly (Gate 2 honesty rule) |
| Divider between every slide, count doubled | outline | keep max 3 dividers; merge the rest into section headers |
| Teal body copy at 3.9:1 shipped as paragraphs | style | swap body to fg, reserve teal for accents ≥18pt |
| Appendix with no notes and no `NO-NOTES` mark | slide | write the 3-part note or mark `NO-NOTES` explicitly |
| Auto-Animate dead from mismatched `data-id` casing | slide | match `data-id` strings exactly across adjacent sections |

## 10. Worked defect log (Acme Q3, 12 slides)

```text
slide 2 — contrast — muted caption on surface 4.1:1 → style, .fix-muted
slide 4 — overflow — 14-line snippet at 13px → slide, cut to 9 lines + repo link
slide 5 — notes — NRR provenance missing → slide, add billing-export line
slide 7 — motion — two morph pairs in one section → style, keep bar growth only
slide 9 — alignment — bento 4-col crushed at 390px → style, 520px collapse
```

Five defects, three at slide layer, two at style. Fix in layer order (slide
first, style second), then re-walk per §11 — never fix mid-walk.

## 11. Re-walk rule

Re-walk only the fixed slides plus their immediate neighbors — morph pairs and
transitions cross slide boundaries. A style-layer token fix means re-walking the
whole deck; tokens have no neighbors. Log the re-walk as one line:
`Re-walk: slides 2, 4–5, 7, 9 green, neighbors clean.`

## 12. Sign-off checklist before export

- [ ] Contrast trio recorded, all pairs pass (Gate 5).
- [ ] Placeholder greps 1–3 return nothing; grep 4 only intentional demo URLs (Gate 6).
- [ ] Fonts ≤2 + mono, code max 12 lines, gradients ≤1 (Gates 7–9).
- [ ] Reduced motion emulated: cuts verified, fragments visible (Gate 10).
- [ ] Notes 1:1 with say/then/provenance (Gate 11).
- [ ] Keyboard-only walk passes, focus ring visible (Gate 12).
- [ ] 390px swipe passes, zero horizontal scroll (Gate 13).
- [ ] Code themes track dark/light toggle, no gray blocks (Gate 14).

## 13. Handoff

Paste one line: `Visual review done: 12/12 slides walked, 3 defects fixed at slide/style layers, sign-off 8/8 — export may proceed.` Keep the defect log in the delivery note for the exporter.
