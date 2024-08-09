def exibir_cliente(cliente):
    return f'Cliente (nome: {cliente["nome"]})'

def exibir_produto(produto):
    return f'Produto (nome: {produto["nome"]}, quantidade: {produto["quantidade"]})'

def exibir_carrinho(cliente, carrinho):
    mensagem = f'CARRINHO DE {cliente["nome"]}\n'
    for produto in carrinho:
        mensagem += f'{exibir_produto(produto)}\n'
    return mensagem

def mensagem_cliente_encontrado():
    print("Cliente encontrado!")

def mensagem_cliente_nao_encontrado():
    print("Cliente não encontrado!")

def mensagem_excluido_cliente(tipo):
    if tipo == 'sucesso':
        print("Cliente removido com sucesso!")
    elif tipo == 'erro':
        print("Cliente não encontrado!")

def mensagem_encerrar_programa():
    print("Finalizando programa.")
    exit()

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    if nome:
        clientes.append({"nome": nome})
        mensagem_cliente_encontrado()
        atualizar_lista_clientes()

def listar_clientes():
    texto_clientes = '\n'.join([exibir_cliente(cliente) for cliente in clientes])
    print(texto_clientes)

def editar_cliente():
    nome_atual = input("Nome atual do cliente: ")
    novo_nome = input("Novo nome do cliente: ")
    for cliente in clientes:
        if cliente["nome"] == nome_atual:
            cliente["nome"] = novo_nome
            mensagem_cliente_encontrado()
            atualizar_lista_clientes()
            return
    mensagem_cliente_nao_encontrado()

def excluir_cliente():
    nome = input("Nome do cliente a ser excluído: ")
    global clientes
    clientes = [cliente for cliente in clientes if cliente["nome"] != nome]
    mensagem_excluido_cliente('sucesso' if any(cliente["nome"] == nome for cliente in clientes) else 'erro')
    atualizar_lista_clientes()

def adicionar_no_carrinho():
    nome_cliente = input("Nome do cliente: ")
    nome_produto = input("Nome do produto: ")
    for cliente in clientes:
        if cliente["nome"] == nome_cliente:
            for produto in produtos:
                if produto["nome"] == nome_produto:
                    carrinhos[cliente["nome"]].append(produto)
                    print("Produto adicionado ao carrinho!")
                    atualizar_carrinho(cliente)
                    return
    print("Cliente ou produto não encontrado!")

def remover_do_carrinho():
    nome_cliente = input("Nome do cliente: ")
    nome_produto = input("Nome do produto: ")
    for cliente in clientes:
        if cliente["nome"] == nome_cliente:
            carrinhos[cliente["nome"]] = [produto for produto in carrinhos[cliente["nome"]] if produto["nome"] != nome_produto]
            print("Produto removido do carrinho!")
            atualizar_carrinho(cliente)
            return
    print("Cliente não encontrado!")

def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade do produto: "))
    if nome and quantidade is not None:
        produtos.append({"nome": nome, "quantidade": quantidade})
        print("Produto cadastrado com sucesso!")
        atualizar_lista_produtos()

def listar_produtos():
    texto_produtos = '\n'.join([exibir_produto(produto) for produto in produtos])
    print(texto_produtos)

def incluir_no_estoque():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade a ser adicionada: "))
    for produto in produtos:
        if produto["nome"] == nome:
            produto["quantidade"] += quantidade
            print("Quantidade atualizada com sucesso!")
            atualizar_lista_produtos()
            return
    print("Produto não encontrado!")

def atualizar_lista_clientes():
    print("\nLista de Clientes Atualizada:")
    listar_clientes()

def atualizar_lista_produtos():
    print("\nLista de Produtos Atualizada:")
    listar_produtos()

def atualizar_carrinho(cliente):
    print("\nCarrinho Atualizado:")
    print(exibir_carrinho(cliente, carrinhos.get(cliente["nome"], [])))

def menu_principal():
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Menu Cliente")
        print("2. Menu Produto")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                menu_cliente()
            case "2":
                menu_produto()
            case "0":
                mensagem_encerrar_programa()
            case _:
                print("Opção inválida!")

def menu_cliente():
    while True:
        print("\nMENU CLIENTE")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("5. Ver carrinho")
        print("6. Adicionar no carrinho")
        print("7. Remover do carrinho")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_cliente()
            case "2":
                listar_clientes()
            case "3":
                editar_cliente()
            case "4":
                excluir_cliente()
            case "5":
                nome_cliente = input("Nome do cliente: ")
                for cliente in clientes:
                    if cliente["nome"] == nome_cliente:
                        atualizar_carrinho(cliente)
                        return
                print("Cliente não encontrado!")
            case "6":
                adicionar_no_carrinho()
            case "7":
                remover_do_carrinho()
            case "0":
                return
            case _:
                print("Opção inválida!")

def menu_produto():
    while True:
        print("\nMENU PRODUTO")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Incluir no estoque")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_produto()
            case "2":
                listar_produtos()
            case "3":
                incluir_no_estoque()
            case "0":
                return
            case _:
                print("Opção inválida!")


clientes = [{"nome": "Xavier"}]
produtos = [{"nome": "Computador", "quantidade": 10}]
carrinhos = {cliente["nome"]: [] for cliente in clientes}

menu_principal()



