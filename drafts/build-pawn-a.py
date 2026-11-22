#!/usr/bin/env python3
"""Build drafts/meme-v8-pawn-a.png — PAWN TICKET, entry 5 alternate draft.

New document family (ZERO pawn entries in the live top 200), same
winning formula as entry 4 (time card, DEV 81.5918%): document
where itemisation is native; wait quantified AND priced; paid as a
visual stamp; ghost integral to the document.

CRITICAL LESSON from entry 4's judge dossier: the time card was
called a "clever infographic more than a punchline" (dry). The
entries that beat/drew it had sharper instant laughs. This draft's
punchlines are the pawn terms themselves: a $0.00 loan whose
INTEREST is 13 YEARS, and the clerk's note that the patience came
back still waiting.

PIL composition only — no AI text, no AI image. Ghost asset reused
from entry 4 (drafts/ghost-logo-150.png).

Layout follows the proven entry-4 / hospital / report-card pattern
(paper on a dark desk, ghost badge top-left, itemised rows, hero
number, red diagonal PAID stamp). Vertical budget: header 44-150,
divider 158, ITEM 176-240, dates box 252-330, terms table 350-478,
clerk's note ~505, redemption hero ~580-660, stamp 740x150 @ -5 deg
-> ~750x214, pasted with box top at y=730, ends y~944, inside the
paper (inner border at 976).
"""
import hashlib
from PIL import Image, ImageDraw, ImageFont

D = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/drafts"
OUT = D + "/meme-v8-pawn-a.png"
OUT480 = D + "/check480/meme-v8-pawn-a-480.png"
GHOST = D + "/ghost-logo-150.png"

W, H = 1024, 1024
PAPER = (250, 246, 236)      # warm white card stock
DESK = (38, 46, 54)          # dark slate margin
INK = (22, 28, 38)           # near-black navy
FAINT = (90, 96, 104)        # label grey
RED = (192, 28, 40)          # stamp red / interest punch
BLUE = (24, 60, 150)         # dates blue (hospital pattern)
RULE = (180, 180, 170)       # light table rule

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_I = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf"
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

# ---------- header: ghost badge (shop logo) + letterhead ----------
ghost = Image.open(GHOST).convert("RGBA")
gs = 110
ghost = ghost.resize((gs, gs), Image.LANCZOS)
mask = Image.new("L", (gs, gs), 0)
ImageDraw.Draw(mask).ellipse([0, 0, gs, gs], fill=255)
img.paste(ghost, (62, 44), mask)
d = ImageDraw.Draw(img)
d.ellipse([62, 44, 62 + gs, 44 + gs], outline=(214, 51, 132), width=5)

f_co = font(SERIF_B, 38)
d.text((192, 56), "LEONIDA PAWN SHOP", font=f_co, fill=INK)
f_sub = font(SERIF, 26)
centered(d, 560, 108, "\u2014 PAWN TICKET \u2014", f_sub, fill=FAINT)

# ticket number top-right: the wait itself is the ticket number
f_tno = font(MONO_B, 22)
tno = "TICKET No. 115464"
d.text((952 - d.textlength(tno, font=f_tno), 66), tno,
       font=f_tno, fill=FAINT)

# ---------- divider ----------
dy = 158
d.line([(M + 44, dy), (W - M - 44, dy)], fill=INK, width=3)
d.line([(M + 44, dy + 7), (W - M - 44, dy + 7)], fill=INK, width=1)

# ---------- item ----------
f_lab = font(SANS_B, 26)
f_val = font(SERIF_B, 40)
d.text((72, 182), "ITEM:", font=f_lab, fill=FAINT)
d.text((200, 176), "1\u00d7 PATIENCE", font=f_val, fill=INK)
f_cond = font(SERIF, 26)
d.text((200, 226), "(MINT CONDITION)", font=f_cond, fill=FAINT)

# ---------- dates box: PAWNED / REDEEMED ----------
bx0, bx1, by0, by1 = 72, 952, 268, 352
d.rectangle([bx0, by0, bx1, by1], outline=INK, width=3)
d.line([(CX, by0), (CX, by1)], fill=INK, width=2)
f_dlab = font(SANS_B, 24)
f_date = font(MONO_B, 40)
centered(d, (bx0 + CX) // 2, by0 + 10, "PAWNED", f_dlab, fill=FAINT)
centered(d, (bx0 + CX) // 2, by0 + 40, "17 SEP 2013", f_date, fill=BLUE)
centered(d, (CX + bx1) // 2, by0 + 10, "REDEEMED", f_dlab, fill=FAINT)
centered(d, (CX + bx1) // 2, by0 + 40, "19 NOV 2026", f_date, fill=BLUE)

# ---------- terms table: LOAN $0.00 / INTEREST 13 YEARS (punchline) ----------
f_row = font(MONO_B, 34)
f_amt = font(MONO_B, 34)
f_punch = font(MONO_B, 44)
d.text((72, 380), "LOAN", font=f_row, fill=INK)
d.text((952 - d.textlength("$0.00", font=f_amt), 380), "$0.00",
       font=f_amt, fill=INK)
d.line([(72, 426), (952, 426)], fill=RULE, width=2)
d.text((72, 444), "INTEREST", font=f_row, fill=INK)
d.text((952 - d.textlength("13 YEARS", font=f_punch), 436), "13 YEARS",
       font=f_punch, fill=RED)
d.line([(72, 496), (952, 496)], fill=INK, width=3)

# ---------- clerk's note: second punchline ----------
f_note = font(SERIF_I, 28)
centered(d, CX, 520,
         "\u201cCONDITION ON RETURN: STILL WAITING.\u201d",
         f_note, fill=INK)

# ---------- redemption due: $79.99 hero ----------
f_rlab = font(SANS_B, 30)
f_rnum = font(MONO_B, 64)
lab = "REDEMPTION DUE"
num = "$79.99"
gap = 28
tw = (d.textlength(lab, font=f_rlab) + gap +
      d.textlength(num, font=f_rnum))
x0 = CX - tw / 2
d.text((x0, 606), lab, font=f_rlab, fill=FAINT)
d.text((x0 + d.textlength(lab, font=f_rlab) + gap, 588), num,
       font=f_rnum, fill=INK)

# ---------- PAID stamp ----------
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
img.paste(st, ((W - st.width) // 2, 730), st)

img.save(OUT, "PNG")
img.resize((480, 480), Image.LANCZOS).save(OUT480, "PNG")

h = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
print("saved:", OUT)
print("sha256:", h)
print("480 check:", OUT480)
