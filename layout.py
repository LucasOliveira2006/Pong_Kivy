from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#Altera a cor do background
from kivy.core.window import Window
Window.clearcolor = (120, 200 , 55)


class MainLayout(App):
    def __init__(self, **kwargs):
        super(MainLayout, self ).__init__(**kwargs)
        #Definindo o layout da aplicação
        self.cols = 2 

        self.sub_layout = GridLayout()
        self.sub_layout.cols = 2

        ######################################################
        #Cria a Label Nome
        self.nome_label = Label(text= 'Nome: ')
        #Adiciona a label Nome ao layout
        self.add_widget(self.nome_label)
        #criando o textimput Nome
        self.nome_do_cliente = TextInput(multiline=False)
        #adiciona o TextImput ao layout
        self.sub_layout.add_widget(self.nome_label)
        ######################################################
        #Cria a Label mesa
        self.mesa_label = Label(text= 'Mesa: ')
        #Adiciona a label Mesa ao layout
        self.add_widget(self.mesa_label)
        #criando o TextImput Mesa
        self.numero_da_mesa = TextInput(multiline=False)
        #adiciona o TextImput Mesa ao layout
        self.sub_layout.dd_widget(self.nome_label)
        ######################################################
        #Cria a Label pedido
        self.pedido_label = Label(text= 'pedido: ')
        #Adiciona a label pedido ao layout
        self.add_widget(self.mese_label)
        #criando o TextImput pedido
        self.Pedido_do_cliente = TextInput(multiline=True)
        #adiciona o TextImput Mesa ao layout
        self.sub_layout.add_widget(self.pedido_label)

        #######################################################

        #cria o botão enviar
        self.enviar = Button(text='Enviar perdido')
        #Adiciona a função callback ao botão
        self.enviar.bind(on_press=self.enviar_pedido)
        #adiciona o botão enviar ao layout
        self.add.widget(self.enviar)
    
    def enviar_pedido(self, instance):
        #criando o Label de confirmação
        self.confimacao = Label(
            text=f'cliente'(self.nome_do_cliente.text)
            (self.Mesa.text)
            (self.Pedido.text)
            )
        
        #Limpando os campos de texto
        self.nome_do_cliente.text = ''
        self.mesa.text = ''
        self.pedido.text = ''




class LanchoneteApp(App):
    def build(self):
        return MainLayout
        


if __name__ == '__main__':
    LanchoneteApp.run()