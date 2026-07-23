import json
from pathlib import Path
from slugify import slugify

with open('sample_events.json', 'r') as f:
    events = json.load(f)

items = []

for event in events:
    slug = f"/{slugify(event['city'])}/{event['subtype']}/{slugify(event['keyword'])}"
    filename = f"{event['subtype']}-{event['keyword']}.html"

    items.append(f'''
    <li>
      <a href="{filename}">
        {event['name']} ({event['city']})
      </a>
    </li>
    ''')

html = f'''
<!DOCTYPE html>
<html>
<head>
  <title>All Generated Event Pages</title>
</head>
<body>
  <h1>All Generated Event Pages</h1>
  <ul>
    {''.join(items)}
  </ul>
</body>
</html>
'''

Path('outputs').mkdir(exist_ok=True)

with open('outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Generated outputs/index.html')