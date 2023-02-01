from Mapas.carros import Carro
from Mapas.mapa_lista import Mapa
from Mapas.mapa_espalhamento import MapaEspalhamento


def _teste_main_mapas():
    
    # Iniciando um Mapa
    lista = Mapa()

    # Testes
    lista.adiciona('wwwwwww', Carro('Corolla','Toyota','Azul', 2001))
    lista.adiciona('zzzzzzz', Carro('Corolla','Toyota','Vermelho', 2001))
    lista.adiciona('yyyyyyy', Carro('Corolla','Toyota','Amarelo', 2001))
    mapa_espalhamento = MapaEspalhamento()
    mapa_espalhamento.adiciona('HXO-ht', Carro('v','v','v', 2))
    mapa_espalhamento.adiciona('HXO-he', Carro('v','v','v', 2))

    # Exibição
    print(mapa_espalhamento)

    