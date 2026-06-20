"""Add Hair Clip link to nav and footer in all retail HTML pages."""
import os

retail_dir = r"C:\Users\14837\Nutstore\1\2\retail"

# Nav: insert Hair Clip link before WhatsApp link
nav_old = '<a href="pet-bib.html">Bib Scarf</a>\n      <a href="https://wa.me/8618271425419"'
nav_new = '<a href="pet-bib.html">Bib Scarf</a>\n      <a href="pet-hairclip.html">Hair Clip</a>\n      <a href="https://wa.me/8618271425419"'

# Nav for pet-bib.html (active class on bib)
nav_old_bib = '<a href="pet-bib.html" class="active">Bib Scarf</a>\n      <a href="https://wa.me/8618271425419"'
nav_new_bib = '<a href="pet-bib.html" class="active">Bib Scarf</a>\n      <a href="pet-hairclip.html">Hair Clip</a>\n      <a href="https://wa.me/8618271425419"'

# Footer: insert Pet Hair Clip after Pet Bib Scarf
footer_old = '<a href="pet-bib.html">Pet Bib Scarf</a>\n    </div>'
footer_new = '<a href="pet-bib.html">Pet Bib Scarf</a>\n      <a href="pet-hairclip.html">Pet Hair Clip</a>\n    </div>'

updated = []
skipped = []

for fname in os.listdir(retail_dir):
    if not fname.endswith('.html'):
        continue
    if fname == 'pet-hairclip.html':
        skipped.append(fname)
        continue
    if fname == 'index.html' or fname == 'refund.html' or fname == 'shipping.html':
        skipped.append(fname)
        continue

    fpath = os.path.join(retail_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Update nav
    if nav_old_bib in content:
        content = content.replace(nav_old_bib, nav_new_bib)
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
