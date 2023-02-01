# Classe Grafo
class Grafo:

    # Método construtor
    def __init__(self, quantidade_nos):

        self.__matriz = []

        # Construindo o grafo de acordo com a quantidade de nós
        for c in range(0, quantidade_nos):

            linha = []

            for i in range(0, quantidade_nos):

                linha.append(0)

            self.__matriz.append(linha)
        
    # Método para adicionar uma aresta
    def _adicionar_aresta(self, no_primario, no_secundario):

        self.__matriz[no_primario-1][no_secundario-1] = 1
        self.__matriz[no_secundario-1][no_primario-1] = 1
    
    # Método para verificar se uma aresta existe
    def _verificar_aresta(self, no_primario, no_secundario):

        if self.__matriz[no_primario-1][no_secundario-1] == 1:

            return True

        else:

            return False
        
    
    # Método Dunder para a função print
    def __str__(self):

         # Declaração da variavel que armazenará os itens em formato de String
        itens_grafo = ''

        # Para cada linha (lista) dentro da matriz
        for linha in self.__matriz:

            # Para cada coluna dentro da matriz
            for coluna in linha:

                itens_grafo += f' {coluna} ' 

            itens_grafo += '\n'
        
        # Retornar os itens da fila em formato de String
        return itens_grafo
        


