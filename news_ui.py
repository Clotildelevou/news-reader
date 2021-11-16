from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("button_image.kv")


class SearchButton(Widget):

    def launch_search(self):
        self.ids.search_button.text = "Searched !"
        self.ids.loupe_img.source = "img/loupe-pressed.png"

    def reset(self):
        self.ids.search_button.text = "Search ?"
        self.ids.loupe_img.source = 'img/loupe.png'


class NewsApp(App):
    def build(self):
        return SearchButton()
