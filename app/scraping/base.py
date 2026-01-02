#app/scraping/base.py

import httpx

class BaseScraper:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    def fetch(self, url: str) -> str:
        with httpx.Client(headers=self.headers, timeout=15) as client:
            response = client.get(url)
            response.raise_for_status()
            return response.text

    def parse(self, html: str):
        raise NotImplementedError

    def scrape(self, url: str):
        html = self.fetch(url)
        return self.parse(html)