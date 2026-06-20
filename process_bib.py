"""Compress bib images to WebP format."""
from PIL import Image
from pathlib import Path

src_dir = Path(r"C:\Users\14837\Nutstore\1\2\口水巾")
out_dir = Path(r"C:\Users\14837\Nutstore\1\2\retail\images\bib")
out_dir.mkdir(parents=True, exist_ok=True)

for i in range(1, 12):
    src = src_dir / f"{i}.jpg"
    if not src.exists():
        print(f"SKIP {src} (not found)")
        continue

    img = Image.open(src).convert("RGB")
    w, h = img.size
    print(f"  {i}.jpg: {w}x{h}")

    # Main image: 1200px wide, quality 80
    if w > 1200:
        ratio = 1200 / w
        main_img = img.resize((1200, int(h * ratio)), Image.LANCZOS)
    else:
        main_img = img
    main_img.save(out_dir / f"{i}.webp", "WEBP", quality=80)
    print(f"    -> {i}.webp ({main_img.size[0]}x{main_img.size[1]})")

    # Thumbnail: 400px wide, quality 75
    if w > 400:
        ratio = 400 / w
        thumb_img = img.resize((400, int(h * ratio)), Image.LANCZOS)
    else:
        thumb_img = img
    thumb_img.save(out_dir / f"{i}_thumb.webp", "WEBP", quality=75)
    print(f"    -> {i}_thumb.webp ({thumb_img.size[0]}x{thumb_img.size[1]})")

print("\nDone! All bib images compressed.")
