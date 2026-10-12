# Pastel Collage — organic freeforms behind rotated photo plates

> Derived from `Chikiwaa.pptx`: 20 slides, 34 images, 5 audio, seven pastels from
> one hue family, all photos plain `rect` rotated ±3–6°, decorative freeforms
> (clouds, arches, confetti) behind them, white card + pill for text.
> Grammar and rules → `../pptx-motion-language.md` §6, §7, §8.

**Use when:** explainers, community/people decks, kid-friendly or warm-brand
stories, "here's how it works" narratives. Never for projector-critical or
data-dense decks (pastels wash out; Gate 4 still applies).

**Anatomy (fixed per deck — 6 shapes):**

| # | Shape | Geometry | Notes |
|---|---|---|---|
| 1–3 | `cloud-a/b/c` | freeform blob | `pastel-N` fill, no stroke |
| 4 | `arch` | `border-radius:50% 50% 0 0` | outline only, behind plate |
| 5 | `plate` | `rect`, `rotate(-4deg)` | photo, no mask |
| 6 | `card` | white rect, r16 | text lives here — no scrim needed |
| 7 | `pill` | r999 | label / page tag |

## Slide 7 — pastel blob-behind plate

```html
<section class="pastel" data-bg="pastel:3">
  <svg class="deco deco-cloud-a" viewBox="0 0 200 160" aria-hidden="true">
    <path d="M12 96c-8-30 14-58 46-58 6-24 34-36 56-22 26-12 58 4 62 30 22 8 26 44 6 58-14 22-52 24-74 12-26 14-56 8-70-12-16 4-24-2-26-8Z"/>
  </svg>
  <svg class="deco deco-arch" viewBox="0 0 120 160" aria-hidden="true">
    <path d="M8 158V72a52 52 0 0 1 104 0v86" fill="none" stroke-width="3"/>
  </svg>

  <figure class="plate">
    <img src="assets/kids-reading.jpg" alt="Trẻ em đọc sách ở thư viện cộng đồng, ảnh chụp thật của dự án">
    <figcaption>Thư viện cộng đồng · 2024</figcaption>
  </figure>

  <div class="card">
    <span class="pill">Bước 3</span>
    <h2 class="t-title">Mỗi đứa trẻ một chiếc kệ</h2>
    <p class="t-body">Kệ gỗ tự chế, sách quyên góp, giá mỗi kệ 12.000đ.</p>
  </div>
</section>
```

```css
.pastel { position: relative; height: 100%; overflow: hidden; background: var(--pastel-3); }

/* 1–4 — decorative freeforms BEHIND the photo. Never mask the photo. */
.deco { position: absolute; z-index: 0; pointer-events: none; }
.deco-cloud-a { left: -6%; top: 22%; width: 46%; fill: var(--pastel-1); }
.deco-arch { right: 4%; top: 12%; width: 30%; stroke: var(--pastel-2); }

/* 5 — the plate: a plain rotated rect. This is the whole trick. */
.plate {
  position: absolute; left: 20%; top: 16%; width: 44%; z-index: 1;
  transform: rotate(-4deg);                 /* ±3–6deg, alternates per slide */
  margin: 0;
}
.plate img { width: 100%; aspect-ratio: 4/3; object-fit: cover; border-radius: 14px; }
.plate figcaption { font-size: 14px; color: var(--muted); margin-top: 8px; text-align: center; }

/* 6 — white card: contrast solved by surface, not by scrim */
.card {
  position: absolute; right: 6%; top: 30%; width: 30%; z-index: 2;
  background: #fff; border-radius: 16px; padding: 24px;
}
.card .t-title { color: var(--ink); }

/* 7 — pill */
.pill {
  display: inline-block; padding: 4px 14px; border-radius: 999px;
  background: var(--accent-soft); color: var(--ink); font-size: 14px; font-weight: 600;
}
```

## The pastel ramp (lock at style time — never invent hexes per slide)

```css
:root {
  --pastel-1: #BBE6F7;  /* powder blue */
  --pastel-2: #FFEFC8;  /* butter */
  --pastel-3: #FFE8F4;  /* blush */
  --pastel-4: #E2EFFB;  /* ice blue */
  --pastel-5: #FFFDE4;  /* cream */
  --pastel-6: #BBFFC8;  /* mint */
  --accent-break: #4EA72E; /* ONE saturated green, section break only */
}
```

Slide backgrounds walk the ramp; **never repeat a pastel twice in a row**
(Gate 13 longest identical-bg run ≤2). `accent-break` appears on exactly one
slide per section.

## Per-slide table for a 6-slide section

| Slide | `--pastel-N` | `.plate` rotate | `.deco-cloud-a` x | `.card` |
|---|---|---|---|---|
| 1 | `-1` | `-4deg` | `-6%` | right |
| 2 | `-2` | `3deg` | `18%` | right |
| 3 | `-3` | `-5deg` | `42%` | left |
| 4 | `-4` | `4deg` | `66%` | left |
| 5 | `-5` | `-3deg` | `88%` | right |
| 6 | `accent-break` | `-4deg` | `112%` | right |

Each row changes **two** things max. `.deco-cloud-a` walking past the edge is
the morph anchor — the blob drifts while the plate tilts.

## Do / Don't

- **Do** put the text on a white card instead of scrimming the photo. That's how
  Chikiwaa gets contrast at pastel lightness.
- **Do** alternate `left`/`right` card placement so the section doesn't read as a
  two-column grid.
- **Do** keep photos as plain rects. The organic feel is 100% freeform decor.
- **Don't** rotate the whole slide or the text card — only the plate and decor.
- **Don't** use `clip-path`/blob masks on the photo here; that's the *other*
  organic device (`photo-collage.md` / arch crop). One device per deck.
- **Don't** add audio unless the mode asks for it; Chikiwaa's 5 audio files are
  a Canva export artifact, not a requirement.