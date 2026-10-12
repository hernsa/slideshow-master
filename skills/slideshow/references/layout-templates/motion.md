# Motion — static-position anchors

> Tokens in [tokens.md](../tokens.md). One page per slide. Repeat fixed left/top slots across slides for the morph feel. NO v-click/fragment — fragments break 1-page-per-slide export.

```html
<!-- slide 1 -->
<h2 data-id="sec-title" style="position:absolute;left:48px;top:48px;font-size:3rem;margin:0">Anh · 1640</h2>
<!-- slide 2: same slot, new text, photo swaps -->
<h2 data-id="sec-title" style="position:absolute;left:48px;top:48px;font-size:3rem;margin:0">My · 1776</h2>
```

Rules: 2 anchors per section (headline block + photo frame). Move one anchor per step, never both. One deck transition (`fade 0.4s`), entrances capped at 3 (`rise .3s`, `100–150ms` stagger, `≤600ms` total). Full grammar: `references/pptx-motion-language.md` §§1-3.

```css
.enter-1 { animation: rise .3s ease-out .1s both; }
.enter-2 { animation: rise .3s ease-out .22s both; }
@keyframes rise { from { opacity: 0; transform: translateY(12px); } }
```

## Don't

- Don't stage reveals with fragments or per-slide transitions — duplicate slides with matching `data-id` instead.
