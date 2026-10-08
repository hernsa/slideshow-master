# Dark Tech — Neon on Near-Black

> Vibe: server room at 2am, phosphor mono, one live wire. Dev aesthetic with strict glow discipline.

**When to use:** hackathons, infra deep-dives, security talks, perf clinics where code and terminals dominate.
**Avoid when:** daylight keynotes, investor pitches, printed handouts. Neon dies under fluorescents and on paper.

## Tokens (near-black + phosphor)

```css
:root, .dark {
  --bg: #05070D; --surface: #0B1220; --card: #0B1220;
  --fg: #E2F3FF; --muted: #7D8DA6; --border: #1E2A3F;
  --primary: #22D3EE; --accent: #A3E635;
  --success: #4ADE80; --warning: #FBBF24;
  --code-bg: #05070D; --code-fg: #E2F3FF;
}
```

Primary cyan `#22D3EE` for links and structure; accent lime `#A3E635` for exactly one live value per slide. Muted `#7D8DA6` holds at 5.4:1 on bg.

## Typography

Display mono `JetBrains Mono` 700 for headings; body `Inter`; code `JetBrains Mono` 400.

```html
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700;800&family=Inter:wght@400;500&display=swap" rel="stylesheet" />
```

```css
--font-display: "JetBrains Mono", ui-monospace, monospace;
--font-body: "Inter", system-ui, sans-serif;
h1, h2 { font-family: var(--font-display); letter-spacing: -0.02em; }
.prompt { color: var(--accent); }
```

Headings set in mono at 600–800 weight read as machine voice. Keep them short: five words maximum.

## Code theme

Shiki `vitesse-dark` only. There is no light mode in Dark Tech; handouts export as dark-on-black PDF.

```js
const html = await codeToHtml(source, {
  lang: 'rust', theme: 'vitesse-dark'
});
```

## Gradient rule

None as fills. Glow is the gradient substitute, capped at one glowing element per slide.

```css
.glow-one {
  border: 1px solid rgba(34,211,238,.55);
  box-shadow: 0 0 24px rgba(34,211,238,.28), inset 0 0 12px rgba(34,211,238,.08);
}
```

Second glow kills the first. If the terminal glows, the stat stays flat.

## Signature layout — mono headline + glowing terminal

```html
<div class="slide-inner">
  <div class="eyebrow" style="color:#7D8DA6">$ shield --enable --edge</div>
  <h2>p95: 412ms <span style="color:#A3E635">→ 243ms</span></h2>
  <pre class="glow-one" style="background:#05070D;color:#E2F3FF;border-radius:12px;padding:20px;font-size:15px;font-family:'JetBrains Mono',monospace"><code><span style="color:#A3E635">❯</span> shield status --live
edge:     HIT 83% · origin rests
p95:      243ms ▼ −41%
rollback: armed · 2 auto this quarter</code></pre>
  <p style="font-size:14px;color:#7D8DA6">Live edge counters · screenshot in PDF export, iframe only on stage.</p>
</div>
```

## Per-engine notes

- **reveal.js:** force dark with `<section data-background-color="#05070D">`; mono headings need `line-height: 1.1` to avoid clipping descenders.
- **Slidev (UnoCSS):** `bg-[#05070D] text-[#E2F3FF] font-mono` shell; glow via arbitrary `shadow-[0_0_24px_rgba(34,211,238,0.28)]`.
- **Marp (`@theme`):** single dark theme file; set `section { background: #05070D; color: #E2F3FF; }` and `code { font-family: 'JetBrains Mono', monospace; }`.

## Anti-slop don'ts

1. Max one glow per slide. Terminal glows or stat glows, never both, never borders plus text-glow plus shadow.
2. No rainbow syntax or multicolor headings. Cyan structure, lime live-value, slate everything else.
3. No stock circuit-board backgrounds. Near-black flat `#05070D` plus one mono grid overlay at 6% opacity is the texture ceiling.
