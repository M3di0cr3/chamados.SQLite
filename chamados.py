import sqlite3

def conexao_banco():
    conexao = sqlite3.connect('chamados.db')
    cursor = conexao.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS chamados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        prioridade TEXT NOT NULL,
        status TEXT NOT NULL,
        usuario TEXT NOT NULL
    )
    '''
    cursor.execute(sql)
    return conexao

def Pesquisar_Usuario():
    usuario = input("Digite o nome do usuário: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM chamados WHERE usuario = ?", (usuario,))
    resultados = cursor.fetchall()
    if resultados:
        for chamado in resultados:
            print(chamado)
    else:
        print("Nenhum chamado encontrado para o usuário informado.")
    conexao.close()
def Pesquisar_Prioridade():
    prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM chamados WHERE prioridade = ?", (prioridade,))
    resultados = cursor.fetchall()
    if resultados:
        for chamado in resultados:
            print(chamado)
    else:
        print("Nenhum chamado encontrado para a prioridade informada.")
    conexao.close()
def Pesquisar_Status():
    status = input("Digite o status (Aberto, Em andamento, Fechado): ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM chamados WHERE status = ?", (status,))
    resultados = cursor.fetchall()
    if resultados:
        for chamado in resultados:
            print(chamado)
    else:
        print("Nenhum chamado encontrado para o status informado.")
    conexao.close()
def Pesquisar_Urgencia():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM chamados WHERE prioridade = 'Alta' AND (status = 'Aberto' OR status = 'Em andamento')")
    resultados = cursor.fetchall()
    if resultados:
        for chamado in resultados:
            print(chamado)
    else:
        print("Nenhum chamado urgente encontrado.")
    conexao.close()

def Abrir_chamado():
    id_chamado = input("Digite o ID do chamado a ser aberto: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("UPDATE chamados SET status = 'Aberto' WHERE id = ?", (id_chamado,))
    if cursor.rowcount == 0:
        print("Chamado não encontrado.")
    else:
        conexao.commit()
        print("Chamado aberto com sucesso!")
    conexao.close()
def Resolver_chamado():
    id_chamado = input("Digite o ID do chamado a ser resolvido: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("UPDATE chamados SET status = 'Em andamento' WHERE id = ?", (id_chamado,))
    if cursor.rowcount == 0:
        print("Chamado não encontrado.")
    else:
        conexao.commit()
        print("Chamado resolvido com sucesso!")
    conexao.close()
def Fechar_chamado():
    id_chamado = input("Digite o ID do chamado a ser fechado: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("UPDATE chamados SET status = 'Fechado' WHERE id = ?", (id_chamado,))
    if cursor.rowcount == 0:
        print("Chamado não encontrado.")
    else:
        conexao.commit()
        print("Chamado fechado com sucesso!")
    conexao.close()
def Criar_chamado():
    titulo = input("Digite o título do chamado: ")
    prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
    if prioridade not in ["Alta", "Média", "Baixa"]:
        print("Prioridade inválida. O chamado não será criado.")
        return
    status = input("Digite o status (Aberto, Em andamento, Fechado): ")
    if status not in ["Aberto", "Em andamento", "Fechado"]:
        print("Status inválido. O chamado não será criado.")
        return
    usuario = input("Digite o nome do usuário: ")

    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO chamados (titulo, prioridade, status, usuario) VALUES (?, ?, ?, ?)",
                   (titulo, prioridade, status, usuario))
    conexao.commit()
    print("Chamado criado com sucesso!")
    conexao.close()
def Excluir_chamado():
    id_chamado = input("Digite o ID do chamado a ser excluído: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM chamados WHERE id = ?", (id_chamado,))
    if cursor.rowcount == 0:
        print("Chamado não encontrado.")
    else:
        conexao.commit()
        print("Chamado excluído com sucesso!")
    conexao.close()

while True:
    print ("=== Sistema de Chamados ===")
    print ("1 - Pesquisar")
    print ("2 - Gerenciar Chamado")
    print ("3 - Mostrar Chamados")
    print ("0 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print ("=== Pesquisar Chamado ===")
        print ("1 - Pesquisar por Usuário")
        print ("2 - Pesquisar por Prioridade")
        print ("3 - Pesquisar por Status")
        print ("4 - Pesquisar por Urgência")
        print ("0 - Voltar")

        opcao_pesquisa = input("Escolha uma opção: ")
        if opcao_pesquisa == "1":
            Pesquisar_Usuario()
        elif opcao_pesquisa == "2":
            Pesquisar_Prioridade()
        elif opcao_pesquisa == "3":
            Pesquisar_Status()
        elif opcao_pesquisa == "4":
            Pesquisar_Urgencia()
        elif opcao_pesquisa == "0":
            continue
        else:
            print("Opção inválida. Tente novamente.")

    elif opcao == "2":
        print ("=== Gerenciar Chamado ===")
        print ("1 - Abrir Chamado")
        print ("2 - Resolver Chamado")
        print ("3 - Fechar Chamado")
        print ("4 - Criar Chamado")
        print ("5 - Excluir Chamado")
        print ("0 - Voltar")

        opcao_gerenciar = input("Escolha uma opção: ")
        if opcao_gerenciar == "1":
            Abrir_chamado()
        elif opcao_gerenciar == "2":
            Resolver_chamado()
        elif opcao_gerenciar == "3":
            Fechar_chamado()
        elif opcao_gerenciar == "4":
            Criar_chamado()
        elif opcao_gerenciar == "5":
            Excluir_chamado()
        elif opcao_gerenciar == "0":
            continue
        else:
            print("Opção inválida. Tente novamente.")
   
    elif opcao == "3":
        print("Mostrando todos os chamados...")
        print("=== Lista de Chamados ===")
        conexao = conexao_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM chamados")
        resultados = cursor.fetchall()
        if resultados:
            for chamado in resultados:
                print(chamado)
        else:
            print("Nenhum chamado encontrado.")
        conexao.close()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")   

