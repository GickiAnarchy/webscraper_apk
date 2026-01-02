from threading import Thread
from kivy.clock import Clock
from scraping.example_site import ExampleSiteScraper


class ScraperWorker(Thread):
    def __init__(self, callback):
        super().__init__(daemon=True)
        self.callback = callback

    def run(self):
        scraper = ExampleSiteScraper()
        data = scraper.scrape("https://example.com")
        Clock.schedule_once(lambda dt: self.callback(data))