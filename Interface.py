from PIL import Image
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
    conteudo = consultar()
    texto_consulta.configure(text=conteudo)

# Configuração da interface
janela = customtkinter.CTk()
janela.title("CRUD MYSQL")
janela.geometry("1920x1080")
customtkinter.set_default_color_theme("dark-blue")

msg_consulta= " "
resposta = " "

# Imagens
icone_usuario = customtkinter.CTkImage(dark_image=Image.open("imagens/icone.png"), size=(40,40))
icone_email = customtkinter.CTkImage(dark_image=Image.open("imagens/email.png"), size=(40,40))

frame_principal = customtkinter.CTkFrame(janela,fg_color="white",width=900, height=1010)
frame_principal.place(x=950,y=1)

# Frame que mostra todos os usuários
frame_consulta = customtkinter.CTkScrollableFrame(janela, fg_color="#AFBF9F", width=800, height=1010)
frame_consulta.place(x=0 ,y=0)

# Caixa de entrada do Nome
entrada_nome = customtkinter.CTkEntry(frame_principal, placeholder_text="NOME", width=600, height=40,corner_radius=10,
                                      border_color="#67735C", fg_color="#D9D9D9", text_color="#262626")
entrada_nome.place(x=160,y=400)

imagem_icone = customtkinter.CTkLabel(frame_principal, image=icone_usuario, text="")
imagem_icone.place(x=160 ,y=350)

# Caixa de entrada do Email
entrada_email = customtkinter.CTkEntry(frame_principal, placeholder_text="E-MAIL", width=600, height=40,corner_radius=10,
                                      border_color="#67735C", fg_color="#D9D9D9", text_color="#262626")
entrada_email.place(x=160 ,y=550)

imagem_email = customtkinter.CTkLabel(frame_principal, image=icone_email, text="")
imagem_email.place(x=160 ,y=500)

# Botão que cadastra o usuário
botao_cadastra = customtkinter.CTkButton(frame_principal, text="CADASTRAR", command=entrada_cadastro,
                                         width=320,height=60, corner_radius=20,
                                         fg_color="#AFBF9F", hover_color="#E9F2C9",text_color="#262626")
botao_cadastra.place(x=290 ,y=620)

# Botão que deleta um usuário
botao_deletar = customtkinter.CTkButton(frame_principal, text="DELETAR", command=entrada_deletar, width=320,height=60,
                                        corner_radius=20,fg_color="#AFBF9F", hover_color="#E9F2C9",text_color="#262626")
botao_deletar.place(x=290,y=700)

# Botão que consulta todos os usuário
botao_consultar = customtkinter.CTkButton(frame_principal, text="CONSULTAR", command=entrada_consultar, width=320,
                                          height=60, corner_radius=20,fg_color="#AFBF9F",
                                          hover_color="#E9F2C9",text_color="#262626")
botao_consultar.place(x=290,y=780)

texto_principal = customtkinter.CTkLabel(frame_principal, text="CRUD", text_color="#67735C", font=("arial", 100))
texto_principal.place(x=200 ,y=100)

# Texto que valida se o usuário foi cadastrado e se o email já está cadastrado
texto_confirmacao = customtkinter.CTkLabel(frame_principal, text=resposta, font=('arial', 30), text_color="#262626")
texto_confirmacao.place(x=160 ,y=250)

# Texto que mostra todas os usuários cadastrados
texto_consulta = customtkinter.CTkLabel(frame_consulta, text=msg_consulta, text_color="white", font=("arial", 15))
texto_consulta.pack()


texto_usuario = customtkinter.CTkLabel(frame_principal, text="USUÁRIO", text_color="#67735C", font=("arial", 40))
texto_usuario.place(x=225 ,y=350)

texto_email = customtkinter.CTkLabel(frame_principal, text="E-MAIL", text_color="#67735C", font=("arial", 40))
texto_email.place(x=225 ,y=500)


janela.mainloop()
