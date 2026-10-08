# Tables — Comparison, Checklist, Metric, Rating

> Exact values live here; charts tell the trend, tables settle the argument. Spacing `16px` cell padding (`16px 24px`), radius `16px` wrapper, header `13px` uppercase muted, body `16–17px`, captions `14px`. Zebra via `var(--surface)`, borders `1px solid var(--border)`, numbers `tabular-nums`.

Shared table CSS (paste once):

```css
.tbl-wrap { border: 1px solid var(--border); border-radius: 16px; overflow: auto; background: var(--card); }
table.data { width: 100%; border-collapse: collapse; font-size: 16px; min-width: 560px; }
table.data th { text-align: left; font-size: 13px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); background: var(--surface); padding: 12px 24px; white-space: nowrap; }
table.data td { padding: 16px 24px; border-top: 1px solid var(--border); vertical-align: top; }
table.data tr:nth-child(even) td { background: color-mix(in srgb, var(--surface) 55%, transparent); }
table.data .tnum { font-variant-numeric: tabular-nums; }
.tbl-src { font-size: 14px; color: var(--muted); margin-top: 8px; }
@media (max-width: 800px) { table.data td, table.data th { padding: 12px 16px; } }
```

Responsive overflow rule (mandatory): every `table.data` sits inside `.tbl-wrap` with `overflow: auto` + `min-width: 560px` so narrow viewports scroll horizontally instead of crushing columns. Never shrink body below `15px` to fit.

Spacing / type tokens: header `13px/700` uppercase `letter-spacing .08em`, body `16px/1.5`, caption `16–17px/700` with `16px` padding, source `14px muted`. Row divider `1px var(--border)`; wrapper radius `16px` clips zebra stripes.

---

## 1. Comparison matrix (plan / tier / option verdict)

### When to use
Tier or vendor verdicts: cache plans, release-train scope, region rollout order. Header states the winner; the table shows why. Max 4 columns, 5 rows.

### When to avoid
More than 4 options (columns crush past `560px` min-width — demote extras to a handout). Rows with long paragraphs (one value + one short note per cell, max).

### Copy-paste HTML sketch

```html
<div class="tbl-wrap">
  <table class="data">
    <caption style="text-align:left;padding:16px 24px;font-weight:700">Cache plans — Blue train pick: Shield Pro</caption>
    <thead><tr><th scope="col">Capability</th><th scope="col">Hobby</th><th scope="col">Shield Pro ★</th><th scope="col">Enterprise</th></tr></thead>
    <tbody>
      <tr><td>Price / mo</td><td class="tnum">$0</td><td class="tnum"><strong>$49</strong> · 4.7M req incl.</td><td class="tnum">$390</td></tr>
      <tr><td>Hit rate (Sep)</td><td class="tnum">41.3%</td><td class="tnum"><strong>83.4%</strong></td><td class="tnum">87.1%</td></tr>
      <tr><td>Purge propagate</td><td class="tnum">~6 min</td><td class="tnum"><strong>~90 sec</strong></td><td class="tnum">~45 sec</td></tr>
      <tr><td>Rollback</td><td>Manual</td><td><strong>One-click</strong></td><td>One-click + policy</td></tr>
      <tr><td>On-call pages / mo</td><td class="tnum">6</td><td class="tnum"><strong>1</strong></td><td class="tnum">0</td></tr>
    </tbody>
  </table>
</div>
<p class="tbl-src">Source: vendor docs + Sep edge logs. ★ = chosen for Green train (Oct 2).</p>
```

Winner column carries `★` + `<strong>` so grayscale still finds it. Keep units inside cells (`$49`, `83.4%`), never in a footnote chase.

### Per-engine notes
- **reveal.js:** raw HTML. Highlight the winner with a second `data-auto-animate` slide that tints the column `background: var(--surface)`.
- **Slidev:** same HTML, or UnoCSS `table w-full border-collapse` + `th:uppercase text-[13px]`. Markdown tables lose zebra — prefer this HTML.
- **Marp:** HTML table inside Markdown works but theme CSS may reset padding — keep inline `padding` on `th`/`td` as above.

---

## 2. Feature checklist matrix (who has what)

### When to use
Coverage audits: which service has preview URLs, shield, auto-rollback. Check = shipped, dash = planned with a date, cross = out of scope. Max 6 rows.

### When to avoid
Grading quality (use §4 rating dots). More than 4 service columns (rotate to two slides: Green train, then Blue train).

### Copy-paste HTML sketch

```html
<div class="tbl-wrap">
  <table class="data">
    <caption style="text-align:left;padding:16px 24px;font-weight:700">Release-train readiness — Green vs Blue</caption>
    <thead><tr><th scope="col">Capability</th><th scope="col">Checkout API</th><th scope="col">Edge shield</th><th scope="col">Billing worker</th></tr></thead>
    <tbody>
      <tr><td>Preview URL per push</td><td>✓ shipped</td><td>✓ shipped</td><td><span style="opacity:.7">— lands Oct 14</span></td></tr>
      <tr><td>One-click rollback</td><td>✓ shipped</td><td>✓ shipped</td><td>✓ shipped</td></tr>
      <tr><td>Stale-while-revalidate 90s</td><td>✓ shipped</td><td>✓ shipped</td><td><span style="opacity:.7">— lands Oct 21</span></td></tr>
      <tr><td>Load-test gate (2× peak)</td><td>✓ 3.1×</td><td>✓ 2.4×</td><td>✕ out of scope</td></tr>
      <tr><td>On-call runbook linked</td><td>✓ shipped</td><td><span style="opacity:.7">— draft Oct 9</span></td><td>✕ out of scope</td></tr>
      <tr><td>Purge ≤ 90 sec verified</td><td>✓ 87 sec</td><td>✓ 62 sec</td><td><span style="opacity:.7">— test Oct 18</span></td></tr>
    </tbody>
  </table>
</div>
<p class="tbl-src">Owner: Ada Okafor. Dashes carry dates; crosses are decisions, not gaps.</p>
```

Use text glyphs (`✓`, `—`, `✕`) plus words (`shipped`, `lands Oct 14`), never emoji-color alone. Dashes always carry a date; crosses mean deliberately excluded.

### Per-engine notes
- **reveal.js:** raw HTML; reveal rows with `class="fragment"` only if you narrate each — otherwise static.
- **Slidev:** UnoCSS `text-green-600 font-semibold` for `✓` is fine, but keep the word `shipped` for export grayscale.
- **Marp:** `✓ / ✕` glyphs export to PDF/PPTX cleanly; emoji variants do not — stick to text glyphs.

---

## 3. Metric table (weekly numbers, tabular-nums)

### When to use
The appendix-grade truth: 6–8 weeks of p95, deploys, rollbacks side by side. One row per week, newest last, deltas in the final row.

### When to avoid
Blending windows (weekly + monthly rows in one table). More than 6 visible rows on a presented slide (fold middle weeks, disclose it, link the full ledger).

### Copy-paste HTML sketch

```html
<div class="tbl-wrap">
  <table class="data">
    <caption style="text-align:left;padding:16px 24px;font-weight:700">Recovery ledger — Jul 19 → Sep 2 (8 wks)</caption>
    <thead><tr><th scope="col">Week</th><th scope="col">p95</th><th scope="col">Deploys</th><th scope="col">Rollbacks</th><th scope="col">Hit rate</th></tr></thead>
    <tbody>
      <tr><td>W1 · Jul 19</td><td class="tnum">412ms</td><td class="tnum">4</td><td class="tnum">3</td><td class="tnum">58.2%</td></tr>
      <tr><td>W2 · Jul 26 ★</td><td class="tnum">388ms</td><td class="tnum">7</td><td class="tnum">2</td><td class="tnum">64.7%</td></tr>
      <tr><td>W4 · Aug 9</td><td class="tnum">338ms</td><td class="tnum">13</td><td class="tnum">2</td><td class="tnum">71.9%</td></tr>
      <tr><td>W6 · Aug 23</td><td class="tnum">271ms</td><td class="tnum">24</td><td class="tnum">1</td><td class="tnum">79.6%</td></tr>
      <tr><td>W8 · Sep 2</td><td class="tnum"><strong>243ms</strong></td><td class="tnum"><strong>31</strong></td><td class="tnum"><strong>2</strong></td><td class="tnum"><strong>83.4%</strong></td></tr>
    </tbody>
  </table>
</div>
<p class="tbl-src">★ shield rollout week. Edge logs + deploy ledger. ±2pt sampling error; W3/W5/W7 folded for slide fit — full log in handout.</p>
```

Every numeric column is `class="tnum"` so `412 / 388 / 338` align. Folded weeks are disclosed in the source line — never silently drop rows.

### Per-engine notes
- **reveal.js:** keep the full table static; use a second slide to zoom one row rather than animating cells.
- **Slidev:** UnoCSS `tabular-nums` utility equals `.tnum`. Long tables overflow the slide — cap at 6 rows visible.
- **Marp:** best exporter of the three for tables; `min-width: 560px` + `.tbl-wrap` scroll keeps PDF columns intact.

---

## 4. Rating matrix (dots, not fake precision)

### When to use
Qualitative verdicts with honest granularity: migration risk per service, docs quality per endpoint. Dots (●●●○○) plus a one-line note — never `4.73/5`.

### When to avoid
Measured data with real units (use §3 metric table). More than 5 dot levels (audiences cannot distinguish ●●●●○ from ●●●●● at 10 feet).

### Copy-paste HTML sketch

```html
<div class="tbl-wrap">
  <table class="data">
    <caption style="text-align:left;padding:16px 24px;font-weight:700">Cutover risk by service — Oct review</caption>
    <thead><tr><th scope="col">Service</th><th scope="col">Risk</th><th scope="col">Note</th></tr></thead>
    <tbody>
      <tr><td>Edge shield</td><td aria-label="1 out of 5">●○○○○</td><td>Proven 6 wks, auto-rollback clean.</td></tr>
      <tr><td>Checkout API</td><td aria-label="2 out of 5">●●○○○</td><td>Needs load gate re-run at 2× peak.</td></tr>
      <tr><td>Search index</td><td aria-label="3 out of 5">●●●○○</td><td>Reindex takes 47 min; freeze writes.</td></tr>
      <tr><td>Billing worker</td><td aria-label="4 out of 5">●●●●○</td><td>Double-charge guard untested — Oct 21.</td></tr>
    </tbody>
  </table>
</div>
<p class="tbl-src">Rated by Jonas Weber + Maria Santos, Oct 6. Dots are judgment, not measurement.</p>
```

Dots are `var(--fg)` filled + `var(--border)` empty via `○`; add `aria-label` with the count. The note column is mandatory — a dot without a reason is decoration.

### Per-engine notes
- **reveal.js:** raw HTML; dots are text so they scale and print perfectly.
- **Slidev:** same HTML. Do not substitute a star-icon component — icon fonts vanish in PDF export.
- **Marp:** text dots survive PPTX export; background-tinted cells do not always — keep meaning in the glyphs.

---

## Accessibility + print

- Headers always `scope="col"`; numeric cells get `tnum`; rating dots get `aria-label` (`1 out of 5`).
- Never color alone: winner = `★` + bold, shipped = `✓` + word, risk = dots + note sentence.
- Print check: one bento-style table in grayscale — borders (`1px var(--border)`) must survive and `★`/`✓`/`✕` must still read.

## Anti-slop don't

- Don't ship `99.99%` uptime or `4.73/5` ratings — use organic `47.2%`, `83.4%`, `●●●○○` with a dated source line and one folded-rows disclosure.
