import requests
from bs4 import BeautifulSoup
from slugify import slugify

class ImageSourcingAgent:
    def __init__(self, rules):
        self.rules = rules
        self.base_url = "https://redgiant.co.ke"

    def generate(self, event):
        keyword = event['keyword']

        # Candidate search URL
        search_url = f"{self.base_url}/?s={keyword}"

        candidates = []

        try:
            response = requests.get(search_url, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                for img in soup.find_all('img')[:5]:
                    src = img.get('src')

                    if src and src.startswith('http'):
                        candidates.append(src)

        except Exception as e:
            candidates.append(f"ERROR: {str(e)}")

        filename = self.rules['image_rules']['filename_format'].format(
            city=slugify(event['city']),
            subtype=event['subtype'],
            keyword=slugify(event['keyword']),
            index=1
        )

        alt_text = self.rules['image_rules']['alt_text_format'].format(
            Keyword=event['name'],
            City=event['city'],
            Section='Hero'
        )

        return {
            'search_url': search_url,
            'candidates': candidates,
            'selected_image': candidates[0] if candidates else None,
            'filename': filename,
            'alt_text': alt_text
        }