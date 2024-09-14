import customtkinter
from PIL import Image
from Funções import *

def entrada_cadastro():
    try:
        encontrado = cadastrar(entrada_nome.get(), entrada_email.get())
    except Exception as banco_dados:
        texto_confirmacao.configure(text=f"ERRO: {banco_dados}", text_color="RED")
        texto_confirmacao.place(x=150 ,y=250)
    else:
        if encontrado == 1:
            texto_confirmacao.configure(text="*DIGITE O NOME E O EMAIL", text_color="RED")
        elif encontrado == 2:
            texto_confirmacao.configure(text="EMAIL JÁ UTILIZADO", text_color="#262626")
        else:
            texto_confirmacao.configure(text="EMAIl CADASTRADO COM SUCESSO", text_color="#262626")
        # Deleta o texto que está na entrada de dados
        entrada_nome.delete(0, "end")
        entrada_email.delete(0, 'end')

def entrada_deletar():
    try:
        confirmacao = remover(entrada_nome.get(), entrada_email.get())
    except ValueError:
        texto_confirmacao.configure(text="DIGITE O E-MAIL OU ID DO USUÁRIO")
    except Exception as banco_dados:
        texto_confirmacao.configure(text=f"ERRO: {banco_dados}", text_color="RED")
        texto_confirmacao.place(x=150 ,y=250)
    else:
        if confirmacao == 1:
            texto_confirmacao.configure(text="*DIGITE O EMAIL OU ID DO USUÁRIO", text_color="RED")
        elif confirmacao:
            texto_confirmacao.configure(text="USUÁRIO REMOVIDO COM SUCESSO!")
        else:
            texto_confirmacao.configure(text="USUÁRIO NÃO CADASTRADO")
        # Deleta o texto que está na entrada de dados
        entrada_nome.delete(0, "end")
        entrada_email.delete(0, "end")


def entrada_consultar():
    try:
        conteudo = consultar()
    except Exception as banco_dados:
        texto_confirmacao.configure(text=f"ERRO: {banco_dados}", text_color="RED")
        texto_confirmacao.place(x=150 ,y=250)
    else:
        texto_consulta.configure(text=conteudo)
        frame_consulta.place(x=50, y=25)

def entrada_frame_atualizar():
    frame_atualizar.place(x=50, y=25)


def entrada_atualizar():
    try:
        confirmacao = atualizar(id_atualizar.get(), nome_atualizar.get(), email_atualizar.get())
    except Exception as banco_dados:
        texto_confirmacao_atualizar.configure(text=f"ERRO: {banco_dados}", text_color="RED")
        texto_confirmacao_atualizar.place(x=80, y=200)
    else:
        if confirmacao == 1:
            texto_confirmacao_atualizar.configure(text="DIGITAR O ID É OBRIGATÓRIO")
        elif confirmacao == 2:
            texto_confirmacao_atualizar.configure(text="ID NÃO ESTÁ CADASTRADO NO SISTEMA")
        elif confirmacao == 3:
            texto_confirmacao_atualizar.configure(text="NOME OU E-MAIL NÃO FORAM DIGITADOS")
        elif confirmacao == 4:
            texto_confirmacao_atualizar.configure(text="DADOS ATUALIZADOS COM SUCESSO ")
        id_atualizar.delete(0, "end")
        nome_atualizar.delete(0, "end")
        email_atualizar.delete(0, "end")


def fechar_frame():
    frame_consulta.place(x=2000, y=2000)

def fechar_frame_atualizar():
    frame_atualizar.place(x=2000, y=2000)

# Configuração da interface janela
janela = customtkinter.CTk()
janela.title("CRUD MYSQL")
janela.geometry("1920x1080")
customtkinter.set_default_color_theme("dark-blue")
resposta = " "
msg_consulta = " "

# Imagens
icone_usuario = customtkinter.CTkImage(dark_image=Image.open("imagens/icon_user.png"), size=(35,35))
icone_email = customtkinter.CTkImage(dark_image=Image.open("imagens/icon_email.webp"), size=(40,40))
icone_fechar = customtkinter.CTkImage(dark_image=Image.open("imagens/x_fechar.png"))

frame_principal = customtkinter.CTkFrame(janela,fg_color="white",width=1055, height=1010)
frame_principal.place(x=800,y=1)

# Frame que mostra todos os usuários
frame_consulta = customtkinter.CTkScrollableFrame(janela, fg_color="#AFBF9F", width=650, height=850, corner_radius=50)

# Frame que atualiza os dados dos usuários
frame_atualizar = customtkinter.CTkFrame(janela, fg_color="white", width=700, height=950, corner_radius=50)

# Frame princípal

# Caixa de entrada do Nome
entrada_nome = customtkinter.CTkEntry(frame_principal, placeholder_text="NOME", width=600, height=40,corner_radius=10,
                                      border_color="#67735C", fg_color="#D9D9D9", text_color="#262626")
entrada_nome.place(x=220,y=400)

imagem_icone = customtkinter.CTkLabel(frame_principal, image=icone_usuario, text="")
imagem_icone.place(x=230 ,y=355)

# Caixa de entrada do Email
entrada_email = customtkinter.CTkEntry(frame_principal, placeholder_text="E-MAIL", width=600, height=40,corner_radius=10,
                                      border_color="#67735C", fg_color="#D9D9D9", text_color="#262626")
entrada_email.place(x=220 ,y=550)

imagem_email = customtkinter.CTkLabel(frame_principal, image=icone_email, text="")
imagem_email.place(x=230 ,y=505)

# Botão que cadastra o usuário
botao_cadastra = customtkinter.CTkButton(frame_principal, text="CADASTRAR", command=entrada_cadastro,
                                         width=320,height=60, corner_radius=20,
                                         fg_color="#AFBF9F", hover_color="#E9F2C9",text_color="#262626")
botao_cadastra.place(x=350 ,y=620)

# Botão que consulta todos os usuário
botao_consultar = customtkinter.CTkButton(frame_principal, text="CONSULTAR", command=entrada_consultar, width=320,
                                          height=60, corner_radius=20,fg_color="#AFBF9F",
                                          hover_color="#E9F2C9",text_color="#262626")
botao_consultar.place(x=350,y=700)

# Botão que abre o frame de atualizar dados
botao_atualizar = customtkinter.CTkButton(frame_principal, text="ATUALIZAR", command=entrada_frame_atualizar, width=320,
                                          height=60, corner_radius=20, fg_color="#AFBF9F",
                                          hover_color="#E9F2C9", text_color="#262626")
botao_atualizar.place(x=350,y=780)

# Botão que deleta um usuário
botao_deletar = customtkinter.CTkButton(frame_principal, text="DELETAR", command=entrada_deletar, width=320,height=60,
                                        corner_radius=20,fg_color="#AFBF9F", hover_color="#E9F2C9",text_color="#262626")
botao_deletar.place(x=350,y=860)

texto_principal = customtkinter.CTkLabel(frame_principal, text="CRUD", text_color="#67735C", font=("arial", 100))
texto_principal.place(x=370 ,y=100)

# Texto que valida se o usuário foi cadastrado e se o email já está cadastrado
texto_confirmacao = customtkinter.CTkLabel(frame_principal, text=resposta, font=('arial', 30), text_color="#262626")
texto_confirmacao.place(x=280 ,y=250)

texto_usuario = customtkinter.CTkLabel(frame_principal, text="USUÁRIO:", text_color="#67735C", font=("arial", 40))
texto_usuario.place(x=280 ,y=350)

texto_email = customtkinter.CTkLabel(frame_principal, text="E-MAIL:", text_color="#67735C", font=("arial", 40))
texto_email.place(x=280 ,y=500)

# Frame consultar

# Texto dos usuários
texto_consulta = customtkinter.CTkLabel(frame_consulta, text=msg_consulta, text_color="white", font=("arial", 15))
texto_consulta.pack()

# Botão que fecha o frame de consulta
botao_fechar_consulta = customtkinter.CTkButton(frame_consulta, image=icone_fechar, command=fechar_frame,
                        text="", width=5, height=5,bg_color="transparent", fg_color="transparent",hover_color= 'grey')
botao_fechar_consulta.place(x=590, y=0)


# Frame atualizar

# Entrada do ID para atualizar dados
id_atualizar = customtkinter.CTkEntry(frame_atualizar, placeholder_text="ID", width=500, height=40,corner_radius=10,
                                      border_color="#67735C", fg_color="#D9D9D9", text_color="#262626")
id_atualizar.place(x=100,y=300)

# Entrada do nome para atualizar dados
nome_atualizar = customtkinter.CTkEntry(frame_atualizar, placeholder_text="NOME", width=500, height=40,corner_radius=10,
                                      border_color="#67735C", fg_color="#D9D9D9", text_color="#262626")
nome_atualizar.place(x=100,y=400)

# Entrada do e-mail para atualizar dados
email_atualizar = customtkinter.CTkEntry(frame_atualizar, placeholder_text="EMAIL", width=500, height=40,corner_radius=10,
                                      border_color="#67735C", fg_color="#D9D9D9", text_color="#262626")
email_atualizar.place(x=100,y=500)

# Texto princípal
texto_principal_atualizar = customtkinter.CTkLabel(frame_atualizar, text="ATUALIZAR DADOS DO USUÁRIO",
                                                   font=('arial', 30),text_color="#67735C")
texto_principal_atualizar.place(x=100, y=100)

# Texto que valida se os dados foram alterados com sucesso
texto_confirmacao_atualizar = customtkinter.CTkLabel(frame_atualizar, text=resposta, font=('arial', 25), text_color="RED")
texto_confirmacao_atualizar.place(x=120 ,y=200)

texto_obrigatorio_atualizar = customtkinter.CTkLabel(frame_atualizar, text="*ID OBRIGATÓRIO", font=('arial', 10),text_color="RED")
texto_obrigatorio_atualizar.place(x=115 ,y=270)

# Botão que fecha o frame que atualiza dados
botao_fechar_atualizar = customtkinter.CTkButton(frame_atualizar, image=icone_fechar, command=fechar_frame_atualizar, text="",
                                width=5, height=5,bg_color="transparent", fg_color="transparent", hover_color= 'grey')
botao_fechar_atualizar.place(x=650, y=25)

# Botão que atualiza os dados dentro do frame_atualizar
botao_frame_atualizar = customtkinter.CTkButton(frame_atualizar, text="ATUALIZAR", command=entrada_atualizar, width=320,
                                                height=60, corner_radius=20, fg_color="#AFBF9F", hover_color="#E9F2C9", text_color="#262626")
botao_frame_atualizar.place(x=150, y=600)

janela.mainloop()
