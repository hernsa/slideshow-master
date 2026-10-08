# Verify Checklist — Ship Gates

Fail any gate = do not ship. Check in order.

- [ ] Contrast >= 4.5:1 checked — body text vs bg measured (large text >= 3:1); muted text rechecked on surface color.
- [ ] `prefers-reduced-motion` fallback present — every animated section has a static cut; verified in DevTools rendering emulation.
- [ ] Keyboard works — arrows / space / PageUp / PageDown advance; Home jumps to first, End to last; focus visible.
- [ ] Mobile swipe works — touch swipe advances both directions; tap targets >= 44px; tested at 390px width.
- [ ] Speaker notes present — every slide has notes; notes render in speaker view (`?notes` / presenter mode).
- [ ] Images exist + licensed — no broken `src`; license recorded per image; local images committed under `assets/`.
- [ ] Alt text on all images — informative images get descriptive alt; decorative images get `alt=""`.
- [ ] Code highlights render — Shiki theme matches light/dark mode; no unstyled gray blocks; horizontal scroll intact.
- [ ] PDF export renders — full page count, no cut-off text, fonts embedded; generated from final commit.
- [ ] PPTX export renders — spot-check title, bento, code, quote slides; transitions acceptably degrade to cuts.
- [ ] No console errors — clean run in Chromium + Firefox; no 404s for assets, fonts, or iframes.
