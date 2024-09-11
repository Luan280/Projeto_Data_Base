import mysql.connector


def cadastrar(nome, email):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Luan280',
        database='projeto_db'
    )
    cursor = conexao.cursor()
    # Verifica se o email já foi cadastrado
    cursor.execute(F"SELECT * FROM pessoas WHERE email = '{email}'")
    resultado = cursor.fetchall()
    conexao.commit()
    encontrado = True
    # Se o email já foi cadastrado a confirmação recebe "FALSE" e retorna a confirmação
    for pessoa in resultado:
        if pessoa[2] == email:
            encontrado = False
    # Se a confirmação for "True", o usuário é cadastrado.
    if encontrado:
        cursor.execute(f"INSERT INTO pessoas (nome, email) VALUES ('{nome}', '{email}')")
    conexao.commit()
    cursor.close()
    conexao.close()
    return encontrado


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
    encontrado = True
    for pessoa in resultado:
        if email == pessoa[2]:
            cursor.execute(f"DELETE FROM pessoas WHERE email = '{email}'")
            conexao.commit()
            cursor.close()
            conexao.close()
            return encontrado
        else:
            encontrado = False
    conexao.commit()
    cursor.close()
    conexao.close()
    return encontrado


def consultar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Luan280',
        database='projeto_db'
    )
    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM pessoas")
    banco_dados = cursor.fetchall()
    conexao.commit()
    with open("arquivo.txt", "w"):
        pass
    for usuario in banco_dados:
        with open("arquivo.txt", "a") as arquivo:
            arquivo.write(f"ID: {usuario[0]}  NOME: {usuario[1]}  EMAIL: {usuario[2]}\n")
            arquivo.write(' \n')
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
    cursor.close()
    conexao.close()
    return conteudo


def atualizar(id_usuario, nome, email):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Luan280',
        database='projeto_db'
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas")
    banco_dados = cursor.fetchall()
    # Se ID não foi digitado
    if id_usuario in "":
        return 1
    for pessoa in banco_dados:
        if int(id_usuario) == pessoa[0]:
            # Se Nome e E-mail estiverem vazios
            if nome in "" and email in "":
                return 3
            # Só atualiza o Nome
            elif nome not in "" and email in "":
                cursor.execute(f"UPDATE pessoas SET nome = '{nome}' WHERE id = '{id_usuario}'")
                conexao.commit()
                cursor.close()
                conexao.close()
                return 4
            # Só atualiza o E-mail
            elif email not in "" and nome in "":
                cursor.execute(f"UPDATE pessoas SET email = '{email}' WHERE id = '{id_usuario}'")
                conexao.commit()
                cursor.close()
                conexao.close()
                return 4
            elif nome not in "" and email not in "":
                cursor.execute(f"UPDATE pessoas SET nome = '{nome}' WHERE id = '{id_usuario}'")
                cursor.execute(f"UPDATE pessoas SET email = '{email}' WHERE id = '{id_usuario}'")
                conexao.commit()
                cursor.close()
                conexao.close()
                return 4
    # Se ID não está cadastrado no sistema
    cursor.close()
    conexao.close()
    return 2