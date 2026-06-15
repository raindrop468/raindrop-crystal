"""Compress rope toy JPGs to WebP (main 1200px + thumb 400px)."""
from PIL import Image
import os

SRC = os.path.join(os.path.dirname(__file__), '玩具')
DST = os.path.join(os.path.dirname(__file__), 'retail', 'images', 'rope-toys')
os.makedirs(DST, exist_ok=True)

files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']

for f in files:
    base = f.replace('.jpg', '')
    img = Image.open(os.path.join(SRC, f)).convert('RGB')

    # Main image (1200px wide)
    w, h = img.size
    main_w = 1200
    ratio = main_w / w
    main_h = int(h * ratio)
    main = img.resize((main_w, main_h), Image.LANCZOS)
    main.save(os.path.join(DST, f'{base}.webp'), 'WEBP', quality=80)
    main_size = os.path.getsize(os.path.join(DST, f'{base}.webp'))

    # Thumbnail (400px wide)
    thumb_w = 400
    ratio2 = thumb_w / w
    thumb_h = int(h * ratio2)
    thumb = img.resize((thumb_w, thumb_h), Image.LANCZOS)
    thumb.save(os.path.join(DST, f'{base}_thumb.webp'), 'WEBP', quality=75)
    thumb_size = os.path.getsize(os.path.join(DST, f'{base}_thumb.webp'))

    print(f'{f}: {w}x{h} -> main {main_w}x{main_h} ({main_size//1024}KB) + thumb {thumb_w}x{thumb_h} ({thumb_size//1024}KB)')

total_src = sum(os.path.getsize(os.path.join(SRC, f)) for f in files)
total_dst = sum(os.path.getsize(os.path.join(DST, f)) for f in os.listdir(DST))
print(f'\nTotal src: {total_src//1024}KB -> dst: {total_dst//1024}KB ({(1-total_dst/total_src)*100:.1f}% reduced)')
