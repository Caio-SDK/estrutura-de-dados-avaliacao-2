from Arvore.no import No


# Classe Arvore
class ArvoreBinariaBusca:

    # Método construtor
    def __init__(self):
        self.__raiz = None
        

    # Raiz getter
    @property
    def raiz(self):
        return self.__raiz
        

    # Método que irá inserir um objeto na arvore
    def _inserir(self, label):

        no = No(label)

        if (self.__raiz is None):

            self.__raiz = no

        else:

            atual = self.__raiz

            while True:

                if(no.label < atual.label):

                    if(atual.esquerda is None):

                        atual.esquerda = no
                        break

                    else:

                        atual = atual.esquerda
                        
                else:

                    if(atual.direita is None):

                        atual.direita = no
                        break

                    else:

                        atual = atual.direita

        
    # Método que exibe o valor na tela
    def _imprimir_pre(self, arvore):
        print(arvore.label)
        
        if arvore.esquerda is not None:

            self._imprimir_pre(arvore.esquerda)
              
        if arvore.direita is not None:

            self._imprimir_pre(arvore.direita)       
    
    
    # Método que exibe os objetos da arvore em ordem
    def _imprimir_ordem(self, arvore):

        if arvore.esquerda is not None:

            self._imprimir_ordem(arvore.esquerda)    
             
        print(arvore.label) 
         
        if arvore.direita is not None:

            self._imprimir_ordem(arvore.direita)        
         
            
    def _imprimir_pos(self,arvore):

        if arvore.esquerda is not None:

            self._imprimir_pos(arvore.esquerda)  

        if arvore.direita is not None:

            self._imprimir_pos(arvore.direita) 
        
        print(arvore.label)
           
    
    
                