# Images — Sourcing, Treatments, Sizing, Engines, Failures

> Every image is local, credited, sized, and verified. Guilty until
> the verify command below exits 0.
> Base deck CSS + `figure.shot` base live in `references/layouts.md` — paste
> once from there, never duplicated here. Max 2 full-bleeds per deck.

Verify command (defined once — every "re-verify" below means this):

```bash
python scripts/verify-images.py slides.md --assets-dir assets
# expect: OK: N image(s) verified in slides.md
```

What the script checks: every local `<img src="...">` and Markdown `![]()`
must exist on disk, must carry non-empty `alt`, and must have a per-stem
license record. Remote `http…` / `data:` URIs skip the file check but still
require `alt`. Exit 1 lists each failure — fix every line, never ship red.

---

## 1. Sourcing ladder (in order — never skip a rung)

| Rung | What | When | Example |
|---|---|---|---|
| 1 | Original inline SVG | Diagrams, arrows, architecture, p95 trend sparkline | Jonas's latency fix diagram drawn in-code |
| 2 | Licensed download: Unsplash / Source URL saved to `assets/` | Real humans, labs, hardware | Maria Santos lab photo, Acme deploy wall |
| 3 | Picsum wireframe slot | Layout review ONLY — never ships | Layout review draft before assets land |

### Rung 1 — Original inline SVG first

SVG is zero-license-risk, zero-byte-overhead, infinitely sharp at projector scale.
Any diagram Jonas could whiteboard in 60 seconds belongs as inline SVG, not a photo.

```html
<div class="slide-inner">
  <div class="eyebrow">The fix — Jonas Weber</div>
  <h2>p95 412 &rarr; 243ms in six weeks</h2>
  <figure class="shot" style="padding:24px">
    <svg viewBox="0 0 640 220" width="100%" height="220" role="img" aria-label="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks">
      <polyline points="0,30 110,55 220,80 330,120 440,150 550,185" fill="none" stroke="#4F7DF3" stroke-width="4" stroke-linecap="round" />
      <circle cx="0" cy="30" r="6" fill="#4F7DF3" />
      <circle cx="550" cy="185" r="6" fill="#16A34A" />
      <text x="8" y="22" font-size="14" font-weight="700">412ms</text>
      <text x="500" y="208" font-size="14" font-weight="700" fill="#16A34A">243ms</text>
    </svg>
    <figcaption class="cap">p95 latency, June &rarr; September. Source: Acme edge dashboard export by Jonas Weber, Oct 2026.</figcaption>
  </figure>
</div>
```

Rule: if the SVG carries data (412 &rarr; 243ms), the `aria-label` states the takeaway,
not the object. Decorative dividers get `aria-hidden="true"`.

### Rung 2 — Unsplash / Source URLs with attribution (download, never hotlink)

Copy the file into `assets/`. Hotlinking fails offline projectors, rots in six months,
and skips the license gate. Attribution is TWO records, not one (see
`workflows/stages/image-review.md` §§4–5). The `CREDITS.md` entry alone fails the gate.

Per-file record — `assets/lab.txt`:

```text
Source: Maria Santos, Acme internal shoot, Sep 2026
License: Acme internal — cleared for conference use
Date: 2026-09-18
```

Deck-level record — append one block per image to `assets/CREDITS.md`:

```markdown
## lab.jpg — Acme lab photo
- File: `assets/lab.jpg` (320KB, 1920px)
- Source: Maria Santos, Acme internal shoot, Sep 2026
- License: Acme internal — cleared for conference use
```

Sourcing procedure per type matches `workflows/stages/image-review.md` §3:

```html
<!-- Stock download sketch: file lands in assets/, credit lands in two places -->
<figure class="shot">
  <img src="assets/lab.jpg" alt="Maria Santos and Jonas Weber reviewing the deploy dashboard in the Acme lab, p95 at 243 milliseconds" style="aspect-ratio:16/9" />
  <figcaption class="cap">Deploy wall, Acme lab. <span class="src">Photo: Maria Santos, Sep 2026. See assets/lab.txt + CREDITS.md.</span></figcaption>
</figure>
```

### Rung 3 — Picsum wireframe slots ONLY

Picsum exists so layout review can happen before assets land. It never ships.
Any `picsum.photos` URL in a shippable deck fails Gate 5.

```html
<!-- WIREFRAME ONLY — replace before image-review sign-off -->
<div class="slide-inner">
  <div class="eyebrow">Wireframe — swap before ship</div>
  <h2>Hero slot reserved for the lab photo</h2>
  <img src="https://picsum.photos/seed/acme-lab/1600/900" alt="Wireframe slot for the Acme lab photo, to be replaced with assets/lab.jpg" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;border:1px solid var(--border)" />
</div>
```

Wireframe eviction (run before the verify command — zero hits required):

```bash
grep -rniE "picsum|todo:|lorem|tbd|fixme" slides.md
# expect: zero hits — Gate 5 fails on any hit outside this command
```

---

## 2. Six image treatments (copy-paste sketches, 8pt tokens throughout)

All sketches reuse the `references/layouts.md` tokens: padding steps `16 / 24 / 32 / 48`,
`border-radius: 16px`, `border: 1px solid var(--border)`,
`box-shadow: 0 8px 30px rgba(2,6,23,.08)`, `aspect-ratio` + `object-fit: cover`,
captions `14px`. Demo content only: Ada Okafor presents, Jonas Weber owns the
p95 fix, Maria Santos owns lab photography.

### Treatment 1 — Framed (default for screenshots, charts, dashboard exports)

Use when the audience could ask to click it: dashboard exports, staging captures,
`latency-6w.png`, `shield-demo.png`. White ground, full caption, no scrim.

```html
<div class="slide-inner">
  <div class="eyebrow">Proof — Jonas Weber</div>
  <h2>p95 412 &rarr; 243ms, six weeks</h2>
  <figure class="shot">
    <img src="assets/latency-6w.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks" style="aspect-ratio:16/9" />
    <figcaption class="cap">Deploys per week, June &rarr; September. <span class="src">Source: Acme edge dashboard export by Jonas Weber, Oct 2026.</span></figcaption>
  </figure>
</div>
```

Framed rules: `aspect-ratio: 16/9` for charts, `4/3` for tall dashboards (see §3).
Re-export at 2x if 14px axis labels blur. Never upscale a 800px capture to 1920px —
blur fails visual review faster than a small-but-crisp figure.

### Treatment 2 — Full-bleed with scrim opacity ladder (60 / 70 / 78%)

One emotional beat with scrimmed text overlay. Max 2 per deck. Never for data slides —
charts need white ground, not photo ground. Full pattern in
`layout-templates/image-fullbleed.md`; the three scrim stops, one sketch:

```html
<!-- 70%: mixed daylight lab, the standard choice -->
<div class="slide-inner">
  <div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
    <img src="assets/lab.jpg" alt="Maria Santos and Jonas Weber at the deploy wall, midday lab light" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
    <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.70) 0%,rgba(11,16,32,.22) 60%,transparent 100%);display:flex;align-items:center;padding:48px">
      <div>
        <div style="font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;opacity:.7;color:#fff">On site — August</div>
        <h2 style="color:#fff;margin:8px 0 0;max-width:16ch">The wall Jonas stared at for six weeks</h2>
        <p style="color:#fff;opacity:.8;margin:12px 0 0;font-size:14px">Photo: Maria Santos, Acme lab. 1920px, 320KB.</p>
      </div>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65;margin-top:8px">70% scrim — default when unsure. Busy right half stays empty.</p>
</div>
```

| Stop | Photo brightness | Gradient head | When |
|---|---|---|---|
| 60% | Dark lab interior, text side already shadowed | `rgba(11,16,32,.60)` | Night shots, stage glow |
| 70% | Mixed daylight lab (sketch above) | `rgba(11,16,32,.70)` | Default when unsure |
| 78% | Bright hardware close-up | `rgba(11,16,32,.78)` | Sunlit exteriors, white benches |

Scrim rules (binding): text zone needs `60–78%` dark at the text edge, fading across.
Test body text at `7:1` on projectors, not just laptops. Busy halves stay empty —
faces and action on the left third. Credit lives inside the scrim at `14px`, plus the
`assets/CREDITS.md` entry. Below 40% the slide fails the projector test every time.
Full-bleed is the single gradient-free scrim allowed as an overlay.

### Treatment 3 — Duotone overlay with mix-blend (brand-tinted storytelling)

Use for section dividers and quote backgrounds where a full-color photo would fight
the accent `#4F7DF3`. One duotone per section maximum — more reads as a filter account.

```html
<div class="slide-inner">
  <div class="eyebrow">The stall — Ada Okafor</div>
  <h2>Every deploy felt like a coin flip</h2>
  <div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border);box-shadow:0 8px 30px rgba(2,6,23,.08)">
    <img src="assets/lab.jpg" alt="Acme lab deploy wall tinted in brand navy, Ada Okafor presenting the stall" style="width:100%;aspect-ratio:16/9;object-fit:cover;display:block;filter:grayscale(1) contrast(1.05)" />
    <div style="position:absolute;inset:0;background:#4F7DF3;mix-blend-mode:multiply" aria-hidden="true"></div>
    <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.70) 0%,transparent 65%);display:flex;align-items:center;padding:48px">
      <p style="color:#fff;font-size:clamp(1.5rem,3vw,2.25rem);line-height:1.15;letter-spacing:-0.015em;margin:0;max-width:20ch">&ldquo;We shipped on Fridays because we had forgotten what Fridays were for.&rdquo;</p>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65;margin-top:8px">Duotone: grayscale photo + multiply accent + 70% scrim. Photo: Maria Santos. See assets/lab.txt.</p>
</div>
```

Duotone rules: `filter: grayscale(1)` on the `<img>`, overlay `<div>` with
`background: #4F7DF3; mix-blend-mode: multiply` (or `#0B1020` at `.55` for navy),
`aria-hidden="true"` on the overlay so screen readers hit the `alt` once. Never
duotone a chart — numbers must stay on white ground with exact hues intact.

### Treatment 4 — Browser-mock chrome (product UI, staging captures)

Use when the screenshot IS the proof: staging UI, Shield block page, edge dashboard.
Chrome signals "this is a real page" and stops the audience asking for the URL mid-talk.

```html
<div class="slide-inner">
  <div class="eyebrow">Live in staging — Ada Okafor</div>
  <h2>Shield blocks the replay, inline</h2>
  <figure class="shot">
    <div style="display:flex;align-items:center;gap:8px;padding:16px;border-bottom:1px solid var(--border);background:var(--surface)">
      <span style="width:12px;height:12px;border-radius:999px;background:#F87171;display:inline-block" aria-hidden="true"></span>
      <span style="width:12px;height:12px;border-radius:999px;background:#FBBF24;display:inline-block" aria-hidden="true"></span>
      <span style="width:12px;height:12px;border-radius:999px;background:#34D399;display:inline-block" aria-hidden="true"></span>
      <span style="margin-left:8px;font-size:14px;opacity:.65;background:var(--bg);border:1px solid var(--border);border-radius:999px;padding:8px 16px">staging.acme.dev/shield — blocked 3 replays</span>
    </div>
    <img src="assets/shield-demo.png" alt="Shield staging page blocking three replay attempts, captured by Ada Okafor" style="aspect-ratio:16/9" />
    <figcaption class="cap">Staging capture, Oct 2026. <span class="src">Source: Ada Okafor — cleared for conference use. See assets/shield-demo.txt.</span></figcaption>
  </figure>
</div>
```

Chrome rules: dots are `12px` circles, URL pill is `14px` muted with `radius 999px`.
Screenshot keeps `aspect-ratio: 16/9` + `object-fit: cover` so the chrome row never
reflows. URL text must match the real staging host. Never chrome a photo.

### Treatment 5 — Avatar circle (faces for quotes, owners, on-call credits)

Use for quote slides and owner rows. Team faces beat avatars-from-nowhere. Display at
64px; never ship a 2MB face — downscale the source, then circle-crop with CSS.

```html
<div class="slide-inner">
  <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:32px;box-shadow:0 8px 30px rgba(2,6,23,.08)">
    <div style="display:flex;align-items:center;gap:16px">
      <img src="assets/maria.jpg" alt="Portrait of Maria Santos, Acme lab photographer" style="width:64px;height:64px;border-radius:999px;object-fit:cover;border:1px solid var(--border);flex:none" />
      <div>
        <div style="font-weight:700">Maria Santos</div>
        <div style="font-size:14px;opacity:.65">Lab photography · Acme internal shoot, Sep 2026</div>
      </div>
    </div>
    <p style="font-size:clamp(1.5rem,3vw,2.25rem);line-height:1.15;letter-spacing:-0.015em;margin:24px 0 0;max-width:28ch">&ldquo;Nobody remembers the deploy that worked. They remember the photo of the wall when it finally went green.&rdquo;</p>
  </div>
  <p style="font-size:14px;opacity:.65;margin-top:8px">Avatar: 64px circle, cover-cropped. Source file: assets/maria.jpg (≤200KB) + assets/maria.txt.</p>
</div>
```

Avatar rules: `width: 64px; height: 64px; border-radius: 999px; object-fit: cover`
— all four, every time. Square source + CSS circle beats pre-cropped circles.
`alt` names the person plus their role.

### Treatment 6 — Split-screen image panel (image carries half the argument)

Use when the photo and the copy are equal partners: lab context left, verdict right.
Grid gap `16px` (or `24px` with body copy). Both panels share `radius 16px` so the
seam reads as one card.

```html
<div class="slide-inner">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:stretch">
    <figure class="shot" style="margin:0;display:flex;flex-direction:column">
      <img src="assets/lab.jpg" alt="Maria Santos photographing the deploy wall while Jonas Weber watches the p95 graph settle at 243 milliseconds" style="aspect-ratio:4/3;flex:1" />
      <figcaption class="cap">Acme lab, Sep 2026. <span class="src">Photo: Maria Santos. See assets/lab.txt.</span></figcaption>
    </figure>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:32px;display:flex;flex-direction:column;justify-content:center">
      <div class="eyebrow">What changed</div>
      <div style="font-size:3rem;font-weight:800;letter-spacing:-0.02em">243ms</div>
      <div style="color:#16A34A;font-weight:600">p95, down from 412ms</div>
      <p style="opacity:.7;max-width:28ch">Edge cache absorbs the repeat reads. Origin handles writes only.</p>
    </div>
  </div>
</div>
```

Split rules: image side uses `4/3` when the text side carries a metric, `16/9`
when the text side is a single verdict line. On narrow viewports the grid collapses
to one column, image first (see §3 responsive row).

### Treatment 7 — Blob and arch masks (beyond the `16px` rect)

Rects are the default; one masked photo per section maximum. Masks never carry
data — charts and screenshots stay framed. Text never sits on the masked photo;
it sits beside it on flat ground.

```html
<div class="slide-inner">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:center">
    <img src="assets/maria.jpg" alt="Portrait of Maria Santos in the Acme lab" style="width:100%;aspect-ratio:1/1;object-fit:cover;clip-path:ellipse(46% 48% at 50% 50%)" />
    <div>
      <div class="eyebrow">Field notes — Maria Santos</div>
      <h2 style="margin:8px 0">One wall, six weeks of evenings</h2>
      <p style="font-size:14px;opacity:.65;margin:8px 0 0">Circle mask for faces; arch rule below for place shots.</p>
    </div>
  </div>
</div>
```

Mask rules: faces get the circle/ellipse mask (`clip-path: ellipse()` or
`border-radius: 999px` on a square source). Place shots get the arch
(`border-radius: 999px 999px 16px 16px` on a `4/5` frame). Organic blobs
(`clip-path: path()` or a blobby polygon) are section-dividers only — one per
deck, because a second blob reads as a theme. Masked images keep the `1px`
border via a wrapper div; `clip-path` clips borders, so the border lives outside it.

### Text ceiling over photos (binding)

Photo slides carry at most 12 words over the image: eyebrow + headline only.
Body copy, metrics, and caveats live below the figure or on the next slide.
The Treatment 2 sketch above is the ceiling demo: 4-word eyebrow, 7-word
headline, 14px credit line — 11 words of argument over pixels. A 13th word
means the slide splits: photo beat first, argument second.

### Dark-showcase and B&W product rule

Hardware close-ups ship on near-black (`#0B1020` card or the 78% scrim stop),
desaturated, never as mid-gray thumbnails. Treatment bounds:
`filter: grayscale(1) contrast(1.05) brightness(.95–1.05)`; floor text at 7:1
against the darkened ground. Dark strokes need the reversed asset or white
ground (see Failure 8) — no `brightness(1.4)` rescue of a muddy capture.
Re-shoot or re-export instead. One B&W showcase per section maximum.

---

## 3. Sizing, aspect, and responsive rules

Budgets (Gate 3 numbers from `workflows/stages/image-review.md` §6):

| Kind | Budget | Width cap | Example |
|---|---|---|---|
| Photos (incl. full-bleed heroes) | ≤400KB | 1920px | `assets/lab.jpg` 320KB, 1920px |
| Backgrounds | ≤200KB | 1920px | Flat, compressible by design |
| Parallax wide | ≤400KB | 3000px (only exception) | Wide stage shot |
| Charts / screenshots | ≤400KB, 14px+ labels | 1920px | `assets/latency-6w.png` 140KB |
| Avatars / QR | Smallest legible (64px display) | 256px source | `assets/maria.jpg` ≤200KB |

| Concern | Rule | Token |
|---|---|---|
| Aspect | Declare it — `16/9` charts/mocks, `4/3` tall dashboards/splits, `21/9` full-bleed heroes (crops to `16/9` under 800px) | `aspect-ratio` + `object-fit: cover` |
| Radius / border / shadow | Cards `16px`; figures `16–24px`; `1px solid var(--border)`; soft shadow | See `references/layouts.md` |
| Responsive | Cover-crop, never squeeze; splits stack image-first under 800px; inner padding `48px` → `24px` under 520px | `references/layouts.md` responsive block |
| Export fit | 1920px max width, lower quality until budget fits, then `ls -lh assets/` | Photos ≤400K, backgrounds ≤200K |

Export at 1920px max width, lower quality until the file fits the budget, then
confirm with `ls -lh assets/`. `object-fit: cover` with a fixed `aspect-ratio`
is mandatory — `fill` and unset heights are never used.

---

## 4. Anti-white-wall rule (binding)

No three consecutive text-only slides. Every deck needs ≥1 image or graphic per
3 slides. Each image must carry a caption or source line. A slide without a visual
is a draft; three in a row is a wall.

Counting method (run during outline review, before any pixel work): re-run the
verify command, then walk the slide order and tag each slide `V` (visual: photo,
chart, SVG, browser mock, avatar quote, split panel) or `T` (text-only). Any `TTT`
run breaks the deck — insert a rung-1 SVG or a framed figure. Target density is
one visual per 2–3 slides; a 12-slide Acme Q3 talk carries 4–5 visuals minimum.

Compliant anchor — visual breaks a text run (Ada presents, Jonas fixes, Maria shoots):

```html
<!-- Slide 7 (V): full-bleed breather before the fix section -->
<div class="slide-inner">
  <div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
    <img src="assets/lab.jpg" alt="Acme lab at night, deploy wall glowing green at 243 milliseconds p95" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
    <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.70) 0%,transparent 65%);display:flex;align-items:center;padding:48px">
      <h2 style="color:#fff;margin:0">The night the wall went green</h2>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65">Photo: Maria Santos. 1 visual per 3 slides — this is slide 7's anchor.</p>
</div>
```

Failing run (do not ship): slides 5–7 tagged `T T T` — insert Jonas's p95 chart
or Maria's lab photo at slide 7. Every inserted visual still needs its `alt`,
its 14px caption, and its `assets/<stem>.txt` record, or the verify exits 1.

---

## 5. Per-engine notes (pins: reveal.js 6 / Slidev 52 / Marp 4)

Pin in `package.json`, verify with `--version` before building. Never float `latest` in CI.
Card sketches from §2 export more predictably than engine backgrounds — use engine
backgrounds only for true full-bleeds. Gotchas live in `references/engines.md`;
export checks live in `workflows/stages/export-verify.md`.

```html
<!-- reveal.js 6: true background full-bleed with scrim -->
<section data-background-image="assets/lab.jpg" data-background-size="cover" data-background-position="center">
  <div style="background:linear-gradient(90deg,rgba(11,16,32,.78) 0%,rgba(11,16,32,.25) 60%,transparent 100%);padding:48px;border-radius:16px">
    <h2 style="color:#fff">Deploy day, minus the fear</h2>
    <p style="color:#fff;opacity:.8;font-size:14px">Photo: Maria Santos. p95 243ms on the wall behind Jonas.</p>
  </div>
</section>
```

```markdown
---
layout: image-right
image: assets/lab.jpg
---

# Deploy day, minus the fear

Photo: Maria Santos. Jonas watched p95 settle at 243ms on this wall.
```

```markdown
---
marp: true
theme: default
---

<!-- Marp 4: full-bleed background with scrimmed Markdown over it -->
![bg cover](assets/lab.jpg)

## <span style="color:white">Deploy day, minus the fear</span>

<span style="color:white;font-size:14px">Photo: Maria Santos — p95 243ms on the wall.</span>
```

---

## 6. Failures + fixes

| Ban | Symptom | Fix |
|---|---|---|
| F1 hotlink rot | Remote URL, projector offline, broken icon | Download into `assets/`, add both records, reference locally |
| F5 missing `alt` | Verifier lists `missing alt text` | `alt` states the takeaway; decorative gets `alt=""`; SVG diagrams get `role="img"` + `aria-label` |
| F6 license missing `.txt` | `CREDITS.md` entry but no per-file record | Write `assets/<stem>.txt`, re-verify; scaffold template lives in `assets/README.txt` |
| F7 `http` in `https` | Mixed-content block kills the image | Local file (rung 2); interim wireframes `https://` only and never ship |

### Failure 2 — 5MB hero (full-bleed that eats the export)

FAIL — `assets/stage-hero.jpg` at 5.2MB, 5000px wide. Marp export stalls, PDF balloons.

```bash
ls -lh assets/
# -rw-r--r-- 1 ada 5.2M stage-hero.jpg  ← over budget 13x
```

Fix — resize to 1920px max, lower quality until ≤400KB, re-verify:

```html
<div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
  <img src="assets/stage-hero.jpg" alt="Frozen projector glow over an empty conference stage" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.78) 0%,transparent 60%)"></div>
</div>
<p style="font-size:14px;opacity:.65">stage-hero.jpg — 1920px, 380KB. AI generation, prompt in CREDITS.md.</p>
```

### Failure 3 — Text over busy photo without scrim

FAIL — white `h2` directly on the bright lab photo. Laptop looks fine,
projector washes to nothing. Below 40% effective dark = fail every time.

```html
<!-- DO NOT SHIP: unscrimmed text on photo -->
<div style="position:relative">
  <img src="assets/lab.jpg" alt="Bright lab photo" style="width:100%;aspect-ratio:21/9;object-fit:cover" />
  <h2 style="position:absolute;top:24px;left:24px;color:#fff">Deploy day</h2>
</div>
```

Fix — 70% scrim at the text edge, white text re-tested at 7:1:

```html
<div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
  <img src="assets/lab.jpg" alt="Engineers reviewing a deploy dashboard in the bright Acme lab" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.70) 0%,rgba(11,16,32,.22) 60%,transparent 100%);display:flex;align-items:center;padding:48px">
    <h2 style="color:#fff;margin:0;max-width:16ch">Deploy day, minus the fear</h2>
  </div>
</div>
```

### Failure 4 — Stretched logos (aspect ignored, `fill` distortion)

FAIL — partner logo squeezed wide, circles become ovals. Stretched images fail review.

```html
<!-- DO NOT SHIP: fill distorts -->
<img src="assets/acme-logo.png" alt="Acme logo" style="width:400px;height:200px;object-fit:fill" />
```

Fix — fixed `aspect-ratio` + `cover` (or `contain` for logos on flat ground), never `fill`:

```html
<figure class="shot" style="padding:24px">
  <img src="assets/acme-logo.png" alt="Acme company logo, navy wordmark on white" style="width:100%;aspect-ratio:16/9;object-fit:contain;background:#fff" />
  <figcaption class="cap">Logo on white ground — contain, never cover, for wordmarks.</figcaption>
</figure>
```

Logos sit on flat ground (`#fff` or `var(--surface)`), `object-fit: contain`, generous
`24px` padding. Photographs use `cover`. Never mix the two.

### Failure 8 — Transparent PNG on dark (ghost edges, vanished strokes)

FAIL — `shield-logo.png` with transparency + dark strokes placed directly on
`#0B1020`. Strokes vanish, soft alpha fringes glow gray under the projector.

```html
<!-- DO NOT SHIP: transparent dark strokes on dark ground -->
<div style="background:#0B1020;padding:48px;border-radius:16px">
  <img src="assets/shield-logo.png" alt="Shield logo" style="width:200px" />
</div>
```

Fix — ground the PNG on white or surface, or swap to the reversed asset:

```html
<figure class="shot" style="padding:24px;background:#fff">
  <img src="assets/shield-logo.png" alt="Shield product logo, navy strokes on white ground" style="width:200px;aspect-ratio:16/9;object-fit:contain" />
  <figcaption class="cap">Dark strokes live on white. Source: Ada Okafor, staging export.</figcaption>
</figure>
```

Rule: audit every transparent PNG on both grounds before sign-off. If only one
asset exists, ground it on the tone its strokes were drawn for and note the
constraint in `assets/CREDITS.md`.

---

## 7. Handoff — image-review sign-off

Handoff lives in `workflows/stages/image-review.md` §9: paste the one-line
`Images done` sign-off when the verify command exits 0 and `ls -lh assets/`
meets budget. Attach the `ls` output to the delivery note.
