# Classe Celula
class CelulaLista:

    # Método construtor
    def __init__(self, elemento, proxima, anterior):

        self.__elemento = elemento
        self.__proxima = proxima
        self.__anterior = anterior

    # Elemento getter
    @property
    def elemento(self):
        return self.__elemento 
    
    # Próxima getter
    @property
    def proxima(self):
        return self.__proxima

    # Proxima setter
    @proxima.setter
    def proxima(self, valor):
        self.__proxima = valor
    
    # Anterior getter
    @property
    def anterior(self):
        return self.__anterior

    # Anterior setter
    @anterior.setter
    def anterior(self, valor):
        self.__anterior = valor
    
    # Método Dunder para a função print
    def __str__(self):
        return self.__elemento