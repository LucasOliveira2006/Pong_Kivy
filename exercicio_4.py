from kivy.app import App
from kivy.uix.widget import Widget
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

        self.terceiro_layout = GridLayout(cols = 2, rows = 2 )
        
        self.terceiro_layout.add_widget(Button(text="button 5"))
        self.terceiro_layout.add_widget(Button(text="button 6"))
        self.terceiro_layout.add_widget(Button(text="button 7"))
        self.terceiro_layout.add_widget(Button(text="button 8"))
        self.add_widget(self.terceiro_layout)

        self.terceiro_layout = GridLayout(cols = 3)
        
        self.terceiro_layout.add_widget(Button(text="button 9"))
        self.terceiro_layout.add_widget(Button(text="button 10"))
        self.terceiro_layout.add_widget(Button(text="button 11"))
        
        self.add_widget(self.terceiro_layout)


class GridLayoutApp(App):
    def build(self):
        return mainGridLayout()
    

if __name__ == "__main__":
    GridLayoutApp().run()