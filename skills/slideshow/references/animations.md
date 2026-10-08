# Animations — Morph / FLIP / View Transitions / Fragments

> Rule: prefer transform + opacity only. Layout-property animation janks. Every section below ends with its reduced-motion fallback.

## 1. Morph continuity (shared element)

Keep the same name on both slides. Names must be unique per deck.

**reveal.js:**
```html
<!-- slide 1 -->
<h2 data-id="hero">Acme Metrics</h2>
<!-- slide 2 -->
<h2 data-id="hero">Acme Metrics: Q3</h2>
```

**View Transitions API:**
```css
.hero-card { view-transition-name: hero; }
```
```js
document.startViewTransition(() => goToSlide(next));
```

**GSAP FLIP:**
```html
<div data-flip-id="hero" class="card">Acme Metrics</div>
```
```js
const state = Flip.getState('[data-flip-id="hero"]');
goToSlide(next);
Flip.from(state, { duration: 0.5, ease: 'power2.out' });
```

*Reduced-motion fallback:* if `prefers-reduced-motion: reduce`, skip FLIP / transition, cut instantly to the next slide.

## 2. reveal.js Auto-Animate

Adjacent sections with matching `data-id` children animate automatically.

```html
<section data-auto-animate>
  <h2 data-id="title">Pipeline</h2>
  <div data-id="bar" style="width:120px;height:24px;background:#2563EB"></div>
</section>
<section data-auto-animate>
  <h2 data-id="title">Pipeline: deployed</h2>
  <div data-id="bar" style="width:320px;height:24px;background:#2563EB"></div>
</section>
```

Transform-only path (translate/scale/opacity) holds 60fps. Animating `font-size`, `width`, or `top` forces layout and drops frames — scale the element instead.

*Reduced-motion fallback:* add `data-auto-animate="false"` or gate `Reveal.initialize({ autoAnimate: !matchMedia('(prefers-reduced-motion: reduce)').matches })`.

## 3. FLIP fallback snippet (no library)

```js
const r1 = el.getBoundingClientRect();
applyNewLayout(); // move / resize el via class change
const r2 = el.getBoundingClientRect();
const dx = r1.left - r2.left;
const dy = r1.top - r2.top;
el.animate(
  [{ transform: `translate(${dx}px,${dy}px)` }, { transform: 'none' }],
  { duration: 400, easing: 'cubic-bezier(.2,.7,.2,1)' }
);
```

*Reduced-motion fallback:* wrap in `if (!matchMedia('(prefers-reduced-motion: reduce)').matches) { ... }`, else apply layout with no animation.

## 4. Marp transitions

Frontmatter default + per-slide override:

```markdown
---
marp: true
theme: default
transition: fade 0.5s
---

# Slide one

---

<!-- _transition: cover-left -->

# Slide two
```

Bespoke HTML template only. Requires Chromium 110+. Anywhere else the deck falls back to an instant cut.

*Reduced-motion fallback:* ship a no-transition build for reduced motion: set `transition: none` frontmatter variant and link it from the first slide.

## 5. Slidev transitions + motion

```markdown
---
transition: slide-left
---

# Cover
```

Click-step reveal:

```html
<div v-click>Step 1</div>
<div v-click>Step 2</div>
```

Directed entrance:

```html
<div v-motion :initial="{x:-80,opacity:0}" :enter="{x:0,opacity:1}">Fly in</div>
```

*Reduced-motion fallback:* set `transition: none` in frontmatter when reduced motion is detected, and replace `v-motion` with static `v-show` content.

## 6. Fragments (reveal.js)

```html
<p class="fragment fade-up">First point</p>
<p class="fragment fade-up" data-fragment-index="1">Second</p>
<p class="fragment fade-up" data-fragment-index="1">Runs in parallel with second</p>
<p class="fragment fade-up" data-fragment-index="2">Third</p>
```

Same `data-fragment-index` = parallel. Omit the index for strict sequence.

*Reduced-motion fallback:* CSS override shows all fragments without animation:

```css
@media (prefers-reduced-motion: reduce) {
  .fragment { opacity: 1 !important; transform: none !important; }
}
```
