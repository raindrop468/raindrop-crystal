"""Compress bolster source images to WebP for retail/images/bolster/"""
import os, sys
from PIL import Image

SRC = r"C:\Users\Administrator\Desktop\2\抱枕"
DST = r"C:\Users\Administrator\Desktop\2\retail\images\bolster"

os.makedirs(DST, exist_ok=True)

IMAGES = ['1','2','3','4','5','6','7','8']

total_src = 0
total_dst = 0

for name in IMAGES:
    src_path = os.path.join(SRC, f"{name}.jpg")
    if not os.path.exists(src_path):
        print(f"  SKIP: {src_path} not found")
        continue
    
    total_src += os.path.getsize(src_path)
    img = Image.open(src_path)
    
    # Main image 1200px
    main = img.copy()
    main.thumbnail((1200, 1200), Image.LANCZOS)
    main_path = os.path.join(DST, f"{name}.webp")
    main.save(main_path, "WEBP", quality=80)
    
    # Thumb 400px
    thumb = img.copy()
    thumb.thumbnail((400, 400), Image.LANCZOS)
    thumb_path = os.path.join(DST, f"{name}_thumb.webp")
    thumb.save(thumb_path, "WEBP", quality=75)
    
    main_sz = os.path.getsize(main_path)
    thumb_sz = os.path.getsize(thumb_path)
    total_dst += main_sz + thumb_sz
    print(f"  {name}.jpg → {name}.webp ({main_sz//1024}KB) + {name}_thumb.webp ({thumb_sz//1024}KB)")

print(f"\nTotal source: {total_src//1024}KB")
print(f"Total output: {total_dst//1024}KB")
print(f"Reduction: {(1 - total_dst/total_src)*100:.1f}%")
print("Done!")
