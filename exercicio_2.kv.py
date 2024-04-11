from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainGridLayout(GridLayout):
   pass


class Exercicos2App(App):
    def build(self):
        return MainGridLayout()
    

if __name__ == "__main__":
    Exercicos2App().run()