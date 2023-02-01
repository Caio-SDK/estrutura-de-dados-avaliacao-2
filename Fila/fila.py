# Classe Fila
class Fila:

    # Método construtor
    def __init__(self):

        self.__estrutura = []
    

     # Método para verificar se a fila está vázia ou não
    def _empty(self):

        if self.__estrutura:

            return False

        else:

            return True
    

    # Método para adicionar algum objeto a fila
    def _add(self, objeto):

        self.__estrutura.append(objeto)
    

    # Método para remover algum objeto a fila
    def _pop(self):

        if self._empty():

            print("A fila já está vazia!!!")
        
        else:
            
            del self.__estrutura[0]
    

    # Método Dunder para a função print
    def __str__(self):

        # Declaração da variavel que armazenará os itens em formato de String
        itens_fila = ""

        # Para cada item dentro da fila
        for item in self.__estrutura:

            itens_fila += str(item) + "\n"
        
        # Retornar os itens da fila em formato de String
        return itens_fila