from model.cliente import Cliente
import view

clientes = [Cliente('thiago')]

# cadastrar
def cadastrar():
    # usuário informa o nome pelo teclado
    nome = view.input_cadastro_cliente()

    # criar a instância do cliente
    novo_cliente = Cliente(nome)

    # salvar na lista clientes
    clientes.append(novo_cliente)

# excluir
def excluir():
    # lógica para excluir cliente (por nome)
    # exibir
    view.exibir_lista_clientes(clientes)
                
    # usuario selecionar
    nome = view.input_exclusao_cliente()

    # excluir
    # percorre a lista
    removido = False
    for cliente in clientes:
        # se encontrar
        if (cliente.nome == nome):
            indice = clientes.index(cliente) # pega o indice
            clientes.pop(indice) # remove da lista pelo indice
            removido = True
            break

    if removido:
        view.mensagem_excluido_cliente('sucesso')
    else:
        view.mensagem_excluido_cliente('erro')