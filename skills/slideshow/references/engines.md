# Engines — PowerPoint 365 via python-pptx + COM

> One engine. `python-pptx` owns geometry and content; PowerPoint COM owns
> transitions, entrances, renders, PDF. There is no fallback engine:
> LibreOffice headless hangs on this box, and Marp/HTML export rasterizes
> slides into uneditable PNGs.

## Install (once per machine)

```bash
python -m pip install python-pptx lxml Pillow pywin32
```

Always `python -m pip` — the `pip.exe` wrapper is corrupt. `pywin32` needs a
post-install typelib pass on first COM use (makepy writes to
`%TEMP%\gen_py\3.12\` — normal, leave it alone).

## PowerPoint location + version floor

- Desktop PowerPoint 365: `C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE`
- Verified: version 16.0.20430 — Morph fully supported.
- Version floor for Morph (`p159:morph option="byObject"`): PowerPoint 2019 /
  Microsoft 365. PowerPoint 2016 or older: ship fade-only (the `<p:fade/>`
  fallback still plays).
- If no desktop PowerPoint exists on the box: content + OOXML verification
  still run, but motion authoring and render inspection are BLOCKED — say so,
  don't fake it.

## COM setup (copy verbatim)

```python
import os, subprocess
subprocess.run(["taskkill", "/F", "/IM", "POWERPNT.EXE"],
               capture_output=True)  # zombie EXEs lock the file + reject calls
from win32com.client.gencache import EnsureDispatch  # NOT win32com.client
app = EnsureDispatch("PowerPoint.Application")
app.DisplayAlerts = 0  # ppAlertsNone = 1, but 0 also suppresses: use 0
pres = app.Presentations.Open(path, WithWindow=False)
```

Notes: `EnsureDispatch` lives in `win32com.client.gencache` (the top-level
re-export is missing in pywin32 v312). `Slide.Export` takes POSITIONAL args:
`slide.Export(path, "PNG", 1920, 1080)`. `Presentations.Open` with
`WithWindow=False` keeps the desktop clean. A zombie `POWERPNT.EXE` answers
COM with `Call was rejected by callee` — taskkill first, always.

## Enum table (read from this machine's own typelibs — do not guess)

| Constant | Value | Use |
|---|---|---|
| `ppEffectFade` | 1793 | break-section transitions |
| `ppEffectMorphByObject` | 3954 | default transition |
| `ppEffectMorphByWord` | 3955 | spare — word-level morph |
| `ppEffectMorphByChar` | 3956 | spare — char-level morph |
| `msoAnimEffectFade` | 10 | entrance effect |
| `msoAnimEffectWipe` | 22 | cinematic entrance (direction via `EffectParameters.Direction`: 1=up, 2=right, 3=down, 4=left) |
| `msoAnimEffectZoom` | 26 | cinematic entrance (serializes as wipe+scale pair) |
| motion-path preset | 86 | base for custom paths (`Behaviors(1).MotionEffect.Path`, pure `animMotion`) |
| `triggerOnPageClick` | 1 | default trigger (avoid) |
| `triggerAfterPrevious` | 3 | entrance chains |
| `animateLevelNone` | 0 | keep paragraphs whole |
| `ppAlertsNone` | 1 | (we set `DisplayAlerts = 0`) |

No `ppTransSpeed` enum exists in the typelib — leave `Speed` at default.

## Serialization (what PowerPoint 365 writes — read-only knowledge)

PowerPoint 365 serializes Morph as `p159` (2015/09), NOT the older `p14` form
in most blog posts:

```xml
<mc:AlternateContent><mc:Choice Requires="p159">
  <p:transition spd="slow" p14:dur="2000">
    <p159:morph option="byObject"/></p:transition>
</mc:Choice><mc:Fallback><p:transition spd="slow"><p:fade/></p:transition>
</mc:Fallback></mc:AlternateContent>
```

Even plain fades get AlternateContent-wrapped. The verifier accepts `p14` or
`p159` morph + a fade fallback. Never hand-write this XML — author it through
COM and assert on the result.

## Canvas lock (stolen from ppt-master — steal the numbers too)

- Slide size 13.333 × 7.5 in = 1280 × 720 @96dpi. 16:9, always.
- Content margins 60px (0.625in) on all sides; live content zone 1160 × 600.
- Background is always an explicit rectangle (theme `bg1` left at default).
- Asset naming: `<NN>_<name>.jpg` (`03_cuavan.jpg`) — order + identity in
  one string. Notes key: slide index + title, same stem.

## What goes where (ownership)

| Concern | Owner | Never |
|---|---|---|
| Shapes, text, pictures, notes | python-pptx (`build.py`) | hand-edit the zip |
| Transitions, entrances, advance | COM (`motion.py`) | python-pptx (no API) |
| Truth on re-run | scripts (rebuild clean) | re-run motion on one file |
| Visual proof | COM PNG renders, read by eye | XML dumps, assumed geometry |
