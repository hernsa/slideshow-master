# Governance: failure-recovery catalog

> Symptom → owning layer → recovery → re-verify gate. Recovery never
> skips its re-verify gate. Scripts are the truth: fix in `build.py` /
> `motion.py`, never in the .pptx.

| # | Symptom | Owning layer | Recovery | Re-verify |
|---|---|---|---|---|
| 1 | `Call was rejected by callee` | COM hygiene | taskkill POWERPNT, rebuild clean, run motion once | Gate 12 |
| 2 | Transitions missing after motion pass | motion.py | add `pres.Save()` before `Close()`; re-run once on a clean rebuild | verify-pptx trans |
| 3 | Morph carries nothing (static cut) | build.py names | exact-match `name=` across slides; check continuity report | Gate 15.3 |
| 4 | White wedge on rotated photo | build.py geometry | bake tilt in PIL (`content_rot`), shape rotation 0, rebuild | render eye |
| 5 | Stretched / squashed photo | assets prep | PIL center-crop to target aspect before `add_picture` | render eye |
| 6 | White-on-daylight body copy | plate/scrim | darken plate (`.85`→`.45`) or widen scrim; cut words, never type size | Gates 4, 10 |
| 7 | `Catastrophic failure` from COM | file lock | close PowerPoint GUI + taskkill zombies, rebuild clean | Gate 12 |
| 8 | `verify-pptx` fx budget breach | motion.py | cut entrances to ≤3 fade-only; rebuild clean, run once | Gate 8 |
| 9 | `advTm present` failure | motion.py | set `AdvanceOnTime = False` on every slide | Gate 8 |
| 10 | Zero rasters / missing CREDITS line | assets | source + prep + credit, rebuild | Gate 3 |
| 11 | `pip` wrapper corrupt (`pip.exe` fails) | environment | always `python -m pip`, never `pip[.exe]` | install |
| 12 | `EnsureDispatch` missing from `win32com.client` | environment | `from win32com.client.gencache import EnsureDispatch` | motion run |
| 13 | LibreOffice headless hangs | environment | abandoned — PowerPoint COM is the render path | Gate 11 |
| 14 | Placeholder text shipped | build.py copy | fix copy from research-notes, rebuild | Gate 5 |
| 15 | Anchor drift after refine | spec discipline | re-read spec `Anchors:` lines, restore names, rebuild | Gate 15.3 |
