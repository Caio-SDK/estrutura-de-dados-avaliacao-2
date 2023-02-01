# Importações do sistema
from Sistema.validacao import Validacao
from Armazenamento_Sequencial.main import teste_main_armazenamento_sequencial

# Importações do Python
import sys
import os


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
[ 2 ] - Teste com a Pilha
[ 3 ] - Teste com a Fila
[ 4 ] - Teste com o Grafo
[ 5 ] - Teste com o Conjunto
[ 6 ] - Teste com a Lista Encadeada
[ 7 ] - Teste com a Árvore
[ 8 ] - Teste com os Mapas
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

                teste_main_armazenamento_sequencial()
            
            

            # Se a opção do usuário for sair do programa
            if opcao_usuario == 9:

                # Sair do programa
                sys.exit()

            
