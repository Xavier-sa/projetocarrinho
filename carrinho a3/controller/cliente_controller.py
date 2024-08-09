from model.cliente import Cliente
import view

clientes = [Cliente('thiago')]

def cadastrar():
    # usuário informa o nome pelo teclado
    nome = view.input_nome_cliente()

    # criar a instância do cliente
    novo_cliente = Cliente(nome)

    # salvar na lista clientes
    clientes.append(novo_cliente)

def listar():
    view.exibir_lista_clientes(clientes)

def editar():
    indice_cliente = _selecionar_cliente()
    
    if indice_cliente is not None:
        # recebe o novo nome
        novo_nome = view.input_nome_cliente()

        # atualizar
        cliente = clientes[indice_cliente]
        cliente.nome = novo_nome


def excluir():
    # lógica para excluir cliente (por nome)                
    indice_cliente = _selecionar_cliente()

    if indice_cliente is not None:
        clientes.pop(indice_cliente) # remove da lista pelo indice


# retorna o indice do cliente
def _selecionar_cliente():
    # recebe o nome do cliente
    nome = view.input_nome_cliente()

    # econtrar o cliente na lista
    for cliente in clientes:
        if cliente.nome == nome:
            view.mensagem_cliente_encontrado()
            return clientes.index(cliente)
        
    view.mensagem_cliente_nao_encontrado()
    return None