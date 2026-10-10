---
marp: true
theme: demo-dark
transition: slide 0.5s
backgroundColor: "#0B1020"
color: "#E8EEF9"
---

<!-- /* @theme demo-dark */ presenter notes: theme tokens shared by all slides — bg #0B1020, accent #4F7DF3, Georgia serif + Segoe UI sans + mono. -->

<style>
/* @theme demo-dark */
section { background: #0B1020; color: #E8EEF9; font-family: "Segoe UI", system-ui, sans-serif; padding: 48px 56px; }
h1, h2 { font-family: Georgia, serif; color: #E8EEF9; }
a, strong.accent, .accent { color: #4F7DF3; }
code, pre { font-family: ui-monospace, Consolas, monospace; }
pre { background: #0E1530; border: 1px solid #26325C; border-radius: 12px; padding: 16px 18px; counter-reset: ln; }
pre code { counter-reset: ln; }
.kicker { color: #4F7DF3; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.7em; }
.panel { background: #131B33; border: 1px solid #26325C; border-radius: 12px; padding: 14px 16px; }
.callout { border: 1px solid #4F7DF3; border-left-width: 8px; background: #131B33; border-radius: 12px; padding: 16px 18px; }
section.lead { text-align: left; }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { transition: none !important; animation: none !important; } }
</style>

<!-- layouts.md: title slide -->
<!-- _class: lead -->
<!-- _transition: fade 0.5s -->

<span class="kicker">DevConf 2026 · October 8</span>

# Why HTML Beats PPTX for Tech Talks

Speaker **Ada Demo** · Frontend Engineer · DevConf Main Stage

Live code, live demos, zero font drama.

<!-- presenter note: Welcome the room, introduce Ada, promise everything shown ships as a link after the talk. -->

---

<!-- layouts.md: thesis statement, big type -->
<!-- _transition: fade 0.5s -->

<span class="kicker">The one sentence to remember</span>

## Slides are software — <span class="accent">version them, test them, ship them</span> like software.

Everything else in this talk follows from that sentence.

<!-- presenter note: Land the thesis slowly and repeat it. Every later slide maps to version, test, or ship. -->

---

<!-- layouts.md: 3-col bento problem slide, varied sizes -->
<!-- _transition: slide 0.5s -->

<span class="kicker">The problem with PPTX</span>

## Death by deck

<div class="panel" style="border-left: 6px solid #4F7DF3;">

**01 · Binary blobs** — no diff, no blame, no pull request. Two files named final_FINAL and nobody knows what changed.
</div>

- **02 · Font roulette** — Calibria on your laptop, tofu boxes on stage.
- **03 · Dead demos** — screenshots of code you cannot run, copy, or click.

<!-- presenter note: Reveal pain points top to bottom. Ask for hands on FINAL_final files, pause for laughs, then move on. -->

---

<!-- layouts.md: stat row -->
<!-- _transition: slide 0.5s -->

<span class="kicker">Measured on last quarter's talks</span>

## HTML decks ship lighter and load faster

| Metric | Value | Delta |
|---|---|---|
| Median deck size | **12 KB** | 84x smaller than PPTX |
| Cold load on venue wifi | **0.4 s** | 6x faster |
| Links still live | **100%** | +38 pts vs exports |
| Community pull requests | **47** | from zero |

<!-- presenter note: Metrics from five internal talks migrated to HTML. Stress the last row: pull requests on slides never happened before. -->

---

<!-- code.md: dark code block with line numbers -->
<!-- _transition: none -->

<span class="kicker">Live data, not screenshots</span>

## Audience votes, straight from the slide

```js
const res = await fetch("https://api.demo.dev/votes", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ talk: "html-beats-pptx" }),
});
const { score } = await res.json();
renderMeter(score);
console.log("live score:", score);
```

Copy it, run it, break it — right here in the browser console.

<!-- presenter note: Run this live against the demo API. Flag the headers line: JSON content-type is the number one copy-paste bug. -->

---

<!-- morph.md: continuity pair, part A -->
<!-- _class: lead -->
<!-- _transition: zoom 0.6s -->

<span class="kicker">Morph moment · before the fix</span>

## <span style="color:#9AA7C7; font-size:1.6em;">72 audience score</span>

Static export. Stale numbers from rehearsal night.

<!-- presenter note: Hold on the gray 72. This is the old world: frozen the moment you hit export. -->

---

<!-- morph.md: continuity pair, part B -->
<!-- _class: lead -->
<!-- _transition: zoom 0.6s -->

<span class="kicker">Morph moment · after going live</span>

## <span class="accent" style="font-size:2.2em;">97 audience score</span>

Same metric, new state — bigger and blue because the data is live.

<!-- presenter note: Advance and let the zoom carry the continuity. Narrate: nothing recreated, the metric itself transitioned. -->

---

<!-- layouts.md: split slide, text + graphic -->
<!-- _transition: cover-left 0.5s -->

<span class="kicker">How it feels in the room</span>

## Text plus picture

- One idea per side, graphic carries the metaphor
- Talk while the graphic breathes, never read bullets aloud
- You carry the narrative

<svg viewBox="0 0 320 220" width="420" role="img" aria-label="Browser window with code and play button"><rect x="8" y="8" width="304" height="204" rx="16" fill="#131B33" stroke="#4F7DF3" stroke-width="3"/><rect x="8" y="8" width="304" height="40" rx="16" fill="#4F7DF3"/><circle cx="30" cy="28" r="6" fill="#0B1020"/><circle cx="50" cy="28" r="6" fill="#0B1020"/><circle cx="70" cy="28" r="6" fill="#0B1020"/><rect x="30" y="70" width="180" height="12" rx="6" fill="#E8EEF9"/><rect x="30" y="94" width="120" height="12" rx="6" fill="#9AA7C7"/><rect x="30" y="118" width="150" height="12" rx="6" fill="#9AA7C7"/><circle cx="252" cy="130" r="34" fill="#4F7DF3"/><polygon points="244,112 244,148 272,130" fill="#0B1020"/></svg>

<!-- presenter note: Gesture to the graphic while telling the deploy story. If you are reading the slide, the slide is winning. -->

---

<!-- components.md: quote with avatar, tinted surface for rotation -->
<!-- _backgroundColor: #131B33 -->
<!-- _transition: fade 0.5s -->

<span class="kicker">From the hallway track</span>

## People notice the difference

<svg viewBox="0 0 96 96" width="84" height="84" role="img" aria-label="Avatar with initials MK"><circle cx="48" cy="48" r="46" fill="#4F7DF3"/><text x="48" y="60" text-anchor="middle" font-size="32" font-family="Georgia, serif" fill="#0B1020" font-weight="bold">MK</text></svg>

**"I copied a working fetch snippet from Ada's slides before she left the stage. First time that ever happened."**

Mira Kessler · Platform Engineer, Northwind

<!-- presenter note: Read the quote verbatim. Add context: Mira filed a docs fix that night — the community loop HTML unlocks. -->

---

<!-- components.md: callout tip box -->
<!-- _transition: fade 0.5s -->

<span class="kicker">Steal this workflow</span>

## One rule that saves every demo

<div class="callout">

**Tip: freeze a fallback build the night before.** Tag it `v1.0-fallback` so venue wifi can die and you still present.
</div>

- Commit slides and demos to the same repo
- Record a 60-second offline screen capture as backup
- Print speaker notes — paper never needs wifi

<!-- presenter note: Tell the Berlin story — venue wifi died, the fallback tag saved the keynote. This is the slide people photograph. -->

---

<!-- layouts.md: closing CTA -->
<!-- _class: lead -->
<!-- _transition: fade 0.5s -->

<span class="kicker">Take it with you</span>

# Fork it tonight

Repo: **github.com/demo/html-beats-pptx**

**3 takeaways:** version your slides · demo live, not screenshots · ship a link, not a file

Contact: Ada Demo · ada@demo.dev — slides, code, and video at the repo above.

<!-- presenter note: Hold the repo URL for ten seconds. Invite questions and note the deck link is already in the chat. -->
