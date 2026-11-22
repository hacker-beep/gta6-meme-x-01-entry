#!/usr/bin/env python3
"""Build drafts/meme-v12-timecardv3-a.png — GTA VI TIME CARD V3, entry 6 draft.

Entry 4's proven frame (DEV 81.5918%) plus ONE purposeful change vs v2
(DEV 80.54%): v2's two-line small-print manager's note ("APPROVED FOR
RETIREMENT — CLOCKED OUT BEFORE IT SHIPPED.") got noticed by the judges
but the dryness critique persisted ("text-dense and slow to read at a
glance"). v3 delivers the SAME retirement punchline as ONE big bold red
line — "RETIRED BEFORE LAUNCH." — instant, no reading required.

Everything that won is kept: ghost letterhead logo, clock in/out,
GIANT 115,464 center-frame, OVERTIME: ALL OF IT, RATE $0.00/HR,
TOTAL DUE $79.99, red PAID stamp. The new line is the third visual
beat: 115,464 biggest, stamp dominant, punch line bold red.

PIL composition only — no AI text. Ghost asset reused from entry 4.
Adapted from drafts/build-timecardv2-a.py (commit d76259a).
"""
import hashlib
from PIL import Image, ImageDraw, ImageFont

D = "/home/hatch/workspace/makefun/gta6-meme-x-01-entry/drafts"
OUT = D + "/meme-v12-timecardv3-a.png"
OUT480 = D + "/check480/meme-v12-timecardv3-a-480.png"
GHOST = D + "/ghost-logo-150.png"

W, H = 1024, 1024
PAPER = (250, 246, 236)      # warm white card stock
DESK = (38, 46, 54)          # dark slate margin
INK = (22, 28, 38)           # near-black navy
FAINT = (90, 96, 104)        # label grey
RED = (192, 28, 40)          # stamp red
BLUE = (27, 58, 140)         # punch ink

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


def fit_font(d, text, path, start, max_w):
    """Largest size <= start whose text fits max_w."""
    size = start
    while size > 12:
        f = font(path, size)
        if d.textlength(text, font=f) <= max_w:
            return f, size
        size -= 1
    return font(path, 12), 12


# ---------- canvas ----------
img = Image.new("RGB", (W, H), DESK)
d = ImageDraw.Draw(img)
M = 28
d.rectangle([M + 6, M + 8, W - M + 6, H - M + 8], fill=(10, 14, 18))
d.rectangle([M, M, W - M, H - M], fill=PAPER)
d.rectangle([M + 12, M + 12, W - M - 12, H - M - 12], outline=INK, width=2)
d.rectangle([M + 20, M + 20, W - M - 20, H - M - 20], outline=INK, width=1)

CX = W // 2

# ---------- header: ghost badge (company logo) + letterhead ----------
ghost = Image.open(GHOST).convert("RGBA")
gs = 120
ghost = ghost.resize((gs, gs), Image.LANCZOS)
mask = Image.new("L", (gs, gs), 0)
ImageDraw.Draw(mask).ellipse([0, 0, gs, gs], fill=255)
img.paste(ghost, (62, 42), mask)
d = ImageDraw.Draw(img)
d.ellipse([62, 42, 62 + gs, 42 + gs], outline=(214, 51, 132), width=5)

f_co = font(SERIF_B, 42)
d.text((200, 56), "LEONIDA TIMEKEEPING CO.", font=f_co, fill=INK)
f_card = font(SERIF, 30)
centered(d, 596, 112, "— EMPLOYEE TIME CARD —", f_card, fill=FAINT)

# punch hole (top-right only — the badge occupies the top-left corner)
d.ellipse([W - 96 - 9, 40, W - 96 + 9, 58], fill=DESK)

# ---------- divider ----------
dy = 158
d.line([(M + 44, dy), (W - M - 44, dy)], fill=INK, width=3)
d.line([(M + 44, dy + 7), (W - M - 44, dy + 7)], fill=INK, width=1)

# ---------- employee / job ----------
f_lab = font(SANS_B, 28)
f_val = font(SERIF_B, 44)
y = 176
d.text((72, y), "EMPLOYEE:", font=f_lab, fill=FAINT)
d.text((290, y - 6), "GTA VI FAN", font=f_val, fill=INK)
y = 224
d.text((72, y), "JOB:", font=f_lab, fill=FAINT)
d.text((290, y - 6), "WAITING FOR GTA VI", font=f_val, fill=INK)

# ---------- punch box: clocked in / out ----------
box_y0, box_y1 = 286, 398
d.rectangle([56, box_y0, W - 56, box_y1], outline=INK, width=3)
d.line([(CX, box_y0), (CX, box_y1)], fill=INK, width=2)
f_plab = font(SANS_B, 26)
f_pdate = font(MONO_B, 50)
centered(d, CX - 228, box_y0 + 8, "CLOCKED IN", f_plab, fill=FAINT)
centered(d, CX - 228, box_y0 + 42, "17 SEP 2013", f_pdate, fill=BLUE)
centered(d, CX + 228, box_y0 + 8, "CLOCKED OUT", f_plab, fill=FAINT)
centered(d, CX + 228, box_y0 + 42, "19 NOV 2026", f_pdate, fill=BLUE)

# ---------- THE NUMBER: total hours (unchanged size — this is what works) ----------
f_hlab = font(SANS_B, 32)
centered(d, CX, 412, "TOTAL HOURS", f_hlab, fill=FAINT, tracking=6)
f_num = font(MONO_B, 140)
centered(d, CX, 446, "115,464", f_num, fill=INK)

# ---------- overtime, then rate / due ----------
f_ot = font(SERIF_B, 40)
centered(d, CX, 592, "OVERTIME: ALL OF IT", f_ot, fill=INK)
f_rate = font(MONO_B, 36)
d.text((72, 638), "RATE $0.00/HR", font=f_rate, fill=INK)
due = "TOTAL DUE $79.99"
d.text((W - 72 - d.textlength(due, font=f_rate), 638), due, font=f_rate,
       fill=INK)

# ---------- THE PUNCHLINE: one big bold red line (v3 — replaces v2's note) --
# Band between the rate row (ends ~674) and the stamp (top 786): the line
# sits centered in it at y=700. Big bold red so it reads instantly at a
# glance — the direct answer to "text-dense, slow to read".
f_punch, punch_size = fit_font(d, "RETIRED BEFORE LAUNCH.", SANS_B, 56, 900)
centered(d, CX, 700, "RETIRED BEFORE LAUNCH.", f_punch, fill=RED)
print("punch size:", punch_size,
      "width:", d.textlength("RETIRED BEFORE LAUNCH.", font=f_punch))

# ---------- PAID stamp: red diagonal, same size/position as v2 ----------
# stamp 620x135 @ -6 deg (clockwise): bbox w = 620*cos6 + 135*sin6
# = 631, h = 620*sin6 + 135*cos6 = 199. Paste box top at y=786 ->
# bottom 985, inside the paper (996). Punch line ends ~756; the
# stamp's top-left corner (highest point, x~196) clears it by ~30px.
SW, SH, ANG = 620, 135, -6
st = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
sd = ImageDraw.Draw(st)
sd.rectangle([5, 5, SW - 5, SH - 5], outline=RED + (235,), width=6)
sd.rectangle([15, 15, SW - 15, SH - 15], outline=RED + (235,), width=2)
f_s1 = font(SANS_B, 57)
f_s2 = font(SANS_B, 25)
centered(sd, SW // 2, 14, "PAID IN FULL", f_s1, fill=RED + (240,))
centered(sd, SW // 2, 86, "BY MY AI AGENT ON MAKE.FUN", f_s2,
         fill=RED + (240,))
for sx in (40, SW - 40):
    sd.text((sx - 10, 84), "\u2605", font=font(SANS_B, 25), fill=RED + (240,))
st = st.rotate(ANG, expand=True, resample=Image.BICUBIC)
print("stamp bbox:", st.size, "expected ~ (631, 199)")
img.paste(st, ((W - st.width) // 2, 786), st)

img.save(OUT, "PNG")
img.resize((480, 480), Image.LANCZOS).save(OUT480, "PNG")

h = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
print("saved:", OUT)
print("sha256:", h)
print("480 check:", OUT480)
