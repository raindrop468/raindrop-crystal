#!/usr/bin/env python3
"""
Raindrop Crystal - 买家秀图片处理脚本
功能：
1. 裁剪底部小红书水印（裁剪底部8%区域）
2. 转换为WebP格式
3. 生成主图(1200px宽, 80%质量)和缩略图(400px宽, 75%质量)
"""

import os
from PIL import Image

INPUT_DIR = "C:/Users/Administrator/Desktop/2/买家秀"
OUTPUT_DIR = "C:/Users/Administrator/Desktop/2/images/reviews"

# 创建输出目录
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 处理所有jpg文件
files = sorted([f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.jpg')],
               key=lambda x: int(os.path.splitext(x)[0]))

print(f"找到 {len(files)} 张图片待处理...")

processed = 0
for filename in files:
    input_path = os.path.join(INPUT_DIR, filename)
    basename = os.path.splitext(filename)[0]

    try:
        with Image.open(input_path) as img:
            # 转换为RGB模式（处理RGBA等）
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            # 1. 裁剪底部8%去除水印
            w, h = img.size
            crop_h = int(h * 0.92)  # 保留顶部92%
            img_cropped = img.crop((0, 0, w, crop_h))

            # 2. 生成主图 (1200px宽, 80%质量)
            main_w = 1200
            ratio = main_w / img_cropped.width
            main_h = int(img_cropped.height * ratio)
            main_img = img_cropped.resize((main_w, main_h), Image.LANCZOS)

            main_path = os.path.join(OUTPUT_DIR, f"{basename}.webp")
            main_img.save(main_path, 'WEBP', quality=80, method=6)

            # 3. 生成缩略图 (400px宽, 75%质量)
            thumb_w = 400
            ratio = thumb_w / img_cropped.width
            thumb_h = int(img_cropped.height * ratio)
            thumb_img = img_cropped.resize((thumb_w, thumb_h), Image.LANCZOS)

            thumb_path = os.path.join(OUTPUT_DIR, f"{basename}_thumb.webp")
            thumb_img.save(thumb_path, 'WEBP', quality=75, method=6)

            # 4. 计算压缩率
            orig_size = os.path.getsize(input_path)
            new_size = os.path.getsize(main_path) + os.path.getsize(thumb_path)

            print(f"  ✓ {filename}: {img.size[0]}x{img.size[1]} → 主图{main_w}x{main_h} + 缩略图{thumb_w}x{thumb_h} (节省 {orig_size - os.path.getsize(main_path):,} bytes)")
            processed += 1

    except Exception as e:
        print(f"  ✗ {filename} 处理失败: {e}")

print(f"\n处理完成: {processed}/{len(files)} 张图片")
print(f"输出目录: {OUTPUT_DIR}")
