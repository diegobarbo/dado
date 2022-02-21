# simulador de dado
# simular o uso de um dado gerando um valor de 1 até 6

import random
from PySimpleGUI import PySimpleGUI as sg

class Simulador_de_Dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        
        # layout
        
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]


    def iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        #fazer alguma coisa com esses valores
        
        
        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.gerar_valor_do_dado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Ok. Até a próxima.')
            else:
                print('Favor digitar sim ou nao.')
        except:
            print('Ocorreu um erro ao receber sua resposta.')


    def gerar_valor_do_dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = Simulador_de_Dado()
simulador.iniciar()
