#!/usr/bin/env python3
"""Build drafts/meme-v9-fakechat-a.png — FAKE GROUP CHAT, entry 5 third candidate.

ZERO fake-chat entries in the live top 200 (census 22 Nov 20:00 WIB).
Entry 4's judge dossier PROVES this format wins pairwise: a group-chat
timeline meme beat/drew the time card twice ("the more instantly
relatable fan joke", "the stronger GTA 6 laugh"). The punchline line
"we're 31. my back hurts." is kept VERBATIM from that dossier.

Winning formula, adapted to chat: wait quantified (2013 -> 2026 date
chips + red "13 YEARS LATER" system chip) AND priced ($79.99 in the
ghost's message); paid gag in the chat's own voice ("paid in full");
ghost INTEGRAL as a chat participant (avatar + name "make.fun").
No separate stamp — the layout is full and the brief allows the ghost
message to carry the paid gag alone.

PIL composition only — no AI text, no AI image. Ghost asset reused
from entry 4 (drafts/ghost-logo-150.png).

Layout (1024x1024, phone screenshot, WhatsApp-style light UI):
  bezel 10px dark, status bar 10-52, header 52-150 (teal),
  chat bg #ECE5DD from 150 to 1014.
  date chip 2013 ~172, bubble 1 ~218, chip 2023 ~306, bubble 2 ~352,
  chip 2025 ~440, bubble 3 ~486, red "13 YEARS LATER" chip ~574,
  punchline bubble ~676 (2 lines, bold 38), ghost bubble ~784
  (avatar + name + 2-line message), input bar ~930-1000.
"""
import hashlib
from PIL import Image, ImageDraw, ImageFont

D = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/drafts"
OUT = D + "/meme-v9-fakechat-a.png"
OUT480 = D + "/check480/meme-v9-fakechat-a-480.png"
GHOST = D + "/ghost-logo-150.png"

W, H = 1024, 1024
BEZEL = (18, 22, 28)         # dark phone frame
TEAL = (7, 94, 84)           # WhatsApp header
TEAL_DARK = (5, 74, 66)      # status bar
CHAT_BG = (236, 229, 221)    # WhatsApp wallpaper beige
BUBBLE_IN = (255, 255, 255)  # incoming bubble
BUBBLE_OUT = (220, 248, 198) # outgoing bubble (WhatsApp green)
CHIP_BG = (211, 220, 212)    # date chip
CHIP_TX = (74, 90, 82)       # date chip text
RED = (192, 28, 40)          # "13 YEARS LATER" chip
INK = (28, 32, 36)           # bubble text
FAINT = (120, 124, 128)      # placeholder / subtle text
PINK = (214, 51, 132)        # make.fun name + ghost ring

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def centered(d, cx, y, text, f, fill):
    w = d.textlength(text, font=f)
    d.text((cx - w / 2, y), text, font=f, fill=fill)
    return w


# ---------- canvas: phone frame ----------
img = Image.new("RGB", (W, H), BEZEL)
d = ImageDraw.Draw(img)
# screen
d.rectangle([10, 10, W - 10, H - 10], fill=CHAT_BG)

# ---------- status bar ----------
d.rectangle([10, 10, W - 10, 52], fill=TEAL_DARK)
f_stat = font(SANS_B, 22)
d.text((30, 18), "21:06", font=f_stat, fill=(255, 255, 255))
# tiny battery glyph (outline + nub + fill)
d.rectangle([920, 22, 968, 38], outline=(255, 255, 255), width=2)
d.rectangle([923, 25, 955, 35], fill=(255, 255, 255))
d.rectangle([970, 26, 976, 34], fill=(255, 255, 255))
# signal bars
for i, bh in enumerate((8, 12, 16, 20)):
    x0 = 872 + i * 10
    d.rectangle([x0, 38 - bh, x0 + 6, 38], fill=(255, 255, 255))

# ---------- header ----------
d.rectangle([10, 52, W - 10, 150], fill=TEAL)
# group avatar: dark circle with ghost-ish "VI" monogram
d.ellipse([30, 72, 110, 152], fill=(255, 255, 255))
d.ellipse([30, 72, 110, 152], outline=PINK, width=3)
f_vi = font(SANS_B, 34)
centered(d, 70, 88, "VI", f_vi, TEAL)
f_grp = font(SANS_B, 34)
d.text((128, 66), "GTA VI HYPE SQUAD", font=f_grp, fill=(255, 255, 255))
f_sub = font(SANS, 22)
d.text((128, 110), "5 members, online", font=f_sub,
       fill=(200, 228, 222))

CX = W // 2


def date_chip(y, text):
    """Centered WhatsApp-style date chip. Returns bottom y."""
    f = font(SANS_B, 22)
    tw = d.textlength(text, font=f)
    w = tw + 44
    h = 34
    x0 = CX - w / 2
    d.rounded_rectangle([x0, y, x0 + w, y + h], radius=10, fill=CHIP_BG)
    centered(d, CX, y + 5, text, f, CHIP_TX)
    return y + h


def system_chip(y, text):
    """Red system chip (the quantified wait). Returns bottom y."""
    f = font(SANS_B, 26)
    tw = d.textlength(text, font=f)
    w = tw + 56
    h = 40
    x0 = CX - w / 2
    d.rounded_rectangle([x0, y, x0 + w, y + h], radius=12, fill=RED)
    centered(d, CX, y + 6, text, f, (255, 255, 255))
    return y + h


def bubble(y, lines, f_text, side="left", sender=None, sender_color=INK,
           x_left=None, bold=False):
    """Draw a chat bubble. lines: list of strings. Returns bottom y.
    side left: white bubble from x_left; side right: green bubble
    ending at x=984. Sender name (if given) sits above the text
    inside the bubble, WhatsApp-group style."""
    pad_x, pad_top, pad_bot = 26, 12, 10
    line_h = int(f_text.size * 1.28)
    f_name = font(SANS_B, 22)
    name_h = 26 if sender else 0
    maxw = max(d.textlength(t, font=f_text) for t in lines)
    if sender:
        maxw = max(maxw, d.textlength(sender, font=f_name))
    bw = maxw + pad_x * 2
    bh = pad_top + name_h + line_h * len(lines) + pad_bot
    if side == "left":
        x0 = x_left if x_left is not None else 40
        x1 = x0 + bw
        fill = BUBBLE_IN
    else:
        x1 = 984
        x0 = x1 - bw
        fill = BUBBLE_OUT
    d.rounded_rectangle([x0, y, x1, y + bh], radius=18, fill=fill)
    # tail
    if side == "left":
        d.polygon([(x0 + 6, y + bh - 6), (x0 - 12, y + bh - 2),
                   (x0 + 6, y + bh - 26)], fill=fill)
    else:
        d.polygon([(x1 - 6, y + bh - 6), (x1 + 12, y + bh - 2),
                   (x1 - 6, y + bh - 26)], fill=fill)
    ty = y + pad_top
    if sender:
        d.text((x0 + pad_x, ty), sender, font=f_name, fill=sender_color)
        ty += name_h
    for t in lines:
        d.text((x0 + pad_x, ty), t, font=f_text, fill=INK)
        ty += line_h
    return y + bh


# ---------- timeline ----------
f_msg = font(SANS, 31)
f_punch = font(SANS_B, 36)
f_ghost_msg = font(SANS, 29)

y = 164
y = date_chip(y, "17 SEP 2013")
y = bubble(y + 12, ["gta 6 gonna be insane"], f_msg,
           side="left", sender="Jason", sender_color=(30, 136, 229))

y = date_chip(y + 12, "5 DEC 2023")
y = bubble(y + 12, ["TRAILER DROPPED!!"], f_msg,
           side="right", sender="Lucia", sender_color=(214, 51, 132))

y = date_chip(y + 12, "MAY 2025")
y = bubble(y + 12, ["delayed AGAIN\u2026"], f_msg,
           side="left", sender="Tommy", sender_color=(67, 160, 71))

y = system_chip(y + 12, "13 YEARS LATER")

# punchline: verbatim from the judge dossier, bold + larger
y = bubble(y + 12, ["we're 31.", "my back hurts."], f_punch,
           side="right", sender="you", sender_color=(245, 124, 0))

# ---------- ghost enters as a participant ----------
gy = y + 14
# ghost avatar (circular, pink ring), left of the bubble
ghost = Image.open(GHOST).convert("RGBA")
gs = 64
ghost = ghost.resize((gs, gs), Image.LANCZOS)
mask = Image.new("L", (gs, gs), 0)
ImageDraw.Draw(mask).ellipse([0, 0, gs, gs], fill=255)
img.paste(ghost, (40, gy), mask)
d = ImageDraw.Draw(img)
d.ellipse([40, gy, 40 + gs, gy + gs], outline=PINK, width=4)
y = bubble(gy, ["paid in full \u2014 $79.99,", "by my AI agent"],
           f_ghost_msg, side="left", sender="make.fun",
           sender_color=PINK, x_left=120)

# ---------- input bar (sells the phone screenshot) ----------
bar_y0, bar_y1 = 944, 1010
d.rectangle([10, bar_y0, W - 10, H - 10], fill=(240, 240, 238))
d.rounded_rectangle([30, bar_y0 + 12, 884, bar_y1 - 4], radius=28,
                    fill=(255, 255, 255))
f_ph = font(SANS, 26)
d.text((62, bar_y0 + 26), "Message", font=f_ph, fill=FAINT)
d.ellipse([908, bar_y0 + 10, 972, bar_y1 - 6], fill=TEAL)
# send arrow (paper-plane-ish triangle)
d.polygon([(930, bar_y0 + 40), (958, bar_y0 + 26), (946, bar_y0 + 52)],
          fill=(255, 255, 255))

img.save(OUT, "PNG")
img.resize((480, 480), Image.LANCZOS).save(OUT480, "PNG")

h = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
print("saved:", OUT)
print("sha256:", h)
print("480 check:", OUT480)
