#!/usr/bin/env python3
"""Compress pet bed abcdef images to WebP."""
import os
from PIL import Image

SRC = r"C:\Users\14837\Nutstore\1\2\宠物垫"
DST = r"C:\Users\14837\Nutstore\1\2\retail\images\petbed"

letters = ['a', 'b', 'c', 'd', 'e', 'f']
count = 0

for letter in letters:
    src_path = os.path.join(SRC, f"{letter}.jpg")
    if not os.path.exists(src_path):
        print(f"NOT FOUND: {letter}.jpg")
        continue

    img = Image.open(src_path)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')

    w, h = img.size

    # Main image: 1200px wide, quality 80
    if w > 1200:
        ratio = 1200 / w
        main_img = img.resize((1200, int(h * ratio)), Image.LANCZOS)
    else:
        main_img = img
    main_path = os.path.join(DST, f"{letter}.webp")
    main_img.save(main_path, "WEBP", quality=80)
    print(f"Main: {letter}.webp ({main_img.size[0]}x{main_img.size[1]})")

    # Thumbnail: 400px wide, quality 75
    if w > 400:
        ratio = 400 / w
        thumb_img = img.resize((400, int(h * ratio)), Image.LANCZOS)
    else:
        thumb_img = img
    thumb_path = os.path.join(DST, f"{letter}_thumb.webp")
    thumb_img.save(thumb_path, "WEBP", quality=75)
    print(f"Thumb: {letter}_thumb.webp ({thumb_img.size[0]}x{thumb_img.size[1]})")
    count += 1

print(f"\nDone! {count} images compressed.")
