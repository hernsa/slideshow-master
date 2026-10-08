# Narrative Mode — Story-Driven Keynote

> 8 slides. Goal: move a mixed audience with a story they retell.
> Use when feeling carries further than a diff — openers, closers, vision talks.

## Arc description

A hero the audience roots for, tension that tightens twice, a turn where
the old tool fails in public, and a resolution that hands the audience a
new identity ("we ship runtimes now"). One idea per slide, one image per
idea, sentences short enough to say out loud. Numbers appear once, late,
as confirmation — never as the opening. When not to use: hands-on teaching
(use `tutorial.md`), evidence-heavy persuasion (use `tech-talk.md`).

Reference thread: "Why HTML beats PPTX for tech talks" as a keynote —
a speaker, a frozen stage, and the night talks stopped being files.

## Per-slide outline

### 1. Cold open — "The Room Went Quiet, and Not in a Good Way"
- Layout: full-bleed dark stage photo + 8-word line + date stamp.
- Beats: smell of hot projector dust, 400 seats, clicker click with no advance.
- Notes hint: `<!-- presenter: 15 seconds of silence after the line. Do not explain yet. -->`

### 2. Hero — "Mara Had Given This Talk Four Times Before"
- Layout: split 40/60 — left portrait treatment, right two-line bio + talk title.
- Beats: backend engineer, habitual over-preparer, PDF backup on a USB stick that also failed.
- Notes hint: full physical inventory rule does not apply here; keep the hero human, not cataloged.

### 3. Tension I — "The Video Played Yesterday. Today It Was a Gray Box."
- Layout: quote slide — audience tweet verbatim + gray-box screenshot small.
- Beats: fonts swapped mid-title, charts unlinked, embedded demo unreachable without Wi-Fi.
- Notes hint: read the tweet flat; let the room laugh before you continue.

### 4. Tension II — "Hallway Re-Export, Knee on the Floor"
- Layout: split 50/50 — left hallway photo (credited), right 3 ticking-clock lines.
- Beats: 90 seconds to doors, borrowed dongle, the organizer's smile thinning.
- Notes hint: smell detail required — burnt coffee from the lobby cart, carpet cleaner, ozone.

### 5. Turn — "What If the Talk Was a URL, Not a File?"
- Layout: section divider — one sentence, oversized type, amber accent bar.
- Beats: the thesis lands here, two-thirds through: "A talk is a runtime, not a file."
- Notes hint: pause a full beat; this line repeats verbatim on slide 8.

### 6. New world — "One Markdown File, Three Shipments"
- Layout: bento 3-cell — live URL / PDF handout / source diff, each with a real thumbnail.
- Beats: `slides.md` → `dist/` SPA, → `deck.pdf` via Playwright, → reviewable diff.
- Notes hint: name `references/engines.md` routing in one breath — Slidev for code, Marp for handouts.

### 7. Proof — "23 Talks Later, Nobody Kneels in Hallways"
- Layout: stat row restrained (2 numbers max) + small stage photo of a calm Q&A.
- Beats: zero hallway re-exports, handout 41% smaller — numbers as benediction, not argument.
- Notes hint: sources in notes only; never read citations aloud on a keynote stage.

### 8. Benediction — "Ship the Runtime. Leave the File Behind."
- Layout: section divider + thesis repeat + speaker name + live URL that stays up.
- Beats: forward momentum — audience pockets phones and walks out repeating the line.
- Notes hint: end standing still on the URL slide; no "Thanks!" wall, no question-mark ending.

## Delivery (18 minutes, one breath per slide)

Minutes 0–3: slides 1–2, slow; let the quiet room and Mara land. Minutes
3–9: slides 3–4, tension tightens — ticking-clock lines read flat, no
rushing. Minute 9–11: slide 5 turn, the longest pause in the talk. Minutes
11–15: slides 6–7, new world brisk, proof gentle. Minutes 15–18: slide 8
benediction, lights up, URL stays while you take three questions max.
Rehearse standing still — pacing the stage leaks the tension you built.

## Sound and smell cues

Each story slide carries one sensory anchor in notes: hot projector dust
(slide 1), lobby coffee and carpet cleaner (slide 4), ozone from the dying
dongle (slide 4), paper handouts in the new world (slide 6). Sound: clicker
click with no advance (slide 1), hallway murmur (slide 4), single exhale
before the turn (slide 5). Sensory notes stay in speaker notes, never on
slides — see `references/layouts.md` for text budgets.

## Visual system

- Palette: Ink Keynote dark (ink `#101014`, bone `#F2EDE4`, amber `#F59E0B` single accent), from `references/colors.md`.
- Fonts: Fraunces display for story slides / Inter for proof slides; no mono except slide 6 thumbnails.
- Images: three full-bleeds max (slides 1, 4, 8 share one grade); all ≥1600px, 16/9, ≥40% scrim under text.
- Morph moment: exactly one — slide 5 thesis text morphs into slide 8 closing line via `data-auto-animate` with matching `data-id`.

## Mode-specific don'ts

1. Don't open with your name and agenda — open with the quiet room.
2. Don't put code on a keynote stage — slide 6 shows thumbnails, never a fence.
3. Don't stack two numbers on one slide before slide 7 — story first, proof late.
4. Don't narrate your visuals — if the photo needs explaining, replace the photo.
5. Don't end on a question — end on physical presence: you, the URL, the lights up.
6. Don't exceed 15 words per story slide — overflow belongs in speaker notes, not smaller type.
