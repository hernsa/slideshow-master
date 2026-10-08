# Layouts — Box Patterns + Composition Guide

> Spacing scale: `8 / 16 / 24 / 32 / 48 / 64` (8pt). Type via `clamp()`: `h1: clamp(2rem, 5vw, 3.5rem)`, `h2: clamp(1.5rem, 3vw, 2.25rem)`, body `17–19px`, captions `14px`. Radius `12–24px` (cards `16px`). Images: `radius 16px`, `1px solid var(--border)`, soft shadow `0 8px 30px rgba(2,6,23,.08)`, `aspect-ratio: 16/9`, `object-fit: cover`.

Base deck CSS (paste once):

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

---

## 1. Bento grid

### When to use
Overview slides with 4–6 items: metrics, features, pillars, roadmap quarters. The hero cell (span 2x2) carries the one number that matters; satellites carry context.

### When to avoid
Dense text blocks. One line + one metric per cell maximum. If any cell needs two sentences, split the slide. Never use bento for sequential steps — grids imply equality, not order.

### Copy-paste HTML sketch

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
  <div style="grid-column:span 2;grid-row:span 2;background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:32px">
    <div class="eyebrow">Headline metric</div>
    <div style="font-size:3rem;font-weight:800;letter-spacing:-0.02em">$2.4M ARR</div>
    <div style="color:#16A34A;font-weight:600">+18% YoY</div>
    <p style="opacity:.7;max-width:28ch">Net expansion carried the quarter. New logos flat.</p>
  </div>
  <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
    <small style="opacity:.65">NPS</small>
    <div style="font-size:2rem;font-weight:700">72</div>
  </div>
  <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
    <small style="opacity:.65">Churn</small>
    <div style="font-size:2rem;font-weight:700">1.1%</div>
  </div>
  <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
    <small style="opacity:.65">NRR</small>
    <div style="font-size:2rem;font-weight:700">128%</div>
  </div>
  <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
    <small style="opacity:.65">CAC</small>
    <div style="font-size:2rem;font-weight:700">$410</div>
  </div>
</div>
```

Responsive collapse (mandatory):

```css
@media (max-width: 800px) {
  .bento { grid-template-columns: 1fr 1fr !important; }
  .bento .hero { grid-column: span 2 !important; grid-row: auto !important; }
}
@media (max-width: 520px) {
  .bento { grid-template-columns: 1fr !important; }
  .bento .hero { grid-column: span 1 !important; }
}
```

### Per-engine native equivalent
- **reveal.js:** plain HTML grid inside `<section>`. No built-in bento; the sketch above is the implementation.
- **Slidev:** `layout: bento` in community themes, else same HTML with UnoCSS: `grid grid-cols-4 gap-4`.
- **Marp:** HTML block inside Markdown (`<div style="...">`). Marp themes center content — wrap in `<div style="width:100%">`.

### Spacing / type tokens
Gap `16px`, hero padding `32px`, satellite padding `24px`. Hero number `3rem/800`, satellite numbers `2rem/700`, labels `13px uppercase muted`.

---

## 2. Split layouts — 50/50, 40/60, header + 2-col

### 2A. Split 50/50

#### When to use
Text versus visual: claim on the left, screenshot/diagram/quote on the right. The default persuasive slide.

#### When to avoid
Heavy text on both sides. Cap the text column at 3 bullets + 1 lead sentence. If both columns need paragraphs, you have two slides.

#### Copy-paste HTML sketch

```html
<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center">
  <div>
    <div class="eyebrow">Deploy story</div>
    <h2>Ships in minutes</h2>
    <ul style="line-height:1.9">
      <li>One CLI command</li>
      <li>Preview URL per push</li>
      <li>One-click rollback</li>
    </ul>
  </div>
  <img src="assets/deploy.png" alt="Deploy dashboard showing green pipeline with preview URL" class="fit" />
</div>
```

### 2B. Split 40/60 (text-narrow, visual-wide)

#### When to use
Diagrams, charts, or code that need room: 40% claim, 60% evidence. Architecture overviews, flame graphs, dashboards.

#### When to avoid
Portrait images in the wide column (they pillarbox). Use 16/9 visuals only in the 60% slot.

#### Copy-paste HTML sketch

```html
<div style="display:grid;grid-template-columns:2fr 3fr;gap:32px;align-items:center">
  <div>
    <h2>p95 down 41%</h2>
    <p class="lead">Origin shield absorbed 83% of repeat traffic.</p>
    <p style="color:#16A34A;font-weight:700">412ms → 243ms</p>
  </div>
  <img src="assets/latency.png" alt="Latency chart falling from 412 to 243 milliseconds over six weeks" class="fit" />
</div>
```

### 2C. Header + 2-col (claim on top, evidence below)

#### When to use
Comparison slides: before/after, us/them, option A/B. Header states the verdict; columns show the proof.

#### When to avoid
Three-way comparisons (columns get cramped — use bento instead). Asymmetric evidence (one column empty reads as unfinished).

#### Copy-paste HTML sketch

```html
<div>
  <h2 style="text-align:center">Before → after the cache migration</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:24px">
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div class="eyebrow">Before</div>
      <p>Origin hit on every request. p95 412ms.</p>
    </div>
    <div style="background:#F0FDF4;border:1px solid #BBF7D0;border-radius:16px;padding:24px">
      <div class="eyebrow">After</div>
      <p>Shield absorbs repeats. p95 243ms.</p>
    </div>
  </div>
</div>
```

### Per-engine native equivalent
- **reveal.js:** `data-layout` is not built in; use the grids above. `r-stack` only for overlays, not splits.
- **Slidev:** `layout: two-cols`, `layout: image-right`, `layout: image-left`. Frontmatter form:
```markdown
---
layout: two-cols
---
# Left slot
::right::
# Right slot (image here)
```
- **Marp:** split via Markdown tables is fragile — prefer the HTML grids. Marp `<!-- _class: split -->` exists only in custom themes.

### Spacing / type tokens
Gap `32px` (50/50), `24px` (header+2col). Text column `h2 clamp(1.5rem,3vw,2.25rem)`, bullets `18px/1.9`. Visual column always bordered + `16px` radius.

---

## 3. Callout — 4 variants (max 1 per slide)

### When to use
Exactly one aside per slide: info (neutral fact), tip (recommended path), warning (risk), danger (do-not). Place after the main content, never before it.

### When to avoid
Stacking two callouts. Body copy inside the callout (callouts hold one sentence + optional inline code). Callouts on every slide (they stop being special by slide 5).

### Copy-paste HTML sketch (all 4)

```html
<!-- INFO -->
<div style="border-left:4px solid #2563EB;background:#EFF6FF;padding:16px 24px;border-radius:12px;margin-top:24px">
  <strong>Info:</strong> migration is reversible until step 3. Snapshot first.
</div>

<!-- TIP -->
<div style="border-left:4px solid #16A34A;background:#F0FDF4;padding:16px 24px;border-radius:12px;margin-top:24px">
  <strong>Tip:</strong> enable the shield in staging for one day before production.
</div>

<!-- WARNING -->
<div style="border-left:4px solid #F59E0B;background:#FFFBEB;padding:16px 24px;border-radius:12px;margin-top:24px">
  <strong>Warning:</strong> cache purge takes up to 90 seconds to propagate globally.
</div>

<!-- DANGER -->
<div style="border-left:4px solid #DC2626;background:#FEF2F2;padding:16px 24px;border-radius:12px;margin-top:24px">
  <strong>Danger:</strong> never purge and redeploy simultaneously — you will cold-start the fleet.
</div>
```

Dark-mode safe variant (border stays, fill darkens):

```css
.dark .callout-info { background: rgba(37,99,235,.14); }
.dark .callout-tip { background: rgba(22,163,74,.14); }
.dark .callout-warn { background: rgba(245,158,11,.14); }
.dark .callout-danger { background: rgba(220,38,38,.16); }
```

### Per-engine native equivalent
- **reveal.js:** raw HTML as above.
- **Slidev:** `> [!INFO]`, `> [!TIP]`, `> [!WARNING]`, `> [!CAUTION]` callout Markdown (MDC enabled).
- **Marp:** blockquote with theme styling: `> **Info:** ...`. Custom colors need theme CSS.

### Spacing / type tokens
`margin-top: 24px`, padding `16px 24px`, left bar `4px`, radius `12px`, text `16–17px`. Max width `70ch`.

---

## 4. Stat cards (row of 3–4)

### When to use
KPI comparison: label + big number + one delta. Traction slides, QBR snapshots, experiment results.

### When to avoid
More than 4 cards (wrap to bento). Two deltas per card (pick the honest one). Mixing units without labels ($, %, ms must each be explicit).

### Copy-paste HTML sketch

```html
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
  <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
    <small style="opacity:.65;letter-spacing:.08em">ARR</small>
    <div style="font-size:2.2rem;font-weight:800" class="tnum">$2.4M</div>
    <span style="color:#16A34A;font-weight:600">▲ +18% YoY</span>
  </div>
  <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
    <small style="opacity:.65;letter-spacing:.08em">NPS</small>
    <div style="font-size:2.2rem;font-weight:800" class="tnum">72</div>
    <span style="color:#16A34A;font-weight:600">▲ +6</span>
  </div>
  <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px">
    <small style="opacity:.65;letter-spacing:.08em">CHURN</small>
    <div style="font-size:2.2rem;font-weight:800" class="tnum">1.1%</div>
    <span style="color:#16A34A;font-weight:600">▼ −0.3pp</span>
  </div>
</div>
```

Delta accessibility (never color alone):

```html
<span style="color:#16A34A">▲ +18%</span> <!-- up-good -->
<span style="color:#DC2626">▼ −4%</span>  <!-- down-bad, arrow + sign redundant with color -->
```

### Per-engine native equivalent
- **All engines:** same HTML. Slidev shortcut: `flex gap-4` + `p-6 rounded-2xl bg-slate-100`.
- **Print:** stat cards survive grayscale if arrows + signs are present. Test by printing one slide in black-and-white.

### Spacing / type tokens
Gap `16px`, padding `24px`, label `12–13px uppercase muted`, number `2.2rem/800 tabular`, delta `15px/600`.

---

## 5. Quote

### When to use
One voice, one sentence, with a face. Customer proof, team motto, press pull. Under 25 words — longer quotes belong in a handout.

### When to avoid
Anonymous quotes (no name = no trust). Two quotes per slide (they compete). Decorative giant quote marks at 200px (use a 40px mark + real typography).

### Copy-paste HTML sketch

```html
<figure style="text-align:center;max-width:640px;margin:32px auto">
  <img src="assets/ada.jpg" alt="Portrait of Ada Okafor" style="width:64px;height:64px;border-radius:50%;object-fit:cover;border:2px solid var(--border)" />
  <blockquote style="font-size:1.5rem;line-height:1.4;margin:16px 0">“Deploy day went from fear to routine.”</blockquote>
  <figcaption style="opacity:.7">Ada Okafor — Platform Lead, Acme Corp</figcaption>
</figure>
```

Editorial variant (serif, left-aligned, for Paper/Botanical decks):

```html
<figure style="max-width:680px;margin:0 auto;border-left:3px solid var(--primary);padding-left:24px">
  <blockquote style="font-family:Fraunces,Georgia,serif;font-size:1.6rem;line-height:1.35">“We stopped dreading Fridays.”</blockquote>
  <figcaption style="margin-top:12px;opacity:.7">Jonas Weber — SRE, Northwind</figcaption>
</figure>
```

### Per-engine native equivalent
- **reveal.js / Marp:** HTML as above.
- **Slidev:** `layout: quote` centers quote styling natively.

### Spacing / type tokens
Avatar `64px circle`, quote `1.5rem/1.4`, attribution `15px muted`, container `max-width 640px`, top margin `32px`.

---

## 6. Code + preview side-by-side

### When to use
Live API or component demos where the audience must connect syntax to behavior. Code capped at 12 lines, preview in an iframe or screenshot.

### When to avoid
Full file dumps (split into two slides or link the repo). Font below 14px to fit (if it does not fit at 15px, cut lines). Preview requiring auth (it will fail on stage Wi-Fi — screenshot it).

### Copy-paste HTML sketch

```html
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start">
  <pre style="background:#0D1117;color:#E6EDF3;border-radius:16px;padding:24px;font-size:15px;line-height:1.6;overflow:auto;margin:0"><code>const app = createApp();

// health probe for deploys
app.get("/health", () =&gt; ({ ok: true }));

// preview URL per push
app.preview({ rollback: true });
app.listen(3000);</code></pre>
  <div>
    <iframe src="./demo/" title="Live demo of preview deployment" style="border:1px solid var(--border);border-radius:16px;width:100%;aspect-ratio:16/9;background:#fff"></iframe>
    <p style="font-size:14px;opacity:.65;margin-top:8px">Live preview — falls back to screenshot in PDF export.</p>
  </div>
</div>
```

Screenshot-fallback variant (for Marp/PDF decks):

```html
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:center">
  <pre style="background:#0D1117;color:#E6EDF3;border-radius:16px;padding:24px;font-size:15px"><code>deploy({ preview: true })</code></pre>
  <img src="assets/demo-shot.png" alt="Screenshot of preview deployment with green checks" class="fit" />
</div>
```

### Per-engine native equivalent
- **reveal.js:** `highlight.js` or Shiki plugin for `<pre><code>`; iframe as above.
- **Slidev:** fenced code blocks with line highlights: ` ```ts {1,3|5} `. Monaco runner via `code-runnable` for live edits.
- **Marp:** fenced code only; iframe unsupported in export — always ship the screenshot variant.

### Spacing / type tokens
Gap `24px`, code padding `24px`, code `15px/1.6 mono`, preview `16/9 + border + radius 16px`, caption `14px muted`.

---

## 7. Section divider / title slide

### When to use
New chapters (max 3 per deck). Full-bleed number + claim. Gives the audience a breath and a landmark.

### When to avoid
Dividers between every slide (they double slide count and halve momentum). Dividers without numbers (audiences use “section 2” to ask questions later).

### Copy-paste HTML sketch

```html
<div style="min-height:60vh;display:flex;flex-direction:column;justify-content:center;gap:16px">
  <div style="font-size:5rem;font-weight:800;opacity:.14">02</div>
  <div class="eyebrow">Part two — evidence</div>
  <h1>The pipeline recovered</h1>
  <p class="lead">Three changes, six weeks, p95 down 41%.</p>
</div>
```

Number-free variant (closing / opening only):

```html
<div style="min-height:60vh;display:flex;flex-direction:column;justify-content:center">
  <div class="eyebrow">Acme Corp — Q3 review</div>
  <h1>Ship calmly.</h1>
  <p class="lead">Ada Okafor · Platform Lead · October 2026</p>
</div>
```

### Per-engine native equivalent
- **reveal.js:** `<section data-background-color="var(--bg)">` + sketch.
- **Slidev:** `layout: section` or `layout: intro`.
- **Marp:** `<!-- _class: lead -->` + `#` heading.

### Spacing / type tokens
Ghost number `5rem/800/14% opacity`, eyebrow `13px uppercase`, title `clamp(2.5rem,6vw,4rem)`, lead `1.2rem muted`.

---

## 8. Agenda / TOC

### When to use
Talks over 15 minutes or 3+ sections. Show it once after the title, then never again (or as a 10px footer progress marker).

### When to avoid
5-minute lightning talks (agenda wastes 20% of the slot). More than 5 items (nobody remembers item 6).

### Copy-paste HTML sketch

```html
<div>
  <div class="eyebrow">Today — 20 minutes</div>
  <h2>Three parts</h2>
  <ol style="list-style:none;padding:0;margin-top:24px;display:grid;gap:16px">
    <li style="display:flex;gap:16px;align-items:baseline">
      <span style="font-weight:800;opacity:.35">01</span>
      <div><strong>The stall</strong><div style="opacity:.65">Why deploys hurt — 4 min</div></div>
    </li>
    <li style="display:flex;gap:16px;align-items:baseline">
      <span style="font-weight:800;opacity:.35">02</span>
      <div><strong>The fix</strong><div style="opacity:.65">Three changes — 10 min</div></div>
    </li>
    <li style="display:flex;gap:16px;align-items:baseline">
      <span style="font-weight:800;opacity:.35">03</span>
      <div><strong>The proof</strong><div style="opacity:.65">Numbers + demo — 6 min</div></div>
    </li>
  </ol>
</div>
```

Timings are mandatory — they tell the audience the talk is planned.

### Per-engine native equivalent
- All engines: same HTML. Slidev: `layout: default` + list. Marp: ordered Markdown list is acceptable here (rare case where Markdown suffices).

### Spacing / type tokens
Number `1.1rem/800/35%`, title `18px/700`, detail `15px muted`, row gap `16px`.

---

## 9. Closing / CTA slide

### When to use
Final slide that stays up during Q&A. One ask + one contact path. Repo URL, QR, or email — pick one, not three.

### When to avoid
“Thank you” as the headline (wastes the most-viewed slide). Walls of links (nobody photographs 8 URLs). New information (closing restates, never introduces).

### Copy-paste HTML sketch

```html
<div style="min-height:60vh;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;gap:16px">
  <div class="eyebrow">Try it tonight</div>
  <h1 style="margin:0">Ship your next deploy<br/>in one command.</h1>
  <code style="background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:12px 20px;font-size:1.05rem">npx acme-deploy --preview</code>
  <p style="opacity:.7">Slides + demo: <strong>acme.dev/talks/q3</strong> · ada@acme.dev</p>
</div>
```

QR variant (in-person talks):

```html
<div style="display:grid;grid-template-columns:1fr auto;gap:32px;align-items:center;min-height:60vh">
  <div>
    <h1>Take the demo home.</h1>
    <p class="lead">Scan for slides, repo, and the 4-minute video.</p>
    <p><strong>acme.dev/talks/q3</strong></p>
  </div>
  <img src="assets/qr.png" alt="QR code linking to slides and demo at acme dot dev slash talks slash q3" style="width:180px;height:180px;border:1px solid var(--border);border-radius:16px" />
</div>
```

### Per-engine native equivalent
- **reveal.js:** final `<section>` with `data-background` tint.
- **Slidev:** `layout: end` or `layout: intro` reused.
- **Marp:** final `#` slide with centered text.

### Spacing / type tokens
Command block `17px mono / 12–20px padding / 12px radius`, contact `16px`, headline left-aligned (centered closings photograph worse).

---

## 10. Image treatments

### When to use
Every photographic slide. Four treatments cover 95% of needs: full-bleed hero, rounded card, avatar row, duotone annotation.

### When to avoid
Uncredited images (see verify checklist). Stretched aspect ratios. Text directly on busy photos without scrim. Stock handshakes (use product screenshots or real team photos).

### Copy-paste HTML sketches

Full-bleed hero with scrim:

```html
<div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
  <img src="assets/lab.jpg" alt="Engineers reviewing a deploy dashboard in a lab" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.78) 0%,rgba(11,16,32,.25) 60%,transparent 100%);display:flex;align-items:center;padding:48px">
    <h2 style="color:#fff;margin:0;max-width:16ch">Deploy day, minus the fear</h2>
  </div>
</div>
```

Rounded card image (default for screenshots):

```html
<img src="assets/dashboard.png" alt="Dashboard with deploy pipeline and three green checks" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;border:1px solid var(--border);box-shadow:0 8px 30px rgba(2,6,23,.08)" />
```

Avatar row (team slide):

```html
<div style="display:flex;gap:12px;align-items:center">
  <img src="assets/ada.jpg" alt="Ada Okafor" style="width:56px;height:56px;border-radius:50%;object-fit:cover;border:2px solid var(--border)" />
  <img src="assets/jonas.jpg" alt="Jonas Weber" style="width:56px;height:56px;border-radius:50%;object-fit:cover;border:2px solid var(--border)" />
  <img src="assets/maria.jpg" alt="Maria Santos" style="width:56px;height:56px;border-radius:50%;object-fit:cover;border:2px solid var(--border)" />
  <span style="opacity:.65">+ 14 engineers</span>
</div>
```

Side-anchored portrait (quote / bio slides):

```html
<div style="display:grid;grid-template-columns:200px 1fr;gap:24px;align-items:center">
  <img src="assets/speaker.jpg" alt="Speaker portrait" style="width:200px;height:240px;object-fit:cover;border-radius:16px;border:1px solid var(--border)" />
  <div><h2>Ada Okafor</h2><p class="lead">Platform Lead — ships daily, sleeps nightly.</p></div>
</div>
```

### Per-engine native equivalent
- All engines accept `<img>` with these styles. Slidev image layouts (`image-left`, `image-right`) handle full-height crops natively.
- Always set `width`/`height` or `aspect-ratio` to prevent layout shift during load.

### Spacing / type tokens
Radius `16px` (cards), `50%` (avatars), scrim `60–78% dark`, caption `14px muted` below every figure.

```html
<figure style="margin:0">
  <img src="assets/chart.png" alt="Bar chart of weekly deploys rising from 4 to 31" class="fit" />
  <figcaption style="font-size:14px;opacity:.65;margin-top:8px">Deploys per week, June → September. Source: Acme internal.</figcaption>
</figure>
```

---

## When-vs-avoid matrix (expanded)

| Pattern | Use when | Avoid when | Max per deck |
|---|---|---|---|
| Bento | 4–6 parallel items | Sequential steps, dense text | 2 |
| Split 50/50 | Claim + visual | Two text walls | 6 |
| Split 40/60 | Wide chart/diagram | Portrait visuals | 3 |
| Header + 2-col | Before/after, A/B | 3-way compare | 2 |
| Callout | One aside | Stacked, on every slide | 3 (1/slide) |
| Stat cards | KPI compare | 5+ KPIs, double deltas | 2 |
| Quote | One voice + face | Anonymous, long | 1–2 |
| Code + preview | Syntax → behavior | File dumps, auth-gated demo | 3 |
| Divider | New chapter | Between every slide | 3 |
| Agenda | 15min+ talks | Lightning talks | 1 |
| Closing CTA | Q&A backdrop | New info, link walls | 1 |
| Hero image | Emotional beat | Data slides | 2 |

Rule of thumb: if two consecutive slides use the same pattern, the second must change the visual (new image, new numbers) or merge into the first.

## Worked example A — title slide (Bento Minimal, light)

Goal: conference keynote opener. One claim, one credential, zero clutter.

```html
<div class="slide-inner">
  <div class="eyebrow">Acme Corp · Q3 engineering review · Oct 2026</div>
  <h1>Ship calmly.</h1>
  <p class="lead">How preview deploys took p95 from 412ms to 243ms in six weeks — and ended Friday fear.</p>
  <div style="display:flex;gap:12px;align-items:center;margin-top:24px">
    <img src="assets/ada.jpg" alt="Portrait of Ada Okafor" style="width:48px;height:48px;border-radius:50%;object-fit:cover" />
    <div><strong>Ada Okafor</strong><div style="opacity:.65;font-size:14px">Platform Lead, Acme</div></div>
  </div>
</div>
```

Why it works: eyebrow orients (who/when), `h1` is two words, lead is one sentence with both numbers, face adds trust. No logo wall, no agenda, no gradient.

## Worked example B — data-story slide (Bento + stat cards hybrid)

Goal: prove the recovery with three numbers and one chart.

```html
<div class="slide-inner">
  <div class="eyebrow">02 · Evidence — six weeks</div>
  <h2>Latency fell, volume held</h2>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:24px 0">
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px">
      <small style="opacity:.65">P95</small>
      <div style="font-size:2rem;font-weight:800">243ms</div>
      <span style="color:#16A34A">▼ −41%</span>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px">
      <small style="opacity:.65">DEPLOYS / WK</small>
      <div style="font-size:2rem;font-weight:800">31</div>
      <span style="color:#16A34A">▲ 8×</span>
    </div>
    <div style="background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:20px">
      <small style="opacity:.65">ROLLBACKS</small>
      <div style="font-size:2rem;font-weight:800">2</div>
      <span style="opacity:.65">both automatic</span>
    </div>
  </div>
  <img src="assets/latency-6w.png" alt="Weekly p95 latency falling from 412 to 243 milliseconds" class="fit" />
  <p style="font-size:14px;opacity:.65">Source: Acme edge logs, June 14 → Sept 2. Shaded band marks shield rollout week.</p>
</div>
```

Why it works: header claims the insight, cards quantify it, chart proves it, caption sources it. One accent color (green) for good deltas only.

## Worked example C — code-demo slide (split 40/60, Midnight SaaS dark)

Goal: show the three-line fix and its live effect.

```html
<div class="slide-inner">
  <div class="eyebrow">03 · The fix — three lines</div>
  <h2>Shield on, origin rests</h2>
  <div style="display:grid;grid-template-columns:2fr 3fr;gap:24px;margin-top:24px;align-items:start">
    <pre style="background:#0D1117;color:#E6EDF3;border-radius:16px;padding:20px;font-size:14.5px;line-height:1.6;margin:0"><code>shield.enable({
  staleWhileRevalidate: 90,
  bypass: ["POST", "auth*"]
});</code></pre>
    <div>
      <img src="assets/shield-demo.png" alt="Demo showing cache hit rate jumping to 83 percent after enabling shield" class="fit" />
      <div style="border-left:4px solid #22C55E;background:rgba(34,197,94,.1);padding:12px 20px;border-radius:12px;margin-top:16px;font-size:15px">
        <strong>Tip:</strong> stage it for a day — hit rate stabilizes before you present it.
      </div>
    </div>
  </div>
</div>
```

Why it works: code is 5 lines (under the 12-line cap) at readable size, visual proves the claim, tip answers the question someone will ask anyway. Dark code block on dark palette keeps screenshots consistent.
