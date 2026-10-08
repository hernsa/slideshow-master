# Image fullbleed layout

> One emotional beat with scrimmed text overlay. Max 2 per deck.
> Reuses `layouts.md` image tokens: radius `16px`, border
> `1px solid var(--border)`, shadow `0 8px 30px rgba(2,6,23,.08)`,
> scrim `60-78%` dark, captions `14px`.

## When to use

- Emotional reset between data runs: lab, crowd, hardware.
- Customer on-site moment that words cannot carry.
- Talk midpoint breather before the fix section.
- Never for data slides; charts need white ground, not photo ground.

## Copy-paste HTML sketch

```html
<div class="slide-inner">
  <div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
    <img src="assets/lab.jpg" alt="Engineers reviewing a deploy dashboard in the Acme lab" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
    <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.78) 0%,rgba(11,16,32,.25) 60%,transparent 100%);display:flex;align-items:center;padding:48px">
      <div>
        <div style="font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;opacity:.7;color:#fff">On site — August</div>
        <h2 style="color:#fff;margin:8px 0 0;max-width:16ch">Deploy day, minus the fear</h2>
        <p style="color:#fff;opacity:.8;margin:12px 0 0">Photo: Maria Santos, Acme lab. 1920px, 320KB.</p>
      </div>
    </div>
  </div>
  <p style="font-size:14px;opacity:.65;margin-top:8px">Full-bleed is the single gradient-free scrim allowed as an overlay.</p>
</div>
```

## Scrim rules

- Text zone needs `60-78%` dark at the text edge, fading across.
- Test body text at `7:1` on projectors, not just laptops.
- Busy right halves stay empty; place faces and action on the left third.
- Credit lives inside the scrim at `14px`, plus `assets/CREDITS.md` entry.

## Per-engine notes

- **reveal.js:** `data-background-image` plus `data-background-size="cover"`
  works, but the card sketch above exports more predictably to PDF.
- **Slidev:** `layout: image-right` or `image-left` handles full-height
  crops natively. Keep the scrim div for text safety.
- **Marp:** paste the card sketch. Marp splits background and content
  oddly across themes, so the self-contained card beats theme backgrounds.

## Responsive

- `21/9` crops to `16/9` under `800px` via `aspect-ratio` swap.
- Overlay padding drops from `48px` to `24px` under `520px`.

## Accessibility

- `alt` describes the scene plus the takeaway, not "lab photo".
- Never place body copy under `14px` on photos; bump to `16px` minimum.

## Anti-slop don't

- Don't set white text on an unscrimmed sky photo. If the scrim drops
  below 40%, the slide fails the projector test every time.
