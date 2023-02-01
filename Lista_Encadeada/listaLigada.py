from Lista_Encadeada.celulaLista import CelulaLista

# Classe Lista Ligada
class ListaLigada:

    # Método construtor
    def __init__(self):
        self.__primeira = None
        self.__total_elementos = 0
        self.__ultima = None


    #adiciona um elemento no inicio da lista
    def adiciona_comeco(self, elemento):
        nova_celula = CelulaLista(elemento,self.__primeira, None)

        #verificando se a lista já tinha elementos
        if self.__total_elementos >= 1:
            self.__primeira.anterior = nova_celula

        #atualizando a lista dizendo que a nova celula é nosso primeiro elemento
        self.__primeira = nova_celula

        #caso a lista não tivesse elementos então nossa nova celula também será a ultima
        if self.__total_elementos == 0:
            self.__ultima = nova_celula

        #atualizando o total de elementos da lista
        self.__total_elementos += 1


    # Adicionando elemento no fim
    def adiciona_fim(self, elemento):

        if self.__total_elementos == 0:

            self.adiciona_comeco(elemento)

        else: 

            nova_celula = CelulaLista(elemento,None, self.__ultima)
            self.__ultima.proxima = nova_celula
            self.__ultima = nova_celula

            self.__total_elementos += 1


    # Adicionando o elemento de acordo com a posição
    def adiciona_posicao(self, elemento, posicao):

        if posicao == 0: 

            self.adiciona_comeco(elemento)

        elif posicao == self.__total_elementos:

            self.adiciona_fim(elemento)

        else:

            anterior = self.pegar(posicao-1)
            nova_celula = CelulaLista(elemento,anterior.proxima, anterior)
            anterior.proxima.anterior = nova_celula
            anterior.proxima = nova_celula
            self.__total_elementos += 1


    # Pegar elemento de acordo com a posição
    def pegar(self, posicao):

        if posicao < 0 or posicao >= self.__total_elementos:

            raise Exception('Posição inválida')

        else:

            atual = self.__primeira

            for _ in range(0, posicao):

                atual = atual.proxima

            return atual

    # Remover o primeiro elemento
    def remover_comeco(self):

        if self.__total_elementos == 1:

            self.__primeira = None
            self.__ultima = None

        else:

            self.__primeira.proxima.anterior = None
            self.__primeira = self.__primeira.proxima

        self.__total_elementos -= 1


    # Tamanho da lista encadeada
    def tamanho(self):

        return self.__total_elementos

    # Verificando se o elemento contem na lista
    def contem(self, elemento):

        atual = self.__primeira

        while atual is not None:
            
            if atual.elemento == elemento:

                return True

            atual = atual.proxima

        return False

    # Remover pela posição
    def remover_posicao(self, posicao):

        if posicao == 0:

            self.remover_comeco()

        elif posicao == self.__total_elementos-1:

            self.remover_fim()

        else:

            celula = self.pegar(posicao)
            celula.anterior.proxima = celula.proxima
            celula.proxima = celula.anterior
            self.__total_elementos -=1
            
    # Removendo o elemento
    def remover_elemento(self, elemento):

        if self.contem(elemento) == False:

            print('Esse elemento não está contido na lista')

        atual = self.__primeira

        if elemento == self.__primeira:

            self.remover_comeco()

        else:

            while atual is not None:
            
                if atual.elemento == elemento:

                    if atual.proxima == None:

                        self.remover_fim()

                    else:

                        atual.anterior.proxima = atual.proxima
                        atual.proxima = atual.anterior
                        self.__total_elementos -=1

                    break

                atual = atual.proxima

    # Apagar todos os elementos
    def remover_todos_elementos(self, elemento):

        if self.contem(elemento) == False:

            print('Esse elemento não está contido na lista') 

        atual = self.__primeira
        
        while atual is not None:
        
            if atual.elemento == elemento: 

                if atual.proxima == None:

                    self.remover_fim()

                elif atual.anterior == None:

                    self.remover_comeco()

                else:

                    atual.anterior.proxima = atual.proxima
                    atual.proxima = atual.anterior
                    self.__total_elementos -=1

            atual = atual.proxima

    # Apagar o último elemento
    def remover_fim(self):

        if self.__total_elementos == 1:

            self.remover_comeco() 

        else: 

            self.__ultima = self.__ultima.anterior
            self.__ultima.proxima = None
            self.__total_elementos -= 1


    # Método Dunder para a função print
    def __str__(self):

        if self.__total_elementos == 0:

            return '[] '

        string_final = '['
        atual = self.__primeira

        for _ in range(0, self.__total_elementos-1):

            string_final = string_final + atual.elemento + ', '
            atual = atual.proxima

        self.__ultima = atual
        self.__ultima.proxima = None
        string_final = string_final + f'{atual.elemento}]'

        return string_final