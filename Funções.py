import mysql.connector


def cadastrar(nome, email):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Luan280',
        database='projeto_db'
    )
    cursor = conexao.cursor()
    cursor.execute(F"SELECT * FROM pessoas WHERE email = '{email}'")
    resultado = cursor.fetchall()
    conexao.commit()
    print(resultado)
    confirmacao = True
    for pessoa in resultado:
        if pessoa[2] == email:
            confirmacao = False
    if confirmacao:
        cursor.execute(f"INSERT INTO pessoas (nome, email) VALUES ('{nome}', '{email}')")
        with open("arquivo.txt", "a") as arquivo:
            arquivo.write(f"{nome}, {email}\n")
    conexao.commit()
    cursor.close()
    conexao.close()
    return confirmacao



def remover(email):
    global confirmacao
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Luan280',
        database='projeto_db'
    )
    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM pessoas")
    resultado = cursor.fetchall()
    conexao.commit()
    for pessoa in resultado:
        if email == pessoa[2]:
            cursor.execute(f"DELETE FROM pessoas WHERE email = '{email}'")
            confirmacao = True
            conexao.commit()
            cursor.close()
            conexao.close()
            return confirmacao
        else:
            confirmacao = False
    conexao.commit()
    cursor.close()
    conexao.close()
    return confirmacao


def consultar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Luan280',
        database='projeto_db'
    )
    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM pessoas")
    conexao.commit()
    resultado = cursor.fetchall()
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
    msg_consulta = conteudo
    return msg_consulta