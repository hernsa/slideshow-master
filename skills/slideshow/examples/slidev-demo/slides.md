---
theme: default
transition: slide-left
highlighter: shiki
background: "#0B1020"
color: "#E8EEF9"
fonts:
  serif: Georgia, serif
  sans: '"Segoe UI", system-ui, sans-serif'
  mono: 'ui-monospace, Consolas, monospace'
---

<!-- layouts.md: title slide -->
# Why HTML Beats PPTX for Tech Talks

DevConf 2026 · October 8 · Speaker **Ada Demo**, Frontend Engineer

Live code, live demos, zero font drama.

<!-- presenter notes: Welcome the room, introduce Ada, promise everything shown ships as a link after the talk. -->

<style>
.slidev-layout { background: #0B1020; color: #E8EEF9; font-family: "Segoe UI", system-ui, sans-serif; }
.slidev-layout h1, .slidev-layout h2 { font-family: Georgia, serif; }
.accent { color: #4F7DF3; }
.panel { background: #131B33; border: 1px solid #26325C; border-radius: 12px; padding: 16px; }
.kicker { color: #4F7DF3; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.7em; }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { transition: none !important; animation: none !important; } }
</style>

---

<!-- layouts.md: thesis statement, big type -->

<div class="kicker">The one sentence to remember</div>

# Slides are software — <span class="accent">version them, test them, ship them</span> like software.

Everything else in this talk follows from that sentence.

<!-- presenter notes: Land the thesis slowly and repeat it. Every later slide maps to version, test, or ship. -->

---

<!-- layouts.md: 3-col bento problem slide with v-click steps -->

<div class="kicker">The problem with PPTX</div>

## Death by deck

<div v-click> <div class="panel" style="border-left: 6px solid #4F7DF3;"> <b>01 · Binary blobs</b> — no diff, no blame, no pull request. Two files named final_FINAL and nobody knows what changed. </div> </div>
<div v-click> <div class="panel"> <b>02 · Font roulette</b> — Calibria on your laptop, tofu boxes on the stage machine. </div> </div>
<div v-click> <div class="panel"> <b>03 · Dead demos</b> — screenshots of code you cannot run, copy, or click. </div> </div>

<!-- presenter notes: Advance clicks one at a time. Ask for hands on FINAL_final files, pause for laughs, then move on. -->

---

<!-- layouts.md: stat row -->

<div class="kicker">Measured on last quarter's talks</div>

## HTML decks ship lighter and load faster

| Metric | Value | Delta |
|---|---|---|
| Median deck size | **12 KB** | ▲ 84x smaller than PPTX |
| Cold load on venue wifi | **0.4 s** | ▲ 6x faster |
| Links still live | **100%** | ▲ +38 pts vs exports |
| Community pull requests | **47** | ▲ from zero |

<!-- presenter notes: Metrics from five internal talks migrated to HTML. Stress the last row: pull requests on slides never happened before. -->

---

<!-- code.md: dark code block -->

<div class="kicker">Live data, not screenshots</div>

## Audience votes, straight from the slide

```ts {all|3|6-7}
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

<!-- presenter notes: Run this live against the demo API. Flag line 3: JSON headers are the number one copy-paste bug. -->

---

<!-- morph.md: v-motion hero metric, part A of continuity -->

<div class="kicker">Morph moment · before the fix</div>

<div v-motion :initial="{x:-80,opacity:0,scale:0.8}" :enter="{x:0,opacity:1,scale:1}">

## <span style="color:#9AA7C7; font-size:2em;">72 audience score</span>

Static export. Stale numbers from rehearsal night.

</div>

<!-- presenter notes: Hold on the gray 72. This is the old world: frozen the moment you hit export. Reduced-motion users see the final state instantly. -->

---

<!-- morph.md: v-motion hero metric, part B of continuity -->

<div class="kicker">Morph moment · after going live</div>

<div v-motion :initial="{x:-80,opacity:0,scale:0.8}" :enter="{x:0,opacity:1,scale:1}">

## <span class="accent" style="font-size:2.6em;">97 audience score</span>

Same metric, new state — it glides in and turns blue because the data is live.

</div>

<!-- presenter notes: Let the motion play. Narrate the continuity: nothing recreated, the metric transitioned, just like live data should. -->

---

<!-- layouts.md: split slide, text + graphic -->

<div class="kicker">How it feels in the room</div>

## Text on the left, picture on the right

<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:center;">
<div>

- One idea per side
- Graphic carries the metaphor
- You carry the narrative

Talk while the graphic breathes. Never read bullets aloud.
</div>
<div>
<svg viewBox="0 0 320 220" width="100%" role="img" aria-label="Browser window with code and play button"><rect x="8" y="8" width="304" height="204" rx="16" fill="#131B33" stroke="#4F7DF3" stroke-width="3"/><rect x="8" y="8" width="304" height="40" rx="16" fill="#4F7DF3"/><circle cx="30" cy="28" r="6" fill="#0B1020"/><circle cx="50" cy="28" r="6" fill="#0B1020"/><circle cx="70" cy="28" r="6" fill="#0B1020"/><rect x="30" y="70" width="180" height="12" rx="6" fill="#E8EEF9"/><rect x="30" y="94" width="120" height="12" rx="6" fill="#9AA7C7"/><rect x="30" y="118" width="150" height="12" rx="6" fill="#9AA7C7"/><circle cx="252" cy="130" r="34" fill="#4F7DF3"/><polygon points="244,112 244,148 272,130" fill="#0B1020"/></svg>
</div>
</div>

<!-- presenter notes: Gesture to the graphic while telling the deploy story. If you are reading the slide, the slide is winning. -->

---

<!-- components.md: quote with avatar -->

<div class="kicker">From the hallway track</div>

## People notice the difference

<div style="display:flex;gap:18px;align-items:center;">
<svg viewBox="0 0 96 96" width="96" height="96" role="img" aria-label="Avatar with initials MK"><circle cx="48" cy="48" r="46" fill="#4F7DF3"/><text x="48" y="60" text-anchor="middle" font-size="32" font-family="Georgia, serif" fill="#0B1020" font-weight="bold">MK</text></svg>
<div>

**"I copied a working fetch snippet from Ada's slides before she left the stage. First time that ever happened."**

Mira Kessler · Platform Engineer, Northwind
</div>
</div>

<!-- presenter notes: Read the quote verbatim. Add context: Mira filed a docs fix that night — the community loop HTML unlocks. -->

---

<!-- components.md: callout tip box -->

<div class="kicker">Steal this workflow</div>

## One rule that saves every demo

<div class="panel" style="border-left: 8px solid #4F7DF3;">

**Tip: freeze a fallback build the night before.** Tag it `v1.0-fallback` so venue wifi can die and you still present.
</div>

- Commit slides and demos to the same repo
- Record a 60-second offline screen capture as backup
- Print speaker notes — paper never needs wifi

<!-- presenter notes: Tell the Berlin story — venue wifi died, the fallback tag saved the keynote. This is the slide people photograph. -->

---

<!-- layouts.md: closing CTA -->

<div class="kicker">Take it with you</div>

## Fork it tonight

Repo: **github.com/demo/html-beats-pptx**

**3 takeaways:** version your slides · demo live, not screenshots · ship a link, not a file

Contact: Ada Demo · ada@demo.dev — slides, code, and video at the repo above.

<!-- presenter notes: Hold the repo URL for ten seconds. Invite questions and note the deck link is already in the chat. -->
