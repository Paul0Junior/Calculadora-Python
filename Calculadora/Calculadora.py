# Importando as bibliotecas necessárias:
from tkinter import *
from tkinter import ttk

# Definindo as cores da janela:
cor1 = '#3B3B3B'
cor2 = '#FeFFFF'
cor3 = '#38576b'
cor4 = '#ECEFF1'
cor5 = '#FFAB40'


# Criando a janela para a calculadora:
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config(bg=cor1)

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


# Criando botões

b_1 = Button(frame_corpo, text='C', width=11, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text='%', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, text='/', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, text='7', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=53)
b_5 = Button(frame_corpo, text='8', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=53)
b_6 = Button(frame_corpo, text='9', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=53)
b_7 = Button(frame_corpo, text='*', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=53)

b_8 = Button(frame_corpo, text='4', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=106)
b_9 = Button(frame_corpo, text='5', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=106)
b_10 = Button(frame_corpo, text='6', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=106)
b_11 = Button(frame_corpo, text='-', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=106)

b_12 = Button(frame_corpo, text='1', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=160)
b_13 = Button(frame_corpo, text='2', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=160)
b_14 = Button(frame_corpo, text='3', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=160)
b_15 = Button(frame_corpo, text='+', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=160)

b_1 = Button(frame_corpo, text='0', width=11, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=212)
b_2 = Button(frame_corpo, text='.', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=212)
b_3 = Button(frame_corpo, text='=', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=212)

janela.mainloop()

