from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Exercicio1App(GridLayout):
    pass

class Exercico1(App):
    def build(self):
        return Exercicio1App()
    

if __name__ == "__main__":
    Exercicio1App().run()