#!/usr/bin/env python3
"""Build the 3 gta6-meme-x-01 draft variants ("GTA VI — THE MOST WANTED WALLET").

Composition rule (team, bontot): in EVERY draft the ghost + the 5 wanted stars DOMINATE
the frame; the grinding player stays small/secondary (corner strip only). Image stays clean.

Assets: real make.fun ghost mark from the press kit (assets/press-kit/.../mark-1024.png).
Canvas 1024x1024; judge sees it shrunk to 480x480, so every text element is large/bold.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
DRAFTS = os.path.join(HERE, "drafts")
os.makedirs(DRAFTS, exist_ok=True)
os.makedirs(os.path.join(DRAFTS, "check480"), exist_ok=True)

W = H = 1024
BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
GHOST = Image.open(os.path.join(ASSETS, "mark-1024.png")).convert("RGBA")

GOLD = (255, 200, 50)        # wanted stars / poster gold
INK_BG = (14, 15, 19)        # near-black poster ground
INK_BG2 = (17, 20, 27)       # dark surface
WHITE = (255, 255, 255)
WARM = (255, 246, 229)       # warm poster white
PINK = (255, 136, 196)       # make.fun magenta ink on dark
GREEN = (133, 187, 101)      # GTA cash green
DIM = (150, 158, 172)        # secondary grey
HAIR = (35, 41, 54)          # hairline


def font(size):
    return ImageFont.truetype(BOLD, size)


def base_canvas(bg=INK_BG):
    img = Image.new("RGB", (W, H), bg)
    # mild radial vignette (edges darker) for depth
    small = Image.new("L", (256, 256), 0)
    px = small.load()
    for yy in range(256):
        for xx in range(256):
            d = math.hypot(xx - 128, yy - 128) / 181.0
            a = max(0.0, (d - 0.45) / 0.55) ** 1.6 * 90
            px[xx, yy] = int(a)
    mask = small.resize((W, H), Image.LANCZOS)
    img.paste((0, 0, 0), (0, 0), mask)
    return img


def star_points(cx, cy, r_out, r_in=None):
    r_in = r_in if r_in is not None else r_out * 0.382
    pts = []
    for i in range(10):
        r = r_out if i % 2 == 0 else r_in
        ang = math.radians(-90 + i * 36)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    return pts


def draw_stars(draw, cy, r, gap, fill=GOLD):
    for i in range(5):
        cx = W // 2 + (i - 2) * gap
        draw.polygon(star_points(cx, cy, r), fill=fill)


def draw_tracked(draw, cx, y, text, fnt, fill, tracking=0):
    """Draw text centered on cx with extra letter spacing, top at y."""
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + tracking


def paste_ghost(img, size, top):
    g = GHOST.resize((size, size), Image.LANCZOS)
    img.paste(g, ((W - size) // 2, top), g)


def cash_stack(draw, x, y, w):
    """Small stack of 3 green banknotes with $ marks, top-left at (x, y)."""
    h = int(w * 0.52)
    note_h = int(h * 0.42)
    for k in range(3):
        ny = y + k * int(note_h * 0.62)
        nx = x + k * 5
        draw.rounded_rectangle([nx, ny, nx + w, ny + note_h], radius=6,
                               fill=(46, 110, 62), outline=(28, 74, 40), width=2)
        draw.ellipse([nx + w * 0.42, ny + 3, nx + w * 0.58, ny + note_h - 3],
                     outline=(133, 187, 101), width=2)
    draw.text((x + w / 2 + 5, y + note_h * 0.62 + note_h / 2), "$",
              font=font(26), fill=(220, 240, 210), anchor="mm")


def frame(draw):
    draw.rectangle([26, 26, W - 26, H - 26], outline=GOLD, width=4)
    draw.rectangle([40, 40, W - 40, H - 40], outline=(255, 200, 50), width=2)


def v1_poster():
    """V1 — classic WANTED poster. Ghost is the mugshot; full poster text.
    Revised per Eva Q2 (round 2): "REWARD: REAL USDC" replaced with
    "THE GHOST ALREADY CASHED OUT" — the old line was ambiguous between satire and
    a financial reward promise. The new line is longer, so it runs at font 50
    (measured 873.6px incl. tracking, fits the 944px inside the frame)."""
    img = base_canvas()
    draw = ImageDraw.Draw(img)
    frame(draw)
    draw_tracked(draw, W // 2, 66, "WANTED", font(138), WARM, tracking=12)
    draw_stars(draw, 272, 34, 92)
    paste_ghost(img, 460, 306)
    draw = ImageDraw.Draw(img)
    draw_tracked(draw, W // 2, 796, "LAST SEEN: VICE CITY", font(40), GOLD, tracking=4)
    draw_tracked(draw, W // 2, 852, "THE GHOST ALREADY CASHED OUT", font(50), WHITE, tracking=1)
    draw_tracked(draw, W // 2, 932, "make.fun", font(38), PINK, tracking=1)
    return img


def v2_contrast():
    """V2 — ghost dominates; the grinder is a small dim strip at the bottom only."""
    img = base_canvas(INK_BG2)
    draw = ImageDraw.Draw(img)
    draw_tracked(draw, W // 2, 48, "WANTED", font(104), WARM, tracking=10)
    draw_stars(draw, 198, 30, 84)
    paste_ghost(img, 480, 240)
    draw = ImageDraw.Draw(img)
    draw_tracked(draw, W // 2, 742, "CASHED OUT.", font(62), WHITE, tracking=2)
    draw_tracked(draw, W // 2, 820, "REAL USDC  ·  make.fun", font(34), PINK, tracking=1)
    # hairline + small grinder strip (secondary, dim): icon + text as one
    # centered group so the icon never overlaps the words.
    draw.line([(180, 892), (W - 180, 892)], fill=HAIR, width=2)
    f1, f2 = font(28), font(28)
    t1, t2 = "everyone else: still grinding ", "GTA$"
    icon_w, gap = 78, 16
    text_w = draw.textlength(t1, font=f1) + draw.textlength(t2, font=f2)
    gx = (W - (icon_w + gap + text_w)) / 2
    cash_stack(draw, int(gx), 916, icon_w)
    tx = gx + icon_w + gap
    draw.text((tx, 924), t1, font=f1, fill=DIM)
    draw.text((tx + draw.textlength(t1, font=f1), 924), t2, font=f2, fill=GREEN)
    return img


def v3_minimal():
    """V3 — minimal: ghost huge, stars, one line. Maximum ghost, minimum text."""
    img = base_canvas(INK_BG2)
    draw = ImageDraw.Draw(img)
    draw_stars(draw, 98, 36, 100)
    paste_ghost(img, 660, 168)
    draw = ImageDraw.Draw(img)
    draw_tracked(draw, W // 2, 858, "WANTED IN LEONIDA", font(54), WHITE, tracking=3)
    draw_tracked(draw, W // 2, 938, "make.fun", font(36), PINK, tracking=1)
    return img


def main():
    variants = [("v1", v1_poster()), ("v2", v2_contrast()), ("v3", v3_minimal())]
    for name, img in variants:
        img.save(os.path.join(DRAFTS, f"meme-{name}.png"))
        img.resize((480, 480), Image.LANCZOS).save(
            os.path.join(DRAFTS, "check480", f"meme-{name}-480.png"))
        print(f"saved meme-{name}.png")
    # contact sheet: 3 drafts side by side at 480px with labels
    sheet = Image.new("RGB", (480 * 3 + 40, 480 + 60), (255, 255, 255))
    sd = ImageDraw.Draw(sheet)
    for i, (name, img) in enumerate(variants):
        sheet.paste(img.resize((480, 480), Image.LANCZOS), (20 + i * 480, 40))
        sd.text((20 + i * 480 + 240, 8), name.upper(), font=font(28),
                fill=(0, 0, 0), anchor="ma")
    sheet.save(os.path.join(DRAFTS, "contact-sheet.png"))
    print("saved contact-sheet.png")


if __name__ == "__main__":
    main()
