from Mapas.associacao import Associacao


# Classe Mapa Espalhamento
class MapaEspalhamento:

    # Método construtor
    def __init__(self):

        self.__tabela_hash = []
        
        for _ in range(0,30):

            self.__tabela_hash.append([])
        
        self.__tamanho = 0
        
    
    # Método que calcula o indice da tabela para saber onde adicionar os objetos
    def calcula_indice_tabela(self,placa):
        codigo_espalhamento = self.funcao_hash(placa)
        codigo_espalhamento = abs(codigo_espalhamento)
        return codigo_espalhamento % len(self.__tabela_hash)


    # Método da função HASH
    def funcao_hash(self,placa):

        codigo = 1

        for i in range(0, len(placa)):

            codigo = 7 * codigo + ord(placa[i])

        return codigo
    
    # Método que verifica se a placa existe na base de dados
    def contem_chave(self, placa):

        indice = self.calcula_indice_tabela(placa)
        lista = self.__tabela_hash[indice]

        for associacao in lista:

            if placa == associacao.placa:

                return True
                
        return False
    
    # Método que adiciona um objeto na tabela de espalhamento
    def adiciona(self, placa, carro):

        if self.contem_chave(placa):

            self.remove(placa)
        
        indice = self.calcula_indice_tabela(placa)
        lista:list = self.__tabela_hash[indice]
        
        associacao = Associacao(carro, placa)
        lista.append(associacao)
        self.__tamanho += 1
    
    
    # Método que remove um objeto do mapa de espalhamento
    def remove(self, placa):

        indice = self.calcula_indice_tabela(placa)
        self.__tabela_hash[indice] = [associacao for associacao in self.__tabela_hash[indice] if associacao.placa != placa]
        self.__tamanho -= 1
    

    # Método que retorna o tamanho do mapa de espalhamento
    def tamanho(self):
        return self.tamanho

    
    # Método que detalha o objeto do mapa de espalhamento
    def pega(self, placa):

        indice = self.calcula_indice_tabela(placa)

        for associacao in self.__tabela_hash[indice]:

            if (associacao.placa == placa):

                return associacao.carro
        
        return 'carro não encontrado'
    

    # Método Dunder para a função print
    def __str__(self):
        return f'{self.__tabela_hash}'
            