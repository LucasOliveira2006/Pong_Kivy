from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class mainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(mainGridLayout, self).__init__(**kwargs)

        self.cols = 2
        
        
        self.add_widget(Button(text="button 1"))
        
        self.segundo_layout = GridLayout(cols = 1 )
        
        self.segundo_layout.add_widget(Button(text="button 2"))
        self.segundo_layout.add_widget(Button(text="button 3"))
        self.segundo_layout.add_widget(Button(text="button 4"))
        self.add_widget(self.segundo_layout)
        
class GridLayoutApp(App):
    def build(self):
        return mainGridLayout()
    

if __name__ == "__main__":
    GridLayoutApp().run()