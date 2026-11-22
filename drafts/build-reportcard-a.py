#!/usr/bin/env python3
"""Build drafts/meme-v7-reportcard-a.png — REPORT CARD, entry 5 draft.

New document family (ZERO report-card entries in the live top 200),
same winning formula as entry 4 (time card, DEV 81.5918%): document
where itemisation is native; wait quantified AND priced; paid as a
visual stamp; ghost integral to the document. Punchline is the
NUMBERS: 115,464 hours waited, $79.99 tuition, and the A+/F grades.
PIL composition only — no AI text, no AI image. Ghost asset reused
from entry 4 (drafts/ghost-logo-150.png).

Layout follows the proven entry-4 / hospital pattern (paper on a dark
desk, ghost badge top-left, 3-row itemised table, hero number, red
diagonal PAID stamp), re-budgeted vertically: school year folded into
the subheader so attendance + teacher's comment + tuition + stamp all
fit inside the paper (stamp 740x150 @ -5 deg -> ~750x214, pasted with
box top at y=752, ends y~966, inside the paper).
"""
import hashlib
from PIL import Image, ImageDraw, ImageFont

D = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/drafts"
OUT = D + "/meme-v7-reportcard-a.png"
OUT480 = D + "/check480/meme-v7-reportcard-a-480.png"
GHOST = D + "/ghost-logo-150.png"

W, H = 1024, 1024
PAPER = (250, 246, 236)      # warm white card stock
DESK = (38, 46, 54)          # dark slate margin
INK = (22, 28, 38)           # near-black navy
FAINT = (90, 96, 104)        # label grey
RED = (192, 28, 40)          # stamp red / F grade
GREEN = (27, 120, 60)        # A+ grade green
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

# ---------- header: ghost badge (school crest) + letterhead ----------
ghost = Image.open(GHOST).convert("RGBA")
gs = 110
ghost = ghost.resize((gs, gs), Image.LANCZOS)
mask = Image.new("L", (gs, gs), 0)
ImageDraw.Draw(mask).ellipse([0, 0, gs, gs], fill=255)
img.paste(ghost, (62, 44), mask)
d = ImageDraw.Draw(img)
d.ellipse([62, 44, 62 + gs, 44 + gs], outline=(214, 51, 132), width=5)

f_co = font(SERIF_B, 38)
d.text((192, 56), "LEONIDA HIGH SCHOOL", font=f_co, fill=INK)
f_sub = font(SERIF, 26)
centered(d, 560, 108, "\u2014 REPORT CARD \u00b7 2013\u20132026 \u2014",
         f_sub, fill=FAINT)

# teacher's red circled A+ top-right (report-card marker)
cxp, cyp, rp = 928, 98, 40
d.ellipse([cxp - rp, cyp - rp, cxp + rp, cyp + rp], outline=RED, width=5)
f_ap = font(SANS_B, 44)
tw = d.textlength("A+", font=f_ap)
d.text((cxp - tw / 2, cyp - 30), "A+", font=f_ap, fill=RED)

# ---------- divider ----------
dy = 158
d.line([(M + 44, dy), (W - M - 44, dy)], fill=INK, width=3)
d.line([(M + 44, dy + 7), (W - M - 44, dy + 7)], fill=INK, width=1)

# ---------- student ----------
f_lab = font(SANS_B, 26)
f_val = font(SERIF_B, 40)
d.text((72, 182), "STUDENT:", font=f_lab, fill=FAINT)
d.text((280, 176), "ROCKSTAR GAMES", font=f_val, fill=INK)

# ---------- grades table: 3 rows, subject left / grade right ----------
f_glab = font(SANS_B, 26)
d.text((72, 248), "GRADES", font=f_glab, fill=FAINT)
gw = d.textlength("GRADE", font=f_glab)
d.text((952 - gw, 248), "GRADE", font=f_glab, fill=FAINT)
f_row = font(MONO_B, 34)
f_grd = font(MONO_B, 44)
rows = [
    (278, "PATIENCE", "A+", GREEN),
    (338, "HYPE", "A+", GREEN),
    (398, "RELEASE DATE (2 DELAYS)", "F", RED),
]
for ry, subj, grade, gcol in rows:
    d.text((72, ry), subj, font=f_row, fill=INK)
    d.text((952 - d.textlength(grade, font=f_grd), ry - 6), grade,
           font=f_grd, fill=gcol)
d.line([(72, 324), (952, 324)], fill=RULE, width=2)
d.line([(72, 384), (952, 384)], fill=RULE, width=2)
d.line([(72, 444), (952, 444)], fill=INK, width=3)

# ---------- attendance: hero number ----------
f_alab = font(SANS_B, 24)
centered(d, CX, 464, "ATTENDANCE", f_alab, fill=FAINT)
f_num = font(MONO_B, 58)
centered(d, CX, 490, "115,464 HOURS", f_num, fill=INK)
f_asub = font(SANS_B, 26)
centered(d, CX, 556, "ALL SPENT WAITING", f_asub, fill=INK)

# ---------- teacher's comment ----------
f_clab = font(SANS_B, 22)
centered(d, CX, 598, "TEACHER'S COMMENT:", f_clab, fill=FAINT)
f_com = font(SERIF, 30)
centered(d, CX, 622, "\u201cEXCELLENT STUDENT. 13 YEARS LATE.\u201d",
         f_com, fill=INK)

# ---------- tuition due: $79.99 hero ----------
f_tlab = font(SANS_B, 30)
f_tnum = font(MONO_B, 64)
lab = "TUITION DUE"
num = "$79.99"
gap = 28
tw = (d.textlength(lab, font=f_tlab) + gap +
      d.textlength(num, font=f_tnum))
x0 = CX - tw / 2
d.text((x0, 686), lab, font=f_tlab, fill=FAINT)
d.text((x0 + d.textlength(lab, font=f_tlab) + gap, 668), num,
       font=f_tnum, fill=INK)

# ---------- PAID stamp (smaller than hospital's to fit the budget) ----------
SW, SH, ANG = 740, 150, -5
st = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
sd = ImageDraw.Draw(st)
sd.rectangle([5, 5, SW - 5, SH - 5], outline=RED + (235,), width=7)
sd.rectangle([17, 17, SW - 17, SH - 17], outline=RED + (235,), width=3)
f_s1 = font(SANS_B, 62)
f_s2 = font(SANS_B, 26)
centered(sd, SW // 2, 18, "PAID IN FULL", f_s1, fill=RED + (240,))
centered(sd, SW // 2, 96, "BY MY AI AGENT ON MAKE.FUN", f_s2,
         fill=RED + (240,))
for sx in (48, SW - 48):
    sd.text((sx - 11, 94), "\u2605", font=font(SANS_B, 26), fill=RED + (240,))
st = st.rotate(ANG, expand=True, resample=Image.BICUBIC)
print("stamp bbox:", st.size, "expected ~ (750, 214)")
img.paste(st, ((W - st.width) // 2, 752), st)

img.save(OUT, "PNG")
img.resize((480, 480), Image.LANCZOS).save(OUT480, "PNG")

h = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
print("saved:", OUT)
print("sha256:", h)
print("480 check:", OUT480)
