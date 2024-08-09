from produto import Produto
from cliente import Cliente
import view

cliente1 = Cliente('Otávio Bonito')
cliente2 = Cliente('Luiz')
cliente3 = Cliente('Matheus')

clientes = [cliente1, cliente2, cliente3]
view.exibir_lista_clientes(clientes)

produto1 = Produto('arroz', 15)
produto2 = Produto('feijão', 20)
produto3 = Produto('abacaxi', 40)
produto4 = Produto('abobora',20)

produtos = [produto1, produto2, produto3, produto4]
view.exibir_lista_produtos(produtos)

print('\n\n\n\n')

cliente1.adicionar_produto(produto4, 3)
view.exibir_carrinho(cliente1, cliente1.carrinho)

print('\n')

cliente2.adicionar_produto(produto4, 2)
view.exibir_carrinho(cliente2, cliente2.carrinho)

print('\n')

cliente3.adicionar_produto(produto4, 1)
view.exibir_carrinho(cliente3, cliente3.carrinho)

