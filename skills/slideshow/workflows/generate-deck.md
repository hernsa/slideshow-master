# Generate Deck — Full Default Procedure

> The quality-bar path. Follow top to bottom; no step is skippable.
> Router input: mode + engine + style slip from `workflows/routing.md`.

## 1. Intake (SKILL.md Phase 1)

Ask all 7 questions in one message with defaults: topic + thesis, audience,
length (~1.5 min/slide, ≤20 slides), code-heavy?, brand constraints,
export target, images. If user says "defaults": mixed-tech audience,
12 slides (or the mode's count — tech-talk 10, pitch 8, tutorial 8,
showcase 6, narrative 8), Midnight SaaS dark, hybrid images + verify,
HTML + PDF. Record answers; a missing thesis means you propose one and
confirm before proceeding.

## 2. Design Read (SKILL.md Phase 2, mandatory one-liner)

Output exactly: `Reading this as: <deck kind> for <audience>, with a <vibe>
language, leaning toward <engine + palette + font pair>.` Then set the three
dials (`DESIGN_VARIANCE` / `MOTION_INTENSITY` / `VISUAL_DENSITY` 1–10) using
the per-mode defaults in `references/modes/_index.md`. Example: "Reading this
as: a conference talk for backend engineers, with a dark-tech language,
leaning toward Slidev 52 + Midnight SaaS + Space Grotesk/Inter/JetBrains Mono."

## 3. Style lock

Pick ONE palette from `references/colors.md`, declare dark/light tokens
explicitly (never auto-invert), max 2 font families + mono for code.
Pick per-slide layouts from `references/layouts.md` (title, bento, 50/50 or
40/60 split, stat row ≤4 cards, quote, code+preview ≤12 lines, divider).
Pick motion from `references/animations.md`: REQUIRED 1–3 morph pairs per deck on element continuations (`data-auto-animate`+`data-id` / `view-transition-name` / `v-motion` pair / Flip), never on body copy, never across sections; deck-wide single transition alone FAILs review (one morph moment per section max still applies).
fragments for stepwise reveals, `prefers-reduced-motion` fallback planned now.

## 4. Research (SKILL.md Phase 3, 2-source rule)

Every factual claim needs 2+ independent sources; every API, CLI flag, and
version number verified against current docs (pin reveal.js 6, Slidev 52,
Marp CLI 4 per `references/engines.md`). Log sources per slide as HTML
comments or presenter notes. Single-source claims marked `[unverified]` and
never stated as fact on the slide.

## 5. Outline (mode file, approval gate)

Open the routed mode file under `references/modes/` and write one line per
slide: title + point + visual + MANDATORY `bg:` tag on every line (per `references/color-usage.md` §1; longest identical-`bg` run ≤2 or ship-blocker; stock `theme: default` with no applied style does not satisfy rotation). Counts: tech-talk 10, pitch 8, tutorial 8,
showcase 6, narrative 8. Demo-universe titles where fitting ("Last Month, My
PPTX Died on Stage Wi-Fi", "Tonight: One URL, Zero Installs"). Paste the
outline for a nod before writing slides — cheap to change now, expensive later.

## 6. Scaffold

Run `scripts/new-deck-scaffold.sh <engine> <deck-dir>` (engines and flags in
`references/engines.md`). Start from `examples/reveal-demo/`,
`examples/slidev-demo/`, or `examples/marp-demo/` — never a blank file.
Confirm `node --version` (want v20+), `npx slidev --version` (52.x),
`npx marp --version` (4.x) before authoring.

## 7. Images (SKILL.md Phase 4)

Source per image (AI / stock with photographer credit / user-supplied),
copy every file into `assets/`, log filename + source + license in
`assets/CREDITS.md`, never hotlink. Treatment per `references/layouts.md` §7:
radius 16–24px, 1px border, soft shadow, `object-fit: cover`, max one
full-bleed per section, ≥40% scrim under text-over-photo.

## 8. Build (SKILL.md Phase 6 order)

Write Markdown source first even for reveal.js; theme tokens from step 3;
code slides ≤12 lines with Shiki dual theme and JetBrains Mono 16–20px;
speaker notes on every substantive slide (`<aside class="notes">` or
`<!-- presenter note -->`); smell-check against the anti-slop list
(no purple-blue gradient, max 1 gradient as accent, captions ≥14px,
contrast ≥4.5:1, ≥7:1 for projectors).
Static-by-default: ship every slide static unless clicks need a narration justification
(one idea per click, max 5 click-steps per slide, max 1 click-built slide per 3 slides);
tables by-row-or-static — reveal by row or ship static, never per-cell (see Gate 20).

## 9. Motion pass (REQUIRED — 1–3 morph pairs or FAIL)

Wire REQUIRED 1–3 morph pairs per deck on element continuations (`data-auto-animate`+`data-id` / `view-transition-name` / `v-motion` pair / Flip), never on body copy, never across sections; deck-wide single transition alone FAILs review. Then wire fragments (`fragment` / `v-click` / `_transition`), and the
reduced-motion fallback. Marp HTML transitions need `--bespoke.transition`;
Slidev `v-click` steps become extra PDF pages (expected, record as 12+N); reveal.js fragments
print as final state unless flagged. Fragment Budget is Gate 20: static-by-default,
≤5 click-steps per slide, tables by-row-or-static. Details: `references/animations.md`.

## 10. Verify checklist (all must pass)

Run `references/verify-checklist.md` gates: `scripts/verify-images.py`
(local, ≥1600px full-bleed, credited); contrast spot-check; no-placeholder
scan (no TODO/lorem/empty-src/hotlinks); reduced-motion emulated in DevTools;
notes present on every substantive slide; export smoke test via
`scripts/export-deck.sh <engine>` (HTML opens, no console errors; PDF/PPTX
paginates). Fix-forward, never ship red.

## 11. Export + ship

Export per target from `references/engines.md` § Export commands: live URL →
static SPA (`npx serve dist/` or equivalent); handout → PDF; sharing → PPTX
(Marp native; Slidev experimental with rasterized code; reveal.js via
decktape→PDF chain). Ship Markdown source alongside the built deck. Paste the
engine decision log (`references/engines.md` § Engine decision log) into the
PR or delivery note.

## Don'ts for this workflow

- Don't build before the outline nod (step 5).
- Don't float `latest` in `package.json` — pin per `references/engines.md`.
- Don't mix runtimes — exactly one engine per deck.
- Don't skip the reduced-motion fallback even for static-looking decks.
- Don't ship without `assets/CREDITS.md` entries for every image.
