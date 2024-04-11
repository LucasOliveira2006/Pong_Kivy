from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class mainGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(mainGridLayout, self).__init__(**kwargs)
        #Denine o numero de colunas
        self.cols = 2
        #Define o espaçamento entre os widgets
        self.spacing = 10
        #Define o9 padding do GridLayout
        self.padding = 30
        #define altura padrao das linhas(como se fosse a altura mínima)
        self.row_default_height = 100
        #Define a largura padrão das linhas(como se fosse a largura mínima)
        self.col_default_width = 200
        # Força a altura padrão das linhas
        self.row_force_default = True
        # Força a largura padrão das linhas
        self.col_force_default =True

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