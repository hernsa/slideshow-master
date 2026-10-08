# Animations — Morph / FLIP / View Transitions / Fragments / Motion Systems

> Golden rule: prefer `transform` + `opacity` only. Anything that animates `width`, `height`, `top`, `left`, `font-size`, or `margin` forces layout and will jank on projectors and low-end laptops. Every technique below ends with its own reduced-motion fallback. No exceptions.

This guide covers the full motion system for slide decks: shared-element morph continuity, the FLIP primitive, GSAP Flip, the View Transitions API, reveal.js Auto-Animate + slide/background transitions + fragments + parallax, Marp transitions, Slidev transitions + `v-click` / `v-motion` / `v-drag`, and scroll-driven timelines. For each you get: what it is, when to use vs avoid, copy-paste code, per-engine notes, performance notes, and a reduced-motion fallback.

Base CSS every deck should ship (paste once):

```css
/* base motion tokens */
:root {
  --ease-out: cubic-bezier(.2,.7,.2,1);
  --ease-in-out: cubic-bezier(.65,0,.35,1);
  --dur-fast: 200ms;
  --dur-med: 400ms;
  --dur-slow: 600ms;
}
.slide *, .reveal *, .marp * {
  will-change: auto;
}
/* never animate these properties directly */
.no-layout-anim {
  transition-property: transform, opacity;
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

Reduced-motion detection helper used in every snippet below:

```js
const prefersReduced = () =>
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;
```

---

## 1. Morph continuity — the shared-element idea

### What it is
Morph continuity is the illusion that one element on slide N *becomes* the element on slide N+1. A headline grows, a card moves, a bar lengthens, a thumbnail expands into a hero image. The audience tracks the object instead of re-scanning the slide. It is the single highest-value animation in presentations.

Three concrete mechanisms implement the same idea:
- `data-id` in reveal.js Auto-Animate (declarative, adjacent slides)
- `view-transition-name` in the View Transitions API (browser-native snapshot morph)
- `data-flip-id` in GSAP Flip (imperative, full control)

Names must be unique per deck. `hero` may appear on exactly two adjacent slides as a morph pair. Never reuse `hero` for three different concepts.

### WHEN to use
- Title continuity: `Acme Metrics` becomes `Acme Metrics: Q3` so the audience knows this is the same story, next chapter.
- Bar / number growth: a bar from 120px to 320px, a KPI from `$1.8M` to `$2.4M`.
- Image expansion: thumbnail grid to full-bleed detail.
- Card repositioning: 4-card overview collapses to 1 focused card.

### WHEN to avoid
- Do not morph body paragraphs. Text reflow during morph is unreadable.
- Do not morph more than 3 elements at once. Five simultaneous morphs read as chaos.
- Do not morph across a section boundary. A new section deserves a hard cut + new title slide.
- Do not morph decorative gradients or backgrounds. Morph *content*, cut *chrome*.

### Copy-paste: reveal.js morph pair

```html
<!-- slide 1 -->
<section data-auto-animate>
  <h2 data-id="hero-title" style="font-size:2.4rem">Acme Metrics</h2>
  <p style="opacity:.7">Q2 baseline — three signals to watch</p>
  <div data-id="hero-bar" style="width:120px;height:24px;background:#2563EB;border-radius:8px"></div>
</section>

<!-- slide 2 (adjacent) -->
<section data-auto-animate>
  <h2 data-id="hero-title" style="font-size:2.4rem">Acme Metrics: Q3</h2>
  <p style="opacity:.7">Pipeline recovered after July deploy</p>
  <div data-id="hero-bar" style="width:320px;height:24px;background:#2563EB;border-radius:8px"></div>
</section>
```

### Copy-paste: View Transitions API morph

```css
.hero-card { view-transition-name: hero-card; }
.chart-title { view-transition-name: chart-title; }
```

```js
function goToSlide(nextIndex) {
  if (document.startViewTransition && !prefersReduced()) {
    document.startViewTransition(() => {
      showSlide(nextIndex); // your DOM swap: hide current, show next
    });
  } else {
    showSlide(nextIndex); // instant cut
  }
}
```

HTML on both slides keeps the same class so the browser can match snapshots:

```html
<!-- slide 1 -->
<h2 class="chart-title">Acme Metrics</h2>
<div class="hero-card">Q2 baseline</div>

<!-- slide 2 -->
<h2 class="chart-title">Acme Metrics: Q3</h2>
<div class="hero-card">Q3 recovery — NRR 128%</div>
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
  goToSlide(next); // swap slide DOM
  Flip.from(state, {
    duration: 0.55,
    ease: 'power2.out',
    absolute: true,
    scale: true
  });
}
```

### Per-engine notes
- **reveal.js:** native via `data-auto-animate` + `data-id`. Zero JS needed. Requires adjacent `<section>` elements.
- **Slidev:** use `v-motion` or View Transitions (`transition: view-transition`). `data-id` is not native.
- **Marp:** no true morph. Fake it with duplicate elements at two sizes, or export to reveal.js if morph is essential.
- **Plain HTML:** View Transitions API is the lightest dependency-free path. GSAP Flip when you need scale + absolute positioning control.

### Performance notes
- Transform-only path holds 60fps on integrated graphics. `translate` + `scale` + `opacity` are compositor-owned.
- Animating `width` from 120px to 320px forces layout per frame. Instead animate `transform: scaleX()` on a fixed-width bar, or let Auto-Animate interpolate the box via transforms.
- Keep morph duration 350–600ms. Under 250ms reads as a flicker. Over 800ms reads as lag.
- Limit morph to viewport-visible elements. `will-change: transform` on the morph pair only, removed after transition.

### Reduced-motion fallback
```js
if (prefersReduced()) {
  showSlide(next); // instant cut, no snapshot, no Flip
}
```
```css
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*),
  ::view-transition-old(*),
  ::view-transition-new(*) { animation: none !important; }
}
```

---

## 2. reveal.js Auto-Animate

### What it is
Auto-Animate is reveal.js declarative morph. Add `data-auto-animate` to two adjacent `<section>` elements. Any children sharing the same `data-id` interpolate automatically — position, scale, rotation, opacity, background-color.

### WHEN to use
- Pipeline diagrams: step 1 highlights, step 2 adds a node, step 3 connects edges.
- Bar / line charts growing between quarters.
- Code diffs: same file, 3 lines added, context lines carry `data-id` so they stay pinned.
- Architecture zooms: overview boxes scale into detail view.

### WHEN to avoid
- Non-adjacent slides. Auto-Animate only works on neighbors. Duplicating a slide to force adjacency confuses the slide counter.
- Lists longer than 6 items. Per-bullet Auto-Animate stutters; use fragments instead.
- Footers / logos with `data-id` on every slide. A global chrome element should not morph; leave it static.

### Full copy-paste code block

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@6.0.0/dist/reveal.css" />
<script src="https://cdn.jsdelivr.net/npm/reveal.js@6.0.0/dist/reveal.js"></script>

<div class="reveal">
  <div class="slides">
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
  </div>
</div>

<script>
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  Reveal.initialize({ autoAnimate: !reduce, hash: true });
</script>
```

Auto-Animate with unmatched elements (fade in/out around the morph):

```html
<section data-auto-animate>
  <h2 data-id="t">Cache layers</h2>
  <ul>
    <li>Edge cache</li>
  </ul>
</section>
<section data-auto-animate>
  <h2 data-id="t">Cache layers</h2>
  <ul>
    <li>Edge cache</li>
    <li>Origin shield (new — fades in, no data-id needed)</li>
  </ul>
</section>
```

### Per-engine notes
- **reveal.js only.** This exact API does not exist in Slidev or Marp.
- **Slidev equivalent:** `transition: slide-left` + `v-motion` entrances. Not automatic; you choreograph each step.
- **Marp equivalent:** none. Use discrete slides with a static bar at two widths.

### Performance notes
- reveal.js Auto-Animate clones nodes and interpolates with WAAPI. Keep each auto-animated slide under ~40 animated nodes.
- Avoid `box-shadow` animation. Shadow interpolation is paint-heavy. Animate the box, then fade the shadow in after.
- Preload fonts. A webfont swapping mid-morph changes text metrics and breaks the interpolation.

### Reduced-motion fallback snippet
```js
Reveal.initialize({
  autoAnimate: !window.matchMedia('(prefers-reduced-motion: reduce)').matches
});
```
```html
<!-- per-deck escape hatch: force one pair to cut -->
<section data-auto-animate="false">
  <h2>Static fallback slide</h2>
</section>
```

---

## 3. FLIP primitive (no library)

### What it is
FLIP stands for First, Last, Invert, Play. Measure the element (First), apply the new layout (Last), compute the delta (Invert), then animate the delta away (Play). It converts any layout change into a transform animation. This is the physics underneath GSAP Flip and Auto-Animate.

### WHEN to use
- Custom HTML decks with no framework where you still want one smooth move.
- Filtering a grid: 8 cards to 3 cards, survivors glide to new slots.
- Expanding a thumbnail into a lightbox without a library.
- Teaching demos: showing the team how morph actually works.

### WHEN to avoid
- Multi-element choreography. Hand-rolled FLIP for 6 elements is 60 lines of bookkeeping; use GSAP Flip instead.
- Text-heavy morphs. FLIP on paragraphs causes glyph swimming.
- When View Transitions API is available and sufficient. Native snapshots are 5 lines vs 20.

### Full copy-paste code block

```html
<style>
  .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
  .card { background: #F1F5F9; border-radius: 12px; padding: 20px; }
  .grid.focus .card.dim { opacity: .3; }
  .grid.focus .card.hero { grid-column: span 2; background: #DBEAFE; }
</style>

<div class="grid" id="grid">
  <div class="card hero" id="hero">Hero metric — $2.4M ARR</div>
  <div class="card">NPS 72</div>
  <div class="card">Churn 1.1%</div>
</div>
<button id="toggle">Focus hero</button>

<script>
  const grid = document.getElementById('grid');
  const hero = document.getElementById('hero');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.getElementById('toggle').addEventListener('click', () => {
    if (reduce) { grid.classList.toggle('focus'); return; }
    const first = hero.getBoundingClientRect();
    grid.classList.toggle('focus');
    const last = hero.getBoundingClientRect();
    const dx = first.left - last.left;
    const dy = first.top - last.top;
    const sx = first.width / last.width;
    const sy = first.height / last.height;
    hero.animate(
      [
        { transform: `translate(${dx}px, ${dy}px) scale(${sx}, ${sy})` },
        { transform: 'none' }
      ],
      { duration: 420, easing: 'cubic-bezier(.2,.7,.2,1)' }
    );
  });
</script>
```

### Per-engine notes
- **Any engine.** This is vanilla DOM + Web Animations API. Drop it into reveal.js `slidechanged` handlers, Slidev `<script setup>`, or plain HTML.
- **reveal.js:** call FLIP inside `Reveal.on('slidechanged', ...)` after the new slide is visible.
- **Slidev:** prefer `v-motion`; use raw FLIP only for grid-filter interactions inside a component.

### Performance notes
- Read (`getBoundingClientRect`) then write (class toggle) then read again. Never interleave reads and writes in a loop — batch them or force synchronous layout.
- Animate the single hero element, not every card. One FLIP is 60fps; eight simultaneous FLIPs on mobile Safari drops frames.
- `scale()` on text blurs glyphs mid-flight. Acceptable for 400ms; for longer flights crossfade text separately.

### Reduced-motion fallback snippet
```js
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  grid.classList.toggle('focus'); // layout change only, no .animate()
} else {
  // FLIP path above
}
```

---

## 4. GSAP Flip plugin

### What it is
GSAP Flip automates FLIP for one or many targets: capture state, mutate DOM, animate from captured state. Adds `absolute: true` (pulls elements out of flow during flight), `scale`, `nested`, and stagger support.

### WHEN to use
- Grid reflow with 4–12 cards.
- Shared-element slide transitions in custom decks where View Transitions support is spotty.
- Staggered entrances tied to layout (cards land in order).
- Any FLIP involving both position and size change plus sibling reflow.

### WHEN to avoid
- Single-element fades. Plain CSS is lighter than a 70KB GSAP payload.
- Marp / static-export decks. GSAP needs a live runtime; exported PDF/PPTX freezes frame one.
- When the audience has motion sensitivity and you cannot test the fallback. GSAP animates unless you gate it.

### Full copy-paste code block

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/Flip.min.js"></script>

<style>
  .deck { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
  .tile { background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 12px; padding: 18px; }
</style>

<div class="deck" id="deck">
  <div class="tile" data-flip-id="a">ARR $2.4M</div>
  <div class="tile" data-flip-id="b">NPS 72</div>
  <div class="tile" data-flip-id="c">Churn 1.1%</div>
  <div class="tile" data-flip-id="d">NRR 128%</div>
</div>

<script>
  gsap.registerPlugin(Flip);
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function reorder() {
    if (reduce) { shuffleDOM(); return; }
    const state = Flip.getState('.tile');
    shuffleDOM(); // your reorder / filter / class change
    Flip.from(state, {
      duration: 0.5,
      ease: 'power2.out',
      absolute: true,
      stagger: 0.03,
      onEnter: els => gsap.fromTo(els, { opacity: 0 }, { opacity: 1, duration: 0.3 }),
      onLeave: els => gsap.to(els, { opacity: 0, duration: 0.25 })
    });
  }
  function shuffleDOM() {
    const deck = document.getElementById('deck');
    deck.appendChild(deck.firstElementChild); // demo rotation
  }
</script>
```

Slide-to-slide Flip variant:

```js
function flipSlideChange(showNext) {
  const state = Flip.getState('[data-flip-id]');
  showNext();
  Flip.from(state, { duration: 0.55, ease: 'power3.out', absolute: true, scale: true });
}
```

### Per-engine notes
- **Custom / reveal.js:** best fit. Load via CDN, call inside slide-change handlers.
- **Slidev:** possible inside `<script setup>` but fights with Vue reactivity. Prefer `v-motion` unless you need true reflow.
- **Marp:** not applicable at runtime (Marp renders static HTML per slide).

### Performance notes
- `absolute: true` prevents sibling jitter but causes overlap during flight. Keep flight under 600ms.
- Cap `stagger` at 0.05s per item. A 12-item stagger at 0.08s adds a full second of motion.
- Kill in-flight tweens before starting new ones: `Flip.killFlipsOf(targets)`.

### Reduced-motion fallback snippet
```js
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  shuffleDOM(); // no Flip.from()
} else {
  const state = Flip.getState('.tile');
  shuffleDOM();
  Flip.from(state, { duration: 0.5, ease: 'power2.out' });
}
```

---

## 5. View Transitions API

### What it is
Browser-native slide morph. `document.startViewTransition(callback)` snapshots old DOM, runs the callback, snapshots new DOM, then crossfades/morphs elements sharing a `view-transition-name`. No library. Chromium 111+, Safari 18+, Firefox 125+ (check current support before relying on it live).

### WHEN to use
- Custom HTML decks where you want morph with zero dependencies.
- SPA slide routers (one page, JS swaps sections).
- Hero-card persistence across slides.
- Crossfade + slight scale on slide change without per-element choreography.

### WHEN to avoid
- Live talks on unknown hardware. If the venue laptop runs an old Chromium, transitions silently vanish (which is fine) — but do not *depend* on them for meaning.
- PDF / PPTX export paths. Snapshots do not export; design slides to read statically.
- Rapid-fire advancement. Spamming `startViewTransition` queues snapshots and lags. Debounce to one transition per 300ms.

### Full copy-paste code block

```css
/* name the persistent elements */
.slide-title { view-transition-name: slide-title; }
.hero-visual { view-transition-name: hero-visual; }

/* customize the flight */
::view-transition-old(slide-title),
::view-transition-new(slide-title) {
  animation-duration: 450ms;
  animation-timing-function: cubic-bezier(.2,.7,.2,1);
}
::view-transition-group(hero-visual) {
  animation-duration: 500ms;
}
```

```js
let current = 0;
const slides = [...document.querySelectorAll('.slide')];

function showSlide(i) {
  slides[current].hidden = true;
  slides[i].hidden = false;
  current = i;
}

function go(i) {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (document.startViewTransition && !reduce) {
    document.startViewTransition(() => showSlide(i));
  } else {
    showSlide(i);
  }
}
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight') go(Math.min(current + 1, slides.length - 1));
  if (e.key === 'ArrowLeft') go(Math.max(current - 1, 0));
});
```

### Per-engine notes
- **Custom HTML:** first-class. This API was built for exactly this router pattern.
- **reveal.js:** possible but redundant — Auto-Animate already covers morph. Use View Transitions only for cross-slide chrome (progress bar, footer).
- **Slidev:** `transition: view-transition` uses this API under the hood. Prefer the frontmatter flag over manual calls.
- **Marp:** no runtime router, so no snapshots. Skip.

### Performance notes
- Snapshot cost scales with viewport pixels. Full-screen 4K snapshots on weak GPUs hitch. Keep slide DOM under ~1500 nodes.
- `view-transition-name` must be unique per live element. Duplicates cancel the morph silently — lint for duplicates in CI.
- Do not nest `startViewTransition` calls. Await `transition.finished` before starting the next.

### Reduced-motion fallback snippet
```js
function goSafe(i) {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    showSlide(i); return;
  }
  return document.startViewTransition
    ? document.startViewTransition(() => showSlide(i))
    : showSlide(i);
}
```

---

## 6. Marp transitions (33 built-ins + per-slide override)

### What it is
Marp supports deck-level `transition` frontmatter plus per-slide `_transition` HTML-comment overrides. Values follow the `name duration` pattern (e.g. `fade 0.5s`, `cover-left 0.6s`). The full catalog is 33 keywords: `none`, `fade`, `cover-left`, `cover-right`, `cover-up`, `cover-down`, `reveal-left`, `reveal-right`, `reveal-up`, `reveal-down`, `push-left`, `push-right`, `push-up`, `push-down`, `wipe-left`, `wipe-right`, `wipe-up`, `wipe-down`, `slide-left`, `slide-right`, `slide-up`, `slide-down`, `zoom-in`, `zoom-out`, `rotate`, `flip-horizontal`, `flip-vertical`, `cube`, `dissolve`, `blink`, `shatter`, `roll`, `explode`. Requires the bespoke HTML template and Chromium 110+; elsewhere the deck cuts instantly (which is the correct fallback).

### WHEN to use
- `fade 0.4s` as the deck default. Invisible, professional, never distracts.
- `cover-left` / `push-left` for forward narrative momentum (chapter advances).
- `reveal-up` for data-story builds (chart rises into view).
- `zoom-in` exactly once per deck for the single most important reveal.

### WHEN to avoid
- A different transition per slide. Twelve flavors reads as a 2003 PowerPoint demo.
- `explode`, `shatter`, `blink`, `roll` in any serious venue. They are novelty effects; they undermine credibility.
- `rotate` / `cube` / `flip-*` on text-heavy slides. 3D flights blur glyphs and tire eyes.
- Durations over 0.8s. The audience waits on every transition; 40 slides at 1s wastes 40 seconds.

### Full copy-paste code block

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

Static table — no motion, prints cleanly
```

Duration + per-slide timing comment variant:

```markdown
<!-- _transition: wipe-up 0.6s -->
```

### Per-engine notes
- **Marp only.** The `transition` frontmatter key and `_transition` comment are Marp directives. reveal.js and Slidev ignore them.
- **Export caveat:** PPTX export drops all transitions (static cuts). HTML export preserves them in Chromium.
- **Bespoke template required:** `npx marp --bespoke.transition deck.md -o deck.html`. The default template ignores transitions.

### Performance notes
- Marp transitions are CSS snapshot flights rendered by the bespoke template. Keep slides GPU-light: no full-bleed video under a transition.
- Chromium 110+ only. Test in the exact venue browser; Safari and Firefox cut instantly.
- One transition per slide change. Chained rapid advances cancel in-flight transitions cleanly — no action needed.

### Reduced-motion fallback snippet

```markdown
---
marp: true
theme: default
transition: none
---

# Reduced-motion build (link from slide 1 of main deck)
```

```html
<!-- link on the title slide of the full-motion deck -->
<a href="./deck-static.html">Reduced-motion version (no transitions)</a>
```

---

## 7. Slidev transitions + v-click + v-motion + v-drag

### What it is
Slidev layers four systems: deck/frontmatter `transition` (slide-to-slide flight), `v-click` (click-step reveals), `v-motion` (directed entrances via Motion One), and `v-drag` (draggable elements in dev/present mode).

### WHEN to use
- `transition: slide-left` as the deck default for left-to-right narrative.
- `transition: view-transition` when you want morph-like continuity with one flag.
- `v-click` for stepwise list builds (3 bullets, 3 clicks).
- `v-motion` for one hero entrance per deck (title flies in once, then stays static).
- `v-drag` during rehearsal to position annotations, then lock positions before shipping.

### WHEN to avoid
- `v-motion` on every element. Ten flying entrances exhaust the audience by slide 4.
- `v-click` chains longer than 5 steps. Split into two slides instead.
- `v-drag` in the shipped deck. It invites fiddling during Q&A and breaks PDF export layout.
- Mixing `transition: slide-left` with heavy `v-motion` on the same slide. Two simultaneous flights collide.

### Full copy-paste code block

```markdown
---
theme: default
transition: slide-left
mdc: true
---

# Acme Metrics

Q2 baseline

---
transition: view-transition
---

# Pipeline: deployed

<div v-click>Step 1 — edge cache hit</div>
<div v-click>Step 2 — origin shield added</div>
<div v-click="3">Step 3 — p95 down 41%</div>

<div v-motion :initial="{ x: -80, opacity: 0 }" :enter="{ x: 0, opacity: 1 }" :transition="{ duration: 450 }">
  Hero callout — flies in once
</div>

<div v-drag="[120, 200, 320, 140]" class="px-4 py-2 rounded-xl bg-blue-100 border border-blue-300">
  Draggable note (rehearsal only)
</div>
```

Click-step with hidden-until-clicked variant:

```html
<span v-click.hide>Revealed on click, hides again on back-nav</span>
<div v-after>Appears after all v-clicks resolve</div>
```

### Per-engine notes
- **Slidev only.** `v-click`, `v-motion`, `v-drag` are Slidev directives. They do not exist in reveal.js or Marp.
- **reveal.js equivalent:** fragments (`class="fragment"`).
- **Marp equivalent:** none — split click-steps into separate slides.

### Performance notes
- `v-motion` runs on Motion One (WAAPI-backed). Keep concurrent motions under 6 per slide.
- `view-transition` in Slidev snapshots the whole slide. Large code blocks + snapshots can hitch on 4K; cap code at 12 lines.
- `v-drag` adds pointer listeners per element. Remove all `v-drag` before export — they bloat the shipped bundle.

### Reduced-motion fallback snippet

```markdown
---
transition: none
---

# Static build

<div>Step 1 — edge cache hit (all steps visible, no clicks)</div>
<div>Step 2 — origin shield added</div>
<div>Step 3 — p95 down 41%</div>
```

```html
<!-- replace v-motion with static content when reduced motion is set -->
<div v-if="!$slidev.configs.reducedMotion">Motion hero</div>
<div v-else>Static hero (same text, no flight)</div>
```

---

## 8. reveal.js slide transitions + background transitions

### What it is
reveal.js separates *slide* transitions (`transition: fade | slide | convex | concave | zoom`) from *background* transitions (`backgroundTransition: fade | slide | convex | concave | zoom`). Backgrounds can crossfade while content slides, or vice versa. Per-slide override via `data-transition` and `data-background-transition`.

### WHEN to use
- Deck default `transition: 'fade'` + `backgroundTransition: 'fade'`. Calm, consistent.
- `data-transition="zoom"` exactly once for the money slide.
- `data-transition="none"` for appendix / backup slides (instant, printable).
- Differing background transition when the background is a full-bleed image and content is text: background fades, content slides.

### WHEN to avoid
- `convex` / `concave` as defaults. They are 3D tilts; charming once, nauseating forty times.
- `zoom` on code slides. Zooming monospaced text shimmers.
- Per-slide transitions on more than 20% of slides. Consistency beats variety.

### Full copy-paste code block

```html
<script>
  Reveal.initialize({
    transition: 'fade',
    transitionSpeed: 'fast', // fast | default | slow
    backgroundTransition: 'fade'
  });
</script>

<!-- per-slide overrides -->
<section data-transition="slide">Forward momentum chapter</section>
<section data-transition="zoom">The one money slide</section>
<section data-transition="none">Appendix — static</section>
<section
  data-background-image="lab.jpg"
  data-background-transition="fade">
  <h2>Background fades, text stays crisp</h2>
</section>
```

Speed tokens: `fast` is ~300ms, `default` ~500ms, `slow` ~800ms. Ship `fast` for 30+ slide decks.

### Per-engine notes
- **reveal.js only.** Slidev uses frontmatter `transition:` names; Marp uses `transition:` + `_transition:` comments.
- **Export:** `?print-pdf` flattens all transitions to static pages. Design each slide to read without motion.

### Performance notes
- `fade` is opacity-only — cheapest. `slide` is transform-only — cheap. `convex`/`concave`/`zoom` involve perspective + scale — heavier on integrated GPUs.
- Full-bleed `data-background-image` over 250KB JPEGs hitches during `slide` flights. Compress backgrounds to under 200KB, `1920px` max width.
- `transitionSpeed: 'fast'` saves ~8 seconds across a 40-slide deck vs `slow`.

### Reduced-motion fallback snippet
```js
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
Reveal.initialize({
  transition: reduce ? 'none' : 'fade',
  backgroundTransition: reduce ? 'none' : 'fade'
});
```

---

## 9. Fragments — reveal.js staged reveals

### What it is
Fragments reveal parts of one slide in steps without changing slides. Every `.fragment` advances on click / space / arrow. Variants control entrance style; `data-fragment-index` controls ordering and parallelism.

### WHEN to use
- 3-bullet builds: one idea per click, audience stays with you.
- Chart annotation: axes first, bars second, callout third.
- Code walkthroughs: highlight line 1, then line 2, then the fix.
- Parallel reveals: two stats appear together on the same click.

### WHEN to avoid
- More than 5 fragment steps per slide. Split the slide.
- Fragments inside Auto-Animate slides without testing. The two systems compose but ordering gets subtle — verify click-by-click.
- Using fragments for entire paragraphs. One fragment equals one line or one visual, never a wall of text.

### Full copy-paste code block (all variants)

```html
<section>
  <h2>Launch checklist</h2>
  <p class="fragment fade-up">Edge cache enabled</p>
  <p class="fragment fade-up">Origin shield added</p>
  <p class="fragment highlight-red">p95 still red — needs work</p>
  <p class="fragment grow">NRR 128% — the headline</p>
  <p class="fragment shrink">Old runbook (shrinks away)</p>
  <p class="fragment strike">Deploys on Fridays</p>
  <p class="fragment highlight-current-blue">Current focus</p>
</section>
```

Fragment style catalog (append to `class="fragment ..."`):
`fade-in`, `fade-out`, `fade-up`, `fade-down`, `fade-left`, `fade-right`, `grow`, `shrink`, `strike`, `highlight-red`, `highlight-green`, `highlight-blue`, `highlight-current-red`, `highlight-current-green`, `highlight-current-blue`, `current-visible`.

Ordering + parallelism with `data-fragment-index`:

```html
<section>
  <p class="fragment fade-up">First (click 1)</p>
  <p class="fragment fade-up" data-fragment-index="1">Second (click 2)</p>
  <p class="fragment fade-up" data-fragment-index="1">Also second — parallel with above</p>
  <p class="fragment fade-up" data-fragment-index="2">Third (click 3)</p>
</section>
```

Rules: same index means parallel. Omit the index for strict document-order sequence. Indices need not be contiguous but must be ascending to avoid confusion.

Code-highlight fragments:

```html
<pre><code data-line-numbers="1|2-3|4">
const cache = new EdgeCache();
cache.enableShield();
deploy({ rollback: true });
  </code></pre>
```

### Per-engine notes
- **reveal.js:** native fragments. Full variant list above.
- **Slidev:** `v-click` is the equivalent. No `data-fragment-index`; use `v-click="1"` numbering.
- **Marp:** no fragments. Author one slide per step.

### Performance notes
- Fragments are opacity/transform shows — nearly free. Hundreds per deck are fine.
- `grow` / `shrink` animate `scale`, not `font-size`. Safe for 60fps.
- `highlight-*` variants animate `background-color` (paint). Limit to one highlight per slide.

### Reduced-motion fallback snippet
```css
@media (prefers-reduced-motion: reduce) {
  .fragment {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
    visibility: visible !important;
  }
}
```
```js
// optionally auto-show all fragments for reduced motion + print
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  Reveal.initialize({ fragments: true });
  document.querySelectorAll('.fragment').forEach(el => el.classList.add('visible'));
}
```

---

## 10. Parallax — both flavors

### What it is
Flavor A is reveal.js `parallaxBackgroundImage`: the background drifts slower than the foreground across horizontal slides, creating depth. Flavor B is scroll-driven parallax in custom decks: foreground layers translate at different rates on scroll.

### WHEN to use
- Flavor A: narrative decks with one panoramic background (city skyline, factory floor, starfield) spanning 3–5 slides.
- Flavor B: single-page scroll decks / poster slides where depth aids storytelling.
- Exactly one parallax zone per deck. More reads as motion sickness.

### WHEN to avoid
- Text over moving backgrounds without a scrim. Contrast collapses mid-flight.
- Parallax on data slides. Moving grids distort bar-length perception.
- Parallax + Auto-Animate on the same slide. Two depth systems fight.

### Full copy-paste: Flavor A (reveal.js background parallax)

```html
<script>
  Reveal.initialize({
    parallaxBackgroundImage: 'skyline-wide.jpg', // 3000px+ wide recommended
    parallaxBackgroundSize: '3000px 800px',
    parallaxBackgroundHorizontal: 200, // px drift per slide
    parallaxBackgroundVertical: 0
  });
</script>
```

Tune drift: `parallaxBackgroundHorizontal: 120` is subtle, `200` is visible, `300+` is dramatic. Start at 150.

Scrim for readability (mandatory over photos):

```css
.reveal .slides section {
  background: linear-gradient(rgba(11,16,32,.72), rgba(11,16,32,.72));
  border-radius: 16px;
}
```

### Full copy-paste: Flavor B (scroll-driven layer parallax)

```html
<style>
  .parallax { position: relative; height: 70vh; overflow: hidden; border-radius: 16px; }
  .layer { position: absolute; inset: 0; display: grid; place-items: center; }
  .layer.back { transform: translateZ(0); }
</style>

<div class="parallax" id="plx">
  <div class="layer back" data-speed="0.25">Mountains image layer</div>
  <div class="layer mid" data-speed="0.5">Mid hill layer</div>
  <div class="layer front" data-speed="0.8"><h2>Acme Metrics</h2></div>
</div>

<script>
  const zone = document.getElementById('plx');
  const layers = [...zone.querySelectorAll('[data-speed]')];
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) {
    window.addEventListener('scroll', () => {
      const r = zone.getBoundingClientRect();
      const progress = 1 - r.top / window.innerHeight;
      layers.forEach(l => {
        const s = parseFloat(l.dataset.speed);
        l.style.transform = `translateY(${(progress - 0.5) * s * 120}px)`;
      });
    }, { passive: true });
  }
</script>
```

### Per-engine notes
- **reveal.js:** Flavor A is built in via `parallaxBackground*` config.
- **Slidev / Marp:** no built-in parallax. Use Flavor B CSS/JS in a custom layout, or skip parallax entirely.
- **Export:** parallax freezes on the first frame in PDF/PPTX. Ensure frame one reads standalone.

### Performance notes
- Background images for parallax should be wide (2800–3500px) but compressed (under 400KB, JPEG quality 70).
- Use `transform: translate3d()` to promote layers to the compositor. Never parallax with `background-position` animation (paint per frame).
- Throttle scroll handlers with `requestAnimationFrame` + `passive: true` as shown.

### Reduced-motion fallback snippet
```js
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  // Flavor A: disable drift
  Reveal.initialize({ parallaxBackgroundImage: '' });
  // Flavor B: skip scroll listener entirely (layers stay static)
}
```

---

## 11. Scroll-driven timelines (CSS + WAAPI)

### What it is
Animations tied to scroll position instead of time: `animation-timeline: view()` / `scroll()` in pure CSS, or Web Animations API with a scroll listener. Elements fade, rise, or progress bars fill as the reader scrolls. Ideal for single-page poster decks and long-form scroll stories.

### WHEN to use
- Scroll-story decks: each viewport is one beat, visuals build as you scroll.
- Progress rails: thin bar at top fills with scroll depth.
- Section headers that pin briefly then release.
- Image reveals: `clip-path` or `opacity` driven by entry into view.

### WHEN to avoid
- Paginated slide decks (reveal.js / Slidev / Marp). Scroll timelines assume continuous scroll, not discrete slides.
- Critical content that only appears mid-animation. If the reader stops halfway, they must still get the point.
- Over 10 scroll-linked animations per page. Each adds intersection + paint cost.

### Full copy-paste code block (pure CSS)

```css
.reveal-on-scroll {
  animation: rise-in linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 40%;
}
@keyframes rise-in {
  from { opacity: 0; transform: translateY(36px); }
  to { opacity: 1; transform: none; }
}

.progress-rail {
  position: fixed; top: 0; left: 0; height: 4px; width: 100%;
  background: #2563EB;
  transform-origin: 0 50%;
  animation: fill-rail linear both;
  animation-timeline: scroll();
}
@keyframes fill-rail {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

```html
<div class="progress-rail"></div>
<section class="reveal-on-scroll"><h2>Signal one — latency down 41%</h2></section>
<section class="reveal-on-scroll"><h2>Signal two — NRR 128%</h2></section>
```

WAAPI variant with explicit range control:

```js
const el = document.querySelector('.hero-visual');
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reduce && el.animate) {
  el.animate(
    [{ opacity: 0, transform: 'translateY(28px)' }, { opacity: 1, transform: 'none' }],
    { duration: 500, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'both' }
  );
}
```

### Per-engine notes
- **Custom HTML:** first-class. Ship as a scroll-story page alongside the slide deck.
- **reveal.js / Slidev / Marp:** not native. These engines own the scroll container; custom timelines fight their navigation. Use only in embedded iframes, not the deck itself.
- **Support:** `animation-timeline` ships in Chromium 115+ and Safari 18+. Firefox support is partial — provide the WAAPI/static fallback.

### Performance notes
- `animation-timeline: view()` is compositor-driven in supporting browsers — cheaper than JS scroll listeners.
- Prefer `opacity` + `translateY` under 40px. Large translations + blur per scroll frame jank on mobile.
- `animation-range: entry 10% cover 40%` keeps flights short. Full `cover 0% cover 100%` stretches one animation across the whole page and feels laggy.

### Reduced-motion fallback snippet
```css
@media (prefers-reduced-motion: reduce) {
  .reveal-on-scroll, .progress-rail {
    animation: none !important;
    opacity: 1 !important;
    transform: none !important;
  }
}
```

---

## 12. Decision flowchart (prose)

Start at the top for every animated beat and walk down:

1. **Is this beat essential without motion?** If the slide is incomprehensible as a static image, redesign the slide first. Motion must be enhancement, never the message carrier. Export paths (PDF/PPTX) freeze frame one.
2. **Is it a continuation of the previous slide?** Yes means morph: reveal.js Auto-Animate if you are in reveal.js, View Transitions if custom HTML, `view-transition` frontmatter if Slidev, duplicate-static slides if Marp.
3. **Is it a stepwise build on one slide?** Yes means fragments (reveal.js) or `v-click` (Slidev) or split slides (Marp). Cap at 5 steps.
4. **Is it a layout reflow (filter/grid)?** Yes means FLIP: hand-rolled primitive for one element, GSAP Flip for many.
5. **Is it a chapter change?** Yes means a slide transition, default `fade 300–400ms`, one `zoom` per deck maximum, `none` for appendix.
6. **Is it atmosphere (depth/scroll)?** Parallax or scroll timelines only for scroll-story pages, never for paginated decks, exactly one zone per deck.
7. **Finally: does reduced motion have a path?** Every yes above must map to an instant cut. If you cannot name the fallback, delete the animation.

Default stack per engine: reveal.js gets `fade` + Auto-Animate + fragments. Slidev gets `slide-left` + `view-transition` on morph chapters + `v-click`. Marp gets `fade 0.4s` deck-wide + two `_transition` overrides maximum. Custom HTML gets View Transitions router + FLIP for interactions.

## 13. Common mistakes (and fixes)

1. **Morphing everything.** Six `data-id` pairs per slide pair looks like soup. Fix: keep 1–3 morph pairs, let the rest cut or fade.
2. **Duplicate morph names.** Two `view-transition-name: hero` elements alive simultaneously cancel the transition silently. Fix: unique names, lint with `document.querySelectorAll('[style*="view-transition-name"]')` length checks.
3. **Animating `width` / `font-size`.** The classic bar-growth mistake. Fix: animate `transform: scaleX()` or let Auto-Animate handle box interpolation; animate `opacity` for emphasis instead of size.
4. **A different transition per slide.** `fade`, then `cube`, then `explode` screams amateur. Fix: one deck default, one override for the money slide, `none` for appendix.
5. **Fragments without order testing.** Clicking through reveals a blank beat or double-advance. Fix: walk every fragment forward and backward in presenter mode before shipping.
6. **Motion as meaning.** Arrows that only make sense mid-flight, numbers that only resolve at animation end. Fix: ensure frame one and the resting frame both communicate; PDF export is the test.
7. **No reduced-motion path.** Shipping `v-motion` / Flip / parallax with no gate. Fix: wrap every path in `prefersReduced()` checks and ship a `transition: none` variant.
8. **Parallax over text without scrim.** Background drift destroys contrast mid-flight. Fix: 60–75% dark scrim + `text-shadow` or solid card behind text.
9. **Overlong durations.** 1.2s flights across 40 slides waste attention. Fix: 200ms micro, 400ms standard, 600ms maximum for hero morphs.
10. **Untested venue hardware.** Buttery on a MacBook Pro, slideshow on a 2018 projector PC. Fix: test at 1366x768 on integrated graphics, throttle CPU 4x in DevTools, and confirm the deck reads at instant-cut speed.

```js
// pre-ship motion audit: paste in console, fix any duplicates
const names = [...document.querySelectorAll('[data-id]')].map(e => e.dataset.id);
const dupes = names.filter((n, i) => names.indexOf(n) !== i);
console.log('duplicate data-id:', [...new Set(dupes)]);
console.log('fragment count:', document.querySelectorAll('.fragment').length);
console.log('reduced-motion respected:', window.matchMedia('(prefers-reduced-motion: reduce)').media);
```
