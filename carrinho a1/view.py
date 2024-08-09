def exibir_cliente(cliente):
    print(f'Cliente (nome: {cliente.nome})')


def exibir_lista_clientes(clientes):
    print('-'*20, 'CLIENTES', '-'*20)

    for cliente in clientes:
        exibir_cliente(cliente)

    print()


def exibir_produto(produto):
    print(f'Produto (nome: {produto.get_nome()}, quantidade: {produto.get_quantidade()})')


def exibir_lista_produtos(produtos):
    print('-'*20, 'PRODUTOS', '-'*20)

    for produto in produtos:
        exibir_produto(produto)

    print()


def exibir_produto_carrinho(produto):
    print(f'Produto (nome: {produto.get_nome()})')


def exibir_carrinho(cliente, carrinho):
    print('-'*20, f'CARRINHO DE {cliente.nome}', '-'*20)

    for produto in carrinho.get_produtos():
        exibir_produto_carrinho(produto)

    print()