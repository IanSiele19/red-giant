from slugify import slugify

class ContentSEOAgent:
    def __init__(self, rules):
        self.rules = rules

    def generate(self, event):
        subtype = event['subtype']
        sections = self.rules['page_sections'][subtype]

        slug = f'/{slugify(event["city"])}' \
               f'/{slugify(subtype)}' \
               f'/{slugify(event["keyword"])}'

        seo = {
            'title': f'{event["name"]} | {event["city"]}',
            'meta_description': f'Join {event["name"]} in {event["city"]}.',
            'h1': event['name'],
            'canonical_url': f'https://example.com{slug}'
        }

        html_sections = []

        for section in sections:
            html_sections.append(f'''
<section id="{section}">
  <h2>{section.replace('_', ' ').title()}</h2>
  <p>Content for {section} goes here.</p>
</section>
''')

        html = f'''
<!DOCTYPE html>
<html>
<head>
  <title>{seo['title']}</title>
  <meta name="description" content="{seo['meta_description']}">
  <link rel="canonical" href="{seo['canonical_url']}">
</head>
<body>
  <h1>{seo['h1']}</h1>
  {''.join(html_sections)}
</body>
</html>
'''

        return {
            'slug': slug,
            'seo': seo,
            'html': html,
            'sections': sections
        }