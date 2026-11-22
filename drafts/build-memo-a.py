#!/usr/bin/env python3
"""Build drafts/meme-v10-memo-a.png — ROCKSTAR INTERNAL MEMO, entry 5 draft.

New document family (ZERO memo entries in the live top 200), same
winning formula as entry 4 (time card, DEV 81.5918%): wait quantified
AND priced; paid as a visual stamp; ghost integral to the document.

EVIDENCE for the memo angle: a memo (the HR grandma memo) beat/drew
our time card in dev judging — the judge called it "sharper, more
quotable". The time card's weakness was dryness ("clever infographic
more than a punchline"). This draft's punchline is one quotable line:
"JUST ONE MORE YEAR." + "(13th year in a row.)"

PIL composition only — no AI text, no AI image. Ghost asset reused
from entry 4 (drafts/ghost-logo-150.png).

Layout follows the proven entry-4 / hospital / report-card / pawn
pattern (paper on a dark desk, ghost badge top-left, red diagonal
PAID stamp). Vertical budget: header 44-150, divider 158, memo block
182-356 (4 rows), light divider 372, punchline 410-485, sub-punch
505-540, attachment 575-610, CC footer 640-670, stamp 740x150 @ -5 deg
-> ~750x214, pasted with box top at y=730, ends y~944, inside the
paper (inner border at 976).
"""
import hashlib
from PIL import Image, ImageDraw, ImageFont

D = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/drafts"
OUT = D + "/meme-v10-memo-a.png"
OUT480 = D + "/check480/meme-v10-memo-a-480.png"
GHOST = D + "/ghost-logo-150.png"

W, H = 1024, 1024
PAPER = (250, 246, 236)      # warm white card stock
DESK = (38, 46, 54)          # dark slate margin
INK = (22, 28, 38)           # near-black navy
FAINT = (90, 96, 104)        # label grey
RED = (192, 28, 40)          # stamp red
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

# ---------- header: ghost badge (letterhead logo) + company name ----------
ghost = Image.open(GHOST).convert("RGBA")
gs = 110
ghost = ghost.resize((gs, gs), Image.LANCZOS)
mask = Image.new("L", (gs, gs), 0)
ImageDraw.Draw(mask).ellipse([0, 0, gs, gs], fill=255)
img.paste(ghost, (62, 44), mask)
d = ImageDraw.Draw(img)
d.ellipse([62, 44, 62 + gs, 44 + gs], outline=(214, 51, 132), width=5)

f_co = font(SERIF_B, 38)
d.text((192, 56), "ROCKSTAR GAMES", font=f_co, fill=INK)
f_sub = font(SERIF, 26)
centered(d, 560, 108, "\u2014 INTERNAL MEMORANDUM \u2014", f_sub, fill=FAINT)

# ---------- divider ----------
dy = 158
d.line([(M + 44, dy), (W - M - 44, dy)], fill=INK, width=3)
d.line([(M + 44, dy + 7), (W - M - 44, dy + 7)], fill=INK, width=1)

# ---------- memo block: TO / FROM / DATE / RE ----------
f_lab = font(SANS_B, 24)
f_val = font(MONO_B, 27)
rows = [
    ("TO:", "GTA FANS"),
    ("FROM:", "ROCKSTAR MANAGEMENT"),
    ("DATE:", "19 NOV 2026"),
    ("RE:", "GTA VI RELEASE DATE"),
]
y = 182
for lab, val in rows:
    d.text((72, y), lab, font=f_lab, fill=FAINT)
    d.text((200, y - 2), val, font=f_val, fill=INK)
    y += 44

# ---------- light divider ----------
d.line([(72, 372), (952, 372)], fill=RULE, width=2)

# ---------- THE punchline, big and bold, center-frame ----------
f_punch = font(SANS_B, 66)
punch = "JUST ONE MORE YEAR."
pw = d.textlength(punch, font=f_punch)
print("punch width:", pw, "content width: 880")
centered(d, CX, 410, punch, f_punch, fill=INK)

# ---------- second punchline: quantifies the wait ----------
f_sub2 = font(SERIF_I, 30)
centered(d, CX, 505, "(13th year in a row.)", f_sub2, fill=INK)

# ---------- attachment line: the price, memo-native ----------
f_att = font(MONO_B, 28)
att = "ATTACHMENT: $79.99 PRE-ORDER \u2014 ALREADY PAID"
aw = d.textlength(att, font=f_att)
print("attachment width:", aw, "content width: 880")
centered(d, CX, 575, att, f_att, fill=INK)

# ---------- footer joke ----------
f_cc = font(SANS_B, 26)
centered(d, CX, 640, "CC: YOUR GRANDKIDS", f_cc, fill=FAINT)

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
