from Mapas.associacao import Associacao
from Mapas.carros import Carro

# Classe mapa
class Mapa:

    # Método construtor
    def __init__(self):

        self.__associacoes = []
        self.__tamanho = 0
    
     # Tamanho getter
    @property
    def tamanho(self):
        return self.__tamanho
    
    
    # Método que adiciona o objeto do mapa
    def adiciona(self, placa:str, carro:Carro):

        if not self.contem_placa(placa):

            associacao = Associacao(carro, placa)
            self.__associacoes.append(associacao)
            self.__tamanho += 1


    # Método que detalha o objeto do mapa
    def pega(self, placa):

        for associacao in self.__associacoes:

            if (associacao.placa == placa):

                return associacao.carro
        
        return 'carro não encontrado'
    

    # Método que remove o objeto do mapa
    def remove(self, placa):

        self.__associacoes = [associacao for associacao in self.__associacoes if associacao.placa != placa]
        self.__tamanho -= 1
        
    
    # Método que verifica se a placa cadastrada recentemente já existe na base de dados
    def contem_placa(self, placa):

        for associacao in self.__associacoes:

            if (associacao.placa == placa):

                return True
                        
        return False
    

    # Método Dunder para a função print
    def __str__(self):

        itens_mapa = '{'

        for associacao in self.__associacoes:

            itens_mapa = itens_mapa + f'\n\t{associacao.placa} : ({associacao.carro}),\n'

        itens_mapa = itens_mapa + '}'

        return itens_mapa
        
        
    