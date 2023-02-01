from Conjunto.conjunto import Conjunto


def _teste_main_conjunto():

    # Iniciando uma Conjunto
    conjunto = Conjunto()

    # Testes
    conjunto._add(2)
    conjunto._add(2)
    conjunto._add(1)
    conjunto._add(2)
    conjunto._remove(2)
    conjunto._add(7)
    conjunto._add(6)
    conjunto._add(0)

    # Exibição
    print(conjunto)