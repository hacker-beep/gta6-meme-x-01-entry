#!/usr/bin/env python3
"""Build drafts/meme-v4-contract-a.png — GTA VI LAUNCH-WEEK CONTRACT.
PIL-only composition: formal contract document, make.fun ghost as the
co-signing agent (drawn to match the brand mark: white sheet ghost,
gold sparkle eyes, small smile, holding a pen).
"""
import math, hashlib
from PIL import Image, ImageDraw, ImageFont

OUT = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/drafts/meme-v4-contract-a.png"
OUT480 = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/drafts/check480/meme-v4-contract-a-480.png"

W, H = 1024, 1024
PAPER = (248, 243, 230)      # ivory
DESK = (32, 43, 51)          # dark slate margin
INK = (26, 35, 50)           # near-black navy
BLUE = (27, 58, 140)         # signature ink
GOLD = (247, 181, 0)         # sparkle eyes
RED = (139, 30, 45)          # clause numbers / accent

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def draw_centered(d, cx, y, text, f, fill=INK, tracking=0):
    """Draw text centered at cx; tracking = extra px between chars."""
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

def star_points(cx, cy, r_out, r_in, rot=0):
    pts = []
    for i in range(8):
        ang = math.radians(rot + i * 45 - 90)
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts

def ghost_points(cx, top, w, h, scallops=4):
    """Outline points of a sheet ghost: dome top, tapering sides,
    scalloped bottom. Returns list of (x, y)."""
    pts = []
    # dome: half-ellipse from left to right over the top
    rx, ry = w / 2, h * 0.32
    cy = top + ry
    for deg in range(180, 360, 4):
        a = math.radians(deg)
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    # right side down to scallop start
    y_side_end = top + h * 0.82
    pts.append((cx + w * 0.46, y_side_end))
    # scallops right -> left (semicircle bumps upward = wavy hem)
    y_hem = top + h
    x0, x1 = cx + w * 0.46, cx - w * 0.46
    seg = (x1 - x0) / scallops
    for s in range(scallops):
        xa = x0 + s * seg
        xb = xa + seg
        mid = (xa + xb) / 2
        # arc bulging upward (hem rises between lobe tips)
        for t in range(0, 13):
            frac = t / 12
            x = xa + (xb - xa) * frac
            y = y_hem - math.sin(math.pi * frac) * h * 0.075
            pts.append((x, y))
    # left side back up
    pts.append((cx - w * 0.46, y_side_end))
    return pts

def draw_ghost(base, cx, baseline_y, h, pen=True):
    """Draw the make.fun ghost standing with feet at baseline_y.
    h = total ghost height. Returns the pen-tip point (x, y)."""
    w = h * 0.78
    top = baseline_y - h
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    pts = ghost_points(cx, top, w, h)
    d.polygon(pts, fill=(255, 255, 255, 255))
    # outline
    d.line(pts + [pts[0]], fill=(17, 17, 17, 255), width=5, joint="curve")
    # eyes: gold sparkle stars
    eye_y = top + h * 0.38
    eye_dx = w * 0.19
    eye_r = h * 0.085
    for ex in (cx - eye_dx, cx + eye_dx):
        d.polygon(star_points(ex, eye_y, eye_r, eye_r * 0.28),
                  fill=GOLD + (255,))
    # smile
    d.arc([cx - w * 0.11, eye_y + h * 0.10, cx + w * 0.11, eye_y + h * 0.24],
          start=15, end=165, fill=(17, 17, 17, 255), width=4)
    # arm (viewer's right side of ghost): two segments with a bend,
    # drawn as black-under-white so it reads as an outlined limb.
    # Hand held HIGH so the pen has room to reach the signature line.
    shoulder = (cx + w * 0.30, top + h * 0.58)
    elbow = (cx + w * 0.44, top + h * 0.66)
    hand = (cx + w * 0.48, baseline_y - h * 0.30)
    for lw, col in ((30, (17, 17, 17, 255)), (20, (255, 255, 255, 255))):
        d.line([shoulder, elbow, hand], fill=col, width=lw, joint="curve")
    # pen: gripped at the hand, angled steeply down, tip on the line
    ang = math.radians(58)
    pen_len, pen_w = 78, 15
    tip = (hand[0] + pen_len * math.cos(ang), hand[1] + pen_len * math.sin(ang))
    ux, uy = math.cos(ang), math.sin(ang)
    px, py = -uy, ux  # perpendicular
    body_end = (hand[0] + (pen_len - 12) * ux, hand[1] + (pen_len - 12) * uy)
    d.polygon([
        (hand[0] + pen_w / 2 * px, hand[1] + pen_w / 2 * py),
        (body_end[0] + pen_w / 2 * px, body_end[1] + pen_w / 2 * py),
        (body_end[0] - pen_w / 2 * px, body_end[1] - pen_w / 2 * py),
        (hand[0] - pen_w / 2 * px, hand[1] - pen_w / 2 * py),
    ], fill=(27, 58, 140, 255))
    d.polygon([
        (body_end[0] + pen_w / 2 * px, body_end[1] + pen_w / 2 * py),
        tip,
        (body_end[0] - pen_w / 2 * px, body_end[1] - pen_w / 2 * py),
    ], fill=(200, 200, 210, 255))
    base.paste(layer, (0, 0), layer)
    return tip

def scrawl(d, x0, y0, width, amp, color=BLUE, lw=5, seed=7):
    """Deterministic signature-like wavy scrawl."""
    import random
    rnd = random.Random(seed)
    pts = []
    n = 90
    # big initial loop
    for t in range(0, 21):
        a = math.radians(t * 18)
        pts.append((x0 + 8 + 14 * math.cos(a), y0 - 6 + 12 * math.sin(a)))
    x = x0 + 26
    while x < x0 + width:
        step = rnd.uniform(4, 9)
        yy = y0 + math.sin(x * 0.11 + seed) * amp * rnd.uniform(0.4, 1.0)
        pts.append((x, yy))
        x += step
    d.line(pts, fill=color, width=lw, joint="curve")
    # underline flourish
    d.line([(x0, y0 + amp + 8), (x0 + width, y0 + amp + 4)],
           fill=color, width=3)

# ---------- canvas ----------
img = Image.new("RGB", (W, H), DESK)
d = ImageDraw.Draw(img)
M = 28  # desk margin
# paper with soft shadow
d.rectangle([M + 6, M + 8, W - M + 6, H - M + 8], fill=(10, 14, 18))
d.rectangle([M, M, W - M, H - M], fill=PAPER)
# double frame
d.rectangle([M + 12, M + 12, W - M - 12, H - M - 12], outline=INK, width=2)
d.rectangle([M + 20, M + 20, W - M - 20, H - M - 20], outline=INK, width=1)

CX = W // 2
# ---------- title ----------
f_title = font(SERIF_B, 96)
d.text((CX - d.textlength("GTA VI", font=f_title) / 2, 56), "GTA VI",
       font=f_title, fill=INK)
f_sub = font("/usr/share/fonts/truetype/noto/NotoSerif-CondensedBold.ttf", 60)
draw_centered(d, CX, 168, "LAUNCH-WEEK CONTRACT", f_sub, tracking=4)

# ---------- divider ----------
dy = 258
d.line([(CX - 300, dy), (CX - 30, dy)], fill=INK, width=2)
d.line([(CX + 30, dy), (CX + 300, dy)], fill=INK, width=2)
d.line([(CX - 300, dy + 6), (CX + 300, dy + 6)], fill=INK, width=1)
d.polygon([(CX, dy - 10), (CX + 10, dy), (CX, dy + 10), (CX - 10, dy)],
          fill=RED)

# ---------- preamble ----------
f_pre = font(SERIF, 29)
draw_centered(d, CX, 284, "THE GAMER AND THE AGENT AGREE AS FOLLOWS:", f_pre)

# ---------- clauses ----------
clauses = [
    ("1.", ["NOV 19\u201329: I PLAY GTA VI", "AS MUCH AS I WANT."]),
    ("2.", ["DO NOT WALK IN FRONT OF THE TV", "DURING A HEIST."]),
    ("3.", ["MY AGENT EARNS THE USDC", "ON make.fun."]),
]
f_num = font(SERIF_B, 46)
f_clause = font(SERIF, 44)
LX = 134          # clause text left edge
NX = 68           # number left edge
y = 336
LH = 56
GAP = 18
for num, lines in clauses:
    d.text((NX, y), num, font=f_num, fill=RED)
    for ln in lines:
        # auto-fit: shrink until it fits the content width
        size = 44
        f = f_clause
        while d.textlength(ln, font=f) > 818 and size > 40:
            size -= 1
            f = font(SERIF, size)
        d.text((LX, y), ln, font=f, fill=INK)
        y += LH
    y += GAP
# y ends ~ 336 + 3*(2*56+18) = 336 + 390 = 726

# ---------- signature divider ----------
sy = 742
d.line([(M + 44, sy), (W - M - 44, sy)], fill=INK, width=2)

# ---------- left: gamer signature ----------
sig_line_y = 878
d.line([(108, sig_line_y), (452, sig_line_y)], fill=INK, width=2)
scrawl(d, 150, sig_line_y - 26, 260, 12, seed=7)
f_lab = font(SERIF_B, 26)
draw_centered(d, 280, sig_line_y + 14, "THE GAMER", f_lab)

# ---------- right: ghost signing ----------
# ghost stands on the signature line; pen tip lands on the line
GHOST_H = 236
ghost_cx = 726
tip = draw_ghost(img, ghost_cx, sig_line_y, GHOST_H)
d = ImageDraw.Draw(img)  # refresh after composite
d.line([(560, sig_line_y), (920, sig_line_y)], fill=INK, width=2)
# ghost's little signature scrawl under the pen tip
scrawl(d, tip[0] - 8, sig_line_y - 12, 70, 5, seed=3, lw=3)
draw_centered(d, 740, sig_line_y + 14, "THE AGENT", f_lab)
f_wm = font(SERIF_B, 36)
draw_centered(d, 740, sig_line_y + 46, "make.fun", f_wm, fill=BLUE)

img.save(OUT, "PNG")
# ---------- 480px check ----------
img480 = img.resize((480, 480), Image.LANCZOS)
img480.save(OUT480, "PNG")

h = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
print("saved:", OUT)
print("sha256:", h)
print("480 check:", OUT480)
