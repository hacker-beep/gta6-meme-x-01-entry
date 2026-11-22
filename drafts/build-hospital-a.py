#!/usr/bin/env python3
"""Build drafts/meme-v6-hospital-a.png — HOSPITAL BILL, entry 5 draft.

New document family (never tried), same winning formula as entry 4:
document where itemisation is native; wait quantified AND priced;
paid as a visual stamp; ghost integral to the document. Punchline is
the NUMBERS: 115,464 hours waited (17 Sep 2013 -> 19 Nov 2026) and
$79.99 total due. PIL composition only — no AI text, no AI image.
Ghost asset reused from entry 4 (drafts/ghost-logo-150.png).

Layout mirrors the entry-4 time card (proven at 480px): paper on a
dark desk, ghost badge top-left, two-column admit/discharge box,
3-row itemised charges table, big TOTAL DUE, red diagonal PAID stamp
sized from its rotated bbox (820x175 @ -6 deg -> ~866x260, pasted
with box top at y=728, ends y=988, inside the paper).
"""
import hashlib
from PIL import Image, ImageDraw, ImageFont

D = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/drafts"
OUT = D + "/meme-v6-hospital-a.png"
OUT480 = D + "/check480/meme-v6-hospital-a-480.png"
GHOST = D + "/ghost-logo-150.png"

W, H = 1024, 1024
PAPER = (250, 246, 236)      # warm white card stock
DESK = (38, 46, 54)          # dark slate margin
INK = (22, 28, 38)           # near-black navy
FAINT = (90, 96, 104)        # label grey
RED = (192, 28, 40)          # stamp red / cross red
BLUE = (27, 58, 140)         # date ink
RULE = (180, 180, 170)       # light table rule

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def centered(d, cx, y, text, f, fill=INK, tracking=0):
    if tracking == 0:
        w = d.textlength(text, font=f)
        d.text((cx - w / 2, y), text, font=f, fill=fill)
        return w
    widths = [d.textlength(ch, font=f) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        d.text((x, y), ch, font=f, fill=fill)
        x += w + tracking
    return total


# ---------- canvas ----------
img = Image.new("RGB", (W, H), DESK)
d = ImageDraw.Draw(img)
M = 28
d.rectangle([M + 6, M + 8, W - M + 6, H - M + 8], fill=(10, 14, 18))
d.rectangle([M, M, W - M, H - M], fill=PAPER)
d.rectangle([M + 12, M + 12, W - M - 12, H - M - 12], outline=INK, width=2)
d.rectangle([M + 20, M + 20, W - M - 20, H - M - 20], outline=INK, width=1)

CX = W // 2

# ---------- header: ghost badge (hospital logo) + letterhead ----------
ghost = Image.open(GHOST).convert("RGBA")
gs = 130
ghost = ghost.resize((gs, gs), Image.LANCZOS)
mask = Image.new("L", (gs, gs), 0)
ImageDraw.Draw(mask).ellipse([0, 0, gs, gs], fill=255)
img.paste(ghost, (62, 46), mask)
d = ImageDraw.Draw(img)
d.ellipse([62, 46, 62 + gs, 46 + gs], outline=(214, 51, 132), width=5)

f_co = font(SERIF_B, 36)  # 40pt ran into the red cross; 36 clears it
d.text((210, 62), "LEONIDA GENERAL HOSPITAL", font=f_co, fill=INK)
f_sub = font(SERIF, 30)
centered(d, 596, 122, "— PATIENT BILL —", f_sub, fill=FAINT)

# red cross emblem, top-right (hospital marker)
d.rectangle([918, 46, 940, 110], fill=RED)
d.rectangle([898, 66, 960, 88], fill=RED)

# ---------- divider ----------
dy = 172
d.line([(M + 44, dy), (W - M - 44, dy)], fill=INK, width=3)
d.line([(M + 44, dy + 7), (W - M - 44, dy + 7)], fill=INK, width=1)

# ---------- patient ----------
f_lab = font(SANS_B, 28)
f_val = font(SERIF_B, 44)
y = 192
d.text((72, y), "PATIENT:", font=f_lab, fill=FAINT)
d.text((290, y - 6), "GTA VI FAN", font=f_val, fill=INK)

# ---------- admit / discharge box ----------
box_y0, box_y1 = 258, 380
d.rectangle([56, box_y0, W - 56, box_y1], outline=INK, width=3)
d.line([(CX, box_y0), (CX, box_y1)], fill=INK, width=2)
f_plab = font(SANS_B, 28)
f_pdate = font(MONO_B, 54)
centered(d, CX - 228, box_y0 + 14, "ADMITTED", f_plab, fill=FAINT)
centered(d, CX - 228, box_y0 + 54, "17 SEP 2013", f_pdate, fill=BLUE)
centered(d, CX + 228, box_y0 + 14, "DISCHARGED", f_plab, fill=FAINT)
centered(d, CX + 228, box_y0 + 54, "19 NOV 2026", f_pdate, fill=BLUE)

# ---------- itemised charges: 3 rows, desc left / price right ----------
f_chg = font(SANS_B, 28)
d.text((72, 398), "CHARGES", font=f_chg, fill=FAINT)
f_row = font(MONO_B, 36)
rows = [
    (430, "WAITING \u2014 115,464 HRS", "$0.00"),
    (494, "DIAGNOSIS: TERMINAL HYPE", "$0.00"),
    (558, "TREATMENT: 1\u00d7 GTA VI", "$79.99"),
]
for ry, desc, price in rows:
    d.text((72, ry), desc, font=f_row, fill=INK)
    d.text((952 - d.textlength(price, font=f_row), ry), price,
           font=f_row, fill=INK)
d.line([(72, 480), (952, 480)], fill=RULE, width=2)
d.line([(72, 544), (952, 544)], fill=RULE, width=2)
d.line([(72, 608), (952, 608)], fill=INK, width=3)

# ---------- TOTAL DUE: $79.99 hero ----------
f_tlab = font(SANS_B, 34)
f_tnum = font(MONO_B, 76)
lab = "TOTAL DUE"
num = "$79.99"
gap = 28
tw = (d.textlength(lab, font=f_tlab) + gap +
      d.textlength(num, font=f_tnum))
x0 = CX - tw / 2
d.text((x0, 648), lab, font=f_tlab, fill=FAINT)
d.text((x0 + d.textlength(lab, font=f_tlab) + gap, 626), num,
       font=f_tnum, fill=INK)

# ---------- PAID stamp: same geometry as entry 4 ----------
SW, SH, ANG = 820, 175, -6
st = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
sd = ImageDraw.Draw(st)
sd.rectangle([5, 5, SW - 5, SH - 5], outline=RED + (235,), width=7)
sd.rectangle([17, 17, SW - 17, SH - 17], outline=RED + (235,), width=3)
f_s1 = font(SANS_B, 76)
f_s2 = font(SANS_B, 32)
centered(sd, SW // 2, 22, "PAID IN FULL", f_s1, fill=RED + (240,))
centered(sd, SW // 2, 112, "BY MY AI AGENT ON MAKE.FUN", f_s2,
         fill=RED + (240,))
for sx in (52, SW - 52):
    sd.text((sx - 13, 110), "\u2605", font=font(SANS_B, 32), fill=RED + (240,))
st = st.rotate(ANG, expand=True, resample=Image.BICUBIC)
print("stamp bbox:", st.size, "expected ~ (866, 260)")
img.paste(st, ((W - st.width) // 2, 728), st)

img.save(OUT, "PNG")
img.resize((480, 480), Image.LANCZOS).save(OUT480, "PNG")

h = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
print("saved:", OUT)
print("sha256:", h)
print("480 check:", OUT480)
