from PIL import Image
import os, glob

src_dir = 'C:/Users/Administrator/Desktop/2/激光台灯'
out_dir = 'C:/Users/Administrator/Desktop/2/retail/images/crystal-lamp'
os.makedirs(out_dir, exist_ok=True)

files = sorted(glob.glob(os.path.join(src_dir, '*')))
total_in = 0
total_out = 0

for f in files:
    name = os.path.splitext(os.path.basename(f))[0]
    img = Image.open(f).convert('RGB')
    w, h = img.size
    total_in += os.path.getsize(f)

    # Main image (1200px wide)
    new_w = 1200
    new_h = int(h * 1200 / w)
    main = img.resize((new_w, new_h), Image.LANCZOS)
    out_main = os.path.join(out_dir, f'{name}.webp')
    main.save(out_main, 'WEBP', quality=80)
    total_out += os.path.getsize(out_main)

    # Thumb (400px wide)
    new_w2 = 400
    new_h2 = int(h * 400 / w)
    thumb = img.resize((new_w2, new_h2), Image.LANCZOS)
    out_thumb = os.path.join(out_dir, f'{name}_thumb.webp')
    thumb.save(out_thumb, 'WEBP', quality=75)
    total_out += os.path.getsize(out_thumb)

    print(f'{name}: {w}x{h} -> {new_w}x{new_h} main + {new_w2}x{new_h2} thumb')

print(f'\nTotal in: {total_in/1024:.0f}KB -> Total out: {total_out/1024:.0f}KB ({100*(1-total_out/total_in):.0f}% reduction)')
