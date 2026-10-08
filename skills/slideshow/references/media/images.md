# Images — Sourcing, Treatments, Sizing, Engines, Failures

> Every image is local, credited, sized, and verified. Guilty until
> `python scripts/verify-images.py slides.md` exits 0.
> Tokens are canonical from `references/layouts.md`: spacing `8 / 16 / 24 / 32 / 48 / 64`
> (8pt), radius `16px` (cards) / `16–24px` (figures), border `1px solid var(--border)`,
> shadow `0 8px 30px rgba(2,6,23,.08)`, `aspect-ratio: 16/9`, `object-fit: cover`,
> captions `14px`, scrim `60–78%` dark. Max 2 full-bleeds per deck.

Base deck CSS (paste once — same block as `references/layouts.md` lines 7–19):

```css
:root {
  --space-1: 8px; --space-2: 16px; --space-3: 24px;
  --space-4: 32px; --space-5: 48px; --space-6: 64px;
  --radius-card: 16px; --radius-pill: 999px;
}
.slide-inner { max-width: 1120px; margin: 0 auto; padding: 48px; }
h1 { font-size: clamp(2rem, 5vw, 3.5rem); letter-spacing: -0.02em; line-height: 1.05; }
h2 { font-size: clamp(1.5rem, 3vw, 2.25rem); letter-spacing: -0.015em; line-height: 1.15; }
.lead { font-size: 1.2rem; opacity: .8; max-width: 60ch; }
img.fit { width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 16px; border: 1px solid var(--border); }
.eyebrow { font-size: .8rem; letter-spacing: .12em; text-transform: uppercase; opacity: .65; }
```

Figure base (paste once — all 6 treatments below extend this):

```css
figure.shot { margin: 0; background: var(--surface); border: 1px solid var(--border); border-radius: 16px; overflow: hidden; box-shadow: 0 8px 30px rgba(2,6,23,.08); }
figure.shot img { width: 100%; display: block; object-fit: cover; }
figcaption.cap { font-size: 14px; opacity: .65; padding: 8px 16px 16px; }
figcaption.cap .src { opacity: .8; }
```

---

## 1. Sourcing ladder (in order — never skip a rung)

| Rung | What | When | Example |
|---|---|---|---|
| 1 | Original inline SVG | Diagrams, arrows, architecture, p95 trend sparkline | Jonas's latency fix diagram drawn in-code |
| 2 | Licensed download: Unsplash / Source URL saved to `assets/` | Real humans, labs, hardware | Maria Santos lab photo, Acme deploy wall |
| 3 | Picsum placeholder | Wireframe ONLY — never ships | Layout review draft before assets land |

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

```html
<div class="slide-inner">
  <div class="eyebrow">Architecture — Ada Okafor</div>
  <h2>Edge cache sits in front of origin</h2>
  <figure class="shot" style="padding:24px">
    <svg viewBox="0 0 640 160" width="100%" height="160" role="img" aria-label="Request flow from browser through edge cache to origin, p95 243 milliseconds">
      <rect x="8" y="48" width="140" height="64" rx="16" fill="none" stroke="currentColor" stroke-width="2" />
      <text x="30" y="84" font-size="14">Browser</text>
      <rect x="250" y="48" width="140" height="64" rx="16" fill="none" stroke="#4F7DF3" stroke-width="2" />
      <text x="262" y="84" font-size="14">Edge cache</text>
      <rect x="492" y="48" width="140" height="64" rx="16" fill="none" stroke="currentColor" stroke-width="2" />
      <text x="518" y="84" font-size="14">Origin</text>
      <line x1="148" y1="80" x2="250" y2="80" stroke="currentColor" stroke-width="2" />
      <line x1="390" y1="80" x2="492" y2="80" stroke="currentColor" stroke-width="2" />
    </svg>
    <figcaption class="cap">Cache-hit path serves p95 in 243ms. Drawn inline — no license record needed.</figcaption>
  </figure>
</div>
```

Rule: if the SVG carries data (412 &rarr; 243ms), the `aria-label` states the takeaway,
not the object. Decorative dividers get `aria-hidden="true"`.

### Rung 2 — Unsplash / Source URLs with attribution (download, never hotlink)

Copy the file into `assets/`. Hotlinking fails offline projectors, rots in six months,
and skips the license gate in `scripts/verify-images.py`.

```bash
python scripts/verify-images.py slides.md
python scripts/verify-images.py slides.md --assets-dir assets
python scripts/verify-images.py deck.md --assets-dir ./marp-deck/assets
```

What the script checks (from `scripts/verify-images.py` argparse + `IMG_RE`):
every local `<img src="...">` and Markdown `![]()` must exist on disk, must carry
non-empty `alt`, and must have a per-stem license record. Remote `http…` / `data:`
URIs skip the file check but still require `alt` — which is why rung 2 downloads
instead of linking. Exit 0 prints `OK: N image(s) verified`; exit 1 lists each
failure. Fix every line, never ship red.

Attribution is TWO records, not one (from `workflows/stages/image-review.md` §§4–5).
The `CREDITS.md` entry alone fails the gate. The per-file `assets/<stem>.txt` is mandatory.

Per-file record — `assets/lab.txt` (or `.md`, `.json`, or `lab.LICENSE` beside the image):

```text
Source: Maria Santos, Acme internal shoot, Sep 2026
License: Acme internal — cleared for conference use
Date: 2026-09-18
```

```text
Source: Unsplash photo by Maria Santos, https://unsplash.com/photos/deploy-wall-8xKt0, downloaded Oct 2026
License: Unsplash License — https://unsplash.com/license
Date: 2026-10-02
```

Deck-level record — append one block per image to `assets/CREDITS.md`:

```markdown
## lab.jpg — Acme lab photo
- File: `assets/lab.jpg` (320KB, 1920px)
- Source: Maria Santos, Acme internal shoot, Sep 2026
- License: Acme internal — cleared for conference use

## latency-6w.png — p95 chart export
- File: `assets/latency-6w.png` (140KB, 1920px)
- Source: Acme edge dashboard export by Jonas Weber, Oct 2026
- License: Acme internal data — cleared for external sharing

## stage-hero.jpg — frozen projector hero (AI)
- File: `assets/stage-hero.jpg` (380KB, 1920px)
- Source: generated with Acme image tool, prompt "empty stage, frozen projector glow, dark tech", Oct 2026
- License: Acme-owned generation — no third-party rights
```

Sourcing procedure per type (same order as `image-review.md` §3):

```html
<!-- Stock download sketch: file lands in assets/, credit lands in two places -->
<figure class="shot">
  <img src="assets/lab.jpg" alt="Maria Santos and Jonas Weber reviewing the deploy dashboard in the Acme lab, p95 at 243 milliseconds" style="aspect-ratio:16/9" />
  <figcaption class="cap">Deploy wall, Acme lab. <span class="src">Photo: Maria Santos, Sep 2026. See assets/lab.txt + CREDITS.md.</span></figcaption>
</figure>
```

```html
<!-- User-supplied screenshot sketch: confirm clearance, then save under assets/ -->
<figure class="shot">
  <img src="assets/latency-6w.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks" style="aspect-ratio:16/9" />
  <figcaption class="cap">p95 412 &rarr; 243ms, June &rarr; September. <span class="src">Source: Acme edge dashboard export by Jonas Weber, Oct 2026 — cleared for external sharing.</span></figcaption>
</figure>
```

### Rung 3 — Picsum placeholders ONLY as wireframe

Picsum exists so layout review can happen before assets land. It never ships.
Any `picsum.photos` URL in a shippable deck fails Gate 6.

```html
<!-- WIREFRAME ONLY — replace before image-review sign-off -->
<div class="slide-inner">
  <div class="eyebrow">Wireframe — swap before ship</div>
  <h2>Hero slot reserved for Maria's lab photo</h2>
  <img src="https://picsum.photos/seed/acme-lab/1600/900" alt="Wireframe placeholder for the Acme lab photo, to be replaced with assets/lab.jpg" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;border:1px solid var(--border)" />
  <p style="font-size:14px;opacity:.65">TODO(image): replace picsum seed with assets/lab.jpg + assets/lab.txt + CREDITS.md entry.</p>
</div>
```

Wireframe eviction command (run before `verify-images.py` — zero hits required):

```bash
python scripts/verify-images.py slides.md --assets-dir assets
```

Then grep the deck source for `picsum`, `todo`, `lorem`, `placeholder` — all must return
nothing except inside the verification grep commands themselves.

---

## 2. Six image treatments (copy-paste sketches, 8pt tokens throughout)

All sketches reuse: padding steps `16 / 24 / 32 / 48`, `border-radius: 16px`,
`border: 1px solid var(--border)`, `box-shadow: 0 8px 30px rgba(2,6,23,.08)`,
`aspect-ratio` + `object-fit: cover`, captions `14px`. Demo content only:
Ada Okafor presents, Jonas Weber owns the p95 fix, Maria Santos owns lab photography.

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

```html
<div class="slide-inner">
  <div class="eyebrow">Demo — Ada Okafor</div>
  <h2>Shield blocks the replay in staging</h2>
  <figure class="shot">
    <img src="assets/shield-demo.png" alt="Shield demo dashboard showing three blocked replay attempts in staging" style="aspect-ratio:16/9" />
    <figcaption class="cap">Staging capture, Oct 2026. <span class="src">Source: Ada Okafor, Acme internal — cleared for conference use.</span></figcaption>
  </figure>
</div>
```

Framed rules: `aspect-ratio: 16/9` for charts, `4/3` for tall dashboards (see §3).
Re-export at 2x if 14px axis labels blur. Never upscale a 800px capture to 1920px —
blur fails visual review faster than a small-but-crisp figure.

### Treatment 2 — Full-bleed with scrim opacity ladder (60 / 70 / 78%)

One emotional beat with scrimmed text overlay. Max 2 per deck. Never for data slides —
charts need white ground, not photo ground. Full pattern from
`layout-templates/image-fullbleed.md`, with the three scrim stops spelled out.

Scrim ladder — pick by photo brightness:

```html
<!-- 60%: dark lab interior, text side already shadowed -->
<div class="slide-inner">
  <div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
    <img src="assets/lab.jpg" alt="Engineers reviewing a deploy dashboard in the dark Acme lab" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
    <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.60) 0%,rgba(11,16,32,.20) 60%,transparent 100%);display:flex;align-items:center;padding:48px">
      <div>
        <div style="font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;opacity:.7;color:#fff">On site — August</div>
        <h2 style="color:#fff;margin:8px 0 0;max-width:16ch">Deploy day, minus the fear</h2>
        <p style="color:#fff;opacity:.8;margin:12px 0 0;font-size:14px">Photo: Maria Santos, Acme lab. 1920px, 320KB.</p>
      </div>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65;margin-top:8px">60% scrim — dark interior, text tests at 7:1 on the projector.</p>
</div>
```

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

```html
<!-- 78%: bright hardware close-up, text needs maximum weight -->
<div class="slide-inner">
  <div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
    <img src="assets/stage-hero.jpg" alt="Frozen projector glow over an empty conference stage" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
    <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.78) 0%,rgba(11,16,32,.25) 60%,transparent 100%);display:flex;align-items:center;padding:48px">
      <div>
        <div style="font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;opacity:.7;color:#fff">Midpoint breather</div>
        <h2 style="color:#fff;margin:8px 0 0;max-width:16ch">Then the projector froze</h2>
        <p style="color:#fff;opacity:.8;margin:12px 0 0;font-size:14px">AI generation, Acme-owned. Prompt on file in CREDITS.md.</p>
      </div>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65;margin-top:8px">78% scrim — bright source, text side darkest. Full-bleed is the single gradient-free scrim allowed as an overlay.</p>
</div>
```

Scrim rules (binding): text zone needs `60–78%` dark at the text edge, fading across.
Test body text at `7:1` on projectors, not just laptops. Busy halves stay empty —
faces and action on the left third. Credit lives inside the scrim at `14px`, plus the
`assets/CREDITS.md` entry. Below 40% the slide fails the projector test every time.

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

```html
<div class="slide-inner">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
    <div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
      <img src="assets/lab.jpg" alt="Deploy wall before the fix, tinted navy, p95 at 412 milliseconds" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block;filter:grayscale(1)" />
      <div style="position:absolute;inset:0;background:#0B1020;mix-blend-mode:multiply;opacity:.55" aria-hidden="true"></div>
      <div style="position:absolute;left:16px;bottom:16px;color:#fff;font-weight:700">Before — 412ms</div>
    </div>
    <div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
      <img src="assets/lab.jpg" alt="Deploy wall after the fix, full color, p95 at 243 milliseconds" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block" />
      <div style="position:absolute;left:16px;bottom:16px;background:#16A34A;color:#fff;font-weight:700;border-radius:999px;padding:8px 16px">After — 243ms</div>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65">Left duotone marks the past; right full-color marks the fix Jonas shipped.</p>
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

```html
<div class="slide-inner">
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:24px;align-items:center">
    <figure class="shot" style="margin:0">
      <div style="display:flex;align-items:center;gap:8px;padding:16px;border-bottom:1px solid var(--border)">
        <span style="width:12px;height:12px;border-radius:999px;background:#F87171;display:inline-block" aria-hidden="true"></span>
        <span style="width:12px;height:12px;border-radius:999px;background:#FBBF24;display:inline-block" aria-hidden="true"></span>
        <span style="width:12px;height:12px;border-radius:999px;background:#34D399;display:inline-block" aria-hidden="true"></span>
        <span style="margin-left:8px;font-size:14px;opacity:.65">edge.acme.dev — p95 243ms</span>
      </div>
      <img src="assets/latency-6w.png" alt="Edge dashboard showing weekly p95 latency at 243 milliseconds" style="aspect-ratio:16/9" />
    </figure>
    <div>
      <div class="eyebrow">Jonas Weber</div>
      <h2 style="margin:8px 0">The graph he kept open for six weeks</h2>
      <p class="lead">412 &rarr; 243ms. Cache-hit path, no origin round-trip.</p>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65">Browser chrome: three 12px dots + URL pill at 14px muted. Never chrome a photo — chrome is for pages.</p>
</div>
```

Chrome rules: dots are `12px` circles, URL pill is `14px` muted with `radius 999px`.
Screenshot keeps `aspect-ratio: 16/9` + `object-fit: cover` so the chrome row never
reflows. URL text must match the real staging host — no `example.com` in a ship deck.

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

```html
<div class="slide-inner">
  <div class="eyebrow">Owners</div>
  <h2>Three names on the fix</h2>
  <div style="display:flex;gap:24px;flex-wrap:wrap">
    <div style="display:flex;align-items:center;gap:16px;background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:16px 24px 16px 16px">
      <img src="assets/ada.jpg" alt="Portrait of Ada Okafor, talk owner" style="width:64px;height:64px;border-radius:999px;object-fit:cover;border:1px solid var(--border);flex:none" />
      <div><div style="font-weight:700">Ada Okafor</div><div style="font-size:14px;opacity:.65">Talk + Shield demo</div></div>
    </div>
    <div style="display:flex;align-items:center;gap:16px;background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:16px 24px 16px 16px">
      <img src="assets/jonas.jpg" alt="Portrait of Jonas Weber, latency fix owner" style="width:64px;height:64px;border-radius:999px;object-fit:cover;border:1px solid var(--border);flex:none" />
      <div><div style="font-weight:700">Jonas Weber</div><div style="font-size:14px;opacity:.65">p95 412 &rarr; 243ms</div></div>
    </div>
    <div style="display:flex;align-items:center;gap:16px;background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:16px 24px 16px 16px">
      <img src="assets/maria.jpg" alt="Portrait of Maria Santos, lab photography" style="width:64px;height:64px;border-radius:999px;object-fit:cover;border:1px solid var(--border);flex:none" />
      <div><div style="font-weight:700">Maria Santos</div><div style="font-size:14px;opacity:.65">Lab photos</div></div>
    </div>
  </div>
</div>
```

Avatar rules: `width: 64px; height: 64px; border-radius: 999px; object-fit: cover`
— all four, every time. Square source + CSS circle beats pre-cropped circles
(the verifier sees one file, the layout stays flexible). `alt` names the person
plus their role, never "avatar image".

### Treatment 6 — Split-screen image panel (image carries half the argument)

Use when the photo and the copy are equal partners: lab context left, verdict right.
Grid gap `16px` (or `24px` with body copy). Image panel keeps figure tokens;
text panel keeps slide tokens. They meet at the same `16px` radius.

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

```html
<div class="slide-inner">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:stretch">
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:32px;display:flex;flex-direction:column;justify-content:center">
      <div class="eyebrow">Ada Okafor — staging note</div>
      <h2 style="margin:8px 0">Screenshots beat stock for anything clickable</h2>
      <p style="opacity:.7;margin:0">The audience trusts the Shield block page because it looks exactly like staging.</p>
    </div>
    <figure class="shot" style="margin:0;display:flex;flex-direction:column">
      <img src="assets/shield-demo.png" alt="Shield block page in staging showing three blocked replay attempts" style="aspect-ratio:4/3;flex:1" />
      <figcaption class="cap">staging.acme.dev/shield. <span class="src">Capture: Ada Okafor, Oct 2026.</span></figcaption>
    </figure>
  </div>
</div>
```

Split rules: image side uses `4/3` when the text side carries a metric, `16/9`
when the text side is a single verdict line. Both panels share `radius 16px` so the
seam reads as one card. On narrow viewports the grid collapses to one column,
image first (see §3 responsive rules).

---

## 3. Sizing, aspect, and responsive rules

Budgets (from `workflows/stages/image-review.md` §6 — Gate 3 numbers):

```bash
ls -lh assets/
# expect: every file present, photos ≤400K, backgrounds ≤200K
```

| Kind | Budget | Width cap | Sketch |
|---|---|---|---|
| Photos (incl. full-bleed heroes) | ≤400KB | 1920px | `assets/lab.jpg` 320KB, 1920px |
| Backgrounds | ≤200KB | 1920px | flat, compressible by design |
| Parallax wide | ≤400KB | 3000px (only exception) | wide stage shot |
| Charts / screenshots | ≤400KB, 14px+ labels | 1920px | `assets/latency-6w.png` 140KB |
| Avatars / QR | smallest legible (64px display) | 256px source | `assets/maria.jpg` ≤200KB |

Aspect-ratio map — declare it, never let the browser guess:

```html
<!-- 16/9: charts, screenshots, browser mocks, duotone dividers -->
<figure class="shot">
  <img src="assets/latency-6w.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks" style="aspect-ratio:16/9" />
  <figcaption class="cap">16/9 default. Deploys per week, June &rarr; September. Source: Jonas Weber.</figcaption>
</figure>
```

```html
<!-- 4/3: tall dashboards, split panels, portrait-leaning lab shots -->
<figure class="shot">
  <img src="assets/lab.jpg" alt="Deploy wall dashboard filling a 4 by 3 frame in the Acme lab" style="aspect-ratio:4/3" />
  <figcaption class="cap">4/3 for tall content. Photo: Maria Santos, Sep 2026.</figcaption>
</figure>
```

```html
<!-- 21/9: full-bleed heroes only, crops to 16/9 under 800px -->
<div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
  <img src="assets/stage-hero.jpg" alt="Frozen projector glow over an empty conference stage" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
</div>
```

Radius / border / shadow (no exceptions without a style override on file):

```html
<figure class="shot" style="border-radius:16px">
  <img src="assets/lab.jpg" alt="Acme lab deploy wall with radius, border, and shadow tokens applied" style="aspect-ratio:16/9;border-radius:0" />
  <figcaption class="cap">Cards 16px; figures 16–24px; border 1px var(--border); shadow 0 8px 30px rgba(2,6,23,.08).</figcaption>
</figure>
```

Responsive `object-fit` rules (paste once per deck):

```css
figure.shot img, .bleed img { object-fit: cover; }
@media (max-width: 800px) {
  .bleed img { aspect-ratio: 16/9 !important; }
  .split { grid-template-columns: 1fr !important; }
  .split figure.shot { order: -1; }
}
@media (max-width: 520px) {
  .slide-inner { padding: 24px; }
  .bleed .overlay { padding: 24px !important; }
  figcaption.cap { padding: 8px 16px 16px; }
}
```

```html
<div class="slide-inner">
  <div class="split" style="display:grid;grid-template-columns:1fr 1fr;gap:24px">
    <figure class="shot" style="margin:0">
      <img src="assets/lab.jpg" alt="Deploy wall collapsing to full width under 800 pixels" style="aspect-ratio:4/3" />
      <figcaption class="cap">Under 800px the image stacks above the copy — never beside it.</figcaption>
    </figure>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:32px">
      <div class="eyebrow">Responsive check — Jonas Weber</div>
      <p style="margin:8px 0 0">p95 243ms holds on a 390px phone because the figure is cover-cropped, not squeezed.</p>
    </div>
  </div>
</div>
```

Export at 1920px max width, lower quality until the file fits the budget, then
confirm with `ls -lh assets/`. Stretched images fail review: `object-fit: cover`
with a fixed `aspect-ratio` is mandatory — `fill` and unset heights are never used.

---

## 4. Anti-white-wall rule (binding)

No three consecutive text-only slides. Every deck needs ≥1 image or graphic per
3 slides. Each image must carry a caption or source line. A slide without a visual
is a draft; three in a row is a wall.

Counting method (run during outline review, before any pixel work):

```bash
python scripts/verify-images.py slides.md --assets-dir assets
```

Then walk the slide order and tag each slide `V` (visual: photo, chart, SVG, browser
mock, avatar quote, split panel) or `T` (text-only). Any `TTT` run breaks the deck —
insert a rung-1 SVG or a framed figure. Target density is one visual per 2–3 slides;
a 12-slide Acme Q3 talk carries 4–5 visuals minimum.

Compliant run — visual every third slide (Ada presents, Jonas fixes, Maria shoots):

```html
<!-- Slide 4 (V): framed chart breaks two text slides -->
<div class="slide-inner">
  <div class="eyebrow">Proof — Jonas Weber</div>
  <h2>p95 412 &rarr; 243ms</h2>
  <figure class="shot">
    <img src="assets/latency-6w.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds" style="aspect-ratio:16/9" />
    <figcaption class="cap">June &rarr; September. Source: Acme edge dashboard, Jonas Weber.</figcaption>
  </figure>
</div>
```

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

```html
<!-- Slide 10 (V): avatar quote breaks the closing text run -->
<div class="slide-inner">
  <div style="display:flex;align-items:center;gap:16px">
    <img src="assets/ada.jpg" alt="Portrait of Ada Okafor, talk owner" style="width:64px;height:64px;border-radius:999px;object-fit:cover;border:1px solid var(--border)" />
    <div><div style="font-weight:700">Ada Okafor</div><div style="font-size:14px;opacity:.65">Closing — Oct 2026</div></div>
  </div>
  <p style="font-size:1.5rem;line-height:1.3;margin:16px 0 0;max-width:30ch">&ldquo;Ship the cache. Photograph the wall. Delete the 412.&rdquo;</p>
</div>
```

Failing run — three text slides in a row (do not ship):

```markdown
Slide 5: problem statement (T)
Slide 6: three bullets on cache theory (T)
Slide 7: timeline of incidents (T)  ← WALL: insert Jonas's p95 chart or Maria's lab photo here
```

Fix: promote the timeline to a rung-1 inline SVG (zero license cost) or drop in the
framed `latency-6w.png`. Every inserted visual still needs its `alt`, its 14px
caption or source line, and — for files — its `assets/<stem>.txt` record, or
`verify-images.py` exits 1 and the deck does not ship.

---

## 5. Per-engine notes (pins: reveal.js 6 / Slidev 52 / Marp 4)

Pin in `package.json`, verify with `--version` before building. Never float `latest` in CI.

```json
{
  "devDependencies": {
    "reveal.js": "^6.0.0",
    "@slidev/cli": "^52.0.0",
    "@marp-team/marp-cli": "^4.1.0",
    "decktape": "^3.0.0"
  },
  "engines": { "node": ">=20" }
}
```

```bash
npm i reveal.js@^6.0.0
npx slidev --version
npx marp --version
python -m py_compile skills/slideshow/scripts/verify-images.py
```

### reveal.js 6 — `data-background` + `r-frame`

Card sketches above export more predictably to PDF than `data-background-image`,
but background attributes win for true full-bleeds. Use `r-frame` for the framed look.

```html
<!-- reveal.js 6: true background full-bleed with scrim -->
<section data-background-image="assets/lab.jpg" data-background-size="cover" data-background-position="center">
  <div style="background:linear-gradient(90deg,rgba(11,16,32,.78) 0%,rgba(11,16,32,.25) 60%,transparent 100%);padding:48px;border-radius:16px">
    <h2 style="color:#fff">Deploy day, minus the fear</h2>
    <p style="color:#fff;opacity:.8;font-size:14px">Photo: Maria Santos. p95 243ms on the wall behind Jonas.</p>
  </div>
</section>
```

```html
<!-- reveal.js 6: framed figure with r-frame tokens -->
<section>
  <div class="slide-inner">
    <h2>p95 412 &rarr; 243ms</h2>
    <img class="r-frame" src="assets/latency-6w.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks" style="border-radius:16px" />
    <p style="font-size:14px;opacity:.65">Source: Jonas Weber, Acme edge dashboard, Oct 2026.</p>
  </div>
</section>
```

reveal.js gotchas: `data-background-image` paths resolve relative to `index.html` —
keep `assets/` beside it. PDF via decktape needs `?print-pdf`; background images
require the decktape background flag or they print white (see `references/engines.md`).

### Slidev 52 — image layouts

Slidev handles full-height crops natively with `image-right` / `image-left`.
Keep the scrim div for text safety — the layout crops, it does not darken.

```markdown
---
layout: image-right
image: assets/lab.jpg
---
```

```markdown
---
layout: image-right
image: assets/lab.jpg
---

# Deploy day, minus the fear

<div style="background:linear-gradient(90deg,rgba(11,16,32,.70) 0%,transparent 100%);padding:24px;border-radius:16px;color:#fff">

Photo: Maria Santos. Jonas watched p95 settle at 243ms on this wall.

</div>
```

```markdown
---
layout: two-cols
---

# p95 412 &rarr; 243ms

June &rarr; September, Jonas Weber.

::right::

<img src="/assets/latency-6w.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;border:1px solid var(--border)" />
<p style="font-size:14px;opacity:.65">Source: Acme edge dashboard export.</p>
```

Slidev gotchas: leading `/assets/` in `image:` frontmatter resolves from `public/`;
relative `assets/` in `<img>` resolves from `slides.md`. Pick one, stay consistent.
`v-click` steps become extra PDF pages on export — visuals with staged reveals
paginate, so keep avatar rows and scrim text on a single click layer.

### Marp 4 — `bg` directives

Marp splits background and content oddly across themes, so the self-contained card
sketch (§2 treatments) beats theme backgrounds for framed, duotone, browser-mock,
avatar, and split work. Use `bg` directives only for true full-bleeds.

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

```markdown
---
marp: true
theme: default
---

<!-- Marp 4: split background (image left, content right) -->
![bg left:40% cover](assets/lab.jpg)

## p95 412 &rarr; 243ms

Jonas Weber, six weeks. Source: Acme edge dashboard.
```

```markdown
---
marp: true
theme: default
---

<!-- Marp 4: self-contained card — preferred for everything except true bleeds -->
<div class="slide-inner">
  <figure class="shot">
    <img src="assets/latency-6w.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds" style="aspect-ratio:16/9" />
    <figcaption class="cap">June &rarr; September. Source: Jonas Weber.</figcaption>
  </figure>
</div>
```

Marp gotchas: local files need `--allow-local-files` or images drop silently from
output (`stages/export-verify.md` §3). Export check:

```bash
npx marp slides.md -o deck.html --allow-local-files
npx marp slides.md -o deck.pdf --allow-local-files
```

---

## 6. Eight common failures + fixes

### Failure 1 — Hotlink rot (remote URL dies mid-tour)

FAIL — remote source, no local file, projector has no network:

```html
<img src="https://example-cdn.com/lab-photo.jpg" alt="Acme lab" />
```

Gate output: remote URIs skip the file check but still require `alt` — and the
projector shows a broken icon. `verify-checklist.md` Gate 3 tone: fail = do not ship.

Fix — download into `assets/`, add both records, reference locally:

```bash
python scripts/verify-images.py slides.md --assets-dir assets
# expect: OK: 5 image(s) verified in slides.md
```

```html
<figure class="shot">
  <img src="assets/lab.jpg" alt="Maria Santos and Jonas Weber reviewing the deploy dashboard in the Acme lab" style="aspect-ratio:16/9" />
  <figcaption class="cap">Photo: Maria Santos. See assets/lab.txt + CREDITS.md.</figcaption>
</figure>
```

### Failure 2 — 5MB hero (full-bleed that eats the export)

FAIL — `assets/stage-hero.jpg` at 5.2MB, 5000px wide. Marp export stalls, PDF balloons.

```bash
ls -lh assets/
# -rw-r--r-- 1 ada 5.2M stage-hero.jpg  ← over budget 13x
```

Fix — resize to 1920px max, lower quality until ≤400KB, re-verify:

```bash
ls -lh assets/
# expect: stage-hero.jpg ≤400K after re-export at 1920px
python scripts/verify-images.py slides.md --assets-dir assets
```

```html
<div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
  <img src="assets/stage-hero.jpg" alt="Frozen projector glow over an empty conference stage" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.78) 0%,transparent 60%)"></div>
</div>
<p style="font-size:14px;opacity:.65">stage-hero.jpg — 1920px, 380KB. AI generation, prompt in CREDITS.md.</p>
```

### Failure 3 — Text over busy photo without scrim

FAIL — white `h2` directly on Maria's bright lab photo. Laptop looks fine,
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

### Failure 5 — Missing alt / aria-label (screen reader hits silence)

FAIL — Gate output from `verify-images.py`:

```text
2 image gate failure(s) in slides.md:
  - missing alt text: assets/lab.jpg
  - missing alt text: assets/latency-6w.png
```

Fix — `alt` states the takeaway, not the object; decorative gets empty `alt`;
SVG diagrams get `role="img"` + `aria-label`:

```html
<img src="assets/lab.jpg" alt="Maria Santos and Jonas Weber reviewing the deploy dashboard as p95 settles at 243 milliseconds" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;border:1px solid var(--border)" />
```

```html
<img src="assets/latency-6w.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;border:1px solid var(--border)" />
```

```html
<svg viewBox="0 0 640 220" width="100%" height="220" role="img" aria-label="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks"></svg>
```

```html
<!-- Decorative divider only: empty alt, hidden from assistive tech -->
<img src="assets/divider.png" alt="" aria-hidden="true" style="width:100%;aspect-ratio:16/9;object-fit:cover" />
```

### Failure 6 — License missing `.txt` (CREDITS entry is not enough)

FAIL — `CREDITS.md` has the lab entry, but no per-file record beside the image:

```text
1 image gate failure(s) in slides.md:
  - no license record for: assets/lab.jpg (add assets/lab.txt)
```

Fix — write `assets/lab.txt` (or `.md` / `.json` / `lab.LICENSE`), then re-run:

```text
Source: Maria Santos, Acme internal shoot, Sep 2026
License: Acme internal — cleared for conference use
Date: 2026-09-18
```

```bash
python scripts/verify-images.py slides.md --assets-dir assets
# expect: OK: 5 image(s) verified in slides.md
```

Scaffold note: `scripts/new-deck-scaffold.sh` writes the template into
`assets/README.txt` — fill one per image. No `.txt` record means exit 1, no exceptions
for AI, stock, or user-supplied. All three are guilty until exit 0.

### Failure 7 — `http` vs `https` (mixed-content block kills the image)

FAIL — `http://` image inside an `https://`-served reveal.js / Slidev SPA.
Browser blocks it, console logs mixed content, slide shows a gap.

```html
<!-- DO NOT SHIP: http inside https -->
<img src="http://picsum.photos/seed/acme-lab/1600/900" alt="Wireframe placeholder" />
```

Fix — download to `assets/` (rung 2) so the scheme question disappears; interim
wireframes use `https://` only and never ship:

```html
<figure class="shot">
  <img src="assets/lab.jpg" alt="Acme lab deploy wall photographed by Maria Santos" style="aspect-ratio:16/9" />
  <figcaption class="cap">Local file — no scheme, no mixed content, no rot.</figcaption>
</figure>
```

Serve check from `stages/visual-review.md`: reveal.js via `npx serve .`
(open `http://localhost:3000/`); Slidev via `npx slidev slides.md`; Marp HTML via
`npx marp slides.md -o deck.html --allow-local-files`. Console must show 0 errors —
a blocked `http` image is an error, not a warning.

### Failure 8 — Transparent PNG on dark (ghost edges, vanished strokes)

FAIL — `shield-logo.png` with transparency + dark strokes placed directly on
`#0B1020`. Strokes vanish, soft alpha fringes glow gray under the projector.

```html
<!-- DO NOT SHIP: transparent dark strokes on dark ground -->
<div style="background:#0B1020;padding:48px;border-radius:16px">
  <img src="assets/shield-logo.png" alt="Shield logo" style="width:200px" />
</div>
```

Fix — ground the PNG on white or surface, or swap to the reversed asset.
Ada's Shield mark ships two files for exactly this reason:

```html
<figure class="shot" style="padding:24px;background:#fff">
  <img src="assets/shield-logo.png" alt="Shield product logo, navy strokes on white ground" style="width:200px;aspect-ratio:16/9;object-fit:contain" />
  <figcaption class="cap">Dark strokes live on white. Source: Ada Okafor, staging export.</figcaption>
</figure>
```

```html
<div style="background:#0B1020;padding:48px;border-radius:16px;border:1px solid var(--border)">
  <img src="assets/shield-logo-reversed.png" alt="Shield product logo, white strokes for dark backgrounds" style="width:200px;aspect-ratio:16/9;object-fit:contain" />
  <p style="color:#fff;opacity:.65;font-size:14px">Reversed asset on dark — never the transparent dark original.</p>
</div>
```

Rule: audit every transparent PNG on both grounds before sign-off. If only one
asset exists, ground it on the tone its strokes were drawn for and note the
constraint in `assets/CREDITS.md`.

---

## 7. Handoff — image-review sign-off line

Paste one line when `verify-images.py` exits 0 and `ls -lh assets/` meets budget.
Attach the `ls` output to the delivery note. Build may proceed only on green.

```text
Images done: 5 local, all ≤400KB, credited + licensed, verify-images.py exit 0 — build may proceed.
```

```bash
ls -lh assets/
python scripts/verify-images.py slides.md --assets-dir assets
# expect: OK: 5 image(s) verified in slides.md
```

Ship record entry (tone matches `references/verify-checklist.md` — numbers, not adjectives):

```markdown
Deck: Acme Q3 — 18 slides — reveal.js 6
Date: 2026-10-08 · Checker: Ada
- Images: 5 local, all ≤400KB, credited
- Placeholders: 0 hits on TODO/lorem/placeholder greps
- Contrast: scrim text 7:1 on projector check
```
