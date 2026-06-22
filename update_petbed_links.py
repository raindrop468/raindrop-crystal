#!/usr/bin/env python3
"""Add Pet Bed link to nav and footer of all retail HTML pages."""
import os
import re

RETAIL_DIR = r"C:\Users\14837\Nutstore\1\2\retail"

# Pages to update (exclude pet-bed.html itself, index.html handled separately)
pages = []
for f in os.listdir(RETAIL_DIR):
    if f.endswith('.html') and f not in ('pet-bed.html', 'index.html', 'shipping.html', 'refund.html'):
        pages.append(os.path.join(RETAIL_DIR, f))

nav_old = '<a href="pet-rug.html">Pet Rug</a>'
nav_new = '<a href="pet-rug.html">Pet Rug</a>\n      <a href="pet-bed.html">Pet Bed</a>'

footer_old = '<a href="pet-rug.html">Custom Pet Rug</a>'
footer_new = '<a href="pet-rug.html">Custom Pet Rug</a>\n      <a href="pet-bed.html">Waterproof Pet Bed</a>'

for page_path in pages:
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Add to nav (before WhatsApp CTA)
    if nav_old in content and 'pet-bed.html' not in content:
        content = content.replace(nav_old, nav_new)
        changed = True

    # Add to footer
    if footer_old in content and 'pet-bed.html">Waterproof Pet Bed' not in content:
        content = content.replace(footer_old, footer_new)
        changed = True

    if changed:
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {os.path.basename(page_path)}")
    else:
        print(f"Skipped (no match): {os.path.basename(page_path)}")

print("\nDone!")
