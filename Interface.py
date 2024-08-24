import time

import customtkinter
from Funções import *
from time import sleep
from tkinter import StringVar



def entrada_cadastro():
    confirmacao = cadastrar(entrada_nome.get(), entrada_email.get())
    if confirmacao:
        msg_confirmacao = customtkinter.CTkLabel(janela, textvariable=text_cadastrado)
        msg_confirmacao.pack()
    else:
        msg_confirmacao = customtkinter.CTkLabel(janela, textvariable=text_usado)
        msg_confirmacao.pack()

def trocar_texto(mensagem):
    mensagem.place(x=2000, y=2000)

def entrada_deletar():
    remover(entrada_email.get())


janela = customtkinter.CTk()
janela.geometry("900x900")
customtkinter.set_default_color_theme("dark-blue")

text_cadastrado = StringVar()
text_usado = StringVar()
text_usado.set("EMAIL JÁ UTILIZADO")
text_cadastrado.set("EMAIl CADASTRADO COM SUCESSO!")
entrada_nome = customtkinter.CTkEntry(janela, placeholder_text="NOME", width=600, height=40)
entrada_nome.pack()

entrada_email = customtkinter.CTkEntry(janela, placeholder_text="E-MAIL", width=600, height=40)
entrada_email.pack()

botao_cadastra = customtkinter.CTkButton(janela, text="CADASTRAR", command=entrada_cadastro)
botao_cadastra.pack()

entrada_remover = customtkinter.CTkButton(janela, text="DELETAR", command=entrada_deletar)
entrada_remover.pack()

janela.mainloop()
