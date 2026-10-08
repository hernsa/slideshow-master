---
marp: true
theme: default
transition: fade 0.5s
backgroundColor: "#0B1020"
color: "#E8EEF9"
---

<style>
section { font-family: Georgia, serif; background: #0B1020; color: #E8EEF9; }
h1, h2 { font-family: Verdana, sans-serif; color: #E8EEF9; }
a, strong { color: #4F7DF3; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition: none !important; animation: none !important; }
}
</style>

# Hello

<!-- presenter note: welcome to the Marp deck -->

---

<!-- _transition: cover-left -->

## Slide 2

```js
fetch("/api/v1/deploy", { method: "POST" })
  .then((r) => r.json())
  .then((d) => console.log(d));
```

<!-- presenter note: run deploy live, then show dashboard -->
