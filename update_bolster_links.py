"""Add pet-bolster.html links to all product pages' nav and footer"""
import os, glob

RETAIL = r"C:\Users\Administrator\Desktop\2\retail"

# All product pages to update (NOT pet-bolster.html itself)
files = glob.glob(os.path.join(RETAIL, "*.html"))
files = [f for f in files if os.path.basename(f) != 'pet-bolster.html']

NAV_INSERT = '<a href="pet-bolster.html">Pillow</a>\n'
FOOTER_INSERT = '<a href="pet-bolster.html">Custom Pet Pillow</a>\n'

for fpath in sorted(files):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Add nav link after bracelet
    if 'href="pet-bracelet.html"' in content:
        content = content.replace(
            '<a href="pet-bracelet.html">Bracelet</a>',
            '<a href="pet-bracelet.html">Bracelet</a>\n      ' + NAV_INSERT.strip()
        )
    
    # Add footer link after bracelet in footer
    footer_marker = '<a href="pet-bracelet.html">Alloy Bracelet &amp; Necklace</a>'
    if footer_marker in content:
        content = content.replace(
            footer_marker,
            footer_marker + '\n      ' + FOOTER_INSERT.strip()
        )
    else:
        # Try without &amp;
        footer_marker2 = '<a href="pet-bracelet.html">Alloy Bracelet & Necklace</a>'
        if footer_marker2 in content:
            content = content.replace(
                footer_marker2,
                footer_marker2 + '\n      ' + FOOTER_INSERT.strip()
            )
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  OK: {fname}")
    else:
        print(f"  SKIP: {fname} (no changes)")

print("\nDone!")
