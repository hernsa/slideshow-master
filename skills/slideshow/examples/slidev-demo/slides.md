---
theme: default
transition: slide-left
highlighter: shiki
background: "#0B1020"
---

# Deploy Day

<div v-click>Step 1</div>
<div v-motion :initial="{x:-80,opacity:0}" :enter="{x:0,opacity:1}">Fly in</div>

<style>
.slidev-layout { font-family: Georgia, serif; background: #0B1020; color: #E8EEF9; }
.slidev-layout h1 { font-family: Verdana, sans-serif; color: #E8EEF9; }
.accent { color: #4F7DF3; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition: none !important; animation: none !important; }
}
</style>

<!-- presenter note: welcome, click Step 1, motion flies in unless reduced motion -->

---

# Ship it

```ts
fetch("/api/v1/deploy", { method: "POST" })
  .then((r) => r.json())
  .then((d) => console.log(d));
```

<!-- presenter note: run deploy live, then show dashboard -->
