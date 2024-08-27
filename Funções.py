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
            print("EMAIL JÁ CADASTRADO")
            confirmacao = False
    if confirmacao:
        cursor.execute(f"INSERT INTO pessoas (nome, email) VALUES ('{nome}', '{email}')")
        print("EMAIL CADASTRADO COM SUCESSO!")
    conexao.commit()
    cursor.close()
    conexao.close()
    return confirmacao



def remover(email):
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
    resultado = cursor.fetchall()
    return resultado