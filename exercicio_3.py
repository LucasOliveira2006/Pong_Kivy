from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class mainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(mainGridLayout, self).__init__(**kwargs)

        self.cols = 3
        self.add_widget(Button(text="button 1"))
        self.add_widget(GridLayout())
        self.add_widget(Button(text="button 2"))
        self.add_widget(GridLayout())
        self.add_widget(Button(text="button 3"))
        self.add_widget(GridLayout())
        self.add_widget(Button(text="button 4"))
        self.add_widget(GridLayout())
        self.add_widget(Button(text="button 5"))

class GridLayoutApp(App):
    def build(self):
        return mainGridLayout()
    

if __name__ == "__main__":
    GridLayoutApp().run()