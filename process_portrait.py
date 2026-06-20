from PIL import Image
import os

src_dir = r'C:\Users\14837\Nutstore\1\2\头像'
dst_dir = r'C:\Users\14837\Nutstore\1\2\retail\images\portrait'

os.makedirs(dst_dir, exist_ok=True)

files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

for i, fname in enumerate(files, 1):
    src_path = os.path.join(src_dir, fname)
    print(f'Processing {fname} -> {i}.webp...')

    img = Image.open(src_path).convert('RGB')

    # Main image: resize to 1200px width
    w, h = img.size
    if w > 1200:
        new_h = int(h * 1200 / w)
        main_img = img.resize((1200, new_h), Image.LANCZOS)
    else:
        main_img = img
    main_img.save(os.path.join(dst_dir, f'{i}.webp'), 'webp', quality=80, method=6)

    # Thumbnail: resize to 400px width
    if w > 400:
        new_h = int(h * 400 / w)
        thumb_img = img.resize((400, new_h), Image.LANCZOS)
    else:
        thumb_img = img
    thumb_img.save(os.path.join(dst_dir, f'{i}_thumb.webp'), 'webp', quality=75, method=6)

    print(f'  Saved {i}.webp + {i}_thumb.webp')

print('Done!')
