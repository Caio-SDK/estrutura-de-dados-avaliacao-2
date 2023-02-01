from Mapas.carros import Carro

# Classe Associação
class Associacao:
    def __init__(self, carro: Carro, placa: str):
        self.__carro = carro
        self.__placa = placa
        
    # Carro getter
    @property
    def carro(self):
        return self.__carro
    
    # Carro setter
    @carro.setter
    def carro(self, carro):
        self.__carro = carro
        
    # Placa getter
    @property
    def placa(self):
        return self.__placa
    
    # Placa setter
    @placa.setter
    def placa(self, placa):
        self.__placa = placa
        
    # Método Dunder para a função print
    def __str__(self):
        return f'{self.__carro.nome}, da marca {self.__carro.marca}, de cor {self.__carro.cor}, do ano {self.__carro.ano}, associado à placa {self.__placa}'
    