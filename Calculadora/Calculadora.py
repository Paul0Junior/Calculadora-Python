# Importando as bibliotecas necessárias:
from tkinter import *
from tkinter import ttk

# Definindo as cores da janela:
cor1 = '#FFFFFF'
cor2 = '#38576B'
cor3 = '#6A5ACD'
cor4 = '#0000FF'
fundo = '#000000'

# Criando a janela para a calculadora:
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.configure(bg=cor1)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_tela = Frame(janela, width=300, height=56, bg=cor3, pady=0, padx=0, relief='flat',)
frame_tela.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340, bg=fundo, pady=0, padx=0, relief='flat',)
frame_quadros.grid(row=2, column=0, sticky=NW)

janela.mainloop()

