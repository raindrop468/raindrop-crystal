"""Compress wool felt product images to WebP (main 1200px + thumb 400px)."""
import os
from PIL import Image

SRC_DIR = r"C:\Users\Administrator\Desktop\2\羊毛、"
OUT_DIR = r"C:\Users\Administrator\Desktop\2\images\wool-felt"
ORIGINALS_DIR = r"C:\Users\Administrator\Desktop\2\originals\wool-felt"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(ORIGINALS_DIR, exist_ok=True)

for i in range(1, 17):
    src = os.path.join(SRC_DIR, f"{i}.jpg")
    if not os.path.exists(src):
        print(f"SKIP: {src} not found")
        continue

    img = Image.open(src).convert("RGB")
    w, h = img.size
    print(f"[{i:02d}] Original: {w}x{h} ({os.path.getsize(src)//1024}KB)")

    # Main image (1200px wide)
    main = img.copy()
    if w > 1200:
        main = main.resize((1200, int(h * 1200 / w)), Image.LANCZOS)
    main_out = os.path.join(OUT_DIR, f"{i}.webp")
    main.save(main_out, "WEBP", quality=80)
    main_size = os.path.getsize(main_out) // 1024

    # Thumb (400px wide)
    thumb = img.copy()
    thumb = thumb.resize((400, int(h * 400 / w)), Image.LANCZOS)
    thumb_out = os.path.join(OUT_DIR, f"{i}_thumb.webp")
    thumb.save(thumb_out, "WEBP", quality=75)
    thumb_size = os.path.getsize(thumb_out) // 1024

    # Backup original
    import shutil
    shutil.copy2(src, os.path.join(ORIGINALS_DIR, f"{i}.jpg"))

    print(f"       Main: {main_out} ({main_size}KB)")
    print(f"       Thumb: {thumb_out} ({thumb_size}KB)")

print("\nDone!")
