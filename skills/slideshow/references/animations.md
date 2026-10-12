# Animations — Continuity Anchors First, One Transition, Fragments, Motion Systems

> Golden rule: prefer `transform` + `opacity` only. Anything that animates `width`, `height`, `top`, `left`, `font-size`, or `margin` forces layout and will jank on projectors and low-end laptops. The global reduced-motion rule in base CSS covers every technique below. No exceptions.

Default motion model is continuity-anchors + `trans=none`. Transition effects are the secondary layer. Lock 2 anchors per section, move ONE per step, 1–2 BIG beats 3 small. This file gives mechanics; the grammar lives in `references/pptx-motion-language.md`. Readers arriving from `workflows/generate-deck.md` step 9 need BOTH this file and `references/pptx-motion-language.md`.

One page per slide. Always. Export paths (PDF/PPTX) freeze frame one — every slide must read static.

Base CSS every deck should ship (paste once). This is the ONLY reduced-motion fallback — all per-section snippets defer to it:

```css
:root {
  --ease-out: cubic-bezier(.2,.7,.2,1);
  --ease-in-out: cubic-bezier(.65,0,.35,1);
  --dur-fast: 200ms;
  --dur-med: 400ms;
  --dur-slow: 600ms;
}
.no-layout-anim { transition-property: transform, opacity; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
  .fragment { opacity: 1 !important; transform: none !important; visibility: visible !important; }
  ::view-transition-group(*),
  ::view-transition-old(*),
  ::view-transition-new(*) { animation: none !important; }
  .reveal-on-scroll, .progress-rail { animation: none !important; opacity: 1 !important; transform: none !important; }
}
```

```js
const prefersReduced = () =>
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;
```

---

## 1. Continuity anchors — the default grammar

### What it is
Two BIG elements repeat across adjacent slides in the same position (headline block, accent shape, photo frame, stat strip). Change position or size of ONE anchor per step, never both at once. The audience tracks the object instead of re-scanning. This beats any transition catalog — the five liked decks ship `trans=none` and still feel modern because anchors are large (138pt headline, full-bleed photo).

Rule: 2 anchors per section, move ONE per step, 1–2 BIG beats 3 small.

Three mechanisms implement the same idea:
- `data-id` in reveal.js Auto-Animate (declarative, adjacent slides)
- `view-transition-name` in the View Transitions API (browser-native snapshot)
- `data-flip-id` in GSAP Flip (imperative, full control)

Names must be unique per deck. `hero` may appear on exactly two adjacent slides as a morph pair. Never reuse `hero` for three different concepts.

### REQUIRED — 1–3 morph pairs per deck (ship-blocker)

Every deck MUST ship 1–3 morph pairs on element continuations. A morph pair is one element continued across two adjacent slides via one of: `data-auto-animate` + `data-id` (reveal.js), `view-transition-name` (View Transitions API / Slidev `transition: view-transition`), paired `v-motion` enter states on the same element across adjacent Slidev slides, or GSAP Flip `data-flip-id`. Deck-wide single transition alone (`slide-left`, `fade 0.4s`, or any one default with zero pairs above) FAILs review — it is chrome motion, not element continuity. Rules: never morph body copy (headlines, KPIs, bars, cards, images only), never morph across a section boundary (new section = hard cut + new title slide), max 3 simultaneously morphing elements per pair. Review check: list each pair as `slides N→N+1 : mechanism + element (e.g. slides 2→3 : data-id hero-bar)`; zero pairs = REQUEST_CHANGES.

### Stagger is the entrance grammar (pointer only)

Entrances stagger in reading order (kicker → headline → body → visual), max 3 per slide, 100–150ms apart, `rise` 200–400ms, total ≤600ms — and a `v-click` chain IS the stagger, never run both (Gate 8 budget binds). CSS lives in `references/pptx-motion-language.md` §3 — use it verbatim, not duplicated here.

### WHEN to use
- Title continuity: `Acme Metrics` becomes `Acme Metrics: Q3`.
- Bar / number growth: bar 120px to 320px via `scaleX`, KPI `$1.8M` to `$2.4M`.
- Image expansion: thumbnail grid to full-bleed detail.
- Card repositioning: 4-card overview collapses to 1 focused card.

### WHEN to avoid
- Do not morph body paragraphs, decorative gradients, or backgrounds. Morph *content*, cut *chrome*.
- Do not morph more than 3 elements at once or across a section boundary.

### Copy-paste: reveal.js morph pair

```html
<!-- slide 1 -->
<section data-auto-animate>
  <h2 data-id="hero-title">Acme Metrics</h2>
  <div data-id="hero-bar" style="width:120px;height:24px;background:#2563EB;border-radius:8px"></div>
</section>
<!-- slide 2 (adjacent) -->
<section data-auto-animate>
  <h2 data-id="hero-title">Acme Metrics: Q3</h2>
  <div data-id="hero-bar" style="width:320px;height:24px;background:#2563EB;border-radius:8px"></div>
</section>
```

### Copy-paste: View Transitions morph

```css
.hero-card { view-transition-name: hero-card; }
.chart-title { view-transition-name: chart-title; }
```

```js
function goToSlide(nextIndex) {
  if (document.startViewTransition && !prefersReduced()) {
    document.startViewTransition(() => showSlide(nextIndex));
  } else {
    showSlide(nextIndex);
  }
}
```

### Copy-paste: GSAP Flip morph

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/Flip.min.js"></script>
<div data-flip-id="hero" class="card">Acme Metrics</div>
```

```js
gsap.registerPlugin(Flip);
function morphToNext() {
  if (prefersReduced()) { goToSlide(next); return; }
  const state = Flip.getState('[data-flip-id="hero"]');
  goToSlide(next);
  Flip.from(state, { duration: 0.55, ease: 'power2.out', absolute: true, scale: true });
}
```

### Engine matrix (single — applies deck-wide)

| Engine | Morph | Step build | Slide flight |
|---|---|---|---|
| reveal.js | `data-auto-animate` + `data-id` | `fragment` | `transition: fade`, `data-transition` override |
| Slidev | `v-motion` pair / `transition: view-transition` | `v-click` / `v-after` | frontmatter `transition: slide-left` |
| Marp | duplicate static at two sizes (no true morph) | split slides (no fragments) | `transition: fade 0.4s`, `<!-- _transition: ... -->` override, `--bespoke.transition` build |

### Performance notes
- Transform-only path holds 60fps. Animate `scaleX` on a fixed-width bar, never `width`.
- Keep morph 350–600ms. `will-change: transform` on the pair only, removed after.
- Cap slide DOM under ~1500 nodes; full-screen 4K snapshots hitch on weak GPUs.

---

## 2. reveal.js Auto-Animate HOW

Add `data-auto-animate` to two adjacent `<section>` elements. Children sharing `data-id` interpolate position, scale, rotation, opacity, background-color. Unmatched children fade in/out.

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@6.0.0/dist/reveal.css" />
<script src="https://cdn.jsdelivr.net/npm/reveal.js@6.0.0/dist/reveal.js"></script>
<div class="reveal"><div class="slides">
  <section data-auto-animate>
    <h2 data-id="title">Pipeline</h2>
    <div data-id="bar" style="width:120px;height:24px;background:#2563EB;border-radius:6px"></div>
    <p data-id="caption">Build: 4m 12s</p>
  </section>
  <section data-auto-animate>
    <h2 data-id="title">Pipeline: deployed</h2>
    <div data-id="bar" style="width:320px;height:24px;background:#16A34A;border-radius:6px"></div>
    <p data-id="caption">Build: 1m 48s — cache hit</p>
  </section>
</div></div>
<script>
  Reveal.initialize({ autoAnimate: !prefersReduced(), hash: true });
</script>
```

Keep each auto-animated slide under ~40 animated nodes. No `box-shadow` interpolation — fade shadow in after. Slidev equivalent is manual `v-motion` choreography; Marp has none (use static pair).

---

## 3. FLIP primitive (pointer — do not hand-roll)

Use §4 `flipSlideChange` for slide-to-slide moves, reveal.js Auto-Animate for adjacent-slide morph, or Slidev `v-motion` for entrances. Hand-rolled First/Last/Invert/Play is only for single-element custom-HTML interactions (grid filter, thumbnail-to-lightbox) via `getBoundingClientRect` + `element.animate` with `transform`. Multi-element choreography belongs in GSAP Flip. Full pattern retired to keep this file lean — see §4.

---

## 4. GSAP Flip — slide-to-slide variant only

```js
function flipSlideChange(showNext) {
  if (prefersReduced()) { showNext(); return; }
  const state = Flip.getState('[data-flip-id]');
  showNext();
  Flip.from(state, { duration: 0.55, ease: 'power3.out', absolute: true, scale: true });
}
```

Cap stagger at 0.05s per item when reflowing grids. Kill in-flight tweens with `Flip.killFlipsOf(targets)`. Skip GSAP for single fades (plain CSS) and for static-export decks (PDF/PPTX freezes frame one). Reduced motion defers to the global base-CSS rule.

---

## 5. View Transitions API HOW

Browser-native morph with zero dependencies. Chromium 111+, Safari 18+, Firefox 125+ — design slides to read if transitions vanish.

```css
.slide-title { view-transition-name: slide-title; }
::view-transition-old(slide-title),
::view-transition-new(slide-title) {
  animation-duration: 450ms;
  animation-timing-function: cubic-bezier(.2,.7,.2,1);
}
```

```js
function go(i) {
  if (document.startViewTransition && !prefersReduced()) {
    document.startViewTransition(() => showSlide(i));
  } else { showSlide(i); }
}
```

Unique `view-transition-name` per live element — duplicates cancel silently. Debounce to one transition per 300ms; await `transition.finished` before the next. In Slidev prefer `transition: view-transition` frontmatter over manual calls. In reveal.js prefer Auto-Animate. Marp skips this API.

---

## 6. One transition deck-wide (replaces catalogs)

Lock ONE transition at style-lock time and use it everywhere. Spend the budget on anchors + entrances instead.

- reveal.js: `Reveal.initialize({ transition: 'fade', transitionSpeed: 'fast', backgroundTransition: 'fade' })`
- Slidev: `transition: slide-left` (or `transition: view-transition` on morph chapters)
- Marp: `transition: fade 0.4s` + `--bespoke.transition` build (`npx marp --bespoke.transition deck.md -o deck.html`)
- Custom HTML: View Transitions router from §5

Overrides allowed: exactly ONE `zoom` showcase for the money slide + ONE `none` appendix. Nothing else.

```markdown
---
marp: true
theme: default
transition: fade 0.4s
paginate: true
---
# Acme Metrics
Q2 baseline — three signals to watch
---
<!-- _transition: cover-left 0.5s -->
# Pipeline: deployed
Build time 4m 12s becomes 1m 48s
---
<!-- _transition: none -->
# Appendix: raw numbers
Static table — prints cleanly
```

```html
<section data-transition="zoom">The one money slide</section>
<section data-transition="none">Appendix — static</section>
```

Fragment Budget caps apply here too — Gate 8 is the numeric authority (full block in §7). Marp reduced-motion build is `transition: none` in frontmatter plus a linked `./deck-static.html`. Slidev reduced-motion build is `transition: none` with all `v-click` steps visible.

---

## 7. Fragments + v-click — recommended subset only

Fragments reveal parts of one slide without changing slides. Slidev `v-click` is the same idea. Marp has none — split into separate slides.

HARD CAP — Fragment Budget (Gate 8 is the numeric authority): ≤5-per-slide for `v-click` + `v-after` combined; max 1 click-built slide per 3 slides; tables reveal by row or ship static. Anti-example: the 20-click-table (Acme Q3 metrics table that shipped 20 cell-by-cell `v-click` steps, 53 clicks across 8 slides) — split it into two slides or collapse to 3 row reveals, never per-cell.

Recommended classes only: `fade-up` for builds, `grow` for the headline number, `highlight-current-blue` for focus. Full 16-variant catalog retired — these three cover every liked deck.

```html
<section>
  <h2>Launch checklist</h2>
  <p class="fragment fade-up">Edge cache enabled</p>
  <p class="fragment fade-up">Origin shield added</p>
  <p class="fragment grow">NRR 128% — the headline</p>
  <p class="fragment highlight-current-blue">Current focus</p>
</section>
```

```markdown
<div v-click>Step 1 — edge cache hit</div>
<div v-click>Step 2 — origin shield added</div>
<div v-click="3">Step 3 — p95 down 41%</div>
<div v-motion :initial="{ x: -80, opacity: 0 }" :enter="{ x: 0, opacity: 1 }">Hero callout — flies in once</div>
```

```html
<p class="fragment fade-up" data-fragment-index="1">Second — parallel</p>
<p class="fragment fade-up" data-fragment-index="1">Also second — same index</p>
<pre><code data-line-numbers="1|2-3|4">const cache = new EdgeCache();
cache.enableShield();
deploy({ rollback: true });</code></pre>
```

Rules: same `data-fragment-index` means parallel; omit for document-order sequence. One fragment equals one line or one visual, never a wall of text. Cap `v-motion` at 6 concurrent motions; cap code at 12 lines under `view-transition`. Remove all `v-drag` before shipping (rehearsal positioning only). Fragments inside Auto-Animate slides compose but verify click-by-click forward and backward. Reduced motion defers to the global base-CSS rule (all fragments visible, no flight).

---

## 8. PPTX visual-motion tokens (compact — pointers, not tables)

Token values live in `references/colors.md` — do not duplicate here. Masks and grammar live in `references/pptx-motion-language.md` §§4–8 — use verbatim.

Scrim stops (text over photo): `linear-gradient(180deg, transparent 40%, rgba(0,0,0,.72))` on full-bleed; card variant `rgba(11,16,32,.72)` with `border-radius: 16px`. See `references/pptx-motion-language.md` §4.

```css
.arch-mask { width: 100%; height: 420px; object-fit: cover; border-radius: 210px 210px 16px 16px; }
.blob-mask { width: 320px; height: 320px; object-fit: cover; border-radius: 58% 42% 55% 45%/48% 55% 45% 52%; }
```

One mask per deck (arch OR blob OR circle). Plain rectangles only for full-bleed backgrounds and screenshots. Pastel rotation and dark showcase tokens per `references/colors.md`; pastel saturation stays under ~35% with near-black text, dark mode is `#000`–`#0A0A0A` with `#F5F5F7` body (Gate 15 binds composition; color-story authority is `references/colors.md`, rotation grammar is `references/pptx-motion-language.md` §§7–8).

Per-slide spec template (copy into `research-notes.md` slide sections per `references/pptx-motion-language.md` §9; Gate 15 is the format authority):

```markdown
## Slide 3 — Pipeline: deployed
Text runs: [kicker 14px mono / headline clamp(2.5rem,6vw,4.5rem) / body 1.1rem ≤25 words]
Z-order: bg photo → scrim → accent shape → headline → body → chip row
Entrances: [rise 300ms d100] headline, [rise 300ms d220] body (≤3, ≤600ms total)
Anchors: sec-title continues from slide 2 (data-id sec-title, position held, size +0)
Transition: none (deck default fade 0.4s)
```

---

## Appendix — scroll-story only, else skip

Scroll parallax and `animation-timeline: view()` / `scroll()` belong on single-page scroll-story pages, never inside paginated reveal.js / Slidev / Marp decks. One parallax zone per deck max, `translate3d` layers with `passive: true` + `requestAnimationFrame`, progress rail via `animation-timeline: scroll()`. Full patterns retired — if the deck paginates, skip this appendix entirely. Reduced motion defers to the global base-CSS rule.

---

## 9. Decision flowchart (prose)

Start at the top for every animated beat and walk down:

1. **Is this beat essential without motion?** If the slide is incomprehensible as a static image, redesign first. Motion is enhancement, never the carrier.
2. **Is it a continuation?** Yes means morph via §1 (Auto-Animate / View Transitions / `view-transition` frontmatter / Flip). Zero morph pairs FAILs review.
3. **Is it a stepwise build?** Yes means §7 fragments / `v-click` / split slides. Cap at 5 steps; Gate 8 binds.
4. **Is it a layout reflow?** Yes means §4 Flip. One element may use the §3 pointer pattern; many elements use GSAP.
5. **Is it a chapter change?** Yes means the §6 locked transition, one `zoom` per deck max, `none` for appendix. Novelty flights (`explode`, `shatter`, `blink`, `roll`) are banned in serious venues; `convex` / `concave` tilt nauseates past one use; durations over 0.8s waste 40 seconds across 40 slides.
6. **Is it atmosphere?** Only for scroll-story pages per the Appendix, never paginated decks, one zone max. No scrim means no parallax over text.
7. **Performance gate:** preload fonts (mid-morph swaps break interpolation), compress full-bleed backgrounds under 200KB at 1920px max, keep flights 200ms micro / 400ms standard / 600ms hero max.
8. **Finally: does reduced motion have a path?** Every yes above maps to the global base-CSS instant cut. If you cannot name the fallback, delete the animation.

Default stack per engine: reveal.js gets `fade` + Auto-Animate + fragments. Slidev gets `slide-left` + `view-transition` on morph chapters + `v-click`. Marp gets `fade 0.4s` deck-wide + two `_transition` overrides maximum. Custom HTML gets View Transitions router + Flip for interactions.

## 10. Common mistakes (and fixes)

1. **Morphing everything.** Six pairs per slide pair looks like soup. Fix: keep 1–3 morph pairs, rest cuts or fades.
2. **Duplicate morph names.** Two `view-transition-name: hero` elements cancel silently. Fix: unique names, lint with the audit snippet below.
3. **Animating `width` / `font-size`.** Fix: `transform: scaleX()` or Auto-Animate box interpolation; `opacity` for emphasis.
4. **A different transition per slide.** Fix: one deck default, one `zoom`, `none` for appendix.
5. **Untested fragment order.**
6. **Motion as meaning.** Fix: frame one and resting frame both communicate; PDF export is the test.
7. **Missing reduced-motion path.**
8. **Parallax over text without scrim.** Fix: 60–75% dark scrim + solid card behind text.
9. **Overlong durations.** Fix: 200ms micro, 400ms standard, 600ms hero max.
10. **Untested venue hardware.**

```js
// pre-ship motion audit: paste in console, fix any duplicates
const names = [...document.querySelectorAll('[data-id]')].map(e => e.dataset.id);
const dupes = names.filter((n, i) => names.indexOf(n) !== i);
console.log('duplicate data-id:', [...new Set(dupes)]);
console.log('fragment count:', document.querySelectorAll('.fragment').length);
console.log('reduced-motion respected:', window.matchMedia('(prefers-reduced-motion: reduce)').media);
```
