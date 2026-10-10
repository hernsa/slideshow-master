#!/usr/bin/env python3
"""Verify deck structure: visual density, no text walls, reveal pacing.

Usage: python verify-deck.py <deck-source-file>
Exits 0 when all gates pass, 1 with a failure list otherwise.
"""
import re
import sys
from pathlib import Path

MD_IMG_RE = re.compile(r'!\[[^\]]*\]\([^)]+\)')
IMG_TAG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
SVG_RE = re.compile(r'<svg\b', re.IGNORECASE)
BG_IMG_RE = re.compile(r'data-background-image\s*=', re.IGNORECASE)
FRONT_IMG_RE = re.compile(r'^\s*image\s*:', re.IGNORECASE | re.MULTILINE)
LAYOUT_IMG_RE = re.compile(r'layout\s*:\s*image-', re.IGNORECASE)
VCLICK_RE = re.compile(r'v-click', re.IGNORECASE)
FRAGMENT_RE = re.compile(r'fragment', re.IGNORECASE)
SECTION_RE = re.compile(r'<section\b', re.IGNORECASE)
FENCE_RE = re.compile(r'^\s*```')
SEPMD_RE = re.compile(r'^[ \t]*---[ \t]*$')
BG_MARK_PATTERNS = [
    re.compile(r'data-background(?:-color|-image|-gradient|-video)?\s*=', re.IGNORECASE),
    re.compile(r'^\s*background\s*:', re.MULTILINE | re.IGNORECASE),
    re.compile(r'_color\s*:', re.IGNORECASE),
    re.compile(r'_backgroundImage\s*:', re.IGNORECASE),
    re.compile(r'_backgroundColor\s*:', re.IGNORECASE),
    re.compile(r'\bbg-[a-z]+-\d+\b', re.IGNORECASE),
]
THEME_TOKEN_RE = re.compile(r'(?:--bg\s*:|@theme\b|^\s*theme\s*:)', re.MULTILINE | re.IGNORECASE)


def _strip_global_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if SEPMD_RE.match(lines[i]):
            return "\n".join(lines[i + 1:])
    return text


def split_slidev(text: str) -> list[str]:
    text = _strip_global_frontmatter(text)
    lines = text.splitlines()
    slides: list[str] = []
    cur: list[str] = []
    in_fence = False
    in_fm = False
    prev_sep = False
    n = len(lines)
    i = 0
    while i < n:
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if FENCE_RE.match(ln):
            in_fence = not in_fence
            cur.append(ln)
            i += 1
            prev_sep = False
            continue
        if not in_fence and SEPMD_RE.match(ln):
            if in_fm:
                in_fm = False
                i += 1
                prev_sep = False
                continue
            if prev_sep:
                in_fm = True
                i += 1
                prev_sep = False
                continue
            slides.append("\n".join(cur))
            cur = []
            prev_sep = True
            i += 1
            continue
        cur.append(ln)
        prev_sep = False
        i += 1
    if cur:
        slides.append("\n".join(cur))
    return [s for s in slides if s.strip()]


def split_reveal(text: str) -> list[str]:
    parts = re.split(r'(?i)(?=<section\b)', text)
    slides = [p for p in parts if SECTION_RE.search(p)]
    return [s for s in slides if s.strip()]


def is_visual(block: str) -> bool:
    if MD_IMG_RE.search(block):
        return True
    if IMG_TAG_RE.search(block):
        return True
    if SVG_RE.search(block):
        return True
    if BG_IMG_RE.search(block):
        return True
    if FRONT_IMG_RE.search(block):
        return True
    if LAYOUT_IMG_RE.search(block):
        return True
    low = block.lower()
    if "screenshot" in low:
        return True
    if "avatar" in low:
        return True
    if "<figure" in low:
        return True
    return False


def count_reveals(block: str) -> int:
    return len(VCLICK_RE.findall(block)) + len(FRAGMENT_RE.findall(block))


def word_count(block: str) -> int:
    s = re.sub(r'<!--.*?-->', ' ', block, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', s)
    s = re.sub(r'[`#>*_\-]', ' ', s)
    return len(s.split())


def background_markers(block: str) -> list[str]:
    found: list[str] = []
    for rx in BG_MARK_PATTERNS:
        found.extend(rx.findall(block))
    return found


def short_preview(block: str, width: int = 52) -> str:
    for ln in block.strip().splitlines():
        s = ln.strip()
        if s:
            if len(s) > width:
                return s[: width - 1] + "…"
            return s
    return "(empty)"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: verify-deck.py <deck-source-file>")
        return 1
    deck = Path(sys.argv[1])
    text = deck.read_text(encoding="utf-8")
    suffix = deck.suffix.lower()
    low = text.lower()
    if suffix in (".html", ".htm"):
        mode = "reveal"
    elif suffix in (".md", ".markdown", ".mdx"):
        mode = "slidev"
    else:
        mode = "reveal" if "<section" in low else "slidev"
    if mode == "reveal":
        slides = split_reveal(text)
        if not slides:
            alt = split_slidev(text)
            if alt:
                slides = alt
                mode = "slidev"
    else:
        slides = split_slidev(text)
    total = len(slides)
    failures: list[str] = []
    if total == 0:
        print(f"Deck: {deck} ({mode}, 0 slides)")
        print(f"Visuals: 0/0 (need >= 1 per 3 slides)")
        print(f"1 deck structure failure(s) in {deck}:")
        print("  - no slides found")
        return 1
    tags = ["V" if is_visual(s) else "T" for s in slides]
    counts = [count_reveals(s) for s in slides]
    words = [word_count(s) for s in slides]
    bg_markers = [background_markers(s) for s in slides]
    visuals = sum(1 for t in tags if t == "V")
    for i in range(total - 2):
        if tags[i] == "T" and tags[i + 1] == "T" and tags[i + 2] == "T":
            failures.append(f"TTT run: slides {i + 1}-{i + 3} are text-only (add a visual on slide {i + 2} or {i + 3})")
    need = (total + 2) // 3
    if visuals * 3 < total:
        failures.append(f"visual density {visuals}/{total} below 1 per 3 slides (need >= {need} visuals, have {visuals})")
    if visuals == 0:
        failures.append("zero visuals in the deck — source or draw at least one image/SVG diagram (media/images.md rung 1)")
    for i, c in enumerate(counts):
        if c > 5:
            failures.append(f"slide {i + 1}: {c} staged reveals (v-click/fragment), max 5")
    for i, w in enumerate(words):
        if w < 10 and tags[i] == "T":
            failures.append(f"slide {i + 1}: thin ({w} words) and no visual — expand content (research-notes 2x rule) or make it a visual divider")
    if sum(len(b) for b in bg_markers) == 0:
        failures.append(f"theme flat: no explicit background variation across {total} slides — add at least one tinted divider/dark quote/accent-band slide (color-usage.md rotation, max 2 consecutive same-bg)")
    if not THEME_TOKEN_RE.search(text):
        failures.append("no theme tokens declared (--bg / @theme / theme:) — apply a visual style from references/visual-styles/")
    print(f"Deck: {deck} ({mode}, {total} slides)")
    for i in range(total):
        print(f"{i + 1:>3}  {tags[i]}  words={words[i]:>4}  reveals={counts[i]:>2}  bg={len(bg_markers[i])}  {short_preview(slides[i])}")
    print(f"Visuals: {visuals}/{total} (need >= 1 per 3 slides)  bg markers={sum(len(b) for b in bg_markers)}")
    if failures:
        print(f"{len(failures)} deck structure failure(s) in {deck}:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"OK: deck structure passes in {deck}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
