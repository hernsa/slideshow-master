#!/usr/bin/env python3
"""Verify every raster a PPTX deck build references exists, is credited,
and fits the size budgets.

Usage: python verify-images.py <deck-dir> [--assets-dir assets]
Scans build.py for ASSETS / "file" refs and string-literal image names,
checks each file exists, checks assets/CREDITS.md names it, fails on
budget breaches (photos <=400KB, backgrounds <=200KB, width <=1920px).
Exits 0 when all gates pass, 1 with a failure list otherwise.
"""
import re
import sys
from pathlib import Path

REF_RE = re.compile(r'ASSETS\s*/\s*["\']([^"\']+)["\']')
LIT_RE = re.compile(r'["\']([A-Za-z0-9_][A-Za-z0-9_\-]*\.(?:jpe?g|png|webp))["\']', re.IGNORECASE)
PHOTO_BUDGET = 400 * 1024
BG_BUDGET = 200 * 1024
MAX_WIDTH = 1920


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: verify-images.py <deck-dir> [--assets-dir assets]")
        return 1
    root = Path(sys.argv[1])
    assets = Path(sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--assets-dir" else "assets")
    if not assets.is_absolute():
        assets = root / assets
    build = root / "build.py"
    if not build.exists():
        print(f"FAIL: no build.py in {root}")
        return 1
    text = build.read_text(encoding="utf-8")
    refs = set(REF_RE.findall(text)) | set(LIT_RE.findall(text))
    refs = {r for r in refs if not r.startswith(("plate_", "sq_", "sqrot_"))}
    failures: list[str] = []
    credits = (assets / "CREDITS.md").read_text(encoding="utf-8", errors="replace") \
        if (assets / "CREDITS.md").exists() else ""
    if not (assets / "CREDITS.md").exists():
        failures.append("assets/CREDITS.md missing")
    for ref in sorted(refs):
        p = assets / ref
        if not p.exists():
            failures.append(f"missing file: assets/{ref}")
            continue
        if ref not in credits and Path(ref).stem not in credits:
            failures.append(f"no CREDITS.md line for: {ref}")
        size = p.stat().st_size
        budget = BG_BUDGET if ref.startswith("plate_") or "bg" in ref else PHOTO_BUDGET
        if size > budget:
            failures.append(f"over budget: {ref} {size // 1024}KB > {budget // 1024}KB")
        try:
            from PIL import Image
            with Image.open(p) as im:
                if im.width > MAX_WIDTH:
                    failures.append(f"too wide: {ref} {im.width}px > {MAX_WIDTH}px")
        except ImportError:
            pass
    if failures:
        print(f"{len(failures)} image gate failure(s) in {root}:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"OK: {len(refs)} image(s) verified in {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
