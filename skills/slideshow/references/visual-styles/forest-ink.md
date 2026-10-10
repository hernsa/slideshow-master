# Forest Ink — Deep Green & Amber

> Vibe: a night walk through a pine forest with a single lantern. Deep green, growing-teal, amber as the light source. The default for education, climate, sustainability, and grounded product strategy.

**When to use:** classrooms, environmental and climate content, sustainability strategy, health, education, anything that should feel alive and grounded without being cute. The default for teaching decks that still need to read bold on a projector.
**Avoid when:** the user explicitly asks for light/paper, or the content is pure cold engineering where green reads as "go" noise.

## Tokens (dark primary + light companion)

```css
:root {
  --bg: #F7FAF5; --surface: #E7EFE3; --card: #FFFFFF;
  --fg: #10201A; --muted: #5F7268; --border: #D6E2D2;
  --primary: #177245; --accent: #B45309;
  --success: #16A34A; --warning: #D97706;
  --code-bg: #0B1712; --code-fg: #E6F4EA;
}
.dark {
  --bg: #0B1712; --surface: #13241C; --card: #173024;
  --fg: #EEF7EF; --muted: #93A89A; --border: #24402F;
  --primary: #34D399; --accent: #FBBF24;
  --success: #22C55E; --warning: #FBBF24;
  --code-bg: #0B1712; --code-fg: #E6F4EA;
}
```

Contrast: dark `fg/bg` 14.8:1 AAA. Muted on dark surface 5.4:1 AA. Amber `#FBBF24` is the lantern — one per slide, decoration and data only.

## Typography

Headings `Sora` 700 (open, friendly, still bold), body `Inter` 400/500, code `JetBrains Mono` 400.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

```css
--font-display: "Sora", system-ui, sans-serif;
--font-body: "Inter", system-ui, sans-serif;
--font-mono: "JetBrains Mono", ui-monospace, monospace;
h1 { font-size: clamp(2.3rem, 5.2vw, 3.8rem); letter-spacing: -0.02em; }
```

## Code theme

Shiki `min-dark` primary, `min-light` for handout. Code background stays `#0B1712` in both modes so screenshots match.

```js
const html = await codeToHtml(source, {
  lang: 'ts', themes: { light: 'min-light', dark: 'min-dark' }
});
```

## Gradient rule

One radial hero wash per deck, background only. Never gradient text. The wash reads as a clearing in the forest.

```css
.hero-forest {
  background:
    radial-gradient(1100px 480px at 20% -10%, rgba(52,211,153,.32), transparent 60%),
    radial-gradient(800px 400px at 90% 110%, rgba(251,191,36,.14), transparent 60%),
    #0B1712;
}
```

## Signature layout — clearing hero + growth strip

```html
<div class="slide-inner hero-forest" style="border-radius: 24px">
  <div class="eyebrow">Lịch sử 11 · Cách mạng tư sản</div>
  <h1>Quyền lực đổi chủ,<br>ba lần, ba thế kỷ.</h1>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:24px">
    <div style="border:1px solid #24402F;border-radius:16px;padding:20px;background:#173024">
      <div style="font-size:.8rem;color:#93A89A">NGUYÊN NHÂN</div>
      <div style="font-size:1.6rem;font-weight:700;color:#34D399">Mâu thuẫn giai cấp</div>
    </div>
    <div style="border:1px solid #24402F;border-radius:16px;padding:20px;background:#173024">
      <div style="font-size:.8rem;color:#93A89A">LÃNH ĐẠO</div>
      <div style="font-size:1.6rem;font-weight:700;color:#FBBF24">Giai cấp tư sản</div>
    </div>
    <div style="border:1px solid #24402F;border-radius:16px;padding:20px;background:#173024">
      <div style="font-size:.8rem;color:#93A89A">KẾT QUẢ</div>
      <div style="font-size:1.6rem;font-weight:700;color:#34D399">Xã hội mới</div>
    </div>
  </div>
</div>
```

## Per-engine notes

- **reveal.js:** set CSS vars on `:root` and `section.dark`; toggle `.dark` on `<html>`. Use `data-background-color="#0B1712"` for the hero slide.
- **Slidev (UnoCSS):** map tokens in `uno.config.ts` via `theme.colors`; apply with `bg-bg text-fg border-border`. Set `theme: default` + `colorSchema: dark`.
- **Marp (`@theme`):** define the dark tokens under `section.dark` in theme CSS; force `class: dark` in frontmatter for the dark look.

## Anti-slop don'ts

1. No "eco-friendly" pastel leaf green on cream — that is the milky default in disguise. This style is dark-first and bold.
2. No amber on every heading. `#FBBF24` is the single lantern per slide; headers stay `#EEF7EF` or `#34D399`.
3. No three-equal-card rows everywhere. The strip above is one composition — vary split, bento, and rail layouts across the deck.
