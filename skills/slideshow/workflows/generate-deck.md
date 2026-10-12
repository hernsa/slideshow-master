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

**Deck shape contract** — from `references/pptx-motion-language.md`:
- Name the deck's **3–8 shape vocabulary** and its **one moving object**
  (§0, §1). Write both into the Design Read. A deck with no moving object is
  a slide sorter.
- Pick **one organic device** for the whole deck — circular tile cluster OR
  blob-behind-plate OR arch crop (§6). Never mix.
- Declare the **value ramp**: 3–4 stops derived from the locked accent by
  lightness+alpha (§7), never new hexes per slide.
- Declare the **type tiers** as named CSS custom properties —
  `--t-hero` / `--t-title` / `--t-head` / `--t-label` / `--t-body`, zero
  letter-spacing, one accent word per slide (§8).
- Pick the section template from `references/layout-templates/_index.md`
  (step 5 of the picker). `photo-collage.md`, `pastel-collage.md`, and
  `annotation-stage.md` are transcribed from the reference decks and are the
  default for photographic, community, and showcase sections.

Pick motion from `references/animations.md`: REQUIRED 1–3 morph pairs per deck on element continuations (`data-auto-animate`+`data-id` / `view-transition-name` / `v-motion` pair / Flip), never on body copy, never across sections; deck-wide single transition alone FAILs review (one morph moment per section max still applies). ONE transition for the whole deck, applied identically everywhere (§3 of the PPTX craft system).
fragments for stepwise reveals, `prefers-reduced-motion` fallback planned now.

## 4. Research (SKILL.md Phase 3, 2-source rule) — REQUIRED artifact

Run `stages/topic-research.md` top to bottom. Produce `research-notes.md`
in the deck dir — **ship-blocking, never skipped**: one section per slide
with 4–8 content bullets (facts, dates, numbers, quoted names) plus the
per-slide source log (2+ independent sources, or `[unverified]`). Content
depth rule: every slide needs enough raw material for 2x its on-slide copy
— if a slide's notes run under ~60 words of distinct facts, research is not
done, re-draft the outline deeper (see step 5 depth rule). Every API, CLI
flag, and version verified against current docs (pin reveal.js 6, Slidev 52,
Marp CLI 4 per `references/engines.md`). Single-source claims marked
`[unverified]` and never stated as fact on the slide. Hand the file to the
user with the outline nod — it is the evidence the deck argues from.

## 5. Outline (mode file, approval gate)

Open the routed mode file under `references/modes/` and write one line per
slide: title + point + visual + MANDATORY `bg:` tag on every line (per `references/color-usage.md` §1; longest identical-`bg` run ≤2 or ship-blocker; stock `theme: default` with no applied style does not satisfy rotation). Counts: tech-talk 10, pitch 8, tutorial 8,
showcase 6, narrative 8. **Depth rule — never one slide per topic**: each
major topic gets 2–3 slides (setup → detail/evidence → consequence), so a
deck with 4 topics runs ≥8 slides; the outline must be ≥1.5× the topic list.
Demo-universe titles where fitting ("Last Month, My
PPTX Died on Stage Wi-Fi", "Tonight: One URL, Zero Installs"). Paste the
outline + `research-notes.md` for a nod before writing slides — cheap to
change now, expensive later.

**`visual-plan.md` — ship-blocking, written in this same pass.** One block per
slide, in the slide's z-order, using the grammar from
`references/pptx-motion-language.md` §9. The `Done when:` line is what makes it
testable — a plan without it is a wish list.

```
## Slide 3 — Hà Nội · 1890          bg: dark-photo
  Template:   photo-collage
  Text runs:  hero "Hà Nội · 1890" {--t-title} ; sub 1 line {--t-body}
  Z-order:    plate → tiles → disc → copy
  Images:     assets/hanoi-1890.jpg (bg) · tile-1..4.jpg · disc-jpeg.jpg  → 6 rasters
  Entrances:  hero .10s, sub .22s
  Anchors:    disc rotates 0° → -89° ; hero copy pinned identical
  Done when:  6 images present, hero glyph-identical to slide 2, disc rotated -89°.
```

**The plan's hard counts (a plan that misses them goes back to the outline):**
- **≥1 photographic or hand-drawn image on every slide.** A deck whose
  `assets/CREDITS.md` says "no external raster images" is a failed deck
  (§5). Ratios worth aiming at, from the reference decks: narrative sections
  run 3–6 rasters per slide, explainers 1–2.
- **≥1 SVG diagram per 2 content slides.** Sequential, comparative, and
  data-heavy slides are the textbook case for `references/data-graphics/`.
- **1–2 decorative primitives per slide** from `references/decorations.md`.
- **≤3 entrances per slide**, sharing the Gate 8 fragment budget.
- **≥2 named anchors per section**, with exactly one anchor moving per step.

Paste the outline, `research-notes.md`, and `visual-plan.md` together for the nod.

## 6. Scaffold

Run `scripts/new-deck-scaffold.sh <engine> <deck-dir>` (engines and flags in
`references/engines.md`). Start from `examples/reveal-demo/`,
`examples/slidev-demo/`, or `examples/marp-demo/` — never a blank file.
Confirm `node --version` (want v20+), `npx slidev --version` (52.x),
`npx marp --version` (4.x) before authoring.

## 7. Images + decorations (SKILL.md Phase 4) — REQUIRED artifact

Execute `visual-plan.md` from step 5 line by line, in z-order, and mark each
line done as you go — every planned SVG diagram is drawn (rung-1, zero license
cost, per `references/media/images.md`), every planned image is sourced. A plan
line with no matching file in `assets/` means the build stops and the plan gets
fixed, not the slide.

Source per image (AI / stock with photographer credit / user-supplied), copy every
file into `assets/`, log filename + source + license in `assets/CREDITS.md`,
never hotlink. Treatment per `references/layouts.md` §7: radius 16–24px, 1px
border, soft shadow, `object-fit: cover`, max one full-bleed per section, ≥40%
scrim under text-over-photo.

Decorate per `references/decorations.md` — 1–2 primitives
per slide (kicker, rule-bar, left-rail, oversized number, background shape,
chip row) and break symmetry: never three-equal-card rows, alternate
left/right-weighted layouts, use the giant-number proof slides. No slide
ships bare text on a flat fill.

Check the counts before leaving this step: **every slide has ≥1 image**, raster
count ÷ slide count is in the ratio step 5 set, and the section's organic
device matches the one chosen at style lock.

**Open the template file for each section and copy its slide-spec block into
`visual-plan.md` before writing a line of that section's HTML.** Do not
improvise a layout when a template already covers it:

| Section reads as | Open this file |
|---|---|
| archive, history, case study, "show me the real thing" | `references/layout-templates/photo-collage.md` |
| community, explainer, people, warm brand | `references/layout-templates/pastel-collage.md` |
| product launch, feature reveal, single-subject stage | `references/layout-templates/annotation-stage.md` |
| mood beat between sections | `references/layout-templates/photo-hero.md` |
| giant one-line statement | `references/layout-templates/display-type.md` |
| open / divide / close the talk | `references/layout-templates/framing.md` |
| continuity across slides without fragments | `references/layout-templates/motion.md` |

The three PPTX-derived templates are the defaults for photographic, community,
and showcase sections. `references/layout-templates/_index.md` step 8 forbids
mixing organic devices — pick one per deck.

## 8. Build (SKILL.md Phase 6 order)

Write Markdown source first even for reveal.js; theme tokens from step 3;
code slides ≤12 lines with Shiki dual theme and JetBrains Mono 16–20px;
speaker notes on every substantive slide (`<aside class="notes">` or
`<!-- presenter note -->`); smell-check against the anti-slop list
(no purple-blue gradient, max 1 gradient as accent, captions ≥14px,
contrast ≥4.5:1, ≥7:1 for projectors).

Copy the HTML/CSS block from the section's template file verbatim and swap the
copy for real content — the geometries, rotations, z-order, and the plate/tile
numbers in `photo-collage.md` and the pastel ramp in `pastel-collage.md` are
load-bearing. Inventing a fresh layout per slide breaks the morph contract
(`pptx-motion-language.md` §2): the deck must ship 3–8 distinct shapes reused
across every slide, not a new composition each time.

Static-by-default: ship every slide static unless clicks need a narration justification
(one idea per click, max 5 click-steps per slide, max 1 click-built slide per 3 slides);
tables by-row-or-static — reveal by row or ship static, never per-cell (see Gate 8).

## 9. Motion pass (REQUIRED — 1–3 morph pairs or FAIL)

Wire REQUIRED 1–3 morph pairs per deck on element continuations (`data-auto-animate`+`data-id` / `view-transition-name` / `v-motion` pair / Flip), never on body copy, never across sections; deck-wide single transition alone FAILs review. Then wire fragments (`fragment` / `v-click` / `_transition`), and the
reduced-motion fallback. Marp HTML transitions need `--bespoke.transition`;
Slidev `v-click` steps become extra PDF pages (expected, record as 12+N); reveal.js fragments
print as final state unless flagged. Fragment Budget is Gate 8: static-by-default,
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
- Don't ship without `visual-plan.md` — it is ship-blocking, same as
  `research-notes.md`.
- Don't let a slide reach the build with zero images; that's a plan failure
  caught at step 7, not a styling preference fixed at step 8.
- Don't float `latest` in `package.json` — pin per `references/engines.md`.
- Don't mix runtimes — exactly one engine per deck.
- Don't skip the reduced-motion fallback even for static-looking decks.
- Don't ship without `assets/CREDITS.md` entries for every image.
