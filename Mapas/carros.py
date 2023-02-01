# Classe Carro
class Carro:

    # Método construtor
    def __init__(self, nome:str, marca:str, cor:str, ano:int):
        self.__nome = nome
        self.__marca = marca
        self.__cor = cor
        self.__ano = ano
    
    # Nome getter
    @property
    def nome(self):
        return self.__nome
    
    # Nome setter
    @nome.setter
    def nome(self,valor):
        self.__nome = valor
    
    # Marca getter
    @property
    def marca(self):
        return self.__marca
    
    # Marca setter
    @marca.setter
    def marca(self,valor):
        self.__marca = valor
        
    # Cor getter
    @property
    def cor(self):
        return self.__cor
    
    # Cor setter
    @cor.setter
    def cor(self,valor):
        self.__cor = valor
        
    # Ano getter
    @property
    def ano(self):
        return self.__ano
    
    # Ano setter
    @ano.setter
    def ano(self,valor):
        self.__ano = valor

    # Método Dunder para a função print 
    def __str__(self):

        return f'{self.__nome}, da marca {self.__marca}, de cor {self.__cor}, do ano {self.__ano}'