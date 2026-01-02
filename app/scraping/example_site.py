#app/scraping/example_site.py

from selectolax.parser import HTMLParser
from .base import BaseScraper


class ExampleSiteScraper(BaseScraper):
    def parse(self, html: str):
        tree = HTMLParser(html)
        items = []

        for node in tree.css("a"):
            items.append(node.text())

        return items