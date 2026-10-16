"""Scaffold a new PPTX deck project.

Usage:  python scaffold.py <deck-dir>

Creates <deck-dir>/ with build.py (helper library + slide stubs),
motion.py (COM transitions/entrances/renders), verify_extra.py
(deck-specific asserts), research-notes.md + visual-plan.md stubs,
plus assets/ and renders/ dirs.
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
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
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


def _rgb(c):
    """RGBColor from a hex string, tolerating a leading '#'."""
    return RGBColor.from_string(c[1:] if c.startswith("#") else c)


# ---------- internals ----------
def solid_alpha(shape, hex_color, alpha_pct):
    """Solid fill + transparency (python-pptx has no API; inject a:alpha)."""
    shape.fill.solid()
    shape.fill.fore_color.rgb = _rgb(hex_color)
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
    r.font.color.rgb = _rgb(color)
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
PRS = None  # module-level presentation; new_slide() with no arg uses it


def _pres():
    global PRS
    if PRS is None:
        PRS = Presentation()
        PRS.slide_width = Inches(SW)
        PRS.slide_height = Inches(SH)
    return PRS


def _align(value):
    """Accept 'left'/'center'/'right' or a PP_ALIGN enum."""
    if isinstance(value, str):
        return {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER,
                "right": PP_ALIGN.RIGHT, "justify": PP_ALIGN.JUSTIFY}.get(
                    value.lower(), PP_ALIGN.LEFT)
    return value


def _height(size):
    """Approximate a textbox height (inches) for a font size. Overflow still
    renders — this only keeps the first line from clipping."""
    return max(0.5, size * 1.5 / 72.0)


def _asset(src):
    p = Path(src)
    return p if p.is_absolute() else HERE / p


def new_slide(prs=None):
    p = prs if prs is not None else _pres()
    return p.slides.add_slide(p.slide_layouts[6])  # blank


def solid_bg(slide, hex_color):
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = _rgb(hex_color)


def plate(slide, src, brightness, name="bg-plate"):
    """Full-bleed darkened plate (PIL-preprocessed, cached in assets/)."""
    out = ASSETS / ("plate_%s_%d.jpg" % (Path(src).stem, int(brightness * 100)))
    if not out.exists():
        im = Image.open(_asset(src)).convert("RGB")
        im = ImageEnhance.Brightness(im).enhance(brightness)
        im = ImageEnhance.Color(im).enhance(0.92)
        im = im.filter(ImageFilter.GaussianBlur(2))
        im.save(out, quality=88)
    pic = slide.shapes.add_picture(str(out), Inches(-0.8), Inches(-0.45),
                                   Inches(SW * 1.12), Inches(SH * 1.12))
    pic.name = name
    pic.line.fill.background()
    return pic


def _scrim(slide, left_in, width_frac, alpha, name):
    sc = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left_in),
                                Inches(0), Inches(SW * width_frac),
                                Inches(SH))
    pct = alpha * 100 if alpha <= 1 else alpha
    solid_alpha(sc, BG, pct)
    no_line(sc)
    sc.name = name
    return sc


def scrim_left(slide, alpha=0.62, name="scrim-left"):
    return _scrim(slide, 0, 0.62, alpha, name)


def scrim_right(slide, alpha=0.62, name="scrim-left"):
    """Mirrored scrim. Keeps 'scrim-left' name so Morph carries it."""
    return _scrim(slide, SW * (1 - 0.62), 0.62, alpha, name)


def _square(src):
    key = "sq_%s.jpg" % Path(src).stem
    if key not in SQ:
        im = Image.open(_asset(src)).convert("RGB")
        s = min(im.size)
        x = (im.width - s) // 2
        y = (im.height - s) // 2
        im.crop((x, y, x + s, y + s)).save(ASSETS / key, quality=90)
        SQ[key] = True
    return ASSETS / key


def _rotated(src, rot, tag):
    """Bake rotation into pixels (cache by rot); re-crop to source aspect."""
    if not rot:
        return _asset(src)
    key = "%s_%s_%d.jpg" % (tag, Path(src).stem, int(rot))
    if key not in SQ:
        im = Image.open(_asset(src)).convert("RGB")
        ar = im.width / im.height
        r = im.rotate(rot, expand=True, resample=Image.BICUBIC)
        if r.width / r.height > ar:
            nw = int(r.height * ar)
            x = (r.width - nw) // 2
            r = r.crop((x, 0, x + nw, r.height))
        else:
            nh = int(r.width / ar)
            y = (r.height - nh) // 2
            r = r.crop((0, y, r.width, y + nh))
        r.save(ASSETS / key, quality=90)
        SQ[key] = True
    return ASSETS / key


def circle_pic(slide, name, src, cx, cy, d):
    pic = slide.shapes.add_picture(str(_square(src)), Inches(cx - d / 2),
                                   Inches(cy - d / 2), Inches(d), Inches(d))
    pic._element.spPr.find(qn("a:prstGeom")).set("prst", "ellipse")
    pic.line.color.rgb = _rgb("FFFFFF")
    pic.line.width = Pt(1.5)
    pic.name = name
    return pic


def diamond_pic(slide, name, src, cx, cy, d, rot=0):
    """Diamond-geometry photo. Shape rotation stays 0 (PowerPoint renders
    rotated custom-geometry pictures with a white wedge); tilt is baked
    into pixels — rot in PIL degrees (CCW+)."""
    key = "sqrot_%s_%d.jpg" % (Path(src).stem, int(rot))
    if key not in SQ:
        im = Image.open(_asset(src)).convert("RGB")
        s = min(im.size)
        x = (im.width - s) // 2
        y = (im.height - s) // 2
        im = im.crop((x, y, x + s, y + s))
        if rot:
            im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
            s2 = min(im.size)
            x = (im.width - s2) // 2
            y = (im.height - s2) // 2
            im = im.crop((x, y, x + s2, y + s2))
        im.save(ASSETS / key, quality=90)
        SQ[key] = True
    pic = slide.shapes.add_picture(str(ASSETS / key), Inches(cx - d / 2),
                                   Inches(cy - d / 2), Inches(d), Inches(d))
    pic._element.spPr.find(qn("a:prstGeom")).set("prst", "diamond")
    pic.line.color.rgb = _rgb("FFFFFF")
    pic.line.width = Pt(1.5)
    pic.rotation = 0.0
    pic.name = name
    return pic


def rect_pic(slide, name, src, x, y, w, h, rot=0):
    """Rectangular photo (name may be None). rot baked in PIL (CCW+)."""
    pic = slide.shapes.add_picture(str(_rotated(src, rot, "sqrot2")),
                                   Inches(x), Inches(y), Inches(w), Inches(h))
    pic.line.color.rgb = _rgb("FFFFFF")
    pic.line.width = Pt(1.0)
    if name:
        pic.name = name
    return pic


def kicker(slide, text, x, y, color, name=None):
    nm = name or "kicker"
    box = add_text(slide, x, y, 11.0, 0.45, name=nm)
    para(box, text, 11, color, bold=True, space_after=Pt(2), first=True)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x),
                                 Inches(y + 0.38), Inches(1.15), Pt(3))
    bar.fill.solid()
    bar.fill.fore_color.rgb = _rgb(color)
    no_line(bar)
    bar.name = nm + "-bar"


def _accent_box(slide, left, top, width, height, text, size, color,
                accent, accent_color, bold, align, name, mono,
                line_spacing, space_after):
    box = add_text(slide, left, top, width, height, name=name,
                   align=_align(align))
    tf = box.text_frame
    p = tf.paragraphs[0]
    p.space_after = space_after
    p.line_spacing = line_spacing
    font = "Consolas" if mono else None
    if accent and accent in text:
        pre, _, post = text.partition(accent)
        if pre:
            _run(p, pre, size, color, bold, font=font)
        _run(p, accent, size, accent_color, bold, font=font)
        if post:
            _run(p, post, size, color, bold, font=font)
    else:
        _run(p, text, size, color, bold, font=font)
    return box


def title(slide, text, x, y, w, size=44, color=INK, accent=None,
          accent_color=None, align="left", name=None, mono=False):
    return _accent_box(slide, x, y, w, _height(size), text, size, color,
                       accent, accent_color or ACCENT, True, align, name,
                       mono, 1.0, Pt(8))


def body(slide, text, x, y, w, size=16, color=INK, accent=None,
         accent_color=None, align="left", name=None, mono=False):
    return _accent_box(slide, x, y, w, _height(size) * 2.2, text, size, color,
                       accent, accent_color or ACCENT, False, align, name,
                       mono, 1.35, Pt(4))


def gloss(slide, text, x, y, w, color=MUTED, size=11, name=None):
    box = add_text(slide, x, y, w, _height(size), name=name)
    para(box, text, size, color, space_after=Pt(0), first=True)
    return box


def pill(slide, text, x, y, w, fill, color, outline=None):
    p = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x),
                               Inches(y), Inches(w), Inches(0.52))
    p.fill.solid()
    p.fill.fore_color.rgb = _rgb(fill)
    if outline:
        p.line.color.rgb = _rgb(outline)
        p.line.width = Pt(1.25)
    else:
        no_line(p)
    p.name = "pill-%s" % text
    tf = p.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.12)
    tf.margin_right = Inches(0.12)
    par = tf.paragraphs[0]
    par.alignment = PP_ALIGN.CENTER
    _run(par, text, 11, color, bold=True)
    return p


def round_rect(slide, name, x, y, w, h, fill, line=None):
    r = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x),
                               Inches(y), Inches(w), Inches(h))
    r.fill.solid()
    r.fill.fore_color.rgb = _rgb(fill)
    if line:
        r.line.color.rgb = _rgb(line)
        r.line.width = Pt(2)
    else:
        no_line(r)
    r.name = name
    return r


def deco_blob(slide, name, cx, cy, w, h, color):
    o = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - w / 2),
                               Inches(cy - h / 2), Inches(w), Inches(h))
    o.fill.solid()
    o.fill.fore_color.rgb = _rgb(color)
    no_line(o)
    o.name = name
    return o


def deco_ring(slide, name, cx, cy, d, color):
    o = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - d / 2),
                               Inches(cy - d / 2), Inches(d), Inches(d))
    o.fill.background()
    o.line.color.rgb = _rgb(color)
    o.line.width = Pt(2.25)
    o.name = name
    return o


def glow(slide, cx, cy, d, color, name="glow", steps=3, alpha_pct=28):
    """Spotlight substitute: concentric translucent ellipses (never OuterGlow)."""
    for i in range(steps, 0, -1):
        dd = d * i / steps
        o = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - dd / 2),
                                   Inches(cy - dd / 2), Inches(dd), Inches(dd))
        solid_alpha(o, color, alpha_pct / i)
        no_line(o)
        o.name = "%s-%d" % (name, i)
    return name


def leader(slide, name, x1, y1, x2, y2, label):
    """Annotation callout: straight line + 12px dot + 18pt label."""
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1),
                                    Inches(y1), Inches(x2), Inches(y2))
    ln.line.color.rgb = _rgb(ACCENT)
    ln.line.width = Pt(1)
    ln.name = name + "-line"
    dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x1 - 0.08),
                                 Inches(y1 - 0.08), Inches(0.16), Inches(0.16))
    dot.fill.solid()
    dot.fill.fore_color.rgb = _rgb(ACCENT)
    no_line(dot)
    dot.name = name + "-dot"
    box = add_text(slide, x2 + 0.15, y1 - 0.22, 4.0, 0.5, name=name)
    para(box, label, 18, INK, first=True, space_after=Pt(0))


def connect(slide, name, x1, y1, x2, y2, color=ACCENT, width_pt=2.25,
            arrow=True):
    """Straight connector (diagram fork arrows). The arrowhead is a baked
    a:tailEnd triangle — never a separate triangle shape (it detaches)."""
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1),
                                    Inches(y1), Inches(x2), Inches(y2))
    ln.line.color.rgb = _rgb(color)
    ln.line.width = Pt(width_pt)
    if arrow:
        tail = ln.line._ln.find(qn("a:tailEnd"))
        if tail is None:
            tail = OxmlElement("a:tailEnd")
            ln.line._ln.append(tail)
        tail.set("type", "triangle")
        tail.set("w", "med")
        tail.set("len", "med")
    ln.name = name
    return ln


def dot(slide, name, cx, cy, d=0.16, color=ACCENT):
    """Standalone anchor dot (icon dots, leader dots). d in inches."""
    o = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - d / 2),
                               Inches(cy - d / 2), Inches(d), Inches(d))
    o.fill.solid()
    o.fill.fore_color.rgb = _rgb(color)
    no_line(o)
    o.name = name
    return o


def _cell_borders(cell, bottom_only=False, rule_color=MUTED, rule_pt=0.75):
    """Kill vertical rules; optional 0.75pt bottom rule (tables.md)."""
    tcPr = cell._tc.get_or_add_tcPr()
    for tag in ("a:lnL", "a:lnR", "a:lnU", "a:lnD"):
        ln = tcPr.find(qn(tag))
        if ln is None:
            ln = OxmlElement(tag)
            tcPr.append(ln)
        ln.clear()
        ln.set("w", str(int(rule_pt * 12700)))
        if bottom_only and tag == "a:lnD":
            fill = OxmlElement("a:solidFill")
            clr = OxmlElement("a:srgbClr")
            clr.set("val", rule_color[1:]
                    if rule_color.startswith("#") else rule_color)
            fill.append(clr)
            ln.append(fill)
        else:
            ln.append(OxmlElement("a:noFill"))


def table(slide, name, x, y, w, h, rows, header_fill=ACCENT,
          header_size=14, body_size=13):
    """Slide table (last resort per charts.md). rows[0] is the header.
    Enforces tables.md: <=4 rows x <=3 cols, 13pt minimum body."""
    if len(rows) > 4 or any(len(r) > 3 for r in rows):
        raise ValueError("table: max 4 rows x 3 cols (tables.md handout rule)")
    if body_size < 13:
        raise ValueError("table: body 13pt minimum (tables.md)")
    nrows, ncols = len(rows), max(len(r) for r in rows)
    gf = slide.shapes.add_table(nrows, ncols, Inches(x), Inches(y),
                                Inches(w), Inches(h))
    tbl = gf.table
    for i in range(ncols):
        tbl.columns[i].width = Inches(w / ncols)
    for r in range(nrows):
        tbl.rows[r].height = Inches(0.42 if r == 0 else 0.38)
        for c in range(ncols):
            cell = tbl.cell(r, c)
            val = str(rows[r][c]) if c < len(rows[r]) else ""
            if r == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = _rgb(header_fill)
                _cell_borders(cell, bottom_only=True)
            else:
                cell.fill.background()
                _cell_borders(cell)
            cell.margin_left = Inches(0.06)
            cell.margin_right = Inches(0.06)
            cell.margin_top = Inches(0.02)
            cell.margin_bottom = Inches(0.02)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = ""
            if r == 0:
                _run(p, val, header_size, "FFFFFF", bold=True)
            else:
                _run(p, val, body_size, INK)
    gf.name = name
    return gf


def chart(slide, name, x, y, w, h, categories, series, kind="column",
          colors=(ACCENT, ACCENT2)):
    """Native chart (trends only — giant stat first per charts.md).
    categories: <=5 labels. series: [(label, [values])], <=2 series.
    kind: 'column' or 'line'. Strips gridlines + legend, flat fills."""
    if len(categories) > 5:
        raise ValueError("chart: max 5 categories (charts.md)")
    if len(series) > 2:
        raise ValueError("chart: max 2 series (charts.md)")
    ctype = (XL_CHART_TYPE.COLUMN_CLUSTERED if kind == "column"
             else XL_CHART_TYPE.LINE)
    cd = ChartData()
    cd.categories = list(categories)
    for label, values in series:
        cd.add_series(label, tuple(values))
    gf = slide.shapes.add_chart(ctype, Inches(x), Inches(y), Inches(w),
                                Inches(h), cd)
    ch = gf.chart
    ch.has_legend = False
    ch.value_axis.has_major_gridlines = False
    for ax in (ch.category_axis, ch.value_axis):
        ax.tick_labels.font.size = Pt(12)
        ax.tick_labels.font.color.rgb = _rgb(MUTED)
    plot = ch.plots[0]
    plot.has_data_labels = True
    plot.data_labels.font.size = Pt(12)
    plot.data_labels.font.color.rgb = _rgb(INK)
    for i, ser in enumerate(plot.series):
        col = colors[i % len(colors)]
        if kind == "column":
            ser.format.fill.solid()
            ser.format.fill.fore_color.rgb = _rgb(col)
            ser.format.line.fill.background()
        else:
            ser.format.line.color.rgb = _rgb(col)
            ser.format.line.width = Pt(2.25)
    gf.name = name
    return gf


def set_notes(slide, text):
    slide.notes_slide.placeholders[1].text_frame.text = text


def set_alt(shape, text):
    """Accessibility alt text (conclusion-first, <=140 chars) on any shape."""
    for el in shape._element.iter():
        if el.tag.endswith("}cNvPr"):
            el.set("descr", text)
            return shape
    return shape


# ---------- slides (FILL FROM visual-plan.md — one function per slide) ----------
def s1_title():
    s = new_slide()
    solid_bg(s, BG)
    kicker(s, "KICKER LINE", x=0.633, y=1.55, color=ACCENT)
    title(s, "Slide one headline", x=0.633, y=2.15, w=7.6, size=54,
          name="hero")
    body(s, "One supporting sentence.", x=0.633, y=4.55, w=7.6, name="sub")
    set_notes(s, "S1 Title\\nFirst spoken beat.")


def main():
    s1_title()
    _pres().save(OUT)
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

# ----- enum constants (from references/engines.md) -----
MORPH_OBJECT = 3954          # ppEffectMorphByObject
MORPH_WORD = 3955            # ppEffectMorphByWord
MORPH_CHAR = 3956            # ppEffectMorphByChar
FADE = 1793                  # ppEffectFade
FX_FADE = 10                 # msoAnimEffectFade
FX_WIPE = 22                 # msoAnimEffectWipe (direction via EffectParameters)
FX_ZOOM = 26                 # msoAnimEffectZoom (serializes as wipe+scale pair)
FX_PATH = 86                 # motion-path preset (Path retargeted per call)
WIPE_UP, WIPE_RIGHT, WIPE_DOWN, WIPE_LEFT = 1, 2, 3, 4  # EffectParameters.Direction
# All four IDs + all four directions measured live on this box via COM
# probes (AddEffect -> save -> read back serialized filter/path).
ON_CLICK = 1                 # triggerOnPageClick
AFTER_PREV = 3               # triggerAfterPrevious
ANIMATE_LEVEL_NONE = 0       # animateLevelNone

# ----- style-locked exceptions (max ~2 per deck) -----
FADE_SLIDES = {1}            # 1-based: slides that take Fade instead of Morph
# Example: FADE_SLIDES = {1, 6}

# ----- cinematic exception (Gate 8: ONE slide per deck, named at style lock) -----
CINEMATIC_SLIDES = set()    # 1-based: e.g. {4} — wipe/zoom/motion-path allowed here

# ----- entrance cadence (shared Gate 8 budget: <=3/slide, 100-150ms apart) -----
STAGGER = [
    (100, 300),   # 1st: kicker / headline
    (220, 300),   # 2nd: body / visual
    (340, 300),   # 3rd: visual / accent
]

# ----- COM helpers -----
def add_fade_entrance(slide, shape, delay_ms, duration_ms=300):
    """Add a fade entrance effect (after-previous chain)."""
    seq = slide.TimeLine.MainSequence
    fx = seq.AddEffect(shape, FX_FADE)
    fx.Timing.TriggerType = AFTER_PREV
    fx.Timing.TriggerDelayTime = delay_ms / 1000.0
    fx.Timing.Duration = duration_ms / 1000.0
    fx.Timing.Accelerate = 0
    fx.Timing.Decelerate = 0
    return fx

def add_wipe_entrance(slide, shape, direction=WIPE_LEFT, delay_ms=100,
                      duration_ms=300):
    """Add a wipe entrance (the sanctioned cinematic entrance).
    direction: WIPE_UP / WIPE_RIGHT / WIPE_DOWN / WIPE_LEFT (left is the deck
    default). Only call for slides named in CINEMATIC_SLIDES (max one/deck).
    """
    seq = slide.TimeLine.MainSequence
    fx = seq.AddEffect(shape, FX_WIPE)
    fx.EffectParameters.Direction = direction
    fx.Timing.TriggerType = AFTER_PREV
    fx.Timing.TriggerDelayTime = delay_ms / 1000.0
    fx.Timing.Duration = duration_ms / 1000.0
    return fx

def add_zoom_entrance(slide, shape, delay_ms=100, duration_ms=300):
    """Add a zoom entrance (serializes as a wipe+scale pair — Gate 8 counts
    it as ONE cinematic entrance on CINEMATIC_SLIDES).
    Only call for slides named in CINEMATIC_SLIDES (max one/deck).
    """
    seq = slide.TimeLine.MainSequence
    fx = seq.AddEffect(shape, FX_ZOOM)
    fx.Timing.TriggerType = AFTER_PREV
    fx.Timing.TriggerDelayTime = delay_ms / 1000.0
    fx.Timing.Duration = duration_ms / 1000.0
    return fx

def stagger_entrances(slide, shapes, base_delays=None):
    """Apply the cadence table to a list of shapes in reading order.
    shapes = [("hero", shape_obj), ("body", shape_obj), ("disc", shape_obj)]
    Returns list of created effects.
    """
    delays = base_delays if base_delays is not None else [d for d, _ in STAGGER]
    dur = STAGGER[0][1]
    for idx, (name, shp) in enumerate(shapes):
        if idx >= len(delays):
            break
        add_fade_entrance(slide, shp, delays[idx], dur)
    # keep paragraphs whole (no animate-by-word/char)
    for _, shp in shapes:
        try:
            shp.TextFrame2.Paragraphs[1].AnimationLevel = ANIMATE_LEVEL_NONE
        except Exception:
            pass

def parked_flight(slide, shape, from_left_in, to_left_in, duration_ms=1500):
    """Animate a parked shape flying in from off-canvas.
    Adds a motion path from (from_left_in, current top) to (to_left_in, current top).
    Pure animMotion: no entrance filter, so it sits outside the Gate 8 fade budget.
    Returns the created effect.
    """
    seq = slide.TimeLine.MainSequence
    fx = seq.AddEffect(slide.Shapes(shape.Name), FX_PATH, ANIMATE_LEVEL_NONE, AFTER_PREV)  # path preset, retargeted below
    # Retarget the preset's motion behavior to a custom left-to-right path
    fx.Behaviors(1).MotionEffect.Path = (
        f"M 0 0 L {int((to_left_in - from_left_in) * 914400)} 0"
    )  # EMU offset
    fx.Timing.Duration = duration_ms / 1000.0
    return fx

def check_anchor_continuity(pres, anchor_names):
    """Assert that named anchors exist on consecutive slides.
    Returns (continuity_pairs, warnings).
    """
    prev = None
    pairs = 0
    warns = []
    for i, slide in enumerate(pres.Slides, start=1):
        names = {s.name for s in slide.Shapes if s.name}
        if prev is not None:
            common = anchor_names & names & prev
            if common:
                pairs += 1
            else:
                warns.append(f"slides {i-1}-{i}: no shared anchor names")
        prev = names
    return pairs, warns


def main():
    subprocess.run(["taskkill", "/F", "/IM", "POWERPNT.EXE"],
                   capture_output=True)
    time.sleep(2)
    from win32com.client.gencache import EnsureDispatch
    app = EnsureDispatch("PowerPoint.Application")
    app.DisplayAlerts = 0  # ppAlertsNone
    pres = app.Presentations.Open(str(PPTX), WithWindow=False)

    # ----- TRANSITIONS -----
    for i, slide in enumerate(pres.Slides, start=1):
        slide.SlideShowTransition.EntryEffect = (
            FADE if i in FADE_SLIDES else MORPH_OBJECT)
        slide.SlideShowTransition.AdvanceOnTime = False
        slide.SlideShowTransition.AdvanceOnClick = True

    # ----- ENTRANCES (per visual-plan Entrances: lines) -----
    # Example pattern for slide 3 (photo-collage disc rotation anchor):
    # slide3 = pres.Slides(3)
    # disc = slide3.Shapes("disc")
    # add_fade_entrance(slide3, disc, 300)  # disc itself enters late
    #
    # Example staggered entrances on slide 2:
    # slide2 = pres.Slides(2)
    # kicker = slide2.Shapes("kicker")
    # hero = slide2.Shapes("hero")
    # sub = slide2.Shapes("sub")
    # stagger_entrances(slide2, [("kicker", kicker), ("hero", hero), ("sub", sub)])

    # Add per-slide blocks here following the visual-plan Entrances: lines.

    OUT.mkdir(exist_ok=True)
    for i, slide in enumerate(pres.Slides, start=1):
        slide.Export(str(OUT / ("s%d.png" % i)), "PNG", 1920, 1080)

    # ----- continuity sanity check (reads plan, not enforced) -----
    # anchors = {"hero", "sub", "disc", "scrim-left", "tile-1", "tile-2", "tile-3", "tile-4"}
    # pairs, warns = check_anchor_continuity(pres, anchors)
    # for w in warns:
    #     print("warn:", w)
    # print(f"continuity pairs: {pairs}/{len(pres.Slides)-1}")

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

RESEARCH_STUB = '''# Research notes (ship-blocking)

One section per planned slide: 4-8 content bullets + a 2-source log per slide.
Fewer than ~60 words of distinct facts per slide = redo. Verify APIs/specs live;
mark anything unverified as `[unverified]`.

## Slide 1 - <title>
- <fact>
- <fact>
- Sources: <source 1>; <source 2>
'''

VISUAL_PLAN_STUB = '''# Visual plan (ship-blocking)

One block per slide, in z-order, using the generate-pptx section-9 grammar.
Copy the matching layout-template recipe's spec block and fill in real values.

Slide 1 - <title>                      bg: surface
  Template: <framing|photo-hero|photo-collage|pastel-collage|display-type|annotation-stage|showcase|motion>
  Text runs:   hero "<line>" {--t-hero} ; body <n> lines {--t-body}
  Z-order:     bg -> <decor> -> <photo> -> copy
  Images:      assets/<NN>_<name>.jpg (<role>)
  Entrances:   <none | fade x N>
  Anchors:     <name> (static) ; <name> parked 14.5in -> <x>in
  Done when:   <objective check>
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
    (root / "research-notes.md").write_text(RESEARCH_STUB, encoding="utf-8")
    (root / "visual-plan.md").write_text(VISUAL_PLAN_STUB, encoding="utf-8")
    print("scaffolded", root)


if __name__ == "__main__":
    main()
