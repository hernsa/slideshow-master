# Verify Checklist — Ship Gates

> Fail any gate = do not ship. Check in order. Each gate below states WHY it matters, HOW to check (exact command or steps), PASS criteria with numbers, a FAIL example, and a fix-it snippet.

Copy-paste ship record (fill per deck):

```markdown
Deck: Acme Q3 — 18 slides — reveal.js 6
Date: 2026-10-08 · Checker: Ada
- Outline approved: yes (2026-10-01, Jonas)
- 2-source rule: 6/6 stats sourced
- Images: 5 local, all ≤400KB, credited
- Contrast: fg/bg 15.8:1, muted/bg 6.1:1, muted/surface 4.9:1
- Placeholders: 0 hits on TODO/lorem/placeholder greps
- Fonts: 2 + mono · Code lines: max 9 · Gradients: 1
- Reduced motion: cuts verified in emulation
- Notes: 18/18 · Keyboard: pass · Mobile 390px: pass
- Export: PDF 18pp clean, PPTX spot-check pass, console 0 errors
```

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

## Gate 3 — Images local + sized + credited

**WHY:** Hotlinked images 404 on venue Wi-Fi. 4MB photos hitch transitions. Uncredited photos are a legal and ethical liability.

**HOW:**
1. All `src` under `assets/` (no `http` images except live-demo iframes).
2. Each file ≤ 400KB photos / ≤ 200KB backgrounds, max width 1920px (parallax 3000px wide allowed, still ≤ 400KB).
3. Credit line per image (photographer / product / “Acme internal”).

```bash
ls -lh assets/
# expect: every file present, photos ≤400K, backgrounds ≤200K
```

**PASS:** `grep -r "http.*img\|src=\"http" slides/` returns only intentional iframe/demo URLs; every `<img>` has a sibling credit or caption; `ls` sizes in budget.

**FAIL:** `<img src="https://placekitten.com/1600/900">`, or `lab-4MB.png`, or a full-bleed photo with no credit.

**Fix:**
```html
<figure style="margin:0">
  <img src="assets/lab.jpg" alt="Engineers reviewing a deploy dashboard" class="fit" />
  <figcaption style="font-size:14px;opacity:.65">Photo: Maria Santos, Acme lab. Compressed 320KB, 1920px.</figcaption>
</figure>
```

## Gate 4 — Alt text on all images

**WHY:** Screen readers, broken-image fallback, and search all depend on `alt`. Decorative images need `alt=""` so they are skipped, not announced as “image”.

**HOW:** Scan every `<img>` / Markdown `![]()`. Informative gets a one-line description with the takeaway, not “image of chart”.

**PASS:** 100% of `<img>` tags carry `alt`; informative alts state the conclusion (`p95 falling from 412 to 243ms`); decorative alts are empty.

**FAIL:** `<img src="assets/chart.png">` (no alt), or `alt="image"` (useless).

**Fix:**
```html
<img src="assets/latency.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks" />
<img src="assets/divider-texture.png" alt="" />
```

## Gate 5 — Contrast ratios measured

**WHY:** Muted-on-surface fails silently and projectors make it worse. Eyes cannot judge 4.4 vs 4.6 — tools can.

**HOW:** Measure three pairs with DevTools picker or WebAIM: `fg/bg`, `muted/bg`, `muted/surface`. Record all three numbers.

**PASS:** Normal text ≥ 4.5:1, large (≥18pt / 14pt bold) ≥ 3:1. All three pairs pass. Code `fg/bg` ≥ 7:1.

**FAIL:** `muted #64748B` on `surface #F1F5F9` assumed fine but measures 4.2:1 on the venue projector. Teal body copy at 3.9:1 shipped as paragraphs.

**Fix:**
```css
/* promote failing muted without redesigning */
.fix-muted { color: var(--fg); opacity: .82; }
```

## Gate 6 — Placeholder scan (zero tolerance)

**WHY:** TODO, lorem, “coming soon”, and duplicate slide titles ship more often than anyone admits. Audiences remember exactly one thing: the placeholder.

**HOW:** Run all four greps from the deck root. Every hit must be zero (except this checklist file itself).

```bash
grep -rni "todo\|placeholder\|coming soon\|fix me\|xxx" --include="*.md" --include="*.html" .
grep -rni "lorem" --include="*.md" --include="*.html" .
grep -rni "slide title here\|untitled\|test test" --include="*.md" --include="*.html" .
grep -rho "src=\"http[^\"]*\"" --include="*.html" --include="*.md" . | sort | uniq -c
```

**PASS:** Greps 1–3 return nothing. Grep 4 returns only intentional demo/iframe URLs documented in notes.

**FAIL:** `<!-- TODO: find real number -->` on slide 9. `Lorem ipsum` in the closing slide from a copied template.

**Fix:** Replace with real content or delete the slide. Never ship “TBD” — cut the beat and tighten the talk.

## Gate 7 — Font count (2 + mono max)

**WHY:** Three body fonts scream template salad. Each extra family adds load time, FOUT risk, and export breakage.

**HOW:** Count `family=` in font links + `@font-face` + theme configs. Code mono is exempt but must be exactly one.

**PASS:** ≤ 2 text families + 1 mono. Example: `Inter` + `Fraunces` + `JetBrains Mono`. Weights ≤ 4 total.

**FAIL:** Inter + Sora + Fraunces + Caveat + Roboto Mono in one deck. Six weights of Inter loaded.

**Fix:**
```html
<!-- keep this, delete the rest -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Fraunces:opsz,wght@9..144,600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet" />
```

## Gate 8 — Code line count (12 max per slide)

**WHY:** Audiences cannot read 30 lines from row 10. Long blocks shrink fonts below legibility and break PPTX rasterization.

**HOW:** Count non-blank lines in every `<pre>` / fenced block. Include the fix: split, fold, or link the repo.

**PASS:** Every code slide ≤ 12 lines, font ≥ 14px (15px preferred), highlight matches the discussed lines, horizontal scroll intact where needed.

**FAIL:** 28-line file dump at 11px. Full Dockerfile nobody walks through.

**Fix:**
```markdown
```ts {2}
shield.enable({ staleWhileRevalidate: 90 });
// full module: github.com/acme/shield (link in notes)
```
```

## Gate 9 — Single-gradient rule

**WHY:** Multiple gradients fight each other and date the deck instantly. Gradient body text fails contrast and exports as raster mush.

**HOW:** Search for `gradient` across CSS/Markdown. Count distinct gradient declarations. Verify none apply to text.

```bash
grep -rni "gradient" --include="*.css" --include="*.html" --include="*.md" . | tee gradients.txt | wc -l
```

**PASS:** Count ≤ 1. The single gradient is a hero background *or* one chart series. Zero `background-clip: text` hits.

**FAIL:** Purple-blue cover + teal CTA + sunset divider + gradient headline = 4 gradients. White text on mid-teal at 2.8:1.

**Fix:**
```css
/* allowed: one hero wash */
.hero { background: linear-gradient(180deg, #F1F5F9 0%, #FFFFFF 70%); }
/* banned: delete all of these */
/* background: linear-gradient(...) on h1, .card, .cta, .divider */
```

## Gate 10 — Reduced-motion fallback present

**WHY:** Vestibular disorders, migraines, and projector flicker make motion a health issue, not a preference. Every animation needs a static cut.

**HOW:** Enable DevTools Rendering → Emulate `prefers-reduced-motion: reduce`, then walk the deck. Confirm instant cuts, visible fragments, static parallax.

**PASS:** All Auto-Animate/Flip/transitions/`v-motion`/parallax/scroll timelines collapse to cuts; all fragments visible without clicks; no flashing over 3Hz anywhere.

**FAIL:** `v-motion` hero never appears under reduced motion (stuck at `opacity: 0`). Marp deck with no static build linked.

**Fix:**
```css
@media (prefers-reduced-motion: reduce) {
  .fragment { opacity: 1 !important; transform: none !important; }
  .reveal-on-scroll, .progress-rail { animation: none !important; opacity: 1 !important; }
}
```

```js
Reveal.initialize({ autoAnimate: !matchMedia('(prefers-reduced-motion: reduce)').matches });
```

## Gate 11 — Speaker notes coverage (every slide)

**WHY:** Notes are the talk. A slide without notes is a slide the speaker will improvise — and ramble.

**HOW:** Count slides vs notes. reveal.js: `<aside class="notes">` per section. Slidev: `<!-- -->` per page. Marp: presenter comment convention per project.

**PASS:** Notes-to-slides ratio 1:1 (appendix exempt only if marked `NO-NOTES`). Each note holds: the one sentence to say, the transition line to the next slide, and any stat provenance.

**FAIL:** 18 slides, 6 notes. Title slide note says “intro myself” with no name/title/timecheck.

**Fix:**
```html
<aside class="notes">Say: p95 fell 41% in six weeks. Then: but July was ugly — next slide. Timecheck: 2:00.</aside>
```

## Gate 12 — Keyboard works

**WHY:** Clickers send keyboard events. If arrows/Space/PageUp/PageDown fail, the speaker is stranded.

**HOW:** Unplug the mouse. Navigate fully by keyboard: Right/Space forward, Left back, Home first, End last. Confirm visible focus on links/buttons.

**PASS:** All keys advance reliably; focus ring visible on every interactive element; no keyboard traps in iframes.

**FAIL:** Custom JS hijacks Space for video play — slides stop advancing. Focus invisible on dark backgrounds.

**Fix:**
```css
:focus-visible { outline: 3px solid var(--primary); outline-offset: 2px; }
```

## Gate 13 — Mobile swipe + 390px layout

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

## Gate 14 — Code highlights render

**WHY:** An unstyled gray block tells the audience the speaker does not care about code. Mismatched light/dark themes flashBang the room on toggle.

**HOW:** Toggle `.dark` (or Slidev/Marp theme). Confirm Shiki theme follows, highlighted lines match the narration, scroll intact.

**PASS:** Shiki dual themes (`vitesse-light/dark` or `github-light/dark`) track the mode toggle; zero gray blocks; discussed lines highlighted; no content hidden behind scroll without affordance.

**FAIL:** Light-mode code pasted as dark screenshot — glowing white box in a light deck. `{2-4}` highlight points at an import block.

**Fix:**
```js
const html = await codeToHtml(source, {
  lang: 'ts',
  themes: { light: 'github-light', dark: 'github-dark' }
});
```

## Gate 15 — Export smoke test (PDF + PPTX + HTML)

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

## Gate 16 — No console errors (Chromium + Firefox)

**WHY:** Console errors are the canary: 404 assets, blocked fonts, dead iframes. If the console is red, something the audience should see is missing.

**HOW:** Open DevTools console in Chromium and Firefox, walk every slide including appendix, watch Network for 404s.

**PASS:** Zero errors, zero 404s for assets/fonts/iframes. Warnings documented or fixed.

**FAIL:** `GET assets/chart-v2.png 404`, `Refused to display iframe (X-Frame-Options)`, `Shiki language 'tsx2' not found`.

**Fix:** Commit the missing asset under `assets/`, replace frame-blocked demos with screenshots + links, correct the language tag to `tsx`.

---

## Pre-ship run (15 minutes, in order)

1. Outline + sources (Gates 1–2) — 2 min
2. Greps: placeholders, gradients, fonts (`grep` Gates 6, 9, 7) — 2 min
3. Images + alt + sizes (Gates 3–4) — 3 min
4. Contrast trio (Gate 5) — 2 min
5. Reduced motion + keyboard + mobile (Gates 10, 12–13) — 3 min
6. Notes + code + exports + console (Gates 11, 14–16) — 3 min
7. Fill the ship record at the top. Sign it. Then present.
