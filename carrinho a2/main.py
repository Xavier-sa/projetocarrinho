from model.produto import Produto
from model.cliente import Cliente
import controller.cliente_controller as cliente_controller
import view

# faça o controle do menu
# op = 1 -> cadastra cliente
# op = 2 -> exclui cliente
# op = 0 -> encerra.
op = -1
while True:
    view.exibir_menu_principal()
    op = view.receber_opcao()
    match op:
        case 1:
            cliente_controller.cadastrar()

        case 2:
            cliente_controller.excluir()

        case 0:
            view.mensagem_encerrar_programa()
            break
