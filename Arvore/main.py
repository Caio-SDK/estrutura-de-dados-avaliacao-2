from arvore import ArvoreBinariaBusca
        
        
def teste_main_arvore():

    # Iniciando uma Arvore
    arvore = ArvoreBinariaBusca()

    # Testes
    arvore.inserir(2)
    arvore.inserir(3)
    arvore.inserir(1)
    arvore.inserir(4)
    arvore.inserir(5)
    arvore.inserir(7)
    arvore.inserir(6)
    arvore.inserir(0)
    arvore.imprimir_ordem(arvore.raiz)

    # Exibição
    print(list(reversed(range(1,11))))
