import customtkinter
from Funções import *

def entrada_cadastro():
    confirmacao = cadastrar(entrada_nome.get(), entrada_email.get())
    if confirmacao:
        texto_confirmacao.configure(text="EMAIl CADASTRADO COM SUCESSO!")
    else:
        texto_confirmacao.configure(text="EMAIL JÁ UTILIZADO")
    entrada_nome.delete(0, "end")
    entrada_email.delete(0, "end")

def entrada_deletar():
    confirmacao = remover(entrada_email.get())
    if confirmacao:
        texto_confirmacao.configure(text="USUÁRIO REMOVIDO COM SUCESSO!")
    else:
        texto_confirmacao.configure(text="USUÁRIO NÃO CADASTRADO")
    entrada_nome.delete(0, "end")
    entrada_email.delete(0, "end")


def entrada_consultar():
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
    texto_consulta.configure(text=conteudo)

# Configuração da interface
janela = customtkinter.CTk()
janela.geometry("900x900")
customtkinter.set_default_color_theme("dark-blue")

msg_consulta=""
resposta = ""

# Caixa de entrada do Nome
entrada_nome = customtkinter.CTkEntry(janela, placeholder_text="NOME", width=600, height=40)
entrada_nome.pack()

# Caixa de entrada do Email
entrada_email = customtkinter.CTkEntry(janela, placeholder_text="E-MAIL", width=600, height=40)
entrada_email.pack()

# Botão que cadastra o usuário
botao_cadastra = customtkinter.CTkButton(janela, text="CADASTRAR", command=entrada_cadastro)
botao_cadastra.pack()

# Botão que deleta um usuário
botao_deletar = customtkinter.CTkButton(janela, text="DELETAR", command=entrada_deletar)
botao_deletar.pack()

# Botão que consulta todos os usuário
botao_consultar = customtkinter.CTkButton(janela, text="CONSULTAR", command=entrada_consultar)
botao_consultar.pack()

# Texto que valida se o usuário foi cadastrado, se o email já existe e se foi deletado com sucesso
texto_confirmacao = customtkinter.CTkLabel(janela, text=resposta)
texto_confirmacao.pack()

# Frame que mostra todos os usuários
frame_consulta = customtkinter.CTkFrame(janela)
frame_consulta.pack()

# Texto que mostra todas os usuários cadastrados
texto_consulta = customtkinter.CTkLabel(frame_consulta, text=msg_consulta)
texto_consulta.pack()

janela.mainloop()
