from Grafos.grafo import Grafo


def _teste_main_grafo():

    # Iniciando uma Grafo
    grafo = Grafo(5)

    # Testes
    grafo._adicionar_aresta(2, 4)
    grafo._adicionar_aresta(3, 5)
    grafo._adicionar_aresta(1, 4)
    grafo._adicionar_aresta(1, 2)
    print(grafo._verificar_aresta(2, 3))
    print(grafo._verificar_aresta(2, 4))

    # Exibição
    print(grafo)