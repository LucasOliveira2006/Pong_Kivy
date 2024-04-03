from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class mainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(mainGridLayout, self).__init__(**kwargs)

        self.cols = 2
        self.spacing = 10
        self.padding = 30

        self.add_widget(Button(text="Main GridLayout 1"))
        self.segundo_layout = GridLayout(cols = 1, spacing = 10)
        
        self.segundo_layout.add_widget(Button(text="Second GridLayout 1"))
        self.segundo_layout.add_widget(Button(text="Second GridLayout 2"))
        self.segundo_layout.add_widget(Button(text="Second GridLayout 3"))
        
        self.add_widget(self.segundo_layout)

        self.add_widget(Button(text="Main GridLayout 2"))
        self.add_widget(Button(text="Main GridLayout 3"))
        self.add_widget(Button(text="Main GridLayout 4"))
        self.add_widget(Button(text="Main GridLayout 5"))
        self.add_widget(Button(text="Main GridLayout 6"))
        self.add_widget(Button(text="Main GridLayout 7"))



class GridLayoutApp(App):
    def build(self):
        return mainGridLayout()
    

if __name__ == "__main__":
    GridLayoutApp().run()