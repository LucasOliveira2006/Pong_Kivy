from kivy.app import App
#guarda os elemento de interface
from kivy.uix.label import Label

#Cria o objeto  do App.
class LabelApp(App):
    #Este método é chamado quando o aplicativo é iniciado
    #Deve sempre se chamar build   
    def build(self):
        label = Label()

        return label

#inicia o aplicativo
if __name__ == '__main__':
    LabelApp().run()