from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

class mainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(mainGridLayout, self).__init__(**kwargs)

class GridLayoutApp(App):
    def build(self):
        return Widget()
    

if __name__ == "__main__":
    GridLayoutApp().run()