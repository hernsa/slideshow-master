# Code demo layout

> Syntax beside behavior. Code capped at 12 lines, preview proves it.
> Reuses `layouts.md` code tokens: gap `24px`, code `15px/1.6` mono,
> padding `24px`, preview `16/9` plus border plus `16px` radius.

## When to use

- Live API or component demos where syntax must map to behavior.
- Three-line fixes with a visible before/after effect.
- CLI flows where the command output is the proof.
- Split into two slides or link the repo when the file runs long.

## Copy-paste HTML sketch

```html
<div class="slide-inner">
  <div class="eyebrow">The fix — three lines</div>
  <h2>Shield on, origin rests</h2>
  <div class="tpl-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start;margin-top:24px">
    <pre style="background:#0D1117;color:#E6EDF3;border-radius:16px;padding:24px;font-size:15px;line-height:1.6;overflow:auto;margin:0"><code>shield.enable({
  staleWhileRevalidate: 90,
  bypass: ["POST", "auth*"]
});
// hit rate 61% to 83% in one day
// full module: link in notes</code></pre>
    <div>
      <img src="assets/shield-demo.png" alt="Demo showing cache hit rate jumping to 83 percent after enabling shield" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:16px;border:1px solid var(--border);display:block" />
      <p style="font-size:14px;opacity:.65;margin-top:8px">Screenshot stand-in. Live frame in presenting view only.</p>
    </div>
  </div>
</div>
```

## Spacing and type tokens

- Code block: `JetBrains Mono`, `15px`, `line-height: 1.6`, dark
  `#0D1117` ground with `#E6EDF3` text, Shiki dual theme in real builds.
- Preview keeps `img.fit` treatment: border, radius, `16/9`, no stretch.
- Caption `14px` muted names the fallback for PDF export.
- Never below `14px` code to squeeze lines. Cut lines instead.

## Per-engine notes

- **reveal.js:** highlight.js or Shiki plugin for `<pre><code>`.
  Live iframe goes in the right cell with `title` set. PDF uses
  the screenshot variant because iframes print blank.
- **Slidev:** fenced blocks with `{1,3}` line highlights and Monaco
  runnable via `code-runnable`. `v-click` steps map to per-line reveals.
- **Marp:** fenced code only. Iframes export poorly, so always ship
  the screenshot variant plus the demo URL in notes.

## Responsive

```css
@media (max-width: 800px) {
  .tpl-grid { grid-template-columns: 1fr !important; }
}
```

## Accessibility

- Code is real text, never a code screenshot. Screen readers get the lines.
- Iframe carries a `title` describing the demo outcome.

## Anti-slop don't

- Don't dump a 28-line file at 11px. Show the 5 lines you narrate,
  link the rest in speaker notes.
