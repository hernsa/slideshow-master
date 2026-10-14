"""Scaffold a new PPTX deck project.

Usage:  python scaffold.py <deck-dir>

Creates <deck-dir>/ with build.py (helper library + slide stubs),
motion.py (COM transitions/entrances/renders), verify_extra.py
(deck-specific asserts), plus assets/ and renders/ dirs.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BUILD_TMPL = '''"""BUILD THIS DECK HERE. Geometry + content + notes live here.
Motion (transitions/entrances) lives in motion.py via PowerPoint COM.
Never hand-edit the .pptx: this file is the truth — rebuild clean.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.oxml.xmlchemy import OxmlElement

HERE = Path(__file__).parent
ASSETS = HERE / "assets"
OUT = HERE / "deck.pptx"  # <-- rename per deck

# ---------- palette (LOCK at style time: BG/INK/ACCENT/ACCENT2/MUTED/CARD) ----------
BG = "06232B"
INK = "F5F5F7"
ACCENT = "34D399"
ACCENT2 = "F4C95D"
MUTED = "9FB8BE"
CARD = "0B3540"
FONT = "Segoe UI"

SW, SH = 13.333, 7.5  # 16:9 stage in inches (= 1280x720 @96dpi)
SQ = {}  # square-crop cache shared by circle_pic / diamond_pic


# ---------- internals ----------
def solid_alpha(shape, hex_color, alpha_pct):
    """Solid fill + transparency (python-pptx has no API; inject a:alpha)."""
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor.from_string(hex_color)
    solid = shape.fill._xPr.find(qn("a:solidFill"))
    clr = solid.find(qn("a:srgbClr"))
    if clr is None:
        clr = solid[0]
    alpha = OxmlElement("a:alpha")
    alpha.set("val", str(int(alpha_pct * 1000)))
    clr.append(alpha)


def no_line(shape):
    shape.line.fill.background()


def add_text(slide, left, top, width, height, name=None, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(Inches(left), Inches(top),
                                   Inches(width), Inches(height))
    box.text_frame.word_wrap = True
    for p in box.text_frame.paragraphs:
        p.alignment = align
    if name:
        box.name = name
    no_line(box)
    box.fill.background()
    return box


def _run(p, text, size, color, bold=False, italic=False, font=None):
    r = p.add_run()
    r.text = text
    r.font.name = font or FONT
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = RGBColor.from_string(color)
    return r


def para(box, text, size, color=INK, bold=False, italic=False,
         space_after=Pt(4), line_spacing=1.15, align=None, first=False):
    tf = box.text_frame
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    if align is not None:
        p.alignment = align
    p.space_after = space_after
    p.line_spacing = line_spacing
    _run(p, text, size, color, bold, italic)
    return p


# ---------- Helper API contract (matches layout-templates/_index.md) ----------
def new_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])  # blank


def solid_bg(slide, hex_color):
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = RGBColor.from_string(hex_color)


def plate(slide, src, brightness, name="bg-plate"):
    """Full-bleed darkened plate (PIL-preprocessed, cached in assets/)."""
    out = ASSETS / ("plate_%s_%d.jpg" % (Path(src).stem, int(brightness * 100)))
    if not out.exists():
        im = Image.open(ASSETS / src).convert("RGB")
        im = ImageEnhance.Brightness(im).enhance(brightness)
        im = ImageEnhance.Color(im).enhance(0.92)
        im = im.filter(ImageFilter.GaussianBlur(2))
        im.save(out, quality=88)
    pic = slide.shapes.add_picture(str(out), Inches(-0.8), Inches(-0.45),
                                   Inches(SW * 1.12), Inches(SH * 1.12))
    pic.name = name
    pic.line.fill.background()
    return pic


def scrim_left(slide, width_frac=0.62, alpha_pct=62, name="scrim-left"):
    sc = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                                Inches(SW * width_frac), Inches(SH))
    solid_alpha(sc, BG, alpha_pct)
    no_line(sc)
    sc.name = name
    return sc


def scrim_right(slide, width_frac=0.62, alpha_pct=62, name="scrim-left"):
    """Mirrored scrim. Keeps 'scrim-left' name so Morph carries it."""
    sc = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                Inches(SW * (1 - width_frac)), Inches(0),
                                Inches(SW * width_frac), Inches(SH))
    solid_alpha(sc, BG, alpha_pct)
    no_line(sc)
    sc.name = name
    return sc


def _square(src):
    key = "sq_%s.jpg" % Path(src).stem
    if key not in SQ:
        im = Image.open(ASSETS / src).convert("RGB")
        s = min(im.size)
        x = (im.width - s) // 2
        y = (im.height - s) // 2
        im.crop((x, y, x + s, y + s)).save(ASSETS / key, quality=90)
        SQ[key] = True
    return ASSETS / key


def circle_pic(slide, src, left, top, size, name):
    pic = slide.shapes.add_picture(str(_square(src)), Inches(left),
                                   Inches(top), Inches(size), Inches(size))
    pic._element.spPr.find(qn("a:prstGeom")).set("prst", "ellipse")
    pic.line.color.rgb = RGBColor.from_string("FFFFFF")
    pic.line.width = Pt(1.5)
    pic.name = name
    return pic


def diamond_pic(slide, src, left, top, size, name, content_rot=0):
    """Diamond-geometry photo. Shape rotation stays 0 (PowerPoint renders
    rotated custom-geometry pictures with a white wedge); tilt is baked
    into pixels — content_rot in PIL degrees (CCW+)."""
    key = "sqrot_%s_%d.jpg" % (Path(src).stem, int(content_rot))
    if key not in SQ:
        im = Image.open(ASSETS / src).convert("RGB")
        s = min(im.size)
        x = (im.width - s) // 2
        y = (im.height - s) // 2
        im = im.crop((x, y, x + s, y + s))
        if content_rot:
            im = im.rotate(content_rot, expand=True,
                           resample=Image.BICUBIC)
            s2 = min(im.size)
            x = (im.width - s2) // 2
            y = (im.height - s2) // 2
            im = im.crop((x, y, x + s2, y + s2))
        im.save(ASSETS / key, quality=90)
        SQ[key] = True
    pic = slide.shapes.add_picture(str(ASSETS / key), Inches(left),
                                   Inches(top), Inches(size), Inches(size))
    pic._element.spPr.find(qn("a:prstGeom")).set("prst", "diamond")
    pic.line.color.rgb = RGBColor.from_string("FFFFFF")
    pic.line.width = Pt(1.5)
    pic.rotation = 0.0
    pic.name = name
    return pic


def rect_pic(slide, src, left, top, width, height, name):
    pic = slide.shapes.add_picture(str(ASSETS / src), Inches(left),
                                   Inches(top), Inches(width), Inches(height))
    pic.line.color.rgb = RGBColor.from_string("FFFFFF")
    pic.line.width = Pt(1.0)
    pic.name = name
    return pic


def kicker(slide, top, text, color, name="kicker", left=0.633):
    box = add_text(slide, left, top, 11.0, 0.45, name=name)
    para(box, text, 11, color, bold=True, space_after=Pt(2), first=True)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left),
                                 Inches(top + 0.38), Inches(1.15), Pt(3))
    bar.fill.solid()
    bar.fill.fore_color.rgb = RGBColor.from_string(color)
    no_line(bar)
    bar.name = name + "-bar"


def _accent_box(slide, left, top, width, height, text, size, color,
                accent, accent_color, bold, align, name, mono,
                line_spacing, space_after):
    box = add_text(slide, left, top, width, height, name=name, align=align)
    tf = box.text_frame
    p = tf.paragraphs[0]
    p.space_after = space_after
    p.line_spacing = line_spacing
    if accent and accent in text:
        pre, _, post = text.partition(accent)
        if pre:
            _run(p, pre, size, color, bold, font="Consolas" if mono else None)
        _run(p, accent, size, accent_color, bold,
             font="Consolas" if mono else None)
        if post:
            _run(p, post, size, color, bold, font="Consolas" if mono else None)
    else:
        _run(p, text, size, color, bold, font="Consolas" if mono else None)
    return box


def title(slide, left, top, width, height, text, size=44, color=INK,
          accent=None, accent_color=ACCENT, bold=True, align=PP_ALIGN.LEFT,
          name=None, mono=False):
    return _accent_box(slide, left, top, width, height, text, size, color,
                       accent, accent_color, bold, align, name, mono, 1.0,
                       Pt(8))


def body(slide, left, top, width, height, text, size=16, color=INK,
         accent=None, accent_color=ACCENT, align=PP_ALIGN.LEFT, name=None):
    return _accent_box(slide, left, top, width, height, text, size, color,
                       accent, accent_color, False, align, name, False, 1.35,
                       Pt(4))


def gloss(slide, left, top, width, text, color=MUTED, name=None):
    box = add_text(slide, left, top, width, 0.4, name=name)
    para(box, text, 11, color, space_after=Pt(0), first=True)
    return box


def pill(slide, left, top, text, color, name, width=2.3, outline=False):
    p = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                               Inches(left), Inches(top),
                               Inches(width), Inches(0.52))
    if outline:
        p.fill.background()
        p.line.color.rgb = RGBColor.from_string(color)
        p.line.width = Pt(2)
    else:
        solid_alpha(p, color, 16)
        p.line.fill.background()
    p.name = name
    tf = p.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.12)
    tf.margin_right = Inches(0.12)
    par = tf.paragraphs[0]
    par.alignment = PP_ALIGN.CENTER
    _run(par, text, 11, color, bold=True)
    return p


def round_rect(slide, left, top, width, height, fill_hex, name,
               line_hex=None):
    r = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                               Inches(left), Inches(top),
                               Inches(width), Inches(height))
    r.fill.solid()
    r.fill.fore_color.rgb = RGBColor.from_string(fill_hex)
    if line_hex:
        r.line.color.rgb = RGBColor.from_string(line_hex)
        r.line.width = Pt(2)
    else:
        no_line(r)
    r.name = name
    return r


def deco_blob(slide, left, top, size, color, alpha_pct, name):
    o = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left), Inches(top),
                               Inches(size), Inches(size))
    solid_alpha(o, color, alpha_pct)
    no_line(o)
    o.name = name
    return o


def deco_ring(slide, left, top, size, color, name, w_pt=2.25):
    o = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left), Inches(top),
                               Inches(size), Inches(size))
    o.fill.background()
    o.line.color.rgb = RGBColor.from_string(color)
    o.line.width = Pt(w_pt)
    o.name = name
    return o


def glow(slide, cx, cy, size, color, name, steps=3, alpha_pct=28):
    """Spotlight substitute: concentric translucent ellipses (never OuterGlow)."""
    for i in range(steps, 0, -1):
        d = size * i / steps
        o = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - d / 2),
                                   Inches(cy - d / 2), Inches(d), Inches(d))
        solid_alpha(o, color, alpha_pct / i)
        no_line(o)
        o.name = "%s-%d" % (name, i)
    return name


def leader(slide, left, top, length, label, color, name):
    """Annotation callout: 1px line + 12px dot + 18pt label."""
    ln = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left),
                                Inches(top), Inches(length), Pt(1))
    ln.fill.solid()
    ln.fill.fore_color.rgb = RGBColor.from_string(color)
    no_line(ln)
    ln.name = name + "-line"
    dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left - 0.08),
                                 Inches(top - 0.08), Inches(0.16),
                                 Inches(0.16))
    dot.fill.solid()
    dot.fill.fore_color.rgb = RGBColor.from_string(color)
    no_line(dot)
    dot.name = name + "-dot"
    box = add_text(slide, left + length + 0.15, top - 0.22, 4.0, 0.5,
                   name=name)
    para(box, label, 18, INK, first=True, space_after=Pt(0))


def set_notes(slide, text):
    slide.notes_slide.placeholders[1].text_frame.text = text


# ---------- slides (FILL FROM visual-plan.md — one function per slide) ----------
def s1_title(prs):
    s = new_slide(prs)
    solid_bg(s, BG)
    kicker(s, 1.55, "KICKER LINE", ACCENT)
    title(s, 0.633, 2.15, 7.6, 2.6, "Slide one headline", size=54,
          name="hero")
    body(s, 0.633, 4.55, 7.6, 1.6, "One supporting sentence.", name="sub")
    set_notes(s, "S1 Title\\nFirst spoken beat.")


def main():
    prs = Presentation()
    prs.slide_width = Inches(SW)
    prs.slide_height = Inches(SH)
    s1_title(prs)
    prs.save(OUT)
    print("saved", OUT)


if __name__ == "__main__":
    main()
'''

MOTION_TMPL = '''"""Transitions + entrances + renders via PowerPoint COM.
REBUILD CLEAN: COM doubles effects on re-run — delete the .pptx, run
build.py, then run this. Never run twice on the same file.
"""
import sys
import subprocess
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = Path(__file__).parent
PPTX = HERE / "deck.pptx"  # <-- rename per deck
OUT = HERE / "renders"

MORPH_OBJECT = 3954
MORPH_WORD = 3955
MORPH_CHAR = 3956
FADE = 1793
FX_FADE = 10
ON_CLICK = 1
AFTER_PREV = 3

FADE_SLIDES = {1}  # 1-based slides that take fade instead of Morph


def main():
    subprocess.run(["taskkill", "/F", "/IM", "POWERPNT.EXE"],
                   capture_output=True)
    time.sleep(2)
    from win32com.client.gencache import EnsureDispatch
    app = EnsureDispatch("PowerPoint.Application")
    app.DisplayAlerts = 0  # ppAlertsNone
    pres = app.Presentations.Open(str(PPTX), WithWindow=False)
    for i, slide in enumerate(pres.Slides, start=1):
        slide.SlideShowTransition.EntryEffect = (
            FADE if i in FADE_SLIDES else MORPH_OBJECT)
        slide.SlideShowTransition.AdvanceOnTime = False
        slide.SlideShowTransition.AdvanceOnClick = True
    # Entrances: <=3 per slide, fade, after-previous, 100-150ms apart.
    # Add per-slide blocks here following the visual-plan Entrances: lines.
    OUT.mkdir(exist_ok=True)
    for i, slide in enumerate(pres.Slides, start=1):
        slide.Export(str(OUT / ("s%d.png" % i)), "PNG", 1920, 1080)
    pres.Save()  # transitions live in the file, not just the session
    pres.Close()
    app.Quit()
    print("renders in", OUT)


if __name__ == "__main__":
    main()
'''

VERIFY_EXTRA_TMPL = '''"""Deck-specific asserts beyond scripts/verify-pptx.py.
Run after verify-pptx.py passes. Add named-anchor and copy checks here.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from pptx import Presentation

PPTX = Path(__file__).parent / "deck.pptx"  # <-- rename per deck

failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


def main():
    prs = Presentation(str(PPTX))
    # Example: every slide carries the deck's named anchors.
    # for i, slide in enumerate(prs.slides, start=1):
    #     names = {s.name for s in slide.shapes}
    #     check("hero" in names, "slide %d: missing anchor 'hero'" % i)
    print("slides: %d" % len(prs.slides._sldIdLst))
    if failures:
        print("FAIL")
        for f in failures:
            print(" -", f)
        sys.exit(1)
    print("OK: deck-specific asserts pass")


if __name__ == "__main__":
    main()
'''


def main():
    if len(sys.argv) != 2:
        print("usage: python scaffold.py <deck-dir>")
        sys.exit(1)
    root = Path(sys.argv[1])
    root.mkdir(parents=True, exist_ok=True)
    (root / "assets").mkdir(exist_ok=True)
    (root / "renders").mkdir(exist_ok=True)
    (root / "build.py").write_text(BUILD_TMPL, encoding="utf-8")
    (root / "motion.py").write_text(MOTION_TMPL, encoding="utf-8")
    (root / "verify_extra.py").write_text(VERIFY_EXTRA_TMPL,
                                          encoding="utf-8")
    print("scaffolded", root)


if __name__ == "__main__":
    main()
