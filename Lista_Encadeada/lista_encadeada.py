# Classe Nó
class No:

    # Método construtor
    def __init__(self, dado):

        self.__dado = dado
        self.__proximo = None


# Classe Lista Encadeada
class ListaEncadeada:

     # Método construtor
    def __init__(self):

        self.__cabeca = None

    
    def add(self, dados):

        novo_no = No(dados)

        if self.__cabeca is None:

            self.__cabeca = novo_no

            return


        no_atual = self.__cabeca

        while no_atual.__proximo:

            no_atual = no_atual.__proximo

        no_atual.__proximo = novo_no
        return 


    def get(self, index):
        pass


    def tamanho(self):

        if self.__cabeca is None:

            return 0
        
        no_atual = self.__cabeca
        total = 0

        while no_atual:
            total += 1
            no_atual = no_atual.__proximo

        return total

    
    def __str__(self):
        
        conteudo = self.__cabeca

        while conteudo:
            
            print(conteudo.__dado)

            conteudo = conteudo.__proximo

