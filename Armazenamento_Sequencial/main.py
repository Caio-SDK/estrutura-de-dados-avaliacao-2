from armazenamento_sequencial import ArmazenamentoSequencial


def teste_main_armazenamento_sequencial():

    # Iniciando um Armazenamento Sequencial
    armazenamento_sequencial = ArmazenamentoSequencial()

    # Testes
    armazenamento_sequencial._add(3)
    armazenamento_sequencial._add(7)
    armazenamento_sequencial._add(10)
    armazenamento_sequencial._pop(2)
    armazenamento_sequencial._add(5)
    armazenamento_sequencial._pop(2)

    # Exibição
    print(armazenamento_sequencial)