from model.produto import Produto
from model.cliente import Cliente
import controller.cliente_controller as cliente_controller
import view.view




#!vamo ver
# def menu_cliente():
#     while True:
#         op_cliente = -1
        
#         view.exibir_menu_cliente()
#         op_cliente = view.receber_opcao()
        
#         match op_cliente:
#             case 1:
#                 cliente_controller.cadastrar()

#             case 2:
#                 cliente_controller.listar()

#             case 3:
#                 cliente_controller.editar()

#             case 4:
#                 cliente_controller.excluir()

#             case 0:
#                 break

# def menu_produto():
#     pass

# op = -1
# while True:

#     view.menu_principal()
#     op = view.receber_opcao()

#     match op:
#         case 1:
#             menu_cliente()

#         case 2:
#             menu_produto()

#         case 0:
#             view.mensagem_encerrar_programa()
#             break