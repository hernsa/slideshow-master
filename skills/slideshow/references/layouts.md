# Layouts — 6 Box Patterns

Global tokens: spacing `8 / 16 / 24 / 32 / 48 / 64` (8pt scale). Type via `clamp()`, e.g. `h1: clamp(2rem, 5vw, 3.5rem)`. Radius `12-24px` (cards `16px`). Images: `radius 16px`, `1px border var(--border)`, soft shadow, `aspect-ratio: 16/9`, `object-fit: cover`.

## 1. Bento grid

- Use: overview slides with 4-6 items.
- Avoid: dense text blocks; one line + one metric per cell max.

```html
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
  <div style="grid-column:span 2;grid-row:span 2;background:var(--surface);border-radius:16px;padding:24px">
    <h3>Hero metric</h3><p>$2.4M ARR</p>
  </div>
  <div style="background:var(--surface);border-radius:16px;padding:24px">NPS 72</div>
  <div style="background:var(--surface);border-radius:16px;padding:24px">Churn 1.1%</div>
  <div style="background:var(--surface);border-radius:16px;padding:24px">NRR 128%</div>
  <div style="background:var(--surface);border-radius:16px;padding:24px">CAC $410</div>
</div>
```

## 2. Split 50/50

- Use: text vs visual (screenshot, diagram, quote).
- Avoid: heavy text on both sides; cap left column at 3 bullets.

```html
<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center">
  <div><h2>Ships in minutes</h2><ul><li>One CLI</li><li>Preview URLs</li><li>Rollback</li></ul></div>
  <img src="deploy.png" alt="Deploy dashboard" style="border-radius:16px;aspect-ratio:16/9;object-fit:cover;width:100%" />
</div>
```

## 3. Callout (max 1 per slide)

- Use: single info / tip / warning / danger note.
- Avoid: stacking two callouts; body copy inside callout.

```html
<div style="border-left:4px solid #2563EB;background:#EFF6FF;padding:16px 24px;border-radius:12px">Info: migration is reversible until step 3.</div>
<!-- tip: border #16A34A bg #F0FDF4 | warning: border #F59E0B bg #FFFBEB | danger: border #DC2626 bg #FEF2F2 -->
```

## 4. Stat cards (row of 3-4)

- Use: KPI comparison; label + big number + delta.
- Avoid: more than 4 cards; two deltas per card.

```html
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
  <div style="background:var(--surface);border-radius:16px;padding:24px"><small>ARR</small><div style="font-size:2rem">$2.4M</div><span style="color:#16A34A">+18%</span></div>
  <div style="background:var(--surface);border-radius:16px;padding:24px"><small>NPS</small><div style="font-size:2rem">72</div><span style="color:#16A34A">+6</span></div>
  <div style="background:var(--surface);border-radius:16px;padding:24px"><small>Churn</small><div style="font-size:2rem">1.1%</div><span style="color:#16A34A">-0.3pp</span></div>
</div>
```

## 5. Quote

- Use: one quote + avatar + name/role.
- Avoid: long paragraphs; keep quote under 25 words.

```html
<figure style="text-align:center;max-width:640px;margin:0 auto">
  <img src="ada.jpg" alt="Portrait of Ada Okafor" style="width:64px;height:64px;border-radius:50%;object-fit:cover" />
  <blockquote style="font-size:1.5rem">"Deploy day went from fear to routine."</blockquote>
  <figcaption>Ada Okafor — Platform Lead, Acme</figcaption>
</figure>
```

## 6. Code + preview side-by-side

- Use: live API / component demo; code capped at 12 lines.
- Avoid: full file dumps; shrink font below 14px to fit.

```html
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">
  <pre style="background:#0D1117;color:#E6EDF3;border-radius:16px;padding:24px;font-size:15px"><code>const app = createApp();
app.get("/health", () => ({ ok: true }));
app.listen(3000);</code></pre>
  <iframe src="./demo/" title="Live demo" style="border:1px solid var(--border);border-radius:16px;width:100%;aspect-ratio:16/9"></iframe>
</div>
```
