# Crimson Bold — Deep Maroon & Red

> Vibe: a raised fist in a dark hall. Deep maroon, signal red, gold as the only flame. The default for history, revolution, and any content that should feel urgent and alive.

**When to use:** history lessons, revolutions, social movements, protest/activism talks, anything with stakes and momentum. The default recommendation for classroom and narrative content.
**Avoid when:** the user explicitly asks for light/paper/minimal, or when the deck is a compliance/legal readout where red reads as danger. On bad projectors the dark maroon holds up better than any cream background.

## Tokens (dark primary + light companion)

```css
:root {
  --bg: #FBF4F0; --surface: #F3E2DA; --card: #FFFFFF;
  --fg: #2B1210; --muted: #7A5C55; --border: #E7CCC3;
  --primary: #B42318; --accent: #C2410C;
  --success: #16A34A; --warning: #D97706;
  --code-bg: #1B1010; --code-fg: #FCE8E4;
}
.dark {
  --bg: #160D0D; --surface: #241515; --card: #2A1A1A;
  --fg: #FFF5F2; --muted: #B8A5A5; --border: #3A2424;
  --primary: #E5484D; --accent: #F4C95D;
  --success: #22C55E; --warning: #FBBF24;
  --code-bg: #1B1010; --code-fg: #FCE8E4;
}
```

Contrast: dark `fg/bg` 15.9:1 AAA. Muted on dark surface 6.2:1 AA. Gold `#F4C95D` is decoration and data only — never body copy.

## Typography

Headings `Syne` 700 (bold, angular, protest-poster energy), body `Inter` 400/500, code `JetBrains Mono` 400.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Syne:wght@600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

```css
--font-display: "Syne", system-ui, sans-serif;
--font-body: "Inter", system-ui, sans-serif;
--font-mono: "JetBrains Mono", ui-monospace, monospace;
h1 { font-size: clamp(2.4rem, 5.5vw, 4rem); letter-spacing: -0.02em; }
```

## Code theme

Shiki `rose-pine-moon` primary, `rose-pine-dawn` for handout. Code background stays `#1B1010` in both modes so screenshots match.

```js
const html = await codeToHtml(source, {
  lang: 'ts', themes: { light: 'rose-pine-dawn', dark: 'rose-pine-moon' }
});
```

## Gradient rule

One radial hero wash per deck, background only. Never gradient text. The wash reads as a bonfire glow.

```css
.hero-crimson {
  background:
    radial-gradient(1200px 500px at 75% -10%, rgba(229,72,77,.4), transparent 60%),
    radial-gradient(900px 420px at 15% 110%, rgba(244,201,93,.16), transparent 60%),
    #160D0D;
}
```

## Signature layout — rally hero + three-count strip

```html
<div class="slide-inner hero-crimson" style="border-radius: 24px">
  <div class="eyebrow">Bourgeois Revolutions · 1640–1789</div>
  <h1>Three revolutions, one idea.</h1>
  <div style="display:flex;gap:16px;margin-top:24px">
    <div style="flex:1;border:1px solid #3A2424;border-radius:16px;padding:20px;background:#2A1A1A">
      <div style="font-size:.8rem;color:#B8A5A5">ANH</div>
      <div style="font-size:2.2rem;font-weight:800;color:#F4C95D">1640</div>
    </div>
    <div style="flex:1;border:1px solid #3A2424;border-radius:16px;padding:20px;background:#2A1A1A">
      <div style="font-size:.8rem;color:#B8A5A5">MỸ</div>
      <div style="font-size:2.2rem;font-weight:800;color:#F4C95D">1776</div>
    </div>
    <div style="flex:1;border:1px solid #3A2424;border-radius:16px;padding:20px;background:#2A1A1A">
      <div style="font-size:.8rem;color:#B8A5A5">PHÁP</div>
      <div style="font-size:2.2rem;font-weight:800;color:#F4C95D">1789</div>
    </div>
  </div>
</div>
```

## Per-engine notes

- **reveal.js:** set CSS vars on `:root` and `section.dark`; toggle `.dark` on `<html>`. Use `data-background-color="#160D0D"` for the hero slide.
- **Slidev (UnoCSS):** map tokens in `uno.config.ts` via `theme.colors`; apply with `bg-bg text-fg border-border`. Set `theme: default` + `colorSchema: dark`.
- **Marp (`@theme`):** define the dark tokens under `section.dark` in theme CSS; force `class: dark` in frontmatter for the dark look.

## Anti-slop don'ts

1. No full-bleed red-to-black linear gradient cover — that is a generic movie-poster cliché. Use the radial bonfire wash only.
2. No more than one gold accent per slide. `#F4C95D` marks numbers and data signals, never headers and never buttons in bulk.
3. No thin `font-weight:300` serif body on the dark maroon. Keep body at Inter 400/500 minimum or it crushes on a projector.
