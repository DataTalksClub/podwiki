#!/usr/bin/env python3
"""Generate the default social share image (assets/og-default.png).

One-off, reproducible generator. Pillow is not a project dependency, so run it
through uvx:

    uvx --with pillow python scripts/make_og_image.py

The output is committed; re-run only when the branding changes.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "og-default.png"

W, H = 1200, 630
BG = (18, 20, 28)
ACCENT = (124, 156, 255)
MUTED = (150, 158, 178)
WHITE = (245, 247, 250)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(name, size)


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # accent bar
    draw.rectangle([0, 0, 16, H], fill=ACCENT)
    margin = 90

    draw.text((margin, 150), "DataTalks.Club", font=font(46, bold=True), fill=ACCENT)
    draw.text((margin, 220), "Podcast Wiki", font=font(104, bold=True), fill=WHITE)
    draw.text(
        (margin, 380),
        "Topic hubs · guides · people · exploration search",
        font=font(38),
        fill=MUTED,
    )
    draw.text(
        (margin, 452),
        "for the DataTalks.Club podcast archive",
        font=font(38),
        fill=MUTED,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG")
    print(f"wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
