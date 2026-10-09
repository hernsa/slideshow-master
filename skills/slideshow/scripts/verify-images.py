#!/usr/bin/env python3
"""Verify every image referenced by a deck exists, has a license record, and has alt text.

Usage: python verify-images.py <deck-source-file> [--assets-dir assets]
Exits 0 when all gates pass, 1 with a failure list otherwise.
"""
import re
import sys
from pathlib import Path

IMG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)|<img\b[^>]*>', re.IGNORECASE)
SRC_RE = re.compile(r'src\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
ALT_RE = re.compile(r'alt\s*=\s*["\']([^"\']*)["\']', re.IGNORECASE)
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
        alt_md = m.group(1)
        src_md = m.group(2)
        if src_md is not None:
            raw = src_md.strip()
            src = raw.split()[0].strip("\"'") if raw else ""
            alt = alt_md or ""
        else:
            tag = m.group(0)
            src_m = SRC_RE.search(tag)
            alt_m = ALT_RE.search(tag)
            src = src_m.group(1).strip() if src_m else ""
            alt = alt_m.group(1) if alt_m else ""
            if not src:
                failures.append(f"missing src in tag: {tag[:80]}")
                continue
        if not alt.strip():
            failures.append(f"missing alt text: {src}")
        if src.startswith(("http://", "https://", "data:")):
            continue  # remote/data URIs skip file + license checks, alt already checked above
        seen += 1
        img_path = deck.parent / src if not Path(src).is_absolute() else Path(src)
        if not img_path.exists():
            failures.append(f"missing file: {src}")
            continue
        stem = img_path.stem
        licensed = any((assets / f"{stem}{ext}").exists() or (img_path.parent / f"{stem}.LICENSE").exists() for ext in LICENSE_EXTS)
        if not licensed:
            failures.append(f"no license record for: {src} (add assets/{stem}.txt)")
    if failures:
        print(f"{len(failures)} image gate failure(s) in {deck}:")
        for f in failures:
            print(f"  - {f}")
        return 1
    if seen == 0:
        print("no local images referenced — nothing to verify")
        return 0
    print(f"OK: {seen} image(s) verified in {deck}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
