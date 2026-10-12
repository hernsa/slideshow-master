# Icons — Inline SVG System + Spec + Layout Patterns

> Base deck CSS + canonical tokens live in `references/layouts.md` — paste once
> from there, then paste any sketch below. Engine specifics live in
> `references/engines.md`; responsive + motion rules live in `references/layouts.md`.

## 1. The system: inline SVG only

Ship every icon as inline `<svg>` pasted directly into the slide HTML. No exceptions for deck-critical icons (arrows, checks, status, chart glyphs, quote marks).

### 1.1 Banned: emoji-as-icons (never `✅ 🚀 ⚠️ 📊 ❤️`)

Rendering varies by OS, browser, and projector machine — the same warning slide
shows a flat triangle on macOS, a thick blob on Windows, a monochrome outline in
PDF. Emoji follows font metrics, not the 8pt grid, so a 24px emoji sits 2–3px
off the baseline. Color cannot inherit `currentColor`; export rasterizes at low
resolution; screen readers announce "rocket" instead of the label. Acme pilot
slide used `⚠️ Memphis paused` — venue laptop showed a flat orange square, PDF
rasterized both glyphs soft.

Fix: replace every emoji with the §2 stroke spec, each paired with a visible
label. Search the deck for emoji codepoints before shipping:

```bash
python scripts/check-repo.py
# Gate 5 also greps for stray emoji in slides
```

### 1.2 Banned: external icon fonts (never FontAwesome / Material / CDN `@font-face`)

Slides render, then icons pop in 300–800ms later when the font arrives — on venue
Wi-Fi this flickers every slide change. Blocked CDNs show tofu boxes where checks
belong. PDF and static export embed text fonts, not icon-font codepoints, so
handouts show blank squares. Version drift renames glyphs; `font-weight`
ligatures break `currentColor` theming. Acme pasted a FontAwesome CDN across
twelve slides — venue Wi-Fi blocked it, export showed blank squares.

Fix: remove the CDN link, paste the §2 SVGs inline, re-export with Wi-Fi
disabled. Grep for `font-awesome`, `cdnjs`, `fa-solid` before shipping — zero
matches required. Inline SVG has zero requests, zero FOUC, embeds in PDF.

### 1.3 Allowed set

- Inline `<svg>` with `viewBox="0 0 24 24"`, `fill="none"`, `stroke="currentColor"`.
- Inline `<svg>` for logos or product marks only when the mark is a single-color simplified glyph redrawn at 24x24. Full-color brand SVGs go in `references/media/images.md`, not here.
- CSS shapes for dots and timeline nodes (`border-radius: 999px`) when no glyph meaning is needed.

Keep the deck icon vocabulary under 12 distinct glyphs. Acme Launch Review deck uses exactly 8: arrow-right, check, alert-triangle, chart-bar, quote-mark, box, clock, shield.

## 2. Stroke-icon spec

Every deck icon follows one spec so icons from different authors match.

```html
<!-- spec template -->
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><g><!-- paths --></g></svg>
```

Rules:

- `viewBox="0 0 24 24"` always. Size with `width` / `height` attributes or CSS, never by editing the viewBox.
- `stroke-width="2"` at 24px base. Scale stroke proportionally only per §3 ladder.
- `stroke-linecap="round"`, `stroke-linejoin="round"` always. Square caps read harsh on projectors.
- `fill="none"` default. Fill only the dot in `alert-circle` style glyphs, never the whole body.
- `stroke="currentColor"` always. Never hardcode `stroke="#000"`. Hardcoded black vanishes on `.dark` (`--bg: #0B1020`).
- `aria-hidden="true"` on decorative icons. Add `<title>` only when the icon alone conveys meaning, and prefer a visible label instead.
- 2px minimum clearspace inside the viewBox. No path should touch `x=0` or `x=24`. Pad inward by 2 units.

### 2.1 arrow-right

Use for next step, CTA direction, flowchart connectors.

```html
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
```

Acme usage: "Ship v2.4 to pilot warehouses" CTA with arrow-right in `--primary`.

### 2.2 check

Use for passed QA gate, completed rollout step, success delta.

```html
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
```

Acme usage: green check next to "p95 latency 243ms, target met" in `--success`.

### 2.3 alert-triangle

Use for risk, breach of SLO, pilot blocker.

```html
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
```

Acme usage: amber alert-triangle in warehouse rollout callout: "Memphis hub paused, scanner firmware 1.8.2 mismatch."

### 2.4 chart-bar

Use for metric cards, experiment results, traction slides.

```html
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>
```

Acme usage: chart-bar chip above "$2.4M ARR, +18% YoY" hero stat.

### 2.5 quote-mark

Use for customer proof slides. Drawn as two filled commas with stroke outline for consistency.

```html
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2.75 2.5-2.75 2.5V11h5V5H4c1.5 0 2 1 2 2v4c0 4-4 6-4 6v4z"/><path d="M14 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2.75 2.5-2.75 2.5V11h5V5h-2c1.5 0 2 1 2 2v4c0 4-4 6-4 6v4z" transform="translate(1 0)"/></svg>
```

Acme usage: quote-mark in `--accent` above "Acme cut dock idle time 31% in six weeks. Rollout took one shift." — Priya Nair, Ops Lead, Port of Tacoma pilot.

Normalize any new glyph to this spec before pasting. Resize via CSS, never by redrawing at 16x16.

## 3. Sizing ladder + pairing rules

### 3.1 Sizing ladder

Five sizes only. No 14px, 18px, 28px, or 64px icons.

| Size | Use | Stroke | Example |
|---|---|---|---|
| `16px` | inline with body `17-19px` and captions `14px`, timeline meta | `2px` unchanged | check inside "Deployed to 14 docks" line |
| `20px` | card eyebrow glyph, callout glyph, button glyph | `2px` unchanged | alert-triangle in warning callout |
| `24px` | default, feature chip glyph, stat card glyph | `2px` | chart-bar in ARR card |
| `32px` | hero stat glyph, section-divider glyph | `2px`, increase to `2.25px` if projected in 200+ seat room | chart-bar above $2.4M ARR hero |
| `48px` | title-hero single accent only, max one per deck | `1.75px` to keep optical weight light | oversized quote-mark on closing proof slide |

CSS ladder (paste once):

```css
.icon { display: inline-flex; flex-shrink: 0; color: inherit; }
.icon svg { display: block; }
.icon-16 svg { width: 16px; height: 16px; }
.icon-20 svg { width: 20px; height: 20px; }
.icon-24 svg { width: 24px; height: 24px; }
.icon-32 svg { width: 32px; height: 32px; }
.icon-32 svg { stroke-width: 2.25; }
.icon-48 svg { width: 48px; height: 48px; }
.icon-48 svg { stroke-width: 1.75; }
```

Never set icon `width` larger than its text partner by more than 8px. A 48px icon next to 14px caption text crushes the line.

### 3.2 Pairing rules

- Icon plus label is the default unit. Pair every meaningful icon with a `12-14px` uppercase label (`letter-spacing: .12em`) or a full sentence. Icon plus "P95 LATENCY" works. Icon alone does not.
- Vertical rhythm: icon to label gap `8px` inline, `16px` stacked. Card padding `24px` standard, `32px` hero. Row gaps `16px`, section gaps `32px` or `48px`.
- Icon chips: `48px` circle or rounded square with `background: var(--surface)`, `border: 1px solid var(--border)`, `border-radius: 999px` for status or `16px` for feature. Center the 24px glyph inside. Chip carries the background, glyph carries `currentColor`.

```html
<div style="width:48px;height:48px;border-radius:999px;background:var(--surface);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;color:var(--primary)">
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>
</div>
<div style="font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;opacity:.65;margin-top:16px">P95 latency</div>
```

- Baseline alignment: inline 16px icons get `vertical-align: -3px` and `margin-right: 8px`. Test at 100% and 200% zoom.
- Touch and click targets: linked icons keep `32px` minimum hit area with `8px` padding around a 16-20px glyph.

## 4. Layout patterns

All sketches assume `.slide-inner` and base deck CSS from `references/layouts.md`. Gaps and padding use 8pt tokens only. Dropped patterns (three-up feature row, timeline rail) reuse the same chips, rail offsets, and gaps from the two sketches below — see `references/layouts.md` grid block.

### 4.1 Icon plus stat card

Use for traction, experiment readout, SLO dashboard. One hero plus two satellites maximum per slide.

```html
<div class="slide-inner">
  <div class="eyebrow">Tacoma pilot · week 6</div>
  <h2 style="font-size:clamp(1.5rem,3vw,2.25rem)">Dock throughput held during peak</h2>
  <div style="display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:16px;margin-top:32px">
    <div style="background:var(--card);border:1px solid var(--border);border-radius:16px;padding:32px">
      <div style="width:48px;height:48px;border-radius:999px;background:var(--surface);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;color:var(--primary)">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>
      </div>
      <div style="font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;opacity:.65;margin-top:16px">Containers / hour</div>
      <div style="font-size:3rem;font-weight:800;letter-spacing:-0.02em;line-height:1.05">42</div>
      <div style="color:var(--success);font-weight:600;font-size:17px">▲ +12% vs baseline</div>
    </div>
    <div style="background:var(--card);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div style="color:var(--success);display:inline-flex"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg></div>
      <div style="font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;opacity:.65;margin-top:16px">P95 scan time</div>
      <div style="font-size:2rem;font-weight:700">243ms</div>
      <p style="font-size:14px;opacity:.65;margin:8px 0 0">Down from 412ms. Target 250ms.</p>
    </div>
    <div style="background:var(--card);border:1px solid var(--border);border-radius:16px;padding:24px">
      <div style="color:var(--warning);display:inline-flex"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div>
      <div style="font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;opacity:.65;margin-top:16px">Uptime</div>
      <div style="font-size:2rem;font-weight:700">99.2%</div>
      <p style="font-size:14px;opacity:.65;margin:8px 0 0">Memphis hub paused for firmware.</p>
    </div>
  </div>
</div>
```

Keep delta text `17px` semibold with arrow plus sign plus color, never color alone.

### 4.2 Callout with icon

Use for single risk, dependency, or ask. One callout per slide maximum.

```html
<div class="slide-inner">
  <div class="eyebrow">Deployment ask</div>
  <h2 style="font-size:clamp(1.5rem,3vw,2.25rem)">We need one night-shift window</h2>
  <div style="display:flex;gap:16px;background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--warning);border-radius:16px;padding:24px;margin-top:32px">
    <div style="color:var(--warning);flex-shrink:0"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div>
    <div>
      <div style="font-weight:700;font-size:17px">Memphis crane firmware 1.8.2 mismatches scanner queue</div>
      <p style="font-size:17px;opacity:.8;margin:8px 0 0">Approve Sunday 02:00–05:00 CT maintenance window. Rollback image staged. Priya Nair owns go/no-go.</p>
      <p style="font-size:14px;opacity:.65;margin:8px 0 0">Source: Field log 2026-03-14, run 412.</p>
    </div>
  </div>
</div>
```

Icon `20px`, gap `16px`, padding `24px`, left accent border `4px` in semantic color, caption `14px` with real source.

## 5. Color rules

- Icons inherit semantic variables only. Active primary action uses `color: var(--primary)`. Accent moments use `color: var(--accent)`. Status uses `var(--success)`, `var(--warning)`, `var(--danger)`. Default body icons use `inherit` or `var(--fg)`. Inactive steps use `var(--muted)`.
- One accent per slide. If the hero stat chip is `--primary`, feature chips on the same slide stay `--primary` or neutral. Never assign primary, accent, success, warning, and danger to five adjacent chips to decorate.
- Never build rainbow icon rows. Acme anti-example: five feature chips in blue, purple, green, amber, red with no meaning. Fix: all chips neutral `var(--fg)` except the single conversion-driving chip in `--primary`.
- Dark mode check mandatory. Toggle `.dark` and confirm `--primary: #4F7DF3` and `--muted: #8A93A6` meet 4.5:1 on `--card: #141B30`. Muted icons on surface fail most often — test `var(--muted)` on `var(--surface)` before shipping.
- Deltas pair arrow plus sign with color, never color alone. Success delta shows `▲ +12%` in `var(--success)`. Danger delta shows `▼ -4.2%` in `var(--danger)`.
- Code: reference variables, never raw hex. If a hex appears outside `:root` or `@theme`, it is a bug. `color="#2563EB"` on an SVG is a bug. `color="var(--primary)"` on the wrapper is correct.

```html
<!-- correct: wrapper owns color, SVG inherits -->
<div style="color:var(--success)"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg></div>
```

## 6. Per-engine notes

- reveal.js: paste inline SVG directly into `<section>`; keep `width` / `height` attributes so slides render before CSS loads; wrap chip plus text in one `.fragment` so the icon never appears without its label. Details in `references/engines.md`.
- Slidev: define one `IconChip.vue` component and reuse it; never import an icon-font package; UnoCSS `w-6 h-6` = 24px, `w-5 h-5` = 20px, `w-4 h-4` = 16px. Details in `references/engines.md`.
- Marp: set `html: true` in frontmatter, keep SVGs on one line to avoid Markdown paragraph splitting, verify PDF export shows glyphs with Wi-Fi disabled. Details in `references/engines.md`.
- Responsive collapse, reduced motion, and grid rules live in `references/layouts.md` — not duplicated here.

## 7. Failures plus fixes

### 7.1 One-pixel strokes disappearing on projectors

Failure: custom glyphs drawn at `stroke-width="1"` looked refined on a Retina MacBook and vanished on a 1024x768 venue projector. Timeline nodes became empty circles from row six.

Fix: reset all deck glyphs to `stroke-width="2"` at 24px base, `2.25` at 32px for large rooms. Re-test by projecting one timeline slide and walking to the back row. If the 16px node glyph is unreadable past ten feet, bump nodes to 20px glyph inside the 32px circle.

### 7.2 Fixed black fill invisible on dark mode

Failure: copied glyph used `fill="#000" stroke="#000"`. On light theme it looked fine. After `.dark` toggle (`--bg: #0B1020`, `--card: #141B30`) the icon disappeared into the background during Q&A.

Fix: set `fill="none" stroke="currentColor"` on every SVG and move color to the wrapper (`color: var(--fg)` or semantic variable). Toggle `.dark` and check contrast: normal glyphs 4.5:1 minimum, large 32-48px glyphs 3:1 minimum.

### 7.3 Forty-eight-pixel icons next to fourteen-pixel text

Failure: 48px chart-bar chip beside `14px` "Source: field log" caption dominated the card. Readers saw the glyph before the $2.4M ARR number.

Fix: apply the ladder. Hero number gets 32px glyph maximum, caption gets 16px inline glyph with `vertical-align: -3px`. Keep size delta under 8px between adjacent icon and text. Reserve 48px for a single title-hero accent per deck.

### 7.4 Icon-only buttons with no label

Failure: closing slide used three icon-only circles (arrow, check, quote) as navigation with no labels. Audience did not know which opened the pilot video. Screen reader announced "button, button, button."

Fix: pair every actionable icon with a visible label. "Watch 2-min Tacoma walkthrough" plus arrow-right. "Download pilot report (PDF)" plus check. Keep `aria-hidden="true"` on the glyph and put the accessible name on the button text. Minimum hit area `32px` with `8px` padding.

---

Anti-slop rule for icons: one vocabulary, one stroke, one accent per slide. If a second accent color appears, it must signal status, not decoration.
