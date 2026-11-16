import re, os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether, HRFlowable)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from config import CO

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("HR", FD + "DejaVuSansCondensed.ttf"))
pdfmetrics.registerFont(TTFont("HR-B", FD + "DejaVuSansCondensed-Bold.ttf"))
pdfmetrics.registerFont(TTFont("HR-I", FD + "DejaVuSansCondensed-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("HR-BI", FD + "DejaVuSansCondensed-BoldOblique.ttf"))
pdfmetrics.registerFontFamily("HR", normal="HR", bold="HR-B", italic="HR-I", boldItalic="HR-BI")

NAVY = colors.HexColor("#1B365D")
TEAL = colors.HexColor("#1F7A8C")
LIGHT = colors.HexColor("#EEF3F8")
GREY = colors.HexColor("#6B7280")
LINE = colors.HexColor("#C9D3DF")
W, H = A4
MARG = 2.0 * cm
CW = W - 2 * MARG  # content width

def S(name, **kw):
    base = dict(fontName="HR", fontSize=9.6, leading=14, textColor=colors.HexColor("#1F2937"), alignment=TA_JUSTIFY)
    base.update(kw)
    return ParagraphStyle(name, **base)

ST = dict(
    title=S("title", fontName="HR-B", fontSize=24, leading=29, textColor=NAVY, alignment=TA_LEFT, spaceAfter=4),
    subtitle=S("subtitle", fontSize=11, leading=15, textColor=TEAL, alignment=TA_LEFT, spaceAfter=14),
    h1=S("h1", fontName="HR-B", fontSize=13, leading=17, textColor=NAVY, alignment=TA_LEFT, spaceBefore=14, spaceAfter=6),
    h2=S("h2", fontName="HR-B", fontSize=10.5, leading=14, textColor=TEAL, alignment=TA_LEFT, spaceBefore=8, spaceAfter=3),
    body=S("body", spaceAfter=5),
    clause=S("clause", leftIndent=34, spaceAfter=4.5),
    bullet=S("bullet", leftIndent=52, spaceAfter=2.5),
    sub=S("sub", leftIndent=52, spaceAfter=2.5),
    cell=S("cell", fontSize=8.6, leading=11.5, alignment=TA_LEFT),
    cellb=S("cellb", fontName="HR-B", fontSize=8.6, leading=11.5, alignment=TA_LEFT),
    cellh=S("cellh", fontName="HR-B", fontSize=8.6, leading=11.5, alignment=TA_LEFT, textColor=colors.white),
    note=S("note", fontSize=9, leading=13, alignment=TA_LEFT),
    small=S("small", fontSize=8, leading=11, textColor=GREY, alignment=TA_LEFT),
    toc=S("toc", fontSize=9.6, leading=14, alignment=TA_LEFT, leftIndent=8),
    right=S("right", alignment=TA_RIGHT),
    center=S("center", alignment=TA_CENTER),
    left=S("left", alignment=TA_LEFT, spaceAfter=3),
    letter=S("letter", fontSize=10, leading=15, spaceAfter=7),
)

def esc(t):
    return re.sub(r"&(?!(amp|lt|gt|nbsp|#\d+);)", "&amp;", str(t))

def P(t, style="body"):
    return Paragraph(esc(t), ST[style])

def table(header, rows, widths=None, zebra=True, bold_first_col=False, fs=None):
    data = []
    if header:
        data.append([Paragraph(esc(h), ST["cellh"]) for h in header])
    for r in rows:
        data.append([Paragraph(esc(c), ST["cellb"] if (bold_first_col and i == 0) else ST["cell"]) for i, c in enumerate(r)])
    ncol = len(header or rows[0])
    if widths:
        tot = float(sum(widths)); cw = [CW * w / tot for w in widths]
    else:
        cw = [CW / ncol] * ncol
    t = Table(data, colWidths=cw, repeatRows=1 if header else 0)
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("GRID", (0, 0), (-1, -1), 0.4, LINE),
             ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
             ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5)]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
    if zebra:
        for i in range(1 if header else 0, len(data)):
            if (i % 2) == 0:
                style.append(("BACKGROUND", (0, i), (-1, i), LIGHT))
    t.setStyle(TableStyle(style))
    return t

def note_box(text, label="Note"):
    p = Paragraph(f"<b>{label}:</b> {esc(text)}", ST["note"])
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFF8E6")),
                           ("LINEBEFORE", (0, 0), (0, -1), 3, colors.HexColor("#E0A100")),
                           ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 8)]))
    return [Spacer(1, 3), t, Spacer(1, 6)]

def make_canvas(title, docid, version, letterhead=False, footer_note=None):
    class NC(canvas.Canvas):
        def __init__(self, *a, **k):
            super().__init__(*a, **k); self._saved = []
        def showPage(self):
            self._saved.append(dict(self.__dict__)); self._startPage()
        def save(self):
            n = len(self._saved)
            for st in self._saved:
                self.__dict__.update(st); self._decor(n); super().showPage()
            super().save()
        def _decor(self, n):
            pg = self._pageNumber
            self.saveState()
            if letterhead:
                self.setFillColor(NAVY); self.setFont("HR-B", 16); self.drawString(MARG, H - 1.6 * cm, CO["name"])
                self.setFillColor(GREY); self.setFont("HR", 7.5)
                self.drawString(MARG, H - 2.05 * cm, CO["hq"])
                self.drawString(MARG, H - 2.4 * cm, f"CIN: {CO['cin']}  |  {CO['hr_mail']}")
                self.setStrokeColor(TEAL); self.setLineWidth(1.5); self.line(MARG, H - 2.65 * cm, W - MARG, H - 2.65 * cm)
            else:
                self.setFillColor(NAVY); self.setFont("HR-B", 9); self.drawString(MARG, H - 1.25 * cm, CO["name"])
                self.setFillColor(GREY); self.setFont("HR", 8); self.drawRightString(W - MARG, H - 1.25 * cm, title)
                self.setStrokeColor(LINE); self.setLineWidth(0.6); self.line(MARG, H - 1.5 * cm, W - MARG, H - 1.5 * cm)
            self.setStrokeColor(LINE); self.setLineWidth(0.6); self.line(MARG, 1.55 * cm, W - MARG, 1.55 * cm)
            self.setFillColor(GREY); self.setFont("HR", 7.5)
            left = footer_note or "CONFIDENTIAL - For internal use of Aurelia Systems employees only"
            self.drawString(MARG, 1.15 * cm, left)
            if docid:
                label = docid + (f"  |  v{version}" if version else "")
                self.drawCentredString(W / 2 + 60, 1.15 * cm, label)
            self.drawRightString(W - MARG, 1.15 * cm, f"Page {pg} of {n}")
            self.restoreState()
    return NC

def build(path, story, title, docid="", version="", letterhead=False, footer_note=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    top = 3.1 * cm if letterhead else 2.0 * cm
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=MARG, rightMargin=MARG, topMargin=top, bottomMargin=2.0 * cm,
                          title=title, author=CO["name"], subject=docid)
    frame = Frame(MARG, 2.0 * cm, CW, H - top - 2.0 * cm, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame])])
    doc.build(story, canvasmaker=make_canvas(title, docid, version, letterhead, footer_note))

# ------------------------------------------------------------------ policy documents
def build_policy(path, meta, sections):
    """meta: doc_id,title,version,effective,owner,approver,review,applies,classification,status,revisions[(ver,date,desc,by)], purpose_tag"""
    s = []
    s.append(Spacer(1, 6))
    s.append(P(meta["title"], "title"))
    s.append(P(f"{CO['name']}  |  Human Resources Policy Manual", "subtitle"))
    ctrl = [
        ["Document ID", meta["doc_id"], "Version", meta["version"]],
        ["Effective date", meta["effective"], "Status", meta.get("status", "Current")],
        ["Policy owner", meta["owner"], "Approved by", meta["approver"]],
        ["Applies to", meta["applies"], "Next review", meta["review"]],
        ["Classification", meta.get("classification", "Internal"), "Queries", meta.get("queries", CO["hr_mail"])],
    ]
    rows = [[Paragraph(f"<b>{esc(a)}</b>", ST["cell"]), Paragraph(esc(b), ST["cell"]),
             Paragraph(f"<b>{esc(c)}</b>", ST["cell"]), Paragraph(esc(d), ST["cell"])] for a, b, c, d in ctrl]
    t = Table(rows, colWidths=[CW * .17, CW * .33, CW * .17, CW * .33])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINE), ("BACKGROUND", (0, 0), (0, -1), LIGHT),
                           ("BACKGROUND", (2, 0), (2, -1), LIGHT), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    s += [t, Spacer(1, 10), P("Revision history", "h2")]
    s.append(table(["Version", "Date", "Summary of change", "Prepared by"],
                   [list(r) for r in meta["revisions"]], widths=[9, 17, 54, 20]))
    s += [Spacer(1, 10), P("Contents", "h2")]
    for i, sec in enumerate(sections, 1):
        s.append(P(f"{i}.&nbsp;&nbsp;{sec['title']}", "toc"))
    s.append(PageBreak())
    for i, sec in enumerate(sections, 1):
        s.append(P(f"{i}. {sec['title']}", "h1"))
        s.append(HRFlowable(width="100%", thickness=0.6, color=LINE, spaceAfter=5))
        k = 0
        for it in sec["items"]:
            kind = it[0]
            if kind == "p":
                s.append(P(it[1], "body"))
            elif kind == "c":
                k += 1
                s.append(Paragraph(esc(it[1]), ParagraphStyle("c", parent=ST["clause"], bulletFontName="HR-B", bulletFontSize=9.6,
                                                              bulletIndent=0), bulletText=f"{i}.{k}"))
            elif kind == "h":
                s.append(P(it[1], "h2"))
            elif kind == "b":
                for b in it[1]:
                    s.append(Paragraph(esc(b), ST["bullet"], bulletText="\u2022"))
            elif kind == "sc":
                for j, b in enumerate(it[1]):
                    s.append(Paragraph(esc(b), ST["sub"], bulletText=f"({chr(97 + j)})"))
            elif kind == "t":
                s.append(Spacer(1, 2)); s.append(table(it[1], it[2], it[3] if len(it) > 3 else None)); s.append(Spacer(1, 7))
            elif kind == "note":
                s += note_box(it[1], it[2] if len(it) > 2 else "Note")
    s.append(KeepTogether([Spacer(1, 14), P("Document approval", "h2"),
        table(["Role", "Name", "Designation", "Date"],
              [["Prepared by", meta["owner"], "Policy owner", meta["revisions"][-1][1]],
               ["Approved by", meta["approver"], "Approving authority", meta["revisions"][-1][1]]], widths=[18, 30, 32, 20])]))
    s.append(Spacer(1, 6))
    s.append(P(f"This document is controlled. Printed or downloaded copies are valid only if they match the latest version published on {CO['hrms']}. "
               f"In case of conflict between this policy and applicable law, the law prevails.", "small"))
    build(path, s, meta["title"], meta["doc_id"], meta["version"])
