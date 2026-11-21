#!/usr/bin/env python3
"""The Passport Page of a Country That Isn't There — Republika Danara.

Deterministic PIL render of an open passport spread (1024x1024 PNG).
Invented river-delta republic of canals and floating markets.
No network, no randomness: both graded runs are byte-identical.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = "/output/entry.png"

FONT_DIRS = ["/usr/share/fonts/truetype/liberation", "/usr/share/fonts/truetype/dejavu"]

def font(names, size):
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()

SERIF_B = lambda s: font(["LiberationSerif-Bold.ttf", "DejaVuSerif-Bold.ttf"], s)
SERIF   = lambda s: font(["LiberationSerif-Regular.ttf", "DejaVuSerif.ttf"], s)
SERIF_I = lambda s: font(["LiberationSerif-Italic.ttf", "DejaVuSerif.ttf"], s)
SANS_B  = lambda s: font(["LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf"], s)
SANS    = lambda s: font(["LiberationSans-Regular.ttf", "DejaVuSans.ttf"], s)
MONO    = lambda s: font(["LiberationMono-Regular.ttf", "DejaVuSansMono.ttf"], s)

INK      = (24, 62, 58)      # deep river teal
INK_SOFT = (84, 106, 102)
PAPER    = (247, 242, 228)
PAPER_R  = (245, 240, 224)
RUST     = (146, 52, 40)
GREEN    = (36, 106, 76)
BLUE     = (44, 82, 142)
GREY_TXT = (96, 104, 108)

img = Image.new("RGB", (W, H), (18, 18, 20))
d = ImageDraw.Draw(img)

LX0, LX1 = 30, 502
RX0, RX1 = 522, 994
PY0, PY1 = 28, 996
d.rectangle([LX0, PY0, LX1, PY1], fill=PAPER)
d.rectangle([RX0, PY0, RX1, PY1], fill=PAPER_R)
for i in range(10):
    shade = 232 - i * 6
    d.line([(502 + i, PY0), (502 + i, PY1)], fill=(shade, shade - 8, shade - 28))
    d.line([(522 - i, PY0), (522 - i, PY1)], fill=(shade, shade - 8, shade - 28))
d.rectangle([LX0, PY0, LX1, PY1], outline=(190, 184, 162), width=1)
d.rectangle([RX0, PY0, RX1, PY1], outline=(190, 184, 162), width=1)

def text(x, y, s, f, fill=INK, anchor="la", spacing=0):
    d.text((x, y), s, font=f, fill=fill, anchor=anchor, spacing=spacing)

# ---------- left page header ----------
cx = (LX0 + LX1) // 2
ex, ey, er = cx, 86, 30
d.ellipse([ex - er, ey - er, ex + er, ey + er], outline=INK, width=2)
d.ellipse([ex - er + 4, ey - er + 4, ex + er - 4, ey + er - 4], outline=INK, width=1)
# delta: one river fanning into three channels over a boat hull
d.line([(ex, ey - 18), (ex, ey - 4)], fill=INK, width=2)
d.line([(ex, ey - 4), (ex - 13, ey + 10)], fill=INK, width=2)
d.line([(ex, ey - 4), (ex, ey + 10)], fill=INK, width=2)
d.line([(ex, ey - 4), (ex + 13, ey + 10)], fill=INK, width=2)
d.polygon([(ex - 16, ey + 12), (ex + 16, ey + 12), (ex + 11, ey + 20), (ex - 11, ey + 20)], outline=INK, width=2)
for wy in (ey + 24,):
    pts = []
    for t in range(-14, 15, 2):
        pts.append((ex + t, wy + (2 if (t // 4) % 2 == 0 else -1)))
    d.line(pts, fill=INK, width=1)

text(cx, 128, "REPUBLIKA DANARA", SERIF_B(25), anchor="ma")
text(cx, 160, "REPUBLIC OF DANARA", SANS(11), fill=INK_SOFT, anchor="ma")
text(cx, 180, "P A S P O R", SANS_B(13), anchor="ma")
d.line([(LX0 + 26, 208), (LX1 - 26, 208)], fill=INK, width=2)

# ---------- portrait ----------
PX0, PYp0, PX1, PYp1 = LX0 + 28, 224, LX0 + 196, 430
d.rectangle([PX0, PYp0, PX1, PYp1], fill=(204, 214, 210), outline=INK, width=2)
ncx = (PX0 + PX1) // 2
# shoulders / blouse
d.polygon([(PX0 + 18, PYp1), (PX0 + 34, PYp1 - 52), (PX0 + 62, PYp1 - 62),
           (PX1 - 62, PYp1 - 62), (PX1 - 34, PYp1 - 52), (PX1 - 18, PYp1)], fill=(32, 92, 80))
d.polygon([(PX0 + 62, PYp1 - 62), (ncx, PYp1 - 38), (PX1 - 62, PYp1 - 62),
           (ncx, PYp1 - 54)], fill=(236, 232, 222))
# neck
d.rectangle([ncx - 12, PYp0 + 118, ncx + 12, PYp0 + 148], fill=(214, 166, 130))
# face
d.ellipse([ncx - 32, PYp0 + 34, ncx + 32, PYp0 + 128], fill=(224, 178, 142))
# hair: bun on top + cap + side strands (rounded ends so the hair reads as hair, not a block)
d.ellipse([ncx - 16, PYp0 + 6, ncx + 16, PYp0 + 34], fill=(34, 28, 24))
d.pieslice([ncx - 35, PYp0 + 22, ncx + 35, PYp0 + 96], start=175, end=365, fill=(34, 28, 24))
d.chord([ncx - 35, PYp0 + 22, ncx + 35, PYp0 + 96], start=175, end=365, fill=(34, 28, 24))
d.rectangle([ncx - 40, PYp0 + 52, ncx - 30, PYp0 + 112], fill=(34, 28, 24))
d.rectangle([ncx + 30, PYp0 + 52, ncx + 40, PYp0 + 112], fill=(34, 28, 24))
d.ellipse([ncx - 40, PYp0 + 102, ncx - 30, PYp0 + 122], fill=(34, 28, 24))
d.ellipse([ncx + 30, PYp0 + 102, ncx + 40, PYp0 + 122], fill=(34, 28, 24))
# ears + earrings
d.ellipse([ncx - 37, PYp0 + 78, ncx - 30, PYp0 + 94], fill=(220, 172, 136))
d.ellipse([ncx + 30, PYp0 + 78, ncx + 37, PYp0 + 94], fill=(220, 172, 136))
d.ellipse([ncx - 36, PYp0 + 96, ncx - 32, PYp0 + 100], fill=(196, 158, 74))
d.ellipse([ncx + 32, PYp0 + 96, ncx + 36, PYp0 + 100], fill=(196, 158, 74))
# brows, eyes, nose, mouth
d.line([(ncx - 20, PYp0 + 76), (ncx - 8, PYp0 + 74)], fill=(34, 28, 24), width=3)
d.line([(ncx + 8, PYp0 + 74), (ncx + 20, PYp0 + 76)], fill=(34, 28, 24), width=3)
d.ellipse([ncx - 17, PYp0 + 82, ncx - 10, PYp0 + 88], fill=(28, 26, 28))
d.ellipse([ncx + 10, PYp0 + 82, ncx + 17, PYp0 + 88], fill=(28, 26, 28))
d.line([(ncx, PYp0 + 88), (ncx - 3, PYp0 + 104), (ncx + 4, PYp0 + 106)], fill=(184, 132, 100), width=2)
d.line([(ncx - 9, PYp0 + 116), (ncx + 9, PYp0 + 116)], fill=(154, 92, 84), width=3)
text(PX0, PYp1 + 8, "FOTO / PHOTOGRAPH", SANS(8), fill=GREY_TXT)

# ---------- data fields ----------
FX = LX0 + 216
fields = [
    ("TIP / TYPE", "P"),
    ("KOD / CODE", "DAN"),
    ("PASPOR NO. / PASSPORT NO.", "DAN 274819"),
    ("NAMA / SURNAME", "DANARTI"),
    ("NAMA DEPAN / GIVEN NAMES", "LARAS AYU"),
    ("WARGA / NATIONALITY", "DANARAN"),
    ("LAHIR / DATE OF BIRTH", "09 SEP 1995"),
    ("TEMPAT LAHIR / PLACE OF BIRTH", "KUALA DANARA"),
    ("JENIS / SEX", "F"),
    ("DITERBITKAN / DATE OF ISSUE", "12 JAN 2024"),
    ("BERLAKU HINGGA / DATE OF EXPIRY", "12 JAN 2034"),
    ("KANTOR / AUTHORITY", "DELTA OFFICE, KUALA DANARA"),
]
fy = 224
for label, val in fields:
    text(FX, fy, label, SANS(8), fill=GREY_TXT)
    text(FX, fy + 12, val, SANS_B(14), fill=INK)
    fy += 40
    if label.startswith("KANTOR"):
        fy -= 6

# signature (nudged down after first render so it clears the authority field)
sy = 732
text(LX0 + 30, sy, "Laras Ayu Danarti", SERIF_I(24), fill=(28, 58, 66))
d.line([(LX0 + 30, sy + 34), (LX0 + 250, sy + 34)], fill=INK_SOFT, width=1)
text(LX0 + 30, sy + 40, "TANDA TANGAN / HOLDER'S SIGNATURE", SANS(8), fill=GREY_TXT)

# ---------- MRZ (ICAO 9303, weights 7-3-1) ----------
def cd(s):
    vals = {c: i for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    vals["<"] = 0
    w = [7, 3, 1]
    return str(sum(vals.get(c, 0) * w[i % 3] for i, c in enumerate(s)) % 10)

line1 = ("P<DANDANARTI<<LARAS<AYU" + "<" * 44)[:44]
pno = "DAN274819"
dob, exp = "950909", "340112"
personal = "<" * 14
line2 = pno + cd(pno) + "DAN" + dob + cd(dob) + "F" + exp + cd(exp) + personal + cd(personal)
line2 += cd(line2[:10] + line2[13:20] + line2[21:43])
assert len(line1) == 44 and len(line2) == 44, (line1, line2)

MX0, MY0, MX1, MY1 = LX0 + 26, 812, LX1 - 26, 916
d.rectangle([MX0, MY0, MX1, MY1], fill=(240, 234, 216), outline=INK_SOFT, width=1)
text(MX0 + 14, MY0 + 18, line1, MONO(15), fill=(30, 34, 40))
text(MX0 + 14, MY0 + 52, line2, MONO(15), fill=(30, 34, 40))
text(LX0 + 28, 952, "2", SERIF(13), fill=GREY_TXT)

# faint watermark emblem, left page (kept clear of the data fields)
wx, wy = LX0 + 112, 560
d.ellipse([wx - 52, wy - 52, wx + 52, wy + 52], outline=(238, 232, 214), width=2)
d.line([(wx, wy - 28), (wx, wy - 6)], fill=(238, 232, 214), width=2)
d.line([(wx, wy - 6), (wx - 20, wy + 16)], fill=(238, 232, 214), width=2)
d.line([(wx, wy - 6), (wx, wy + 16)], fill=(238, 232, 214), width=2)
d.line([(wx, wy - 6), (wx + 20, wy + 16)], fill=(238, 232, 214), width=2)
d.polygon([(wx - 24, wy + 18), (wx + 24, wy + 18), (wx + 17, wy + 30), (wx - 17, wy + 30)], outline=(238, 232, 214), width=2)

# ---------- right page ----------
text(RX0 + 26, 52, "VISA / VISAS", SERIF_B(24))
text(RX1 - 26, 58, "12", SERIF(13), fill=GREY_TXT, anchor="ra")
d.line([(RX0 + 26, 92), (RX1 - 26, 92)], fill=INK, width=2)
text(RX0 + 26, 102, "ENTRY AND EXIT STAMPS — TRAVEL HISTORY", SANS(9), fill=GREY_TXT)

stamps = [
    ("DANARA", "DEPARTURE", "KUALA DANARA", "05 MAR 2024", RUST, -3, "rect"),
    ("KARANGA", "ARRIVAL", "KUALA KARANG", "06 MAR 2024", BLUE, 2, "rect"),
    ("KARANGA", "DEPARTURE", "KUALA KARANG", "20 MAR 2024", BLUE, -2, "rect"),
    ("DANARA", "ARRIVAL", "KUALA DANARA", "21 MAR 2024", RUST, 2, "rect"),
    ("DANARA", "DEPARTURE", "KUALA DANARA", "14 AUG 2024", RUST, 3, "oval"),
    ("BINTARA", "ARRIVAL", "PELABUHAN BINTARA", "15 AUG 2024", GREEN, -2, "oval"),
    ("BINTARA", "DEPARTURE", "PELABUHAN BINTARA", "30 AUG 2024", GREEN, 2, "oval"),
    ("DANARA", "ARRIVAL", "KUALA DANARA", "31 AUG 2024", RUST, -2, "oval"),
]

def stamp(x, y, w, h, country, kind, port, date, color, angle, shape):
    s = Image.new("RGBA", (w + 8, h + 8), (0, 0, 0, 0))
    sd = ImageDraw.Draw(s)
    if shape == "oval":
        sd.ellipse([3, 3, w + 4, h + 4], outline=color + (255,), width=3)
        sd.ellipse([8, 8, w - 1, h - 1], outline=color + (255,), width=1)
    else:
        sd.rounded_rectangle([3, 3, w + 4, h + 4], radius=10, outline=color + (255,), width=3)
        sd.rounded_rectangle([8, 8, w - 1, h - 1], radius=7, outline=color + (255,), width=1)
    f1, f2, f3 = SANS_B(14), SANS(9), SANS_B(12)
    cxx = (w + 8) // 2
    sd.text((cxx, 16), country, font=f1, fill=color + (255,), anchor="ma")
    sd.text((cxx, 36), kind, font=f2, fill=color + (255,), anchor="ma")
    sd.text((cxx, 49), port, font=f2, fill=color + (255,), anchor="ma")
    sd.text((cxx, 64), date, font=f3, fill=color + (255,), anchor="ma")
    s = s.rotate(angle, expand=True, resample=Image.BICUBIC)
    img.paste(s, (x, y), s)

SW, SH = 196, 92
pos = [(RX0 + 30, 132), (RX0 + 244, 130), (RX0 + 30, 242), (RX0 + 244, 244),
       (RX0 + 30, 352), (RX0 + 244, 350), (RX0 + 30, 462), (RX0 + 244, 464)]
for (c, k, p, dt, col, ang, sh), (x, y) in zip(stamps, pos):
    stamp(x, y, SW, SH, c, k, p, dt, col, ang, sh)

# conditions box
BX0, BY0, BX1, BY1 = RX0 + 26, 592, RX1 - 26, 806
d.rectangle([BX0, BY0, BX1, BY0 + 32], fill=INK)
text(BX0 + 14, BY0 + 7, "CONDITIONS OF ISSUE", SANS_B(14), fill=(247, 242, 228))
d.rectangle([BX0, BY0, BX1, BY1], outline=INK, width=2)
lines = [
    "Valid for travel on registered river ferries and canal",
    "barges of the Danara Delta. The bearer must present",
    "this passport at the nearest canal lock-keeper's post",
    "within 48 hours of arrival for entry in the Delta",
    "Register. Not valid in the closed monsoon season",
    "(November–January) without a Delta Transit Permit.",
]
ly = BY0 + 46
for ln in lines:
    text(BX0 + 14, ly, ln, SERIF(13.5), fill=(52, 62, 60))
    ly += 21
text(BX0 + 14, ly + 6, "No. 274819  ·  Fee paid at issue", SANS(9), fill=GREY_TXT)

# fee stamp (circle, overlapping box corner)
fs = Image.new("RGBA", (150, 150), (0, 0, 0, 0))
fd = ImageDraw.Draw(fs)
fd.ellipse([4, 4, 146, 146], outline=RUST + (255,), width=3)
fd.ellipse([12, 12, 138, 138], outline=RUST + (255,), width=1)
fd.text((75, 42), "CANAL DUES", font=SANS_B(15), fill=RUST + (255,), anchor="ma")
fd.text((75, 64), "PAID", font=SANS_B(17), fill=RUST + (255,), anchor="ma")
fd.text((75, 90), "12 JAN", font=SANS_B(15), fill=RUST + (255,), anchor="ma")
fs = fs.rotate(-12, expand=True, resample=Image.BICUBIC)
img.paste(fs, (BX1 - 138, BY1 - 104), fs)

text(RX0 + 26, 838, "This passport remains the property of the Republic of Danara.", SERIF_I(12), fill=GREY_TXT)
text(RX0 + 26, 858, "If found, please return to any Danaran consulate or canal lock post.", SERIF_I(12), fill=GREY_TXT)

os.makedirs("/output", exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT}: {os.path.getsize(OUT)} bytes, {img.size}")
