import yaml
from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict

# Load rules
with open('agent-rules/layer0-rules.yaml', 'r') as f:
    rules = yaml.safe_load(f)

outputs = Path('outputs')
html_files = list(outputs.glob('*.html'))

print('\\n===== QA REPORT =====\\n')

orphan_pages = []
link_targets = set()

for file in html_files:
    soup = BeautifulSoup(file.read_text(encoding='utf-8'), 'html.parser')

    subtype = file.name.split('-')[0]

    # Collect links
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    link_targets.update(links)

    # Check required sections
    expected_sections = rules['page_sections'][subtype]

    missing = []

    for section in expected_sections:
        if soup.find(id=section) is None:
            missing.append(section)

    # Check SEO tags
    title_ok = soup.title is not None
    meta_ok = soup.find('meta', attrs={'name': 'description'}) is not None
    canonical_ok = soup.find('link', attrs={'rel': 'canonical'}) is not None

    print(f'{file.name}')
    print(f'  Title tag      : {title_ok}')
    print(f'  Meta desc      : {meta_ok}')
    print(f'  Canonical      : {canonical_ok}')
    print(f'  Missing sections: {missing if missing else "None"}\\n')

# Orphan check
for file in html_files:
    slug = '/' + file.stem.replace('-', '/')
    if slug not in link_targets:
        orphan_pages.append(file.name)

print('===== ORPHAN PAGE CHECK =====')

if orphan_pages:
    print('Potential orphans:')
    for p in orphan_pages:
        print(f'  - {p}')
else:
    print('No orphan pages detected')

print(f'\\nTotal pages checked: {len(html_files)}')