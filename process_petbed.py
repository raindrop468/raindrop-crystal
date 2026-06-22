#!/usr/bin/env python3
"""Compress pet bed images to WebP and copy video."""
import os
from PIL import Image

SRC = r"C:\Users\14837\Nutstore\1\2\宠物垫"
DST = r"C:\Users\14837\Nutstore\1\2\retail\images\petbed"

os.makedirs(DST, exist_ok=True)

count = 0
for f in sorted(os.listdir(SRC)):
    src_path = os.path.join(SRC, f)
    name, ext = os.path.splitext(f)
    ext_lower = ext.lower()

    # Copy video as-is
    if ext_lower == '.mp4':
        dst_path = os.path.join(DST, f)
        import shutil
        shutil.copy2(src_path, dst_path)
        print(f"Copied video: {f}")
        continue

    # Skip non-images
    if ext_lower not in ('.jpg', '.jpeg', '.png'):
        continue

    try:
        img = Image.open(src_path)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')

        # Main image: 1200px wide, quality 80
        w, h = img.size
        if w > 1200:
            ratio = 1200 / w
            main_img = img.resize((1200, int(h * ratio)), Image.LANCZOS)
        else:
            main_img = img
        main_path = os.path.join(DST, f"{name}.webp")
        main_img.save(main_path, "WEBP", quality=80)
        print(f"Main: {name}.webp ({main_img.size[0]}x{main_img.size[1]})")

        # Thumbnail: 400px wide, quality 75
        if w > 400:
            ratio = 400 / w
            thumb_img = img.resize((400, int(h * ratio)), Image.LANCZOS)
        else:
            thumb_img = img
        thumb_path = os.path.join(DST, f"{name}_thumb.webp")
        thumb_img.save(thumb_path, "WEBP", quality=75)
        print(f"Thumb: {name}_thumb.webp ({thumb_img.size[0]}x{thumb_img.size[1]})")
        count += 1
    except Exception as e:
        print(f"ERROR on {f}: {e}")

print(f"\nDone! {count} images compressed + 1 video copied.")
