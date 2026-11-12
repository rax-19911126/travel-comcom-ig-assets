# travel.comcom reusable templates

- `cta_card.png` — fixed closing CTA card (1080×1350) for intro-type carousels. Paper background, serif heading, emoji drawn with Noto Color Emoji.
- `make_cta_card.py` — regenerates it: `python3 make_cta_card.py [out.png] [out.jpg]`. Edit `ROWS` / `HEADING` to change text; the script refuses emoji missing from the font (no tofu boxes).
