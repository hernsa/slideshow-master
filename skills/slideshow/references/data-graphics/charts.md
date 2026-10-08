# Charts — Pure HTML/CSS/SVG

> No external chart libs. Bars are flex `%` widths, lines are inline SVG polylines, donuts are SVG `stroke-dasharray` segments. Spacing `8 / 16 / 24 / 32`, radius `16px` cards / `999px` bars, type `17–19px` body / `14px` captions. Colors via `var(--primary, --accent, --success, --warning, --muted, --surface, --border)`.

Shared chart CSS (paste once):

```css
.chart-card { background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 24px; }
.chart-title { font-size: 15px; font-weight: 700; margin: 0 0 4px; }
.chart-sub { font-size: 14px; color: var(--muted); margin: 0 0 16px; }
.chart-src { font-size: 14px; color: var(--muted); margin-top: 16px; }
.tnum { font-variant-numeric: tabular-nums; }
@media (max-width: 800px) { .chart-card { padding: 16px; } }
```

---

## 1. Bar chart (flex bars with % widths)

### When to use
Ranked comparison of 3–6 categories: deploys per service, p95 per region, incidents per release train. One value per row, longest bar = the story.

### When to avoid
Time series (use §2 line). More than 6 rows (bars shrink to stripes — split the slide). Two series per row (use a table).

### Copy-paste HTML sketch

```html
<div class="chart-card">
  <p class="chart-title">Deploys per week by service — September</p>
  <p class="chart-sub">Release train Green · 31 total deploys</p>
  <div style="display:grid;gap:16px">
    <div>
      <div style="display:flex;justify-content:space-between;font-size:15px;margin-bottom:8px">
        <span><strong>Checkout API</strong> <span style="opacity:.65">· Jonas Weber</span></span>
        <span class="tnum"><strong>14</strong> <span style="opacity:.65">· 45.2%</span></span>
      </div>
      <div style="background:var(--surface);border-radius:999px;height:16px">
        <div style="width:92%;height:100%;border-radius:999px;background:var(--primary)"></div>
      </div>
    </div>
    <div>
      <div style="display:flex;justify-content:space-between;font-size:15px;margin-bottom:8px">
        <span><strong>Edge shield</strong> <span style="opacity:.65">· Ada Okafor</span></span>
        <span class="tnum"><strong>9</strong> <span style="opacity:.65">· 29.0%</span></span>
      </div>
      <div style="background:var(--surface);border-radius:999px;height:16px">
        <div style="width:59%;height:100%;border-radius:999px;background:var(--primary);opacity:.75"></div>
      </div>
    </div>
    <div>
      <div style="display:flex;justify-content:space-between;font-size:15px;margin-bottom:8px">
        <span><strong>Billing worker</strong> <span style="opacity:.65">· Maria Santos</span></span>
        <span class="tnum"><strong>5</strong> <span style="opacity:.65">· 16.1%</span></span>
      </div>
      <div style="background:var(--surface);border-radius:999px;height:16px">
        <div style="width:33%;height:100%;border-radius:999px;background:var(--accent)"></div>
      </div>
    </div>
    <div>
      <div style="display:flex;justify-content:space-between;font-size:15px;margin-bottom:8px">
        <span><strong>Search index</strong> <span style="opacity:.65">· Kenji Tanaka</span></span>
        <span class="tnum"><strong>3</strong> <span style="opacity:.65">· 9.7%</span></span>
      </div>
      <div style="background:var(--surface);border-radius:999px;height:16px">
        <div style="width:20%;height:100%;border-radius:999px;background:var(--muted)"></div>
      </div>
    </div>
  </div>
  <p class="chart-src">Source: deploy ledger, Sep 1–30. Widths are share of max (14 = 92% track).</p>
</div>
```

Tokens: track `var(--surface)` `16px` tall, bar `999px` radius, row gap `16px`, value `tabular-nums`. One `primary` series; second color only to separate the tail.

### Per-engine notes
- **reveal.js:** raw HTML in one `<section>`. Animate growth with two `data-auto-animate` slides (widths `0%` → final).
- **Slidev:** same HTML, or UnoCSS: `flex justify-between text-[15px]`, track `bg-slate-200 rounded-full h-4`, bar `rounded-full`. Avoid `v-click` per row (exports 4 PDF pages).
- **Marp:** HTML `<div>` block verbatim + `<style>` for `.chart-card`. Marp centers content — wrap in `<div style="width:100%">`.

### Anti-slop don't
- Don't round to `45% / 30% / 15% / 10%` theater — ship the ledger's messy `45.2% / 29.0% / 16.1% / 9.7%`.

---

## 2. Line / sparkline (inline SVG polyline)

### When to use
Trend over 6–12 points: p95 latency by week, failed deploys per train, cache hit rate after shield rollout. One line answers "did it get better?"

### When to avoid
Fewer than 5 points (bars read better). Two crossing lines with a legend paragraph (use a table + one line for the hero series).

### Copy-paste HTML sketch

```html
<div class="chart-card">
  <p class="chart-title">p95 latency, Jun 14 → Sep 2 (ms)</p>
  <p class="chart-sub">Shield rollout week shaded · 412ms → 243ms, −41%</p>
  <svg viewBox="0 0 400 140" role="img" aria-label="Line chart: p95 falling from 412 to 243 milliseconds over eight weeks" style="width:100%;height:auto;display:block">
    <line x1="0" y1="35" x2="400" y2="35" stroke="var(--border)" stroke-width="1" />
    <line x1="0" y1="75" x2="400" y2="75" stroke="var(--border)" stroke-width="1" />
    <line x1="0" y1="115" x2="400" y2="115" stroke="var(--border)" stroke-width="1" />
    <rect x="228" y="0" width="52" height="140" fill="var(--primary)" opacity="0.08" rx="8" />
    <polyline points="0,18 52,26 104,31 156,48 208,62 260,84 312,104 368,116"
      fill="none" stroke="var(--primary)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    <circle cx="368" cy="116" r="5" fill="var(--success)" stroke="var(--card)" stroke-width="2" />
  </svg>
  <div class="tnum" style="display:flex;justify-content:space-between;font-size:14px;color:var(--muted);margin-top:8px">
    <span>412ms · W1</span><span>338ms · W4</span><span>243ms · W8</span>
  </div>
  <p class="chart-src">Source: edge logs. Shaded band = shield rollout (Jul 26). Sampling error ±2 points.</p>
</div>
```

Sparkline variant (inline in a stat card, `120×36`):

```html
<span class="tnum" style="font-size:2rem;font-weight:800">31 <small style="font-size:14px;opacity:.65">deploys/wk</small></span>
<svg viewBox="0 0 120 36" role="img" aria-label="Sparkline rising from 4 to 31 deploys" style="width:120px;height:36px">
  <polyline points="0,30 20,28 40,26 60,22 80,16 100,10 120,5" fill="none" stroke="var(--success)" stroke-width="2.5" stroke-linecap="round" />
</svg>
```

Tokens: gridlines `var(--border)` `1px`, line `3px` rounded, endpoint dot `success` with card halo. Labels `14px muted`, never on the line.

### Per-engine notes
- **reveal.js:** inline SVG needs no plugin. Draw-on via `stroke-dasharray` animation between two `data-auto-animate` slides if wanted.
- **Slidev:** inline SVG works; UnoCSS sizing `w-full h-auto block`. Keep `viewBox` fixed so scaling never distorts stroke badly.
- **Marp:** inline SVG exports cleanly to PDF/PPTX (vector survives). Always include `role="img"` + `aria-label`.

### Anti-slop don't
- Don't smooth the line into a marketing curve or start the y-axis at 390 to fake a cliff — show gridlines and the real `412 → 243` endpoints.

---

## 3. Donut (SVG stroke-dasharray segments)

### When to use
Part-to-whole with 2–4 slices: cache hit vs origin (83/17), deploy outcomes (26 green / 3 rolled back / 2 failed), traffic by region.

### When to avoid
More than 4 slices (slivers under 8% are unreadable — merge into "other"). Change-over-time (donuts freeze one moment; use bars or lines).

### Copy-paste HTML sketch

```html
<div class="chart-card">
  <p class="chart-title">September traffic: who served it?</p>
  <p class="chart-sub">4.7M requests · shield absorbed the repeats</p>
  <div style="display:flex;gap:32px;align-items:center;flex-wrap:wrap">
    <svg viewBox="0 0 120 120" role="img" aria-label="Donut: shield 83 percent, origin 11 percent, stale 6 percent" style="width:160px;height:160px;transform:rotate(-90deg)">
      <circle cx="60" cy="60" r="48" fill="none" stroke="var(--surface)" stroke-width="20" />
      <circle cx="60" cy="60" r="48" fill="none" stroke="var(--primary)" stroke-width="20"
        stroke-dasharray="83 100" pathLength="100" stroke-linecap="butt" />
      <circle cx="60" cy="60" r="48" fill="none" stroke="var(--accent)" stroke-width="20"
        stroke-dasharray="11 100" pathLength="100" stroke-dashoffset="-83" stroke-linecap="butt" />
      <circle cx="60" cy="60" r="48" fill="none" stroke="var(--muted)" stroke-width="20"
        stroke-dasharray="6 100" pathLength="100" stroke-dashoffset="-94" stroke-linecap="butt" />
    </svg>
    <div class="tnum" style="display:grid;gap:8px;font-size:15px">
      <div><span style="display:inline-block;width:12px;height:12px;border-radius:4px;background:var(--primary)"></span> Shield hit — <strong>83.4%</strong> (3.9M)</div>
      <div><span style="display:inline-block;width:12px;height:12px;border-radius:4px;background:var(--accent)"></span> Origin — <strong>10.8%</strong> (508K)</div>
      <div><span style="display:inline-block;width:12px;height:12px;border-radius:4px;background:var(--muted)"></span> Stale reval — <strong>5.8%</strong> (273K)</div>
    </div>
  </div>
  <p class="chart-src">Source: edge logs, Sep 1–30. Center stays empty — the total lives in the subtitle.</p>
</div>
```

Tokens: ring `20px` on `r=48`, track `var(--surface)`, `pathLength="100"` so dash math is percent-literal. Legend swatches `12px` squares, values `tabular-nums`.

### Per-engine notes
- **reveal.js:** raw SVG. Rotate `-90deg` so segment 1 starts at 12 o'clock; animate by stepping `stroke-dasharray` across auto-animate slides.
- **Slidev:** same SVG or UnoCSS legend (`grid gap-2 text-[15px]`). No chart component needed — keep it dependency-free.
- **Marp:** SVG + `<div>` legend exports to PDF/PPTX as vector. Test at 50% projector brightness: `muted` slice must still separate from track.

### Anti-slop don't
- Don't ship a 3D pie with a `99.99%` uptime slice — flat donut, butt caps, messy `83.4 / 10.8 / 5.8` shares that sum to 100.

---

## 4. KPI progress rings + stat deltas

### When to use
One KPI near a target: shield hit rate at `83%` of `90%` goal, error budget remaining, migration `7 of 9` services cut over. Ring = progress, delta = direction.

### When to avoid
Two rings competing on one slide (pick the hero KPI; demote the rest to stat cards). Rings as decoration next to a bar chart saying the same thing.

### Copy-paste HTML sketch

```html
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
  <div class="chart-card" style="text-align:center">
    <svg viewBox="0 0 120 120" role="img" aria-label="Ring: cache hit rate 83 percent of 90 percent goal" style="width:120px;height:120px;transform:rotate(-90deg)">
      <circle cx="60" cy="60" r="52" fill="none" stroke="var(--surface)" stroke-width="12" />
      <circle cx="60" cy="60" r="52" fill="none" stroke="var(--success)" stroke-width="12"
        stroke-dasharray="83 100" pathLength="100" stroke-linecap="round" />
    </svg>
    <div class="tnum" style="font-size:2rem;font-weight:800;margin-top:8px">83%</div>
    <small style="opacity:.65;letter-spacing:.08em">CACHE HIT · GOAL 90%</small>
    <div style="color:#16A34A;font-weight:600;font-size:15px;margin-top:4px">▲ +11pp in 6 wks</div>
  </div>
  <div class="chart-card" style="text-align:center">
    <svg viewBox="0 0 120 120" role="img" aria-label="Ring: error budget 64 percent remaining" style="width:120px;height:120px;transform:rotate(-90deg)">
      <circle cx="60" cy="60" r="52" fill="none" stroke="var(--surface)" stroke-width="12" />
      <circle cx="60" cy="60" r="52" fill="none" stroke="var(--warning)" stroke-width="12"
        stroke-dasharray="64 100" pathLength="100" stroke-linecap="round" />
    </svg>
    <div class="tnum" style="font-size:2rem;font-weight:800;margin-top:8px">64%</div>
    <small style="opacity:.65;letter-spacing:.08em">ERROR BUDGET LEFT</small>
    <div style="opacity:.65;font-weight:600;font-size:15px;margin-top:4px">−9pp after Blue train</div>
  </div>
  <div class="chart-card" style="text-align:center">
    <svg viewBox="0 0 120 120" role="img" aria-label="Ring: migration 7 of 9 services" style="width:120px;height:120px;transform:rotate(-90deg)">
      <circle cx="60" cy="60" r="52" fill="none" stroke="var(--surface)" stroke-width="12" />
      <circle cx="60" cy="60" r="52" fill="none" stroke="var(--primary)" stroke-width="12"
        stroke-dasharray="77.8 100" pathLength="100" stroke-linecap="round" />
    </svg>
    <div class="tnum" style="font-size:2rem;font-weight:800;margin-top:8px">7/9</div>
    <small style="opacity:.65;letter-spacing:.08em">SERVICES CUT OVER</small>
    <div style="color:#16A34A;font-weight:600;font-size:15px;margin-top:4px">▲ +2 this train</div>
  </div>
</div>
```

Delta accessibility: arrow + sign + color together (`▲ +11pp`, never green alone). Print check: rings differ by label + number, not hue alone.

### Per-engine notes
- **reveal.js:** raw HTML grid. Reveal rings with `class="fragment"` in DOM order; keep `pathLength="100"` so print-PDF matches screen.
- **Slidev:** `grid grid-cols-3 gap-4` + `p-6 rounded-2xl` cards. Each `v-click` adds an export page — prefer one static slide.
- **Marp:** paste HTML verbatim; wrap grid in full-width `<div>`. `round` linecaps rasterize fine at PDF export.

### Anti-slop don't
- Don't show `99.99%` precision on a ring — `77.8%` is honest, `83%` with a dated delta (`+11pp in 6 wks`) is a story.

---

## Responsive + accessibility

```css
.donut-wrap, .ring-grid { display: flex; gap: 32px; flex-wrap: wrap; }
@media (max-width: 800px) {
  .ring-grid { grid-template-columns: 1fr 1fr !important; }
  svg[viewBox] { max-width: 100%; }
}
```

Every chart carries `role="img"` + `aria-label` with its real numbers, a visible source line, and deltas that survive grayscale (arrow + sign, not color alone).
