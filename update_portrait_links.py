import os
import re

retail_dir = r'C:\Users\14837\Nutstore\1\2\retail'

# Files to update (all .html files except the new one)
html_files = [f for f in os.listdir(retail_dir) if f.endswith('.html') and f != 'pet-portrait.html']

nav_insert = '      <a href="pet-portrait.html">Portrait</a>\n'
footer_insert = '      <a href="pet-portrait.html">Custom Portrait</a>\n'

for fname in html_files:
    fpath = os.path.join(retail_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Add Portrait link in nav: after the Pillow link
    # Pattern: <a href="pet-bolster.html">Pillow</a>
    content = content.replace(
        '<a href="pet-bolster.html">Pillow</a>\n',
        '<a href="pet-bolster.html">Pillow</a>\n' + nav_insert
    )

    # 2. Add Custom Portrait link in footer Collections
    # Pattern: <a href="pet-bolster.html">Custom Pet Pillow</a>
    # Insert before the closing </div> of Collections column
    # Find the Collections section and add before the closing </div>
    if 'Custom Pet Pillow</a>' in content and 'Custom Portrait</a>' not in content:
        content = content.replace(
            '<a href="pet-bolster.html">Custom Pet Pillow</a>\n',
            '<a href="pet-bolster.html">Custom Pet Pillow</a>\n' + footer_insert
        )

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {fname}')
    else:
        print(f'Skipped (no match): {fname}')

print('Done!')
