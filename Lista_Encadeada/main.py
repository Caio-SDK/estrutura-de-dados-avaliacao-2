
from Lista_Encadeada.listaLigada import ListaLigada


def _teste_main_lista_ligada():

    # Iniciando uma Lista Ligada
    lista_ligada = ListaLigada()

    # Testes
    lista_ligada.adiciona_fim('Caio')
    lista_ligada.adiciona_comeco('Caio Henrique')
    lista_ligada.adiciona_posicao('Henrique',1)
    lista_ligada.adiciona_fim('Caio')
    lista_ligada.remover_todos_elementos('Henrique')
    lista_ligada.adiciona_fim('Alice')

    # Exibição
    print(lista_ligada)