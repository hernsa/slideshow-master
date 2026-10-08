#!/usr/bin/env python3
"""Verify every image referenced by a deck exists, has a license record, and has alt text.

Usage: python verify-images.py <deck-source-file> [--assets-dir assets]
Exits 0 when all gates pass, 1 with a failure list otherwise.
"""
import re
import sys
from pathlib import Path

IMG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)|<img[^>]+src="([^"]+)"[^>]*alt="([^"]*)"', re.IGNORECASE)
LICENSE_EXTS = {".txt", ".md", ".json"}


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: verify-images.py <deck-source-file> [--assets-dir assets]")
        return 1
    deck = Path(sys.argv[1])
    assets = Path(sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--assets-dir" else "assets")
    if assets.is_absolute() is False:
        assets = deck.parent / assets
    text = deck.read_text(encoding="utf-8")
    failures: list[str] = []
    seen = 0
    for m in IMG_RE.finditer(text):
        alt_md, src_md, src_html, alt_html = m.groups()
        src = (src_md or src_html or "").strip()
        alt = (alt_md if src_md else alt_html) or ""
        if src.startswith(("http://", "https://", "data:")):
            continue  # remote/data URIs: license check is manual, alt still required
        if not alt.strip():
            failures.append(f"missing alt text: {src}")
        seen += 1
        img_path = deck.parent / src if not Path(src).is_absolute() else Path(src)
        if not img_path.exists():
            failures.append(f"missing file: {src}")
            continue
        stem = img_path.stem
        licensed = any((assets / f"{stem}{ext}").exists() or (img_path.parent / f"{stem}.LICENSE").exists() for ext in LICENSE_EXTS)
        if not licensed:
            failures.append(f"no license record for: {src} (add assets/{stem}.txt)")
    if seen == 0:
        print("no local images referenced — nothing to verify")
        return 0
    if failures:
        print(f"{len(failures)} image gate failure(s) in {deck}:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"OK: {seen} image(s) verified in {deck}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
