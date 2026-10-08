# Diagrams — Architecture, Flow, Timeline, Org

> Boxes-and-arrows without a diagram tool. CSS grid places boxes, inline SVG draws connectors, arrows are pure CSS. Spacing `16 / 24 / 32px` gaps, card padding `24px`, radius `16px`, borders `1px solid var(--border)`. Label rule: **never under 14px** — box titles `16px/700`, body `14–15px`, captions `14px muted`.

Shared diagram CSS (paste once):

```css
.dgm-card { background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 24px; }
.dgm-title { font-size: 15px; font-weight: 700; margin: 0 0 4px; }
.dgm-sub { font-size: 14px; color: var(--muted); margin: 0 0 16px; }
.dgm-box { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 16px 24px; font-size: 15px; }
.dgm-box strong { display: block; font-size: 16px; }
.dgm-box small { font-size: 14px; color: var(--muted); }
.dgm-src { font-size: 14px; color: var(--muted); margin-top: 16px; }
@media (max-width: 800px) {
  .dgm-flow { grid-template-columns: 1fr !important; }
  .dgm-card { padding: 16px; }
  .dgm-arch { grid-template-columns: 1fr !important; }
  .dgm-arch .arrow { transform: rotate(90deg); }
}
```

---

## 1. Architecture boxes-and-arrows (grid + SVG connectors)

### When to use
How traffic flows: browser → edge shield → origin → DB. Three to five boxes, one direction, labels on the arrows with real numbers.

### When to avoid
More than 5 boxes (becomes a poster — split into two slides). Bidirectional arrows everywhere (pick the request path; mention callbacks in the caption).

### Copy-paste HTML sketch

```html
<div class="dgm-card">
  <p class="dgm-title">Request path — September (4.7M requests)</p>
  <p class="dgm-sub">Shield absorbs repeats; origin rests</p>
  <div class="dgm-arch" style="display:grid;grid-template-columns:1fr 40px 1fr 40px 1fr;gap:8px;align-items:stretch">
    <div class="dgm-box"><strong>Browser</strong><small>31K daily users · 412ms before</small></div>
    <div class="arrow" style="display:flex;align-items:center;justify-content:center;font-size:20px;color:var(--primary)" aria-hidden="true">→</div>
    <div class="dgm-box" style="border-color:var(--primary);border-width:2px"><strong>Edge shield</strong><small>83.4% hits · 3.9M served</small></div>
    <div class="arrow" style="display:flex;align-items:center;justify-content:center;font-size:20px;color:var(--primary)" aria-hidden="true">→</div>
    <div class="dgm-box"><strong>Origin + DB</strong><small>10.8% miss · 243ms p95</small></div>
  </div>
  <svg viewBox="0 0 400 28" role="img" aria-label="Fallback arrow: origin purge returns in 90 seconds" style="width:100%;height:28px;margin-top:16px">
    <defs><marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="var(--muted)" /></marker></defs>
    <line x1="330" y1="14" x2="150" y2="14" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#ah)" />
    <text x="200" y="12" text-anchor="middle" font-size="11" fill="var(--muted)">purge ~90s</text>
  </svg>
  <p class="dgm-src">Dashed return = purge path. Numbers: edge logs Sep 1–30.</p>
</div>
```

Tokens: arrows are text `→` at `20px` (screen-reader hidden, meaning lives in box order + caption). Hero box gets `2px primary` border. Return path is a dashed SVG line with a real label (`purge ~90s`), never an unlabeled loop.

### Per-engine notes
- **reveal.js:** raw HTML grid. Build in two `data-auto-animate` slides: boxes first, arrows + numbers second.
- **Slidev:** same HTML or UnoCSS `grid grid-cols-[1fr_40px_1fr_40px_1fr] gap-2 items-stretch`. Keep arrow glyphs as text for export.
- **Marp:** HTML grid + inline SVG export cleanly. Marp centers slides — wrap in `<div style="width:100%">`.

---

## 2. Swimlane / flow (pure CSS arrows)

### When to use
Who does what in order: deploy train Green — dev pushes, shield previews, on-call approves. Two to three lanes, four to six steps, one owner per step.

### When to avoid
Parallel systems with no handoff (use §1 architecture). More than 6 steps (split into train A / train B slides).

### Copy-paste HTML sketch

```html
<div class="dgm-card">
  <p class="dgm-title">Green train — Sep 12 deploy (31 ships, 2 rollbacks)</p>
  <p class="dgm-sub">Push → preview → approve → cut over</p>
  <div class="dgm-flow" style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
    <div class="dgm-box"><strong>1 · Push</strong><small>Jonas Weber · 09:14 · 7 commits</small><div style="font-size:14px;margin-top:8px">CI runs 4 min, 212 tests green.</div></div>
    <div class="dgm-box"><strong>2 · Preview</strong><small>Ada Okafor · 09:21 · URL per push</small><div style="font-size:14px;margin-top:8px">Shield warms cache, p95 251ms.</div></div>
    <div class="dgm-box"><strong>3 · Approve</strong><small>Maria Santos · 10:02 · on-call</small><div style="font-size:14px;margin-top:8px">Load gate 2.4× peak, runbook linked.</div></div>
    <div class="dgm-box" style="border-color:var(--success);border-width:2px"><strong>4 · Cut over</strong><small>Auto · 10:07 · 83.4% hits</small><div style="font-size:14px;margin-top:8px">2 auto-rollbacks, zero pages.</div></div>
  </div>
  <div style="display:flex;gap:16px;margin-top:16px;font-size:14px;color:var(--muted)" aria-hidden="true">
    <span>──▶ handoff = approval + URL</span><span>▓ final = customer-visible</span>
  </div>
  <p class="dgm-src">Source: deploy ledger Sep 12. Final box tinted success — the only green on the slide.</p>
</div>
```

Connect handoffs with CSS only: adjacent boxes imply order; the legend line (`──▶`) names what an arrow means. Owner + timestamp on every step (`Jonas Weber · 09:14`).

### Per-engine notes
- **reveal.js:** `class="fragment"` per box in DOM order for click-walk narration.
- **Slidev:** `v-click` per box works but each adds a PDF page — prefer static + one highlight on box 4.
- **Marp:** static grid prints best; fragments become duplicate PDF pages, so keep one state.

---

## 3. Timeline (vertical rail)

### When to use
When order plus duration matters: six-week recovery, incident review, migration waves. Four to six dated stops on one rail, newest at the bottom.

### When to avoid
Unordered categories (use bars). More than 6 stops (rail runs off the slide — move detail to handout).

### Copy-paste HTML sketch

```html
<div class="dgm-card">
  <p class="dgm-title">Recovery — Jun 14 → Sep 2 (p95 412ms → 243ms)</p>
  <p class="dgm-sub">Three changes, two trains, one shield</p>
  <div style="display:grid;grid-template-columns:28px 1fr;gap:0 16px">
    <div style="display:flex;flex-direction:column;align-items:center" aria-hidden="true">
      <div style="width:14px;height:14px;border-radius:50%;background:var(--muted)"></div>
      <div style="width:2px;flex:1;background:var(--border);min-height:48px"></div>
    </div>
    <div style="padding-bottom:24px"><strong style="font-size:16px">W1 · Jun 14 — the stall</strong><div style="font-size:14px;color:var(--muted)">4 deploys/wk · p95 412ms · 3 rollbacks</div></div>
    <div style="display:flex;flex-direction:column;align-items:center" aria-hidden="true">
      <div style="width:14px;height:14px;border-radius:50%;background:var(--primary);box-shadow:0 0 0 5px color-mix(in srgb, var(--primary) 18%, transparent)"></div>
      <div style="width:2px;flex:1;background:var(--border);min-height:48px"></div>
    </div>
    <div style="padding-bottom:24px"><strong style="font-size:16px">W3 · Jul 26 — shield on (staging)</strong><div style="font-size:14px;color:var(--muted)">Hit rate 64.7% in a day · Ada Okafor</div></div>
    <div style="display:flex;flex-direction:column;align-items:center" aria-hidden="true">
      <div style="width:14px;height:14px;border-radius:50%;background:var(--primary)"></div>
      <div style="width:2px;flex:1;background:var(--border);min-height:48px"></div>
    </div>
    <div style="padding-bottom:24px"><strong style="font-size:16px">W6 · Aug 23 — Blue train cut over</strong><div style="font-size:14px;color:var(--muted)">24 deploys/wk · p95 271ms · 1 rollback</div></div>
    <div style="display:flex;flex-direction:column;align-items:center" aria-hidden="true">
      <div style="width:14px;height:14px;border-radius:50%;background:var(--success)"></div>
      <div style="width:0"></div>
    </div>
    <div><strong style="font-size:16px">W8 · Sep 2 — calm</strong><div style="font-size:14px;color:var(--muted)">31 deploys/wk · p95 243ms · 83.4% hits</div></div>
  </div>
  <p class="dgm-src">Rail dots: muted = past pain, primary = intervention, success = outcome. ±2pt sampling error.</p>
</div>
```

Tokens: rail `2px var(--border)`, dots `14px` circles, stop gap `24px` bottom padding, dates bold `16px` with metric line `14px muted` beneath. Exactly one `success` dot (the outcome).

### Per-engine notes
- **reveal.js:** reveal stops top-to-bottom with fragments; keep the rail itself always visible so late stops have context.
- **Slidev:** same HTML; UnoCSS `grid grid-cols-[28px_1fr]` works. Avoid `v-motion` on the rail (export jitter).
- **Marp:** vertical rail exports perfectly to PDF; cap at 5 stops so it fits one Marp page without scrolling.

---

## 4. Org / tree (who owns what)

### When to use
Ownership at a glance: platform team for the Green train. One lead, three to four owners, each with one metric they move. Max 5 nodes.

### When to avoid
Reporting-line politics (use a handout). More than 5 people (faces shrink past recognition — show leads only, `+ N` the rest).

### Copy-paste HTML sketch

```html
<div class="dgm-card" style="text-align:center">
  <p class="dgm-title">Platform team — Green train owners</p>
  <p class="dgm-sub">One metric per owner · Sep 2026</p>
  <div class="dgm-box" style="display:inline-block;min-width:280px"><strong>Ada Okafor — Platform Lead</strong><small>owns p95 243ms · shield 83.4%</small></div>
  <div style="display:grid;grid-template-columns:32px 1fr 32px;align-items:start;margin:0 auto;max-width:560px" aria-hidden="true">
    <div style="border-top:2px solid var(--border);border-left:2px solid var(--border);height:24px;border-top-left-radius:8px"></div>
    <div style="border-top:2px solid var(--border);height:24px"></div>
    <div style="border-top:2px solid var(--border);border-right:2px solid var(--border);height:24px;border-top-right-radius:8px"></div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;text-align:left">
    <div class="dgm-box"><strong>Jonas Weber</strong><small>Checkout API · 14 ships</small><div style="font-size:14px;margin-top:8px">Load gate 3.1× peak.</div></div>
    <div class="dgm-box"><strong>Maria Santos</strong><small>Billing · 5 ships</small><div style="font-size:14px;margin-top:8px">Double-charge guard Oct 21.</div></div>
    <div class="dgm-box"><strong>Kenji Tanaka</strong><small>Search · 3 ships</small><div style="font-size:14px;margin-top:8px">Reindex 47 min freeze.</div></div>
  </div>
  <p class="dgm-src">+ 14 engineers on rotation. Photos on the title slide; names + metrics here.</p>
</div>
```

Connectors are CSS borders (`2px var(--border)` elbows), not images — they survive grayscale and PPTX. Every node names its metric (`14 ships`, `47 min freeze`).

### Per-engine notes
- **reveal.js:** raw HTML; add `alt`-style caption listing the hierarchy for screen readers (connectors are `aria-hidden`).
- **Slidev:** `grid grid-cols-3 gap-4` for reports; keep connector elbows as plain `<div>` borders (UnoCSS `border-t-2`).
- **Marp:** elbows + boxes export as vector; keep `min-width: 280px` on the lead so the tree never collapses.

---

## Label + accessibility rules

- Floor `14px` everywhere: titles `16px/700`, owner lines `15px`, meta `14px muted`. If it does not fit at `14px`, cut a box — never shrink type.
- Decorative connectors (`→`, rails, elbows) are `aria-hidden`; meaning lives in DOM order + visible source line + SVG `role="img"` labels.
- Print check: one architecture + one timeline in grayscale — hero borders (`2px primary/success`) must still read as shape, not hue.

## Anti-slop don't

- Don't label anything under `14px` or draw arrows without numbers — every connector carries its value (`purge ~90s`, `83.4% hits`, `09:14`), and every box names an owner plus one real metric.
