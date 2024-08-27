from tkinter import *
import random


ppt = ['pedra', 'papel', 'tesoura']
res = 'JOGAR'

root = Tk()
root.geometry('800x600')
root.title('ROCK - PAPER - SCISSORS')

frame_texto = Frame(root)
frame_texto.pack(side=BOTTOM)
frame_texto.place(height=100, width=200, x=300, y=300)

# Creias 1 vez a label
texto = Label(frame_texto, text= res, fg='red', font=('Times New Roman', 40))
texto.pack()

# Aqui só modificas o texto da Label texto
def res_texto(res):
    texto.config(text=res)

def jogar_pedra(event):
    x = random.choice(ppt)
    if x == 'pedra':
        res = 'EMPATE'
        res_texto(res)
    elif x == 'papel':
        res = 'PERDEU'
        res_texto(res)
    elif x == 'tesoura':
        res = 'GANHOU'
        res_texto(res)

def jogar_papel(event):
    x = random.choice(ppt)
    if x == 'pedra':
        res = 'GANHOU'
        res_texto(res)
    elif x == 'papel':
        res = 'EMPATE'
        res_texto(res)
    elif x == 'tesoura':
        res = 'PERDEU'
        res_texto(res)

def jogar_tesoura(event):
    x = random.choice(ppt)
    if x == 'pedra':
        res = 'PERDEU'
        res_texto(res)
    elif x == 'papel':
        res = 'GANHOU'
        res_texto(res)
    elif x == 'tesoura':
        res = 'EMPATE'
        res_texto(res)


instrucoes = Label(root, text='Escolha pedra, papel ou tesoura', font = ('Times New Roman', 20), fg='black')
instrucoes.pack()

pedra = Button(root, text='Pedra', font=(30))
pedra.bind('<Button-1>', jogar_pedra)
pedra.pack()
pedra.place(x=250, y=100)

papel = Button(root, text='Papel', font=(30))
papel.bind('<Button-1>', jogar_papel)
papel.pack()
papel.place(x= 350, y=100)

tesoura = Button(root, text='Tesoura', font=(30))
tesoura.bind('<Button-1>', jogar_tesoura)
tesoura.pack()
tesoura.place(x=450, y=100)

root.mainloop()