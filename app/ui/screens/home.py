from kivymd.uix.screen import MDScreen
from workers.scraper_thread import ScraperWorker


class HomeScreen(MDScreen):
    def start_scrape(self):
        worker = ScraperWorker(self.on_results)
        worker.start()

    def on_results(self, data):
        print("Scraped:", data)
        self.manager.current = "results"