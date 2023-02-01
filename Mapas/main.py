from carros import Carro
from mapa_lista import Mapa
from mapa_espalhamento import MapaEspalhamento

# Iniciando um Mapa
lista = Mapa()

# Testes
lista.adiciona('wwwwwww', Carro('Corolla','Toyota','Azul', 2001))
lista.adiciona('zzzzzzz', Carro('Corolla','Toyota','Vermelho', 2001))
lista.adiciona('yyyyyyy', Carro('Corolla','Toyota','Amarelo', 2001))
l = MapaEspalhamento()
l.adiciona('HXO-ht', Carro('v','v','v', 2))
l.adiciona('HXO-he', Carro('v','v','v', 2))

# Exibição
print(l)

    