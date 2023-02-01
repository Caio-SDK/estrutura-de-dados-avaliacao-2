from Pilha.pilha import Pilha


def _teste_main_pilha():

    # Iniciando uma pilha
    pilha = Pilha()

    # Testes
    pilha.add(2)
    pilha.add(3)
    pilha.pop()
    pilha.pop()
    pilha.add(1)

    # Exibição
    print(pilha)