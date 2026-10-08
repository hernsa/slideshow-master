# Quote layout

> One voice, one sentence, with a face. Under 25 words.
> Reuses `layouts.md` quote tokens: avatar `64px` circle,
> quote `1.5rem/1.4`, attribution `15px` muted, container `640px`.

## When to use

- Customer proof after a claim slide.
- Team motto before a section divider.
- Press pull when the outlet name adds weight.
- Longer praise belongs in a handout, not on a slide.

## Copy-paste HTML sketch

```html
<div class="slide-inner">
  <div class="eyebrow" style="text-align:center">Customer proof</div>
  <figure style="text-align:center;max-width:640px;margin:32px auto">
    <img src="assets/ada.jpg" alt="Portrait of Ada Okafor, Platform Lead at Acme" style="width:64px;height:64px;border-radius:50%;object-fit:cover;border:2px solid var(--border)" />
    <blockquote style="font-size:1.5rem;line-height:1.4;margin:16px 0">"Deploy day went from fear to routine."</blockquote>
    <figcaption style="opacity:.7;font-size:15px">Ada Okafor — Platform Lead, Acme Corp</figcaption>
    <figcaption style="opacity:.55;font-size:14px;margin-top:8px">Said after six weeks on preview deploys, August review.</figcaption>
  </figure>
</div>
```

## Editorial variant

```html
<figure style="max-width:680px;margin:0 auto;border-left:3px solid var(--primary);padding-left:24px">
  <blockquote style="font-family:Fraunces,Georgia,serif;font-size:1.6rem;line-height:1.35">"We stopped dreading Fridays."</blockquote>
  <figcaption style="margin-top:12px;opacity:.7;font-size:15px">Jonas Weber — SRE, Northwind</figcaption>
</figure>
```

## Spacing and type tokens

- Center variant for keynotes, left serif variant for Paper decks.
- Quote marks stay inline at text size, never a 200px decoration.
- Attribution holds name, role, company. Second line holds context.
- Top margin `32px` gives the face room to breathe.

## Per-engine notes

- **reveal.js:** HTML as-is in one `<section>`. No fragment on quotes;
  the sentence lands whole. Note the exact say-line in `<aside>`.
- **Slidev:** native `layout: quote` centers styling. Keep the `img`
  avatar explicit; Slidev does not inject faces automatically.
- **Marp:** HTML as-is. Marp `lead` class also centers, but keep the
  explicit figure so PDF export matches the HTML view.

## Responsive

- Avatar stays `64px` at all widths. Quote drops to `1.25rem` under `520px`.
- Attribution wraps, never truncates names.

## Accessibility

- Avatar `alt` names the person. Quote is a real `<blockquote>`.
- Never use an unnamed quote; no name means no trust.

## Anti-slop don't

- Don't stack two quotes side by side. They compete and both lose.
  One slide, one voice, then move on.
