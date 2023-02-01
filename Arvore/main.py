from Arvore.arvore import ArvoreBinariaBusca
        
        
def _teste_main_arvore():

    # Iniciando uma Arvore
    arvore = ArvoreBinariaBusca()

    # Testes
    arvore._inserir(2)
    arvore._inserir(3)
    arvore._inserir(1)
    arvore._inserir(4)
    arvore._inserir(5)
    arvore._inserir(7)
    arvore._inserir(6)
    arvore._inserir(0)
    arvore._imprimir_ordem(arvore.raiz)

    # Exibição
    print(list(reversed(range(1,11))))
