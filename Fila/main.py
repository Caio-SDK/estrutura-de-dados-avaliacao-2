from Fila.fila import Fila


def _teste_main_fila():

    # Iniciando uma Fila
    fila = Fila()

    # Testes
    fila._add(2)
    fila._add(1)
    fila._pop()
    fila._add(2)
    fila._pop()
    fila._add(7)
    fila._add(6)
    fila._pop()

    # Exibição
    print(fila)