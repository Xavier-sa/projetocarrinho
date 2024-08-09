class Carrinho:
    def __init__(self):
        self.__lista_produto = []

    def get_produtos(self):
        return self.__lista_produto

    def adicionar_ao_carrinho(self, produto, quantidade):
        # validar a quantidade que o cliente vai adicionar ao carrinho
        if quantidade > 0:

            # validar quantidade em estoque
            if produto.possui_quantidade_disponivel(quantidade):

                for _ in range(quantidade):
                    self.__lista_produto.append(produto)

                produto.debitar_quantidade(quantidade)
            else:
                raise Exception ('Quantidade indisponivel em estoque!')

        else:
            raise Exception('Quantidade selecionada inválida!')

