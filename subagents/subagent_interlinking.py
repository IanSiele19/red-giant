from slugify import slugify

class InterlinkingAgent:
    def __init__(self, rules):
        self.rules = rules

    def generate(self, event, all_events):
        current_slug = f"/{slugify(event['city'])}/{event['subtype']}/{slugify(event['keyword'])}"

        related = []

        for other in all_events:
            if other['keyword'] == event['keyword']:
                continue

            # Same city or same subtype
            if other['city'] == event['city'] or other['subtype'] == event['subtype']:
                related.append({
                    'name': other['name'],
                    'slug': f"/{slugify(other['city'])}/{other['subtype']}/{slugify(other['keyword'])}"
                })

        related = related[:3]

        breadcrumbs = [
            {'label': 'Home', 'url': '/'},
            {'label': event['city'], 'url': f"/{slugify(event['city'])}"},
            {'label': event['subtype'].title(), 'url': f"/{slugify(event['city'])}/{event['subtype']}"},
            {'label': event['name'], 'url': current_slug}
        ]

        aio = {
            'faq_schema': True,
            'event_schema': True,
            'breadcrumb_schema': True,
            'recommended_entities': [event['city'], event['name']]
        }

        return {
            'breadcrumbs': breadcrumbs,
            'related_links': related,
            'aio': aio
        }