from Armazenamento_Sequencial.armazenamento_sequencial import ArmazenamentoSequencial


def _teste_main_armazenamento_sequencial():

    # Iniciando um Armazenamento Sequencial
    armazenamento_sequencial = ArmazenamentoSequencial()

    # Testes
    armazenamento_sequencial._add(3)
    armazenamento_sequencial._add(2)
    armazenamento_sequencial._add(10)
    armazenamento_sequencial._remove(2)
    armazenamento_sequencial._add(5)
    armazenamento_sequencial._remove(5)

    # Exibição
    print(armazenamento_sequencial)