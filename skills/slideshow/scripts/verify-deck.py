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


def split_slidev(text: str) -> list[str]:
    lines = text.splitlines()
    blocks: list[str] = []
    cur: list[str] = []
    in_fence = False
    for ln in lines:
        if FENCE_RE.match(ln):
            in_fence = not in_fence
            cur.append(ln)
            continue
        if not in_fence and SEPMD_RE.match(ln):
            blocks.append("\n".join(cur))
            cur = []
        else:
            cur.append(ln)
    blocks.append("\n".join(cur))
    if text.lstrip().startswith("---") and len(blocks) >= 3:
        cand = blocks[1]
        low = cand.lower()
        has_head = any(l.lstrip().startswith("#") for l in cand.splitlines())
        has_visual = ("![" in cand or "<img" in low or "<svg" in low)
        has_key = (":" in cand)
        if has_key and not has_head and not has_visual:
            return [b for b in blocks[2:] if b.strip()]
        return [b for b in blocks[1:] if b.strip()]
    return [b for b in blocks if b.strip()]


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
    visuals = sum(1 for t in tags if t == "V")
    for i in range(total - 2):
        if tags[i] == "T" and tags[i + 1] == "T" and tags[i + 2] == "T":
            failures.append(f"TTT run: slides {i + 1}-{i + 3} are text-only (add a visual on slide {i + 2} or {i + 3})")
    need = (total + 2) // 3
    if visuals * 3 < total:
        failures.append(f"visual density {visuals}/{total} below 1 per 3 slides (need >= {need} visuals, have {visuals})")
    for i, c in enumerate(counts):
        if c > 5:
            failures.append(f"slide {i + 1}: {c} staged reveals (v-click/fragment), max 5")
    print(f"Deck: {deck} ({mode}, {total} slides)")
    for i in range(total):
        print(f"{i + 1:>3}  {tags[i]}  reveals={counts[i]}  {short_preview(slides[i])}")
    print(f"Visuals: {visuals}/{total} (need >= 1 per 3 slides)")
    if failures:
        print(f"{len(failures)} deck structure failure(s) in {deck}:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"OK: deck structure passes in {deck}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
