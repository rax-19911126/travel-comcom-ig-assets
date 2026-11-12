#!/usr/bin/env python3
"""Build travel.comcom Instagram Highlights covers (v1).

Original line icons drawn as SVG and rasterized with cairosvg, then
composited with Pillow onto 1080x1920 canvases. No third-party icon packs.
"""

from __future__ import annotations

import math
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
LABELED = ROOT / "labeled"
ICONS = ROOT / "icons"

# ---------------------------------------------------------------------------
# Palette — 「亞麻暖沙」one shared earth-tone set for all 8 covers
# ---------------------------------------------------------------------------
BG = "#EFE8DC"
CIRCLE_FILL = "#F7F3EB"
RING = "#C9B89F"
RING_OUTER = "#D7CBB8"
ICON = "#5C4A3A"
LABEL = "#5C4A3A"
PREVIEW_BG = "#FAFAFA"
PREVIEW_TITLE = "#262626"
PREVIEW_SUB = "#8E8E8E"
PREVIEW_CAPTION = "#262626"

W, H = 1080, 1920
CX, CY = W // 2, H // 2

# All important content sits in a ~660px central safe circle (IG crop ~600–700).
CIRCLE_D = 620  # filled medallion
RING_D = 668  # outer decorative ring
ICON_PX = 280  # icon viewBox maps to this size
SAFE_D = 700

# Labeled version: category name sits below the ring, outside the crop.
LABEL_GAP = 58
LABEL_SIZE = 52

CATEGORIES = [
    {
        "id": "01_taichung_weekend",
        "name": "台中週末",
        "icon": "calendar_sun",
        "optical_dy": 4,  # rings sit high; nudge down slightly
    },
    {
        "id": "02_cafe_dessert",
        "name": "咖啡甜點",
        "icon": "coffee",
        "optical_dy": 6,
    },
    {
        "id": "03_local_food",
        "name": "在地美食",
        "icon": "bowl",
        "optical_dy": 2,
    },
    {
        "id": "04_central_sights",
        "name": "中部景點",
        "icon": "mountain",
        "optical_dy": 4,
    },
    {
        "id": "05_seasonal",
        "name": "季節限定",
        "icon": "maple",
        "optical_dy": 2,
    },
    {
        "id": "06_airfare",
        "name": "機票優惠",
        "icon": "plane",
        "optical_dy": 0,
    },
    {
        "id": "07_abroad",
        "name": "出國靈感",
        "icon": "globe",
        "optical_dy": 0,
    },
    {
        "id": "08_guides",
        "name": "實用攻略",
        "icon": "notebook",
        "optical_dy": 0,
    },
]

# Stroke is identical across every icon (viewBox 0 0 24 24).
STROKE = 1.8

ICONS_SVG = {
    # 台中週末：月曆＋陽光（週末出遊）
    "calendar_sun": f'''
      <rect x="4" y="6.2" width="16" height="14.6" rx="2"/>
      <path d="M 8.2 3.6 V 8.2"/>
      <path d="M 15.8 3.6 V 8.2"/>
      <path d="M 4 10.4 H 20"/>
      <circle cx="12" cy="15.6" r="2.15"/>
      <path d="M 12 12.15 V 11.45"/>
      <path d="M 12 19.05 V 19.75"/>
      <path d="M 8.75 15.6 H 8.05"/>
      <path d="M 15.95 15.6 H 16.65"/>
      <path d="M 9.62 13.22 L 9.12 12.72"/>
      <path d="M 14.38 18.0 L 14.88 18.5"/>
      <path d="M 14.38 13.22 L 14.88 12.72"/>
      <path d="M 9.62 18.0 L 9.12 18.5"/>
    ''',
    # 咖啡甜點：咖啡杯、蒸氣、托盤
    "coffee": f'''
      <path d="M 9.1 4.6 C 9.1 3.35 10.55 3.35 10.55 4.6 C 10.55 5.85 9.1 5.85 9.1 7.15"/>
      <path d="M 12.0 3.85 C 12.0 2.6 13.45 2.6 13.45 3.85 C 13.45 5.1 12.0 5.1 12.0 6.4"/>
      <path d="M 14.9 4.6 C 14.9 3.35 16.35 3.35 16.35 4.6 C 16.35 5.85 14.9 5.85 14.9 7.15"/>
      <path d="M 6.2 9.7 H 17.8"/>
      <path d="M 7.15 9.7 L 8.25 19.05 C 8.42 20.2 9.4 21.05 10.55 21.05 H 13.45 C 14.6 21.05 15.58 20.2 15.75 19.05 L 16.85 9.7"/>
      <path d="M 16.85 11.7 C 20.15 11.85 20.35 17.05 16.55 17.2"/>
      <path d="M 5.4 22.15 C 8.2 23.25 15.8 23.25 18.6 22.15"/>
    ''',
    # 在地美食：碗＋雙筷
    "bowl": f'''
      <ellipse cx="12" cy="13.15" rx="8.6" ry="2.15"/>
      <path d="M 3.4 13.15 C 3.6 17.4 7.1 20.85 12 20.85 C 16.9 20.85 20.4 17.4 20.6 13.15"/>
      <path d="M 14.15 4.2 L 17.35 12.15"/>
      <path d="M 16.55 3.95 L 19.75 11.9"/>
    ''',
    # 中部景點：雙峰山（前低後高，帶簡易雪線）
    "mountain": f'''
      <path d="M 2 20 H 22"/>
      <path d="M 10.4 20 L 16.4 6.1 L 22 20"/>
      <path d="M 2.2 20 L 8.55 7.3 L 15.5 20"/>
      <path d="M 7.15 10.15 L 8.55 7.3 L 9.95 10.15"/>
      <path d="M 14.9 9.3 L 16.4 6.1 L 17.85 9.3"/>
    ''',
    # 季節限定：五裂楓葉＋中脈（線條清晰，避免圓成樹冠）
    "maple": f'''
      <path d="
        M 12 16.6
        L 14.2 14.9
        Q 17.4 16.6 20.4 14.9
        Q 18.2 12.8 16.3 11.2
        Q 19.2 9.0 19.3 6.0
        Q 16.4 6.6 14.5 7.7
        Q 13.8 4.8 12 2.3
        Q 10.2 4.8 9.5 7.7
        Q 7.6 6.6 4.7 6.0
        Q 4.8 9.0 7.7 11.2
        Q 5.8 12.8 3.6 14.9
        Q 6.6 16.6 9.8 14.9
        Z"/>
      <path d="M 12 16.5 V 6.4"/>
      <path d="M 12 16.6 V 21.25"/>
    ''',
    # 機票優惠：由上往下俯視的飛機輪廓
    "plane": f'''
      <path d="
        M 12 2.15
        L 13.55 8.85
        L 21.6 11.2
        L 21.6 13.05
        L 13.55 12.05
        L 13.95 16.55
        L 17.55 20.25
        L 17.55 21.45
        L 12 19.05
        L 6.45 21.45
        L 6.45 20.25
        L 10.05 16.55
        L 10.45 12.05
        L 2.4 13.05
        L 2.4 11.2
        L 10.45 8.85
        Z"/>
    ''',
    # 出國靈感：地球儀
    "globe": f'''
      <circle cx="12" cy="12" r="8.6"/>
      <ellipse cx="12" cy="12" rx="3.5" ry="8.6"/>
      <path d="M 3.4 12 H 20.6"/>
      <path d="M 4.55 8.05 C 8.2 6.85 15.8 6.85 19.45 8.05"/>
      <path d="M 4.55 15.95 C 8.2 17.15 15.8 17.15 19.45 15.95"/>
    ''',
    # 實用攻略：筆記本＋清單
    "notebook": f'''
      <rect x="4.6" y="3.1" width="15.2" height="17.8" rx="2"/>
      <path d="M 8.15 3.1 V 20.9"/>
      <path d="M 10.15 7.55 L 11.25 8.7 L 13.45 6.4"/>
      <path d="M 14.55 7.7 H 17.7"/>
      <path d="M 10.15 11.85 L 11.25 13.0 L 13.45 10.7"/>
      <path d="M 14.55 12.0 H 17.7"/>
      <rect x="10.0" y="15.35" width="2.55" height="2.55" rx="0.35"/>
      <path d="M 14.55 16.6 H 17.7"/>
    ''',
}


def svg_for(icon_key: str, px: int, color: str = ICON, stroke: float = STROKE) -> bytes:
    body = ICONS_SVG[icon_key].strip()
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{px}" height="{px}"
     viewBox="0 0 24 24" fill="none" stroke="{color}"
     stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round">
  {body}
</svg>'''
    return svg.encode("utf-8")


def render_icon(icon_key: str, px: int) -> Image.Image:
    """Rasterize an icon at 4x then downsample for crisp edges."""
    scale = 4
    raw = cairosvg.svg2png(
        bytestring=svg_for(icon_key, px * scale),
        output_width=px * scale,
        output_height=px * scale,
    )
    im = Image.open(__import__("io").BytesIO(raw)).convert("RGBA")
    return im.resize((px, px), Image.Resampling.LANCZOS)


def font(path: str, size: int, index: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size, index=index)


FONT_SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
FONT_SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_SANS_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
TC = 3


def draw_cover(icon: Image.Image, label: str | None, optical_dy: int = 0) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Soft, barely-there radial lift behind the medallion so the circle
    # doesn't feel pasted on a flat field — still the same hue family.
    glow = Image.new("RGB", (W, H), BG)
    gdraw = ImageDraw.Draw(glow)
    glow_d = RING_D + 180
    gdraw.ellipse(
        [CX - glow_d / 2, CY - glow_d / 2, CX + glow_d / 2, CY + glow_d / 2],
        fill="#F5F0E6",
    )
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    img = Image.blend(img, glow, 0.55)
    draw = ImageDraw.Draw(img)

    # Outer thin ring, then filled circle with a slightly stronger ring.
    def circle(d, outline, width, fill=None):
        r = d / 2
        bbox = [CX - r, CY - r, CX + r, CY + r]
        draw.ellipse(bbox, fill=fill, outline=outline, width=width)

    circle(RING_D, RING_OUTER, 3, fill=None)
    circle(CIRCLE_D, RING, 5, fill=CIRCLE_FILL)

    ix = CX - icon.size[0] // 2
    iy = CY - icon.size[1] // 2 + optical_dy
    img.paste(icon, (ix, iy), icon)
    draw = ImageDraw.Draw(img)

    if label:
        f = font(FONT_SERIF, LABEL_SIZE, TC)
        # Slight tracking so the four characters feel editorial, not cramped.
        chars = list(label)
        gap = 10
        widths = [draw.textlength(ch, font=f) for ch in chars]
        total = sum(widths) + gap * (len(chars) - 1)
        x = CX - total / 2
        y = CY + RING_D / 2 + LABEL_GAP
        for ch, cw in zip(chars, widths):
            draw.text((x, y), ch, font=f, fill=LABEL, anchor="lt")
            x += cw + gap

    return img


def crop_circle(src: Image.Image, diameter: int) -> Image.Image:
    """Crop the central safe circle and mask it to a transparent circle."""
    left = CX - diameter // 2
    top = CY - diameter // 2
    tile = src.crop((left, top, left + diameter, top + diameter)).convert("RGBA")
    mask = Image.new("L", (diameter, diameter), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, diameter - 1, diameter - 1), fill=255)
    # Feather 1px to avoid jagged edges on the preview.
    out = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
    out.paste(tile, (0, 0))
    out.putalpha(mask)
    return out


def draw_text_centered(draw, xy, text, font_, fill):
    draw.text(xy, text, font=font_, fill=fill, anchor="mm")


def build_preview(covers: list[tuple[dict, Image.Image]]) -> Image.Image:
    """A single-row mock of the Instagram profile Highlights strip."""
    n = len(covers)
    circle_d = 200
    gap = 56
    side = 80
    top = 150
    label_space = 78
    bottom = 70
    width = side * 2 + n * circle_d + (n - 1) * gap
    height = top + circle_d + label_space + bottom

    img = Image.new("RGB", (width, height), PREVIEW_BG)
    draw = ImageDraw.Draw(img)

    title_f = font(FONT_SANS_BOLD, 36, TC)
    sub_f = font(FONT_SANS, 24, TC)
    name_f = font(FONT_SANS, 26, TC)

    draw_text_centered(draw, (width / 2, 52), "travel.comcom", title_f, PREVIEW_TITLE)
    draw_text_centered(draw, (width / 2, 96), "精選動態預覽", sub_f, PREVIEW_SUB)

    # Hairline under the header, like a profile divider.
    draw.line([(side, 124), (width - side, 124)], fill="#EFEFEF", width=1)

    for i, (meta, cover) in enumerate(covers):
        x = side + i * (circle_d + gap)
        y = top
        # IG-style pale ring slightly larger than the cover circle.
        ring_pad = 6
        draw.ellipse(
            [x - ring_pad, y - ring_pad, x + circle_d + ring_pad, y + circle_d + ring_pad],
            outline="#DBDBDB",
            width=3,
        )
        badge = crop_circle(cover, SAFE_D).resize((circle_d, circle_d), Image.Resampling.LANCZOS)
        img.paste(badge, (x, y), badge)

        cx = x + circle_d / 2
        cy = y + circle_d + 28
        draw_text_centered(draw, (cx, cy), meta["name"], name_f, PREVIEW_CAPTION)

    return img


def write_readme():
    text = f"""# travel.comcom 精選動態封面 v1

8 張 Instagram Highlights 封面，風格統一，重點都落在畫面正中央直徑約 700px 的圓形安全區內。

## 色盤（全系列共用「亞麻暖沙」）

| 用途 | 色碼 |
| --- | --- |
| 背景 | `{BG}` |
| 圓形填色 | `{CIRCLE_FILL}` |
| 圓形描邊 | `{RING}` |
| 外圈細環 | `{RING_OUTER}` |
| 圖示／分類名 | `{ICON}` |

## 圖示來源與授權

圖示為本專案以 SVG 路徑原創繪製的單色線條圖（向量風、筆畫粗細一致），再用 cairosvg 轉成點陣，**沒有使用 AI 生成，也沒有使用付費或有版權的圖示包**。

授權：與本資料夾圖檔一併以 [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) 釋出（作者放棄相關著作權利，可自由使用）。繪製腳本見 `build.py`。

中文分類名使用系統字型 **Noto Serif CJK TC**（SIL Open Font License）。

## 檔案

- `01_taichung_weekend.png` … `08_guides.png`：主版（圖示為主，圓形下方不加字；IG 精選只會看到中央圓形）。
- `labeled/`：對照版，在圓形正下方加上分類名，方便核對，不建議當正式精選封面。
- `preview_grid.png`：8 個封面裁成圓形並排，模擬 IG 個人頁精選列。
- `icons/`：各圖示的透明 PNG，方便檢查線條。

建議在 Instagram 為每一個精選自行設定名稱（台中週末、咖啡甜點、在地美食、中部景點、季節限定、機票優惠、出國靈感、實用攻略），與主版圖檔搭配。
"""
    (ROOT / "README.md").write_text(text, encoding="utf-8")


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    LABELED.mkdir(parents=True, exist_ok=True)
    ICONS.mkdir(parents=True, exist_ok=True)

    covers: list[tuple[dict, Image.Image]] = []
    for meta in CATEGORIES:
        icon = render_icon(meta["icon"], ICON_PX)
        icon.save(ICONS / f"{meta['id']}.png")
        cover = draw_cover(icon, label=None, optical_dy=meta["optical_dy"])
        labeled = draw_cover(icon, label=meta["name"], optical_dy=meta["optical_dy"])
        cover.save(ROOT / f"{meta['id']}.png", "PNG", optimize=True)
        labeled.save(LABELED / f"{meta['id']}.png", "PNG", optimize=True)
        covers.append((meta, cover))
        print(f"wrote {meta['id']}")

    preview = build_preview(covers)
    preview.save(ROOT / "preview_grid.png", "PNG", optimize=True)
    print("wrote preview_grid.png", preview.size)

    # Also save a debug overlay showing the 700px safe circle on slide 01.
    debug = covers[0][1].copy()
    d = ImageDraw.Draw(debug)
    r = SAFE_D / 2
    d.ellipse([CX - r, CY - r, CX + r, CY + r], outline="#FF0000", width=2)
    debug.save(ROOT / "_debug_safezone.png", "PNG")

    write_readme()
    print("done")


if __name__ == "__main__":
    main()
