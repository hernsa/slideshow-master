# Title hero layout

> Conference opener: one claim, one credential, zero clutter.
> Reuses `layouts.md` title tokens: `h1: clamp(2rem,5vw,3.5rem)`,
> `letter-spacing: -0.02em`, lead `1.2rem` muted at `60ch`,
> `.slide-inner` with `48px` padding.

## When to use

- Talk opener with the thesis as the headline.
- Keynote moment before any agenda or outline.
- Recorded intros where the title card thumbnails well.
- Never use for section two onward; that job belongs to dividers.

## Copy-paste HTML sketch

```html
<div class="slide-inner" style="min-height:60vh;display:flex;flex-direction:column;justify-content:center">
  <div class="eyebrow">Acme Corp · Q3 engineering review · Oct 2026</div>
  <h1 style="margin:12px 0 0">Ship calmly.</h1>
  <p class="lead" style="margin-top:16px">How preview deploys took p95 from 412ms to 243ms in six weeks — and ended Friday fear.</p>
  <div style="display:flex;gap:12px;align-items:center;margin-top:24px">
    <img src="assets/ada.jpg" alt="Portrait of Ada Okafor" style="width:48px;height:48px;border-radius:50%;object-fit:cover" />
    <div><strong>Ada Okafor</strong><div style="opacity:.65;font-size:14px">Platform Lead, Acme</div></div>
    <div style="opacity:.4;margin-left:16px;font-size:14px">20 min · 12 slides · live demo</div>
  </div>
</div>
```

## Spacing and type tokens

- Eyebrow names org, event, date in one line.
- `h1` is two to four words. Lead is one sentence with both numbers.
- Face row: `48px` avatar, name `16px/700`, role `14px` muted.
- Meta line (`20 min`) sits right of the face, never above the title.

## Per-engine notes

- **reveal.js:** first `<section>` with `data-background-color` matching
  the theme ground. No fragments on the hero; it lands whole.
- **Slidev:** `layout: intro` or `layout: cover` plus the HTML face row.
  Set `title:` in frontmatter to match the `h1` for correct tab text.
- **Marp:** `<!-- _class: lead -->` plus `#` heading. Keep the face row
  as HTML because Markdown image sizing drifts across Marp themes.

## Responsive

- `h1` clamps down naturally. Face row wraps under `520px`.
- Lead maxes at `60ch` so lines stay short on wide screens.

## Accessibility

- Page `title` matches the `h1`. Avatar `alt` names the speaker.
- Contrast on eyebrow still needs `4.5:1`; raise opacity if the theme dims it.

## Anti-slop don't

- Don't open with a logo wall plus "Welcome to my talk".
  Open with the claim the audience will repeat at dinner.
