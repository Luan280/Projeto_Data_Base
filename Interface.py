import customtkinter
from Funções import *


def entrada_cadastro():
    confirmacao = cadastrar(entrada_nome.get(), entrada_email.get())
    if confirmacao:
        msg_confirmacao.configure(text="EMAIl CADASTRADO COM SUCESSO!")
    else:
        msg_confirmacao.configure(text="EMAIL JÁ UTILIZADO")
    entrada_nome.delete(0, "end")
    entrada_email.delete(0, "end")

def entrada_deletar():
    confirmacao = remover(entrada_email.get())
    if confirmacao:
        msg_confirmacao.configure(text="USUÁRIO REMOVIDO COM SUCESSO!")
    else:
        msg_confirmacao.configure(text="USUÁRIO NÃO CADASTRADO")
    entrada_nome.delete(0, "end")
    entrada_email.delete(0, "end")


def janela_consultar():
    texto = consultar()
    for pessoa in texto:
        print(f"ID:{pessoa[0]} NOME: {pessoa[1]} EMAIL: {pessoa[2]}")
    frame_consulta = customtkinter.CTkFrame(janela)
    frame_consulta.pack()
    texto_consulta = customtkinter.CTkLabel(frame_consulta, text=texto)
    texto_consulta.pack()


janela = customtkinter.CTk()
janela.geometry("900x900")
customtkinter.set_default_color_theme("dark-blue")

resposta = ""
entrada_nome = customtkinter.CTkEntry(janela, placeholder_text="NOME", width=600, height=40)
entrada_nome.pack()

entrada_email = customtkinter.CTkEntry(janela, placeholder_text="E-MAIL", width=600, height=40)
entrada_email.pack()

botao_cadastra = customtkinter.CTkButton(janela, text="CADASTRAR", command=entrada_cadastro)
botao_cadastra.pack()

botao_deletar = customtkinter.CTkButton(janela, text="DELETAR", command=entrada_deletar)
botao_deletar.pack()

botao_consultar = customtkinter.CTkButton(janela, text="CONSULTAR", command=janela_consultar)
botao_consultar.pack()

msg_confirmacao = customtkinter.CTkLabel(janela, text=resposta)
msg_confirmacao.pack()
janela.mainloop()
