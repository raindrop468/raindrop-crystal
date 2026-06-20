#!/usr/bin/env python3
"""Add Pet Rug link to nav and footer in all retail HTML pages."""
import os
import re
from pathlib import Path

retail_dir = Path(r"C:\Users\14837\Nutstore\1\2\retail")
exclude = {"index.html", "shipping.html", "refund.html", "pet-rug.html"}

# Nav: add before WhatsApp link
nav_old = '<a href="pet-hairclip.html">Hair Clip</a>'
nav_new = '<a href="pet-hairclip.html">Hair Clip</a>\n      <a href="pet-rug.html">Pet Rug</a>'

# Footer: add after Pet Hair Clip link
footer_old = '<a href="pet-hairclip.html">Pet Hair Clip</a>'
footer_new = '<a href="pet-hairclip.html">Pet Hair Clip</a>\n      <a href="pet-rug.html">Custom Pet Rug</a>'

count = 0
for html_file in sorted(retail_dir.glob("*.html")):
    if html_file.name in exclude:
        continue
    
    content = html_file.read_text(encoding="utf-8")
    changed = False
    
    # Update nav
    if nav_old in content and 'href="pet-rug.html">Pet Rug' not in content:
        content = content.replace(nav_old, nav_new)
        changed = True
    
    # Update footer
    if footer_old in content and 'href="pet-rug.html">Custom Pet Rug' not in content:
        content = content.replace(footer_old, footer_new)
        changed = True
    
    if changed:
        html_file.write_text(content, encoding="utf-8")
        print(f"  Updated: {html_file.name}")
        count += 1
    else:
        print(f"  Skipped (no change needed): {html_file.name}")

print(f"\nDone! {count} files updated.")
