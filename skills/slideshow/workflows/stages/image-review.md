# Image Review — Hybrid Image Pipeline

> Every image is local, credited, sized, and reachable by the verify script.
> AI, stock, or user-supplied — the pipeline below treats all three as guilty
> until `scripts/verify-images.py` exits 0.

## 1. When this stage runs

- Full path: `generate-deck.md` step 7, right after `scripts/new-deck-scaffold.sh` creates `<deck>/assets/`.
- Fast path: sprint 0:08–0:12 — screenshots plus one hero photo only, same gates, smaller set.
- Re-entry: `stages/refine-spec.md` routes every image swap back through §§4–6.

## 2. Sourcing decision — AI vs stock vs user-supplied

| Source | Use when | Example (Acme Q3 talk) |
|---|---|---|
| AI-generated | No photo exists: abstract concepts, architecture diagrams, tension scenes | "Frozen projector glow over an empty conference stage, dark tech" hero |
| Stock (credited) | Real humans, offices, labs needed fast | Lab engineers at a deploy dashboard (Maria Santos credit line) |
| User-supplied | Screenshots, dashboards, team faces, product UI | `latency-6w.png` chart export, `shield-demo.png` staging capture |

Rules: never hotlink — copy every file into `assets/`. Max one full-bleed
photo per section. Screenshots beat stock for anything the audience could ask
to click. Team faces beat avatars-from-nowhere on quote slides.

## 3. Sourcing procedure per type

1. AI: generate at 1920px wide minimum, save as `assets/<slug>.jpg`, record the prompt and tool in `assets/CREDITS.md` so the image is reproducible.
2. Stock: download the licensed file (never screenshot a preview), save as `assets/<slug>.jpg`, record photographer + license URL + date.
3. User-supplied: confirm the sender may share it (internal clearance or own work), save under `assets/`, record "Acme internal — cleared for conference use" with the sender's name and date.

## 4. Credit logging — `assets/CREDITS.md` plus per-file license records

`assets/CREDITS.md` carries one entry per image:

```markdown
## lab.jpg — Acme lab photo
- File: `assets/lab.jpg` (320KB, 1920px)
- Source: Maria Santos, Acme internal shoot, Sep 2026
- License: Acme internal — cleared for conference use

## latency-6w.png — p95 chart export
- File: `assets/latency-6w.png` (140KB, 1920px)
- Source: Acme edge dashboard export by Jonas Weber, Oct 2026
- License: Acme internal data — cleared for external sharing

## stage-hero.jpg — frozen projector hero (AI)
- File: `assets/stage-hero.jpg` (380KB, 1920px)
- Source: generated with Acme image tool, prompt "empty stage, frozen projector glow, dark tech", Oct 2026
- License: Acme-owned generation — no third-party rights
```

Second, `scripts/verify-images.py` requires a per-file license record beside the
image: `assets/<stem>.txt` (or `.md`, `.json`, or `<stem>.LICENSE`). The scaffold
writes the template into `assets/README.txt`; fill one per image:

```text
Source: Maria Santos, Acme internal shoot, Sep 2026
License: Acme internal — cleared for conference use
Date: 2026-09-18
```

No `.txt` record means the script exits 1 — the CREDITS entry alone is not enough.

## 5. `verify-images.py` usage

Run from the skill root against the deck source file:

```bash
python scripts/verify-images.py slides.md
python scripts/verify-images.py slides.md --assets-dir assets
python scripts/verify-images.py deck.md --assets-dir ./marp-deck/assets
```

What it checks: every local `<img src>` and Markdown `![]()` must exist on disk,
must carry non-empty `alt` text, and must have its per-stem license record.
Remote (`http…`) and `data:` URIs skip the license check but still require `alt`.
Exit 0 prints `OK: N image(s) verified`; exit 1 lists each failure — fix every
line, never ship red.

## 6. Sizing and compression targets (Gate 3 numbers)

| Kind | Budget | Notes |
|---|---|---|
| Photos | ≤400KB, max width 1920px | full-bleed heroes included |
| Backgrounds | ≤200KB | flat, compressible by design |
| Parallax wide | 3000px wide allowed, still ≤400KB | the only width exception |
| Charts/screenshots | ≤400KB at readable 14px+ labels | re-export at 2x if text blurs |
| Avatars/QR | smallest legible size (avatars 64px display) | never ship a 2MB face |

Export at 1920px max width, lower quality until the file fits the budget, then confirm:

```bash
ls -lh assets/
# expect: every file present, photos ≤400K, backgrounds ≤200K
```

## 7. Scrim rules for text over photo

Bare text on a busy photo always fails. Minimum 40% scrim under any text-over-photo
(`generate-deck.md` step 7); the standard from `references/layouts.md` §10 is a
60–78% dark gradient, text side darkest:

```html
<div style="position:relative;border-radius:16px;overflow:hidden;border:1px solid var(--border)">
  <img src="assets/lab.jpg" alt="Engineers reviewing a deploy dashboard in the Acme lab" style="width:100%;aspect-ratio:21/9;object-fit:cover;display:block" />
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.78) 0%,rgba(11,16,32,.25) 60%,transparent 100%);display:flex;align-items:center;padding:48px">
    <h2 style="color:#fff;margin:0;max-width:16ch">Deploy day, minus the fear</h2>
  </div>
</div>
```

White text over the scrim must still pass the contrast spot-check in
`stages/visual-review.md`. Captions sit below the figure at 14px muted — never
burned into the photo.

## 8. Treatment checklist (from `references/layouts.md` §10)

- Radius 16–24px on cards, 1px `var(--border)`, soft shadow `0 8px 30px rgba(2,6,23,.08)`.
- `object-fit: cover` with a fixed `aspect-ratio` (16/9 default) — stretched images fail review.
- `alt` states the takeaway, not the object: `alt="Weekly p95 latency falling from 412 to 243 milliseconds over six weeks"`; decorative images get `alt=""`.
- Every `<figure>` carries a 14px muted caption with source: `Deploys per week, June → September. Source: Acme internal.`

## 9. Handoff

Paste one line: `Images done: 5 local, all ≤400KB, credited + licensed, verify-images.py exit 0 — build may proceed.` Attach the `ls -lh assets/` output to the delivery note.
