"""Add Necklace link to nav and footer in all retail HTML pages."""
import os
import re

retail_dir = r"C:\Users\14837\Nutstore\1\2\retail"

# Nav: insert Necklace link before WhatsApp link
nav_old = '<a href="pet-portrait.html">Portrait</a>\n      <a href="https://wa.me/8618271425419"'
nav_new = '<a href="pet-portrait.html">Portrait</a>\n      <a href="pet-necklace.html">Necklace</a>\n      <a href="https://wa.me/8618271425419"'

# Footer: insert Pearl Pet Collar after Custom Portrait
footer_old = '<a href="pet-portrait.html">Custom Portrait</a>\n    </div>'
footer_new = '<a href="pet-portrait.html">Custom Portrait</a>\n      <a href="pet-necklace.html">Pearl Pet Collar</a>\n    </div>'

# For pet-portrait.html, the nav has class="active" on portrait link
nav_old_portrait = '<a href="pet-portrait.html" class="active">Portrait</a>\n      <a href="https://wa.me/8618271425419"'
nav_new_portrait = '<a href="pet-portrait.html" class="active">Portrait</a>\n      <a href="pet-necklace.html">Necklace</a>\n      <a href="https://wa.me/8618271425419"'

# For pet-necklace.html, skip (already has correct nav)

updated = []
skipped = []

for fname in os.listdir(retail_dir):
    if not fname.endswith('.html'):
        continue
    if fname == 'pet-necklace.html':
        skipped.append(fname)
        continue
    if fname == 'index.html':
        skipped.append(fname)  # Handle separately
        continue

    fpath = os.path.join(retail_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Update nav
    if nav_old_portrait in content:
        content = content.replace(nav_old_portrait, nav_new_portrait)
        changed = True
    elif nav_old in content:
        content = content.replace(nav_old, nav_new)
        changed = True

    # Update footer
    if footer_old in content:
        content = content.replace(footer_old, footer_new)
        changed = True

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append(fname)
    else:
        skipped.append(fname)

print(f"Updated ({len(updated)}): {updated}")
print(f"Skipped ({len(skipped)}): {skipped}")
