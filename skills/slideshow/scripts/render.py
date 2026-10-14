"""Generic COM pass: Morph-byObject everywhere (fade where told),
manual advance, PNG renders. Rebuild clean before running — COM
doubles effects on re-run.

Usage: python render.py <deck.pptx> [--fades 1,6] [--out renders/]
Per-deck entrances belong in the deck's own motion.py (see
scaffold.py); this script is the no-entrance fallback.
"""
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MORPH_OBJECT = 3954
FADE = 1793


def main():
    args = sys.argv[1:]
    if not args:
        print("usage: python render.py <deck.pptx> [--fades 1,6] "
              "[--out renders/]")
        sys.exit(1)
    pptx = Path(args[0]).resolve()
    fades = set()
    out = pptx.parent / "renders"
    if "--fades" in args:
        fades = {int(x) for x in
                 args[args.index("--fades") + 1].split(",") if x.strip()}
    if "--out" in args:
        out = Path(args[args.index("--out") + 1])
    subprocess.run(["taskkill", "/F", "/IM", "POWERPNT.EXE"],
                   capture_output=True)
    time.sleep(2)
    from win32com.client.gencache import EnsureDispatch
    app = EnsureDispatch("PowerPoint.Application")
    app.DisplayAlerts = 0  # ppAlertsNone
    pres = app.Presentations.Open(str(pptx), WithWindow=False)
    for i, slide in enumerate(pres.Slides, start=1):
        slide.SlideShowTransition.EntryEffect = (
            FADE if i in fades else MORPH_OBJECT)
        slide.SlideShowTransition.AdvanceOnTime = False
        slide.SlideShowTransition.AdvanceOnClick = True
    out.mkdir(parents=True, exist_ok=True)
    for i, slide in enumerate(pres.Slides, start=1):
        slide.Export(str(out / ("s%d.png" % i)), "PNG", 1920, 1080)
    pres.Save()  # transitions live in the file, not just the session
    pres.Close()
    app.Quit()
    print("renders in", out)


if __name__ == "__main__":
    main()
