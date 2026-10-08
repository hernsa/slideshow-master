# Botanical Warm — Human / Edu

> Vibe: sunlit classroom, cream paper, leaf green. The friendliest palette here; trust over precision.

**When to use:** workshops, nonprofits, education, community talks, onboarding where warmth keeps attention.
**Avoid when:** dense dashboards (cream reduces perceived grid alignment) and late-night hacker venues where low light washes out cream backgrounds.

## Tokens (warm paper + evening variant)

```css
:root {
  --bg: #FEFCF8; --surface: #F5F0E6; --card: #FFFDF7;
  --fg: #1C1917; --muted: #78716C; --border: #E7DFCF;
  --primary: #15803D; --accent: #C2410C;
  --success: #15803D; --warning: #C2410C;
  --code-bg: #FFFFFF; --code-fg: #1C1917;
}
.dark {
  --bg: #1C1917; --surface: #292524; --card: #292524;
  --fg: #FAF7F0; --muted: #A8A29E; --border: #44403C;
  --primary: #4ADE80; --accent: #FB923C;
  --success: #4ADE80; --warning: #FB923C;
  --code-bg: #0D1117; --code-fg: #E6EDF3;
}
```

Contrast: `fg/bg` 15.1:1 AAA. Muted `#78716C` on cream 4.6:1 — keep muted at 14px and up.

## Typography

Headings warm serif `Fraunces`, body `Inter`, one handwritten `Caveat` annotation per deck maximum.

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&family=Caveat:wght@500&display=swap" rel="stylesheet" />
```

```css
--font-display: "Fraunces", Georgia, serif;
--font-body: "Inter", system-ui, sans-serif;
--font-hand: "Caveat", cursive;
.annot { font-family: var(--font-hand); font-size: 1.3rem; color: var(--accent); }
```

## Code theme

Shiki `github-light` on neutral white cards, `github-dark` for evening. Warm-tinted code backgrounds shift token hues, so code stays white even on cream slides.

```js
const html = await codeToHtml(source, {
  lang: 'python', themes: { light: 'github-light', dark: 'github-dark' }
});
```

## Gradient rule

One sunrise wash allowed, welcome slide only.

```css
.hero-botanical {
  background: linear-gradient(180deg, #FEFCF8 0%, #F5F0E6 60%, #EDE5D3 100%);
}
```

## Signature layout — welcome + terracotta callout

```html
<div class="slide-inner hero-botanical" style="border-radius:24px;border:1px solid var(--border)">
  <div class="eyebrow">Welcome · foundations workshop</div>
  <h1 style="font-family:Fraunces,serif">Grow steady, ship kindly.</h1>
  <p class="lead" style="max-width:56ch">Three sessions, one shared garden. Bring a notebook and a question you have carried all year.</p>
  <div style="border-left:4px solid #C2410C;background:#FFF7ED;padding:16px 24px;border-radius:12px;margin-top:24px;max-width:60ch">
    <strong>Today:</strong> roots first — setup, signup, and your first green check.
  </div>
  <p class="annot">you belong here — Mara</p>
</div>
```

## Per-engine notes

- **reveal.js:** apply `.hero-botanical` to the opening `<section>`; keep `Caveat` to one absolutely-positioned note so it never reflows body text.
- **Slidev (UnoCSS):** `font-[Fraunces]` for headings via `font-display` mapping; callout as `border-l-4 border-[#C2410C] bg-[#FFF7ED] rounded-xl px-6 py-4`.
- **Marp (`@theme`):** `section.lead { background: #FEFCF8; }` plus `section.lead h1 { font-family: Fraunces, serif; }`.

## Anti-slop don'ts

1. No second handwritten note. One `Caveat` annotation per deck; two reads as a greeting card.
2. No cream code blocks. Code sits on `#FFFFFF` with a `#E7DFCF` border, never on `#F5F0E6`.
3. No icon confetti or leaf-pattern borders. One terracotta rule plus real photography carries the warmth.
