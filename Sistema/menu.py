# Importações do sistema
from Sistema.validacao import Validacao
from Armazenamento_Sequencial.main import _teste_main_armazenamento_sequencial
from Arvore.main import _teste_main_arvore
from Conjunto.main import _teste_main_conjunto
from Fila.main import _teste_main_fila
from Grafos.main import _teste_main_grafo
from Lista_Encadeada.main import _teste_main_lista_ligada
from Mapas.main import _teste_main_mapas
from Pilha.main import _teste_main_pilha

# Importações do Python
import sys
import os
import time


# Classe do Menu
class Menu:

    # Mensagem de Bem-Vindo ao Usuário
    mensagem_bem_vindo = """
OLÁ!
SEJA BEM-VINDO(A) AO PROGRAMA DE TESTE PARA AS ESTRTURAS DE DADOS V.1
ESPERO QUE SUA EXPERIENCIA SEJA AGRÁDAVEL
"""

    # Opções do Usuario
    opcoes = """
[ 1 ] - Teste com o Armazenamento Sequencial
[ 2 ] - Teste com a Árvore
[ 3 ] - Teste com o Conjunto
[ 4 ] - Teste com a Fila
[ 5 ] - Teste com o Grafo
[ 6 ] - Teste com a Lista Encadeada
[ 7 ] - Teste com os Mapas
[ 8 ] - Teste com a Pilha
[ 9 ] - Sair do programa
"""


    # Função que criará o menu principal para o usuário
    @staticmethod
    def _menu_principal():

        # Exibir a mensagem de bem-vindo ao usuário
        print(Menu.mensagem_bem_vindo)

        while True:

            # Limpando o terminal para não haver poluição visual
            os.system("cls")
            
            # Exibir as Opções
            print(Menu.opcoes)

            # Entrada do Usuário
            opcao_usuario = Validacao._ValidacaoOpcoes("Digite sua opção: ", 1, 11)

            if opcao_usuario == 1:

                _teste_main_armazenamento_sequencial()
            
            elif opcao_usuario == 2:

                _teste_main_arvore()
            
            elif opcao_usuario == 3:

                _teste_main_conjunto()
            
            elif opcao_usuario == 4:

                _teste_main_fila()

            elif opcao_usuario == 5:

                _teste_main_grafo()
            
            elif opcao_usuario == 6:

                _teste_main_lista_ligada()

            elif opcao_usuario == 7:

                _teste_main_mapas()

            elif opcao_usuario == 8:

                _teste_main_pilha()

            # Se a opção do usuário for sair do programa
            if opcao_usuario == 9:

                # Sair do programa
                sys.exit()
            
            # Dando uma pausa para o Usuário observar a saída dos testes
            time.sleep(5)

            
