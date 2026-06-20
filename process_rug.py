#!/usr/bin/env python3
"""Compress rug images to WebP format."""
from PIL import Image
from pathlib import Path
import os

src_dir = Path(r"C:\Users\14837\Nutstore\1\2\地毯")
out_dir = Path(r"C:\Users\14837\Nutstore\1\2\retail\images\rug")
out_dir.mkdir(parents=True, exist_ok=True)

count = 0
for img_path in sorted(src_dir.glob("*.jpg"), key=lambda p: int(p.stem)):
    num = img_path.stem
    img = Image.open(img_path).convert("RGB")

    # Main image: max 1200px wide, quality 80
    main = img.copy()
    if main.width > 1200:
        ratio = 1200 / main.width
        main = main.resize((1200, int(main.height * ratio)), Image.LANCZOS)
    main.save(out_dir / f"{num}.webp", "WEBP", quality=80)
    print(f"  {num}.webp ({main.width}x{main.height})")

    # Thumbnail: max 400px wide, quality 75
    thumb = img.copy()
    if thumb.width > 400:
        ratio = 400 / thumb.width
        thumb = thumb.resize((400, int(thumb.height * ratio)), Image.LANCZOS)
    thumb.save(out_dir / f"{num}_thumb.webp", "WEBP", quality=75)
    print(f"  {num}_thumb.webp ({thumb.width}x{thumb.height})")

    count += 1

print(f"\nDone! {count} images processed, {count * 2} WebP files created.")
