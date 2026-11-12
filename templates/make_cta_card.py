#!/usr/bin/env python3
"""travel.comcom fixed closing CTA card (1080x1350), reusable for intro-type carousels.

Usage:  python3 make_cta_card.py [out.png] [out.jpg]
Default output: templates/cta_card.png next to this script.
Style: paper background, serif heading, ink rules — matches the magazine-style sets.
Emoji are rendered with Noto Color Emoji (bitmap font, drawn at 109px then scaled),
so no tofu boxes. Fonts: Noto Serif CJK TC / Noto Sans CJK TC (index 3 in the .ttc).
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
PAPER = (245, 242, 236)
INK = (38, 40, 42)
SUB = (110, 108, 102)
RULE = (205, 199, 188)
CARD = (252, 250, 246)
RED = (186, 38, 38)
WHITE = (255, 255, 255)
SERIF_B = ('/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc', 3)
SERIF_R = ('/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc', 3)
SANS_R = ('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', 3)
SANS_B = ('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', 3)
EMOJI = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'

HEADING = ('喜歡這篇分享嗎？', '✨')
ROWS = [
    ('❤️', '按個讚，給我們一點動力'),
    ('📤', '分享給想一起出發的人'),
    ('💬', '留言跟我們說你的下一站'),
    ('👉', '追蹤 @travel.comcom，一起發現更多中部好去處'),
]


def F(spec, size):
    return ImageFont.truetype(spec[0], size, index=spec[1])


def tsize(s, f):
    l, t, r, b = ImageDraw.Draw(Image.new('L', (1, 1))).textbbox((0, 0), s, font=f)
    return r - l, b - t, l, t


def emoji(ch, size):
    """Render one emoji with Noto Color Emoji (CBDT, fixed 109px) and scale to `size` px tall."""
    f = ImageFont.truetype(EMOJI, 109)
    im = Image.new('RGBA', (220, 220), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((20, 20), ch, font=f, embedded_color=True)
    bb = im.getbbox()
    assert bb, f'emoji {ch!r} rendered empty'
    im = im.crop(bb)
    # guard against tofu: every non-variation-selector codepoint must exist in the emoji font
    from fontTools.ttLib import TTFont
    cmap = TTFont(EMOJI).getBestCmap()
    for cp in map(ord, ch):
        assert cp == 0xFE0F or cp in cmap, f'U+{cp:04X} missing from Noto Color Emoji'
    r = size / im.height
    return im.resize((max(1, round(im.width * r)), size), Image.Resampling.LANCZOS)


def build():
    c = Image.new('RGBA', (W, H), (*PAPER, 255))
    d = ImageDraw.Draw(c)
    x0, x1 = 96, W - 96
    # masthead
    fm = F(SERIF_R, 24)
    d.text((x0, 120), 'travel.comcom', font=fm, fill=SUB)
    s = '旅遊生活情報站'
    d.text((x1, 120), s, font=F(SANS_R, 20), fill=SUB, anchor='ra')
    d.line((x0, 166, x1, 166), fill=INK, width=2)
    # heading
    fh = F(SERIF_B, 72)
    w, h, l, t = tsize(HEADING[0], fh)
    y = 262
    d.text((x0 - l, y - t), HEADING[0], font=fh, fill=INK)
    e = emoji(HEADING[1], 64)
    c.alpha_composite(e, (x0 + w + 10, y + (h - e.height) // 2))
    y += h + 30
    d.text((x0, y), 'THANK YOU FOR READING', font=F(SERIF_R, 20), fill=SUB)
    y += 80
    # rows
    fb = F(SANS_R, 33)
    fbb = F(SANS_B, 33)
    for i, (em, txt) in enumerate(ROWS):
        last = i == len(ROWS) - 1
        tx = x0 + 130
        maxw = x1 - 40 - tx
        lines = [txt]
        if tsize(txt, fb)[0] > maxw and '，' in txt:
            a, b = txt.split('，', 1)
            lines = [a + '，', b]
        lh = tsize('國', fb)[1]
        ch = 56 + len(lines) * lh + (len(lines) - 1) * 16 + 4
        ch = max(ch, 140)
        box = (x0, y, x1, y + ch)
        sh = Image.new('RGBA', c.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((box[0] + 2, box[1] + 6, box[2] + 2, box[3] + 6), 22, fill=(0, 0, 0, 40))
        c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
        d = ImageDraw.Draw(c)
        d.rounded_rectangle(box, 22, fill=INK if last else CARD, outline=None if last else RULE, width=1)
        # emoji disc
        cx, cy = x0 + 66, y + ch // 2
        d.ellipse((cx - 42, cy - 42, cx + 42, cy + 42), fill=(255, 255, 255) if last else PAPER)
        e = emoji(em, 48)
        c.alpha_composite(e, (cx - e.width // 2, cy - e.height // 2))
        d = ImageDraw.Draw(c)
        ty = y + (ch - (len(lines) * lh + (len(lines) - 1) * 16)) // 2
        for ln in lines:
            w_, h_, l_, t_ = tsize(ln, fb)
            assert w_ <= maxw, (ln, w_, maxw)
            col = WHITE if last else INK
            if last and '@travel.comcom' in ln:
                pre, post = ln.split('@travel.comcom', 1)
                xx = tx
                d.text((xx - l_, ty - t_), pre, font=fb, fill=col)
                xx += d.textlength(pre, font=fb)
                d.text((xx, ty - t_), '@travel.comcom', font=fbb, fill=(255, 221, 140))
                xx += d.textlength('@travel.comcom', font=fbb)
                d.text((xx, ty - t_), post, font=fb, fill=col)
            else:
                d.text((tx - l_, ty - t_), ln, font=fb, fill=col)
            ty += lh + 16
        y += ch + 34
    assert y < H - 120, y
    # footer
    d.line((x0, H - 140, x1, H - 140), fill=RULE, width=1)
    d.text((W // 2, H - 96), 'see you on the next trip', font=F(SERIF_R, 22), fill=SUB, anchor='ma')
    return c


if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    out_png = Path(sys.argv[1]) if len(sys.argv) > 1 else here / 'cta_card.png'
    im = build()
    im.convert('RGB').save(out_png)
    print('saved', out_png)
    if len(sys.argv) > 2:
        srgb = open('/usr/share/color/icc/ghostscript/srgb.icc', 'rb').read()
        im.convert('RGB').save(sys.argv[2], 'JPEG', quality=92, subsampling=0, icc_profile=srgb, optimize=True)
        print('saved', sys.argv[2])
