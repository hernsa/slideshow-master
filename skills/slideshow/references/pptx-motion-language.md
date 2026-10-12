# PPTX Motion Language — What the Liked Decks Actually Do

> Source: five reference decks the user likes (`23.4`, `28.3`, `Chikiwaa`, `Slide AirPods Pro 2`, Viet Nam ppt) plus three Vietnamese rebuild-prompt PDFs. Parsed shape-by-shape from the OOXML. This file is the motion/design grammar those decks share — apply it on top of `animations.md` mechanics and `layouts.md` patterns. Still 1 page per slide. Always.

## 1. Continuity anchors (the core move)

Every liked deck repeats the SAME shapes across adjacent slides at different positions/sizes — and ships ZERO explicit transitions (`trans=none` in all five decks). The "morph" feel comes from repeated anchors, not from transition effects:

- **Chikiwaa:** same `!!`-named freeforms (blob, arch, circle) persist across slides, moved/resized each time. The eye tracks the shape; the slide change reads as motion.
- **AirPods:** identical picture/textbox layout across slides 2–4, product photo swaps position left→right→center while the headline stays put.
- **28.3:** identical 19-shape layout on all 4 slides — only the background photo changes. Rock-solid frame, changing window.

**Rule — 2+ continuity anchors per section:** pick two elements (headline block, accent shape, photo frame, stat strip) and repeat them on every slide of the section in the same relative position. Change position/size of ONE anchor per slide step, never both anchors at once. In HTML terms this is exactly `animations.md` §1 morph pairs — but the PPTX decks prove the pair count can stay at 1–2 and still feel modern, because the anchors are BIG (full-bleed photo, 138pt headline) rather than small cards.

```html
<!-- anchor: same headline block, same position, slides 2-4 -->
<!-- slide 2 --><h2 data-id="sec-title" style="font-size:3rem">Anh · 1640</h2>
<!-- slide 3 --><h2 data-id="sec-title" style="font-size:3rem">Mỹ · 1776</h2>
<!-- slide 4 --><h2 data-id="sec-title" style="font-size:3rem">Pháp · 1789</h2>
```

## 2. One transition for the whole deck

The rebuild prompts specify a SINGLE transition applied to every slide (Morph byObject 1500–2000ms in the templates; the promo uses uniform entrances). No per-slide transition roulette.

**Rule:** lock ONE slide transition at style-lock time (`fade 0.4s`, `slide-left`, or `view-transition`), use it everywhere, spend the motion budget on entrances + anchors instead. Per-slide transition overrides are banned except a single `zoom` showcase or `none` appendix (already in `animations.md` §12 — this is the why).

## 3. Staggered entrances, capped

The 25.7s promo packs 349 effects on ONE slide — that is a video, not a deck, do not copy the count. What to copy is the *stagger grammar*: elements enter in reading order (kicker → headline → body → visual), each 100–150ms apart, fast fade + slight rise (`opacity 0→1`, `translateY(12px)→0`), total entrance budget ≤600ms per slide.

**Rule:** max 3 staggered entrances per slide (the 4th element is already visible). Stagger delay 100–150ms, duration 200–400ms, `transform` + `opacity` only. Anything already covered by Gate 8 fragment budget counts against it — a `v-click` chain IS the stagger, do not run both.

```css
.enter-1 { animation: rise .3s var(--ease-out) .1s both; }
.enter-2 { animation: rise .3s var(--ease-out) .22s both; }
.enter-3 { animation: rise .3s var(--ease-out) .34s both; }
@keyframes rise { from { opacity: 0; transform: translateY(12px); } }
```

## 4. Photo-background + minimal text

`23.4`/`28.3` slides are a full-bleed photo with a display title + one short body line. Text never fights the photo: dark scrim band behind text (≥60% black gradient from bottom), title ≥48px, body ≤25 words.

```html
<div style="position:relative;min-height:100%;background:url(assets/hanoi-1890.jpg) center/cover">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(0,0,0,.72))"></div>
  <div style="position:absolute;left:48px;bottom:48px;max-width:640px">
    <div class="eyebrow" style="color:#F4C95D">HÀ NỘI · 1890</div>
    <h2 style="color:#fff;font-size:3.2rem;margin:0 0 8px">Đông Kinh Nghĩa Thục</h2>
    <p style="color:#E8EEF9;font-size:1.1rem;margin:0">Trường học miễn phí đầu tiên — 20 chữ, không hơn.</p>
  </div>
</div>
```

## 5. Oversized display type

Fenice 36pt titles, SF Pro Display up to 138pt, accent script fonts (iCiel Stabile, SVN-Good Dog) for one-word emphasis. Translation: one display face at 2.5–4x body size per slide, plus ONE accent word in a contrasting face (serif italic, script, or mono) — never a whole paragraph.

**Rule:** display headline `clamp(2.5rem, 6vw, 4.5rem)`; accent word wrapped in `<em class="accent-word">` with the style's secondary face; body stays the workhorse face. Counts against the 2-font cap (display + body; accent word reuses one of them in italic/script cut, or the mono).

## 6. Photos in custom shapes (blob / arch masks)

The liked decks never drop a raw rectangle photo on a designed slide — photos sit inside custom freeform geometry (arch tops, blob outlines, circle crops) via `CUST geom + PIC fill`. HTML equivalent: `border-radius` asymmetric values + `clip-path`.

```html
<!-- arch mask: photo with rounded top, flat bottom -->
<img src="assets/temple-arch.jpg" alt="Cổng đền Angkor — vòm đá ong"
     style="width:100%;height:420px;object-fit:cover;border-radius:210px 210px 16px 16px">
<!-- blob mask: organic crop for portraits -->
<img src="assets/speaker.jpg" alt="Diễn giả Thu Hà"
     style="width:320px;height:320px;object-fit:cover;border-radius:58% 42% 55% 45%/48% 55% 45% 52%">
```

**Rule:** plain rectangles allowed only for full-bleed backgrounds and screenshots. Every other photo gets a shape: arch, blob, circle, or duotone panel. One mask style per deck — do not mix arch + blob + circle.

## 7. Tinted background rotation (pastel mode)

Chikiwaa rotates `BBE6F7 → FFFDE4 → E2EFFB` — pale blue, pale yellow, pale steel. Pastel rotation works when: saturation stays under ~35%, text stays near-black (`#1F2328`-class), accent stays single. This is the light-mode answer to Gate 13 rotation — three tints, same family, zero chrome.

## 8. Dark showcase mode

AirPods deck: pure-black `tx1` background, white SF Pro type, product photo as the only color. Use for one section max per deck (showcase, demo, finale): bg `#000`–`#0A0A0A`, body `#F5F5F7`, one accent, photos uncropped or arch-masked, no cards, no borders — the photo IS the decoration.

## 9. The rebuild-prompt discipline (organization)

The three prompt PDFs are rebuild specs, and their structure is the real lesson — every slide spec carries: exact text-style run table (size/font/weight per run), z-order list, entrance list with timings, transition name + duration, and a sync rule (repeated content identical across slides). Steal the format for `research-notes.md` slide sections: each slide gets `Text runs:` (content + size role), `Z-order:` (bg → shapes → text), `Entrances:` (≤3, with delays), `Anchors:` (which 2 elements continue from the previous slide).

## Anti-slop don'ts

1. No transition roulette — one deck transition, no per-slide overrides (except one zoom/one none).
2. No 349-effect promos — stagger capped at 3 entrances, ≤600ms total, fragments and stagger share one budget.
3. No raw rectangle photos on designed slides — full-bleed, arch, blob, or circle. Pick one mask per deck.
4. No morphing body copy — anchors are headlines, shapes, photos, numbers (`animations.md` §1 still binds).
5. No pastel + neon in one deck — pastel rotation OR dark showcase OR saturated style. One color story.
