# Verify Checklist — Ship Gates

> Fail any gate = do not ship. Check in order. Each gate below states WHY it matters, HOW to check (exact command or steps), PASS criteria with numbers, a FAIL example, and a fix-it snippet. The content-density pre-condition sits outside the numbered gates and blocks ship the same way.

Copy-paste ship record (fill per deck):

```markdown
Deck: Acme Q3 — 18 slides — reveal.js 6
Date: 2026-10-08 · Checker: Ada
- Outline approved: yes (2026-10-01, Jonas)
- 2-source rule: 6/6 stats sourced
- Images & media: 5 local, all ≤400KB, credited, alt 100%, 6 visuals captioned
- Contrast: fg/bg 15.8:1, muted/bg 6.1:1, muted/surface 4.9:1
- Placeholders: 0 hits on greps 1–3, grep 4 demo URLs only
- Style tokens: 2 + mono · Gradients: 1
- Code slides: max 9 lines, Shiki dual-theme, zero gray blocks
- Motion & input: cuts verified, fragments ≤5/slide, keyboard pass
- Notes: 18/18 · Mobile 390px: pass
- Export: PDF 18pp clean, PPTX spot-check pass, console 0 errors
- Theme & rotation: STRONG, longest bg run ≤2 · Icons: inline SVG only
- Composition: visual-plan done, 1 transition, anchors paired, photo grammar holds
- Content density pre-condition: research-notes.md 4–8 bullets/slide, no thin slides
```

---

## Pre-condition — Content density (research-notes artifact + min words/slide)

**WHY:** The builder's deck had `slides-content.md` only 3405 B (thin) and no `research-notes.md`. Every slide needs ~2x content depth before visuals begin.

**HOW:** (1) `research-notes.md` exists in deck dir with one section per slide, 4-8 bullets + 2-source log — ship-blocking artifact from `workflows/generate-deck.md` step 4; (2) `scripts/verify-deck.py` word count per slide ≥ 10 for text-only slides; (3) outline ≥ 1.5x topic list (`workflows/generate-deck.md` step 5 depth rule). Full procedure: `workflows/stages/topic-research.md`.

**PASS:** `research-notes.md` present with full bullets + sources; no thin slides; outline depth ≥ 1.5x topics.

**FAIL:** Missing `research-notes.md`; any slide < 10 words text-only; outline 1-slide-per-topic.

**Fix:** Run `workflows/stages/topic-research.md` fully, produce `research-notes.md`, expand each slide's bullets, enforce depth rule in outline (2-3 slides per major topic).

---

## Gate 1 — Outline approved

**WHY:** Slide polish cannot fix a broken arc. Unapproved outlines drift into 40-slide braindumps with no verdict.

**HOW:** Confirm a dated approval (doc comment, issue, or message link) before building visuals. No approval = stop.

**PASS:** Approval timestamp + approver name recorded; slide titles match the approved beats 1:1.

**FAIL:** “I’ll figure out the story while designing slide 12.” Deck has 6 sections but the outline promised 3.

**Fix:** Freeze the outline first:
```markdown
Outline v3 — APPROVED 2026-10-01 (Jonas)
1. The stall (3 slides) 2. The fix (6 slides) 3. The proof (5 slides) + appendix (4)
```

## Gate 2 — Two-source rule (every stat sourced twice or flagged)

**WHY:** Single-source numbers die in Q&A. “Where did 41% come from?” must have an answer on the slide or in notes.

**HOW:** For each stat, record source + corroboration (second query, dashboard, or teammate confirm). Mark estimates explicitly as estimates.

**PASS:** 100% of headline stats carry a caption or notes citation; estimates labeled `~` with method in notes.

**FAIL:** Slide claims “NRR 128%” with no source anywhere. Speaker improvises provenance live.

**Fix:**
```html
<p style="font-size:14px;opacity:.65">Source: edge logs Jun 14 → Sep 2, confirmed against billing export.</p>
<!-- notes: query id q-8821, rerun 2026-10-06, ±2pp sampling error -->
```

## Gate 3 — Images & media (local + sized + credited + alt + density)

**WHY:** Hotlinked images 404 on venue Wi-Fi. 4MB photos hitch transitions. Uncredited photos are a legal and ethical liability. Screen readers, broken-image fallback, and search all depend on `alt`. Text-only stretches lose the room — one visual every 3 slides holds attention, and uncaptioned images break the narrative.

**HOW:**
1. All `src` under `assets/` (no `http` images except live-demo iframes).
2. Each file ≤ 400KB photos / ≤ 200KB backgrounds, max width 1920px (parallax 3000px wide allowed, still ≤ 400KB).
3. Credit line per image (photographer / product / “Acme internal”).
4. Scan every `<img>` / Markdown `![]()`. Informative gets a one-line description with the takeaway, not “image of chart”. Decorative gets `alt=""`.
5. Count slides vs visuals (photo, chart, diagram, icon-graphic, terminal screenshot). Divide: visuals ÷ slides must clear 1:3. Every `<img>` needs a sibling caption or credit line stating what it proves plus its source.

```bash
ls -lh assets/
# expect: every file present, photos ≤400K, backgrounds ≤200K
```

**PASS:** `grep -r "http.*img\|src=\"http" slides/` returns only intentional iframe/demo URLs; every `<img>` has a sibling credit or caption; `ls` sizes in budget. 100% of `<img>` tags carry `alt`; informative alts state the conclusion (`p95 falling from 412 to 243ms`); decorative alts are empty. Ratio ≥ 1 visual per 3 slides (an 18-slide deck holds ≥ 6 visuals). 100% of images carry a caption or credit (`Photo: Maria Santos, Acme lab` / `Source: edge logs Jun 14 → Sep 2`). No hotlinked `src="http"` outside documented demo iframes.

**FAIL:** `<img src="https://placekitten.com/1600/900">`, or `lab-4MB.png`, or a full-bleed photo with no credit. `<img src="assets/chart.png">` (no alt), or `alt="image"` (useless). 12-slide deck with 2 visuals (both on slides 2–3), then 9 straight text slides. Lab photo full-bleed with no credit or caption.

**Fix:**
```html
<figure style="margin:0">
  <img src="assets/lab.jpg" alt="Engineers reviewing the Shield deploy dashboard as p95 falls" class="fit" />
  <figcaption style="font-size:14px;opacity:.65">Photo: Maria Santos, Acme lab. p95 412 → 243ms week of Jul 19.</figcaption>
</figure>
```

## Gate 4 — Contrast ratios measured

**WHY:** Muted-on-surface fails silently and projectors make it worse. Eyes cannot judge 4.4 vs 4.6 — tools can.

**HOW:** Measure three pairs with DevTools picker or WebAIM: `fg/bg`, `muted/bg`, `muted/surface`. Record all three numbers.

**PASS:** Normal text ≥ 4.5:1, large (≥18pt / 14pt bold) ≥ 3:1. All three pairs pass. Code `fg/bg` ≥ 7:1.

**FAIL:** `muted #64748B` on `surface #F1F5F9` assumed fine but measures 4.2:1 on the venue projector. Teal body copy at 3.9:1 shipped as paragraphs.

**Fix:**
```css
/* promote failing muted without redesigning */
.fix-muted { color: var(--fg); opacity: .82; }
```

## Gate 5 — Placeholder scan (zero tolerance)

**WHY:** TODO, lorem, “coming soon”, and duplicate slide titles ship more often than anyone admits. Audiences remember exactly one thing: the placeholder.

**HOW:** Run all four greps from the deck root. Every hit must be zero (except this checklist file itself).

```bash
grep -rni "todo\|placeholder\|coming soon\|fix me\|xxx" --include="*.md" --include="*.html" .
grep -rni "lorem" --include="*.md" --include="*.html" .
grep -rni "slide title here\|untitled\|test test" --include="*.md" --include="*.html" .
grep -rho "src=\"http[^\"]*\"" --include="*.html" --include="*.md" . | sort | uniq -c
```

**PASS:** Greps 1–3 return nothing. Grep 4 returns only intentional demo/iframe URLs documented in notes.

**FAIL:** An unfilled `<!-- FILL IN: real number -->` marker on slide 9. Filler-text paragraph in the closing slide from a copied template.

**Fix:** Replace with real content or delete the slide. Never ship unfinished beats — cut them and tighten the talk.

## Gate 6 — Style tokens (2 + mono fonts max, single gradient)

**WHY:** Three body fonts scream template salad. Each extra family adds load time, FOUT risk, and export breakage. Multiple gradients fight each other and date the deck instantly. Gradient body text fails contrast and exports as raster mush.

**HOW:** Count `family=` in font links + `@font-face` + theme configs. Code mono is exempt but must be exactly one. Search for `gradient` across CSS/Markdown. Count distinct gradient declarations. Verify none apply to text.

```bash
grep -rni "gradient" --include="*.css" --include="*.html" --include="*.md" . | tee gradients.txt | wc -l
```

**PASS:** ≤ 2 text families + 1 mono. Example: `Inter` + `Fraunces` + `JetBrains Mono`. Weights ≤ 4 total. Gradient count ≤ 1. The single gradient is a hero background *or* one chart series. Zero `background-clip: text` hits.

**FAIL:** Inter + Sora + Fraunces + Caveat + Roboto Mono in one deck. Six weights of Inter loaded. Purple-blue cover + teal CTA + sunset divider + gradient headline = 4 gradients. White text on mid-teal at 2.8:1.

**Fix:**
```html
<!-- keep this, delete the rest -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Fraunces:opsz,wght@9..144,600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet" />
```
```css
/* allowed: one hero wash */
.hero { background: linear-gradient(180deg, #F1F5F9 0%, #FFFFFF 70%); }
/* banned: delete all of these */
/* background: linear-gradient(...) on h1, .card, .cta, .divider */
```

## Gate 7 — Code slides (12 lines max, Shiki dual-theme render)

**WHY:** Audiences cannot read 30 lines from row 10. Long blocks shrink fonts below legibility and break PPTX rasterization. An unstyled gray block tells the audience the speaker does not care about code. Mismatched light/dark themes flash the room on toggle.

**HOW:** Count non-blank lines in every `<pre>` / fenced block. Include the fix: split, fold, or link the repo. Toggle `.dark` (or Slidev/Marp theme). Confirm Shiki theme follows, highlighted lines match the narration, scroll intact.

**PASS:** Every code slide ≤ 12 lines, font ≥ 14px (15px preferred), highlight matches the discussed lines, horizontal scroll intact where needed. Shiki dual themes (`vitesse-light/dark` or `github-light/dark`) track the mode toggle; zero gray blocks; discussed lines highlighted; no content hidden behind scroll without affordance.

**FAIL:** 28-line file dump at 11px. Full Dockerfile nobody walks through. Light-mode code pasted as dark screenshot — glowing white box in a light deck. `{2-4}` highlight points at an import block.

**Fix:**
```markdown
```ts {2}
shield.enable({ staleWhileRevalidate: 90 });
// full module: github.com/acme/shield (link in notes)
```
```
```js
const html = await codeToHtml(source, {
  lang: 'ts',
  themes: { light: 'github-light', dark: 'github-dark' }
});
```

## Gate 8 — Motion & input (fragment budget + reduced-motion cut + keyboard pass)

**WHY:** A real Slidev test deck shipped ~53 v-click steps across 8 slides (one Acme Q3 metrics table carried 20 cell-by-cell clicks). Click-spam breaks PDF exports, strands keyboard clickers, and buries the narration. Vestibular disorders, migraines, and projector flicker make motion a health issue, not a preference. Clickers send keyboard events — if arrows/Space/PageUp/PageDown fail, the speaker is stranded.

**HOW:** Three sub-checks, all must pass:
- **Fragment budget:** count v-click per `---` slide block (v-click/v-after/fragment together) and reject per-cell table clicks. Run from the deck root. FAIL if >5 in any block:
```bash
grep -c "v-click\|v-after\|class=\"fragment\"" slides.md
awk 'BEGIN{RS="\n---\n"} {c=gsub(/v-click|v-after|class="fragment"/,"&"); if(c>0) print "block " NR ": " c " click-steps"}' slides.md
# FAIL if any block reports >5 — split the slide
# per-cell FAIL pattern — v-click on table cells must return nothing:
grep -rPn "v-click" --include="*.md" . | grep -P "\|"
grep -rPn "<t[dh][^>]*v-click" --include="*.md" --include="*.html" .
```
- **Reduced-motion cut:** enable DevTools Rendering → Emulate `prefers-reduced-motion: reduce`, then walk the deck. Confirm instant cuts, visible fragments, static parallax.
- **Keyboard pass:** unplug the mouse. Navigate fully by keyboard: Right/Space forward, Left back, Home first, End last. Confirm visible focus on links/buttons.

**PASS:** Max 5 click-steps per slide (v-click/fragment/v-after total); max 1 click-built slide per 3 slides; tables reveal by row or ship static (never per-cell); Slidev step count recorded as 12+N PDF pages. Greps above show zero blocks >5 and zero per-cell hits. All Auto-Animate/Flip/transitions/`v-motion`/parallax/scroll timelines collapse to cuts; all fragments visible without clicks; no flashing over 3Hz anywhere. All keys advance reliably; focus ring visible on every interactive element; no keyboard traps in iframes.

**FAIL:** 8-slide Slidev deck with 53 v-clicks; Acme Q3 metrics table with 20 cell-by-cell v-clicks; any `---` block with 6+ hits; any `v-click` on table cells. `v-motion` hero never appears under reduced motion (stuck at `opacity: 0`). Marp deck with no static build linked. Custom JS hijacks Space for video play — slides stop advancing. Focus invisible on dark backgrounds.

**Fix:** Split the overloaded slide, collapse to row reveals, or ship static:
```markdown
<!-- before: 20 per-cell clicks — banned -->
<!-- <div v-click>cell 1</div> ... x20 -->

<!-- after: row reveals (3 clicks) or static -->
<div v-click>Row 1 — edge cache hit, p95 412ms</div>
<div v-click>Row 2 — origin shield added, p95 301ms</div>
<div v-click>Row 3 — Q3 recovery, NRR 128%</div>
<!-- or delete all v-click and ship the full Acme table static -->
```
```css
@media (prefers-reduced-motion: reduce) {
  .fragment { opacity: 1 !important; transform: none !important; }
  .reveal-on-scroll, .progress-rail { animation: none !important; opacity: 1 !important; }
}
```
```js
Reveal.initialize({ autoAnimate: !matchMedia('(prefers-reduced-motion: reduce)').matches });
```
```css
:focus-visible { outline: 3px solid var(--primary); outline-offset: 2px; }
```

## Gate 9 — Speaker notes coverage (every slide)

**WHY:** Notes are the talk. A slide without notes is a slide the speaker will improvise — and ramble.

**HOW:** Count slides vs notes. reveal.js: `<aside class="notes">` per section. Slidev: `<!-- -->` per page. Marp: presenter comment convention per project.

**PASS:** Notes-to-slides ratio 1:1 (appendix exempt only if marked `NO-NOTES`). Each note holds: the one sentence to say, the transition line to the next slide, and any stat provenance.

**FAIL:** 18 slides, 6 notes. Title slide note says “intro myself” with no name/title/timecheck.

**Fix:**
```html
<aside class="notes">Say: p95 fell 41% in six weeks. Then: but July was ugly — next slide. Timecheck: 2:00.</aside>
```

## Gate 10 — Mobile swipe + 390px layout

**WHY:** Attendees open the link on phones. Broken overflow is the difference between “great talk” and “couldn’t read slide 7”.

**HOW:** DevTools device toolbar at 390×844. Swipe forward/back, check tap targets, scroll for horizontal overflow.

**PASS:** Swipe works both directions; tap targets ≥ 44px; zero horizontal scroll; bento/stat grids collapse to 1–2 columns; code scrolls internally without breaking layout.

**FAIL:** 4-column bento at 390px renders 90px-wide unreadable cells. 12px code overflows the viewport.

**Fix:**
```css
@media (max-width: 520px) {
  .bento, .stats { grid-template-columns: 1fr !important; }
  pre { font-size: 13.5px; overflow-x: auto; }
  a, button { min-height: 44px; min-width: 44px; }
}
```

## Gate 11 — Export smoke test (PDF + PPTX + HTML)

**WHY:** The export is the artifact that outlives the talk. “Works on my laptop” means nothing if the PDF cuts text and the PPTX drops fonts.

**HOW:** Generate all three from the final commit, then check: full page count, no cut-off text, fonts embedded/readable, spot-check title + bento + code + quote slides.

```bash
# Marp path
npx marp slides.md -o deck.pdf --allow-local-files
npx marp slides.md -o deck.pptx --allow-local-files
# Slidev path
npx slidev export --format pdf slides.md
# reveal.js path
npx decktape reveal "http://localhost:8000/?print-pdf" deck.pdf
```

**PASS:** PDF page count equals slide count (+ click-steps where applicable); zero clipped lines at 100% zoom; PPTX opens in PowerPoint + Google Slides with readable fonts; transitions acceptably degrade to cuts.

**FAIL:** PDF ends mid-sentence on slide 11 (overflow). PPTX code slide renders in fallback serif. HTML references `localhost` demo URL.

**Fix:** Freeze overflow slides (split or cut lines), screenshot auth-gated demos, embed/swap to system fonts for PPTX deliverables.

## Gate 12 — No console errors (Chromium + Firefox)

**WHY:** Console errors are the canary: 404 assets, blocked fonts, dead iframes. If the console is red, something the audience should see is missing.

**HOW:** Open DevTools console in Chromium and Firefox, walk every slide including appendix, watch Network for 404s.

**PASS:** Zero errors, zero 404s for assets/fonts/iframes. Warnings documented or fixed.

**FAIL:** `GET assets/chart-v2.png 404`, `Refused to display iframe (X-Frame-Options)`, `Shiki language 'tsx2' not found`.

**Fix:** Commit the missing asset under `assets/`, replace frame-blocked demos with screenshots + links, correct the language tag to `tsx`.

## Gate 13 — Theme & rotation (STRONG lock, no 3 consecutive same-bg)

**WHY:** The builder's deck shipped 8 slides on flat cream `#FEFCF8` that read white on projector — no visual identity. Three identical backgrounds in a row read as an unfinished template, not calm design. Rotation is planned in the outline — polish cannot retrofit it.

**HOW:** Check deck source: (1) theme tokens present (`--bg:` / `@theme` / `theme:` non-default) — verify-deck.py Gate; (2) rotation present (bg markers ≥1) — verify-deck.py Gate; (3) no stock `theme: default` without applied style in Markdown frontmatter; (4) palette from `references/visual-styles/` STRONG tier unless user explicitly requests SOFT. List the page fill per slide (`base`, `surface`, `divider`, `photo`, `dark-quote`, `dark-code`, `cta`). Scan for any run of 3+ consecutive `base` text slides. Photo sequences count as one change stretched over two slides; live-demo runs up to 4 dark slides must be noted in speaker notes.

**PASS:** Deck declares a STRONG-tier palette (Crimson Bold, Navy Signal, Forest Ink, Midnight SaaS, Dark Tech, Brutalist, Teal Serenity, Bento Minimal, Glassmorphism), tokens applied, rotation active. Longest run of identical consecutive backgrounds is ≤ 2. Every 3rd slide changes surface (tinted divider, image bleed, accent band, dark quote/code slide). Outline carries a `bg:` tag per slide matching the built deck.

**FAIL:** `theme: default` alone; tokens missing; all slides one flat fill; SOFT palette (Botanical Warm, Paper Editorial, GitHub Tech, Swiss Minimal) without explicit user request. Slides 4–6 all on base `bg #FFFFFF`: rollout timeline, config list, p95 chart — no divider, photo, or band between them.

**Fix:**
```markdown
Outline v3 — APPROVED 2026-10-01 (Jonas)
4. fix — Shield rollout, 3 regions (bg: base)
5. fix — stale-while-revalidate snippet (bg: dark code)
6. DIVIDER — "The proof" tinted surface (bg: SURFACE CHANGE)
```
Apply a STRONG palette from `references/visual-styles/_index.md`; add at least one tinted divider/dark quote/accent-band slide.

## Gate 14 — Icon discipline (zero emoji-as-icons, all SVG inline currentColor)

**WHY:** Emoji render as mismatched color blobs across platforms and projectors, break screen readers, and rasterize badly in PDF/PPTX export. Inline SVG in `currentColor` inherits the palette and stays sharp everywhere.

**HOW:** Search for emoji and icon fonts across slides and CSS. Confirm every icon is an inline `<svg>` using `currentColor` with an accessible name or `aria-hidden`.

```bash
grep -rPn "[\x{1F300}-\x{1FAFF}\x{2600}-\x{27BF}\x{2B00}-\x{2BFF}]" --include="*.html" --include="*.md" .
grep -rni "font-awesome\|material-icons\|emoji" --include="*.css" --include="*.html" --include="*.md" . | tee icons.txt | wc -l
```

**PASS:** Emoji grep returns nothing outside documented demo content. Icon-font grep returns nothing. Every icon is inline SVG with `fill="currentColor"` or `stroke="currentColor"` plus `aria-hidden="true"` (decorative) or `<title>` (meaningful).

**FAIL:** `✅ Ship it` and `⚠️ Risk` as bullet icons — green check renders gray on the projector, warning triangle reads as text on screen readers. Font Awesome CDN linked for three arrows.

**Fix:**
```html
<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2">
  <title>Pass</title>
  <path d="M2.5 8.5l3.5 3.5 7-8" stroke-linecap="round" stroke-linejoin="round" />
</svg>
<span>Shield rollout passed in 3 regions</span>
```

## Gate 15 — Composition & motion-language (decorations + anchors + one transition + photo grammar)

**WHY:** The builder's deck was fully centered, symmetrical, no decorations — "everything centered/creamy/symmetrical". Five liked reference decks feel modern with zero explicit transitions: 2+ big repeated anchors per section, one deck-wide transition, staggered entrances, full-bleed or masked photos, oversized display type. Without this gate decks default to transition roulette + small-card morphs + raw rectangle photos.

**HOW:** Per `references/pptx-motion-language.md`: (1) `visual-plan.md` exists with one line per visual (SVG diagram to draw + image to source + landing slide — ship-blocking artifact from `workflows/generate-deck.md` step 5); (2) `references/decorations.md` primitives used 1-2 per slide (kicker, rule-bar, left-rail, oversized number, background shape, chip row); (3) no three-equal-card rows; (4) layouts alternate left/right weighted; (5) oversized-number proof slides present for key metrics; (6) each section lists its 2 continuity anchors (same element, same position, adjacent slides); (7) ONE slide transition locked for the whole deck (one zoom/none exception max); (8) entrances staggered ≤3 per slide, ≤600ms total, sharing the Gate 8 fragment budget; (9) photos are full-bleed-with-scrim or deck-mask-shaped (arch/blob/circle, one mask per deck); (10) one display headline per slide `clamp(2.5rem,6vw,4.5rem)` + one accent word max.

**PASS:** `visual-plan.md` present; decorations applied per `references/decorations.md`; asymmetry enforced; visual plan executed. Anchors listed per section and morph-paired; single transition; stagger capped; photo grammar holds; display type oversized.

**FAIL:** No `visual-plan.md`; all slides centered/flat; three-equal-card rows; zero decorations; all visuals same treatment. Per-slide transition overrides; stagger + v-click chains stacked; raw rectangle photos on designed slides; body-size headlines everywhere; zero repeated anchors across adjacent slides.

**Fix:** Create `visual-plan.md` at outline (draw SVG diagrams rung-1 zero license, source images per `references/media/images.md`, apply `references/decorations.md` primitives, break symmetry). Lock anchors at outline (`Anchors:` line per slide), set one transition at style lock, convert extra clicks to static, mask or full-bleed the photos, scale the headline.
```markdown
## Slide 3 — Pipeline: deployed
Text runs: [kicker 14px mono / headline clamp(2.5rem,6vw,4.5rem) / body 1.1rem ≤25 words]
Z-order: bg photo → scrim → accent shape → headline → body → chip row
Entrances: [rise 300ms d100] headline, [rise 300ms d220] body (≤3, ≤600ms total)
Anchors: sec-title continues from slide 2 (data-id sec-title, position held, size +0)
Transition: none (deck default fade 0.4s)
```

---

## Render-screenshot verification (headless Chrome)

- Authority: `workflows/stages/export-verify.md` §1 (export runs only after visual sign-off) + per-engine flags in `scripts/export-deck.sh`.
- Structural checks run on source via `scripts/verify-deck.py`; render-screenshot covers visual regression only (layout overflow, fragment visibility, reduced-motion).
- reveal.js over HTTP (`hash:true`, navigate via `#/N`); headless Chrome `--screenshot` with `--virtual-time-budget`; allow 2–3s for the async write before checking.
- Read clean source files directly for DOM counts — never diagnose from piped dumps with broken codepages.

---

## Pre-ship run (15 minutes, in order)

1. Research + outline → `workflows/stages/topic-research.md` §1 (gap list closed, outline approved)
2. Images + credits + sizing → `workflows/stages/image-review.md` §1 (local, credited, in budget)
3. Built-deck walk → `workflows/stages/visual-review.md` §1 (contrast → code → motion → notes sign-off)
4. Export + ship record → `workflows/stages/export-verify.md` §1 (artifacts open clean, record signed, then present)
