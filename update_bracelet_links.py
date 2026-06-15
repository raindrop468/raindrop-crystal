"""Add Bracelet links to all retail product pages' nav and footer."""
import os
import glob

RETAIL_DIR = os.path.join(os.path.dirname(__file__), 'retail')

# Product page files to update (exclude index.html — handled separately)
pages = [
    'classic.html', 'zodiac.html',
    'pet-urn.html', 'pet-keychain.html', 'pet-leather.html',
    'pet-fridge.html', 'pet-plush.html', 'pet-ring.html',
    'pet-patches.html', 'pet-wool-felt.html', 'pet-crystal-lamp.html',
    'pet-puzzle.html', 'pet-rope-toys.html'
]

for page in pages:
    path = os.path.join(RETAIL_DIR, page)
    if not os.path.exists(path):
        print(f'SKIP (not found): {page}')
        continue

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Add Bracelet nav link (before WhatsApp nav-cta)
    # Skip if already has bracelet link
    if 'pet-bracelet.html' not in content:
        nav_cta = '<a href="https://wa.me/8618271425419" target="_blank" rel="noopener" class="nav-cta">'
        bracelet_nav = '      <a href="pet-bracelet.html">Bracelet</a>\n' + nav_cta
        if nav_cta in content:
            content = content.replace(nav_cta, bracelet_nav, 1)
            modified = True
            print(f'NAV: {page}')
        else:
            print(f'WARN: nav-cta not found in {page}')

    # 2. Add Bracelet footer link (before Help section in footer)
    # Look for the pattern: </div> then <div class="footer-col"> with <h4>Help</h4>
    help_pattern = '    </div>\n    <div class="footer-col">\n      <h4>Help</h4>'
    bracelet_footer = '      <a href="pet-bracelet.html">Alloy Bracelet &amp; Necklace</a>\n    </div>\n    <div class="footer-col">\n      <h4>Help</h4>'
    if help_pattern in content:
        content = content.replace(help_pattern, bracelet_footer)
        modified = True
        print(f'FOOTER: {page}')
    else:
        # Try alternative pattern (maybe formatting differs)
        if '<h4>Help</h4>' in content and 'Alloy Bracelet' not in content:
            print(f'WARN: Help section found but pattern mismatch in {page}')

    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'OK: {page}')
    else:
        print(f'SKIP (already updated): {page}')

print('\nDone!')
