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

def exibir_menu_cliente():
    print('-'*20, f'MENU CLIENTE', '-'*20)
    print('1. Cadastrar')
    print('2. Listar')
    print('3. Editar')
    print('4. Excluir')
    print('0. Voltar')
    print()

def exibir_menu_principal():
    print('-'*20, f'MENU PRINCIPAL', '-'*20)
    print('1. Cliente')
    print('2. Produto')
    print('0. Sair')
    print()

def receber_opcao():
    try:
        return int(input('Informe: '))
    except: 
        # Desafio: interromper o programa quando digitar CTRL+C
        print('Opção inválida!')

def input_nome_cliente():
    return input('Nome do cliente: ')

def mensagem_cliente_encontrado():
    print('Cliente encontrado!')

def mensagem_cliente_nao_encontrado():
    print('Cliente não encontrado!')

def mensagem_excluido_cliente(tipo):
    if tipo == 'sucesso':
        print('Cliente removido com sucesso!')
    elif tipo == 'erro':
        print('Cliente não encontrado!')

def mensagem_encerrar_programa():
    print('Finalizando programa.')