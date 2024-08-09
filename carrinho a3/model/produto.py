class Produto:
    def __init__(self, nome: str, quantidade: int):
        self.__nome = nome
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome
    
    def get_quantidade(self):
        return self.__quantidade
    
    def possui_quantidade_disponivel(self, qtd_desejada):
        if qtd_desejada <= self.__quantidade:
            return True
        else:
            return False
        

    def debitar_quantidade(self, quantidade):
        if quantidade <= 0:
            raise Exception ("Quantidade inválida!")
        else:
            self.__quantidade -= quantidade
        

        

        