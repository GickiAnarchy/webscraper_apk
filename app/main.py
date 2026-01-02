#app/main.py

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from ui.screens.home import HomeScreen
from ui.screens.results import ResultsScreen
from ui.screens.settings import SettingsScreen


class WebScraperApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        Builder.load_file("app.kv")

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ResultsScreen(name="results"))
        sm.add_widget(SettingsScreen(name="settings"))
        return sm


if __name__ == "__main__":
    WebScraperApp().run()