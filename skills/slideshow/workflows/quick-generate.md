# Quick Generate — 15-Minute Fast Path

> Marp-first, fixed style, minimal gates. Use when the router sends you here:
> lightning talk, internal sync, fix-forward, ≤15 min. Not for client-facing work.

## Fixed choices (no decisions, no questions)

- Engine: Marp CLI 4 (`npx marp slides.md -o deck.html --allow-local-files`).
- Style: bento-minimal — Paper Editorial light for text decks, Midnight SaaS
  dark for stage decks; Inter body + one display font; single accent bar.
- Source: `examples/marp-demo/` copied verbatim, then 6–8 slides swapped in.
- Images: screenshots and one hero photo only, all local in `assets/`.
- Motion: `transition: fade 0.4s` deck-wide, max two `_transition` overrides.

## 5-step sprint (time-boxed)

### 0:00–0:02 — Intake lite (2 answers, then go)
Topic + thesis in one sentence, slide count (default 6, showcase shape).
Skip audience, brand, and image-sourcing questions — defaults apply:
mixed audience, ~1.5 min/slide, hybrid images + verify, HTML + PDF.
Example thesis: "A talk is a runtime, not a file — so ship the runtime."

### 0:02–0:04 — Design Read lite (one line, fixed dials)
Emit: `Reading this as: a lightning talk for a mixed-tech room, with a
minimal language, leaning toward Marp + Midnight SaaS + Inter/JetBrains Mono.`
Dials locked: `DESIGN_VARIANCE 5`, `MOTION_INTENSITY 2`, `VISUAL_DENSITY 3`.
Layouts: title, bento, stat row, quote, code (≤10 lines), divider — from
`references/layouts.md`. No custom tokens beyond the accent swap.

### 0:04–0:08 — Outline + build (mode-compressed)
Write 6 one-liners using the showcase shape (fastest to author):
1. "Why HTML Beats PPTX for Tech Talks" (title + thesis).
2. "Last Month, My PPTX Died on Stage Wi-Fi" (problem photo).
3. "Tonight: One URL, Zero Installs" (QR + URL bento).
4. "12 Lines: Shiki, Fragments, Notes" (code ≤10 lines).
5. "Export Drill: 11 Seconds vs 4 Minutes" (2-bar stat row).
6. "Ship the Runtime: URL, PDF, Source" (contact strip + QRs).
Write straight into `slides.md` frontmatter (`marp: true, paginate: true,
transition: fade 0.4s`) — no outline approval wait; the deck is disposable.
For 7–8 slide variants, insert "Hallway Re-Export, Knee on the Floor"
(tension photo) after slide 2 and "Paper Editorial: The Board-Forward Deck"
(handout spread) before the closer — both from the demo universe.

### 0:08–0:12 — Images + verify lite
Copy hero + screenshots to `assets/`, one line each in `assets/CREDITS.md`.
Run: `scripts/verify-images.py` (must pass), contrast eyeball (≥4.5:1),
placeholder scan (no TODO text, no filler Latin, no empty-src, no hotlinks).
Add `--bespoke.transition` only if transitions are required for the live view.
Keep `object-fit: cover`, radius 16–24px, one full-bleed max per section per
`references/layouts.md` §7 — even in a hurry, stretched logos still fail review.

### 0:12–0:15 — Export + ship
`npx marp slides.md -o deck.html --allow-local-files` then
`npx marp slides.md -o deck.pdf --allow-local-files`. Open both, confirm
pagination, ship the single HTML + PDF + `slides.md` source. Log the routing
slip in one line: `quick: showcase-6 + Marp 4 + bento-minimal`.
If Chromium is missing, install once via `npx playwright install chromium`
(see `references/engines.md` § Marp troubleshooting) and re-run — never ship
an unchecked PDF to save two minutes.

## Skipped gates (listed explicitly — re-add for full quality)

1. 2-source research rule (`SKILL.md` Phase 3) — stats marked `[unverified]` in notes.
2. Outline approval nod (`generate-deck.md` step 5) — build directly from the 6-liner.
3. Full `references/verify-checklist.md` — lite subset only (images, contrast eyeball, placeholders).
4. Reduced-motion emulation in DevTools — `fade 0.4s` + static PDF assumed safe; verify later for stage reuse.
5. Speaker notes on every slide — notes on slides 2, 4, 5 only.
6. Engine decision log — one-line slip instead of the full log block.
7. PPTX export test — Marp PPTX assumed (`-o deck.pptx`); verify only if requested.

## Upgrade triggers (stop and switch to `workflows/generate-deck.md`)

- Audience adds investors, execs, or external clients mid-request.
- Live code runner or iframe becomes essential (Marp cannot do either live).
- Deck grows past 8 slides or needs a second accent color.
- Any skipped gate turns red (missing image, unreadable contrast, broken export).

## Don'ts for the fast path

- Don't add reveal.js or Slidev mid-sprint — Marp-only for 15 minutes.
- Don't hunt stock photos — screenshots + one hero, then build.
- Don't tune motion beyond fade — transitions are the first thing cut for speed.
- Don't shrink code font to fit — cut lines to ≤10 instead.
- Don't ship without opening both HTML and PDF once, even in a hurry.
