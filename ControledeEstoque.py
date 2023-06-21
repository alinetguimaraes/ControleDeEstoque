#
# Projeto: Controle de Estoque
# Autora: Aline Torres Guimarães
# Data de criação: 01/12/2022
#


import sys
from abc import ABC, abstractmethod


class ProdutoAbstrato(ABC):
    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def atualizar(self):
        pass

class Produto(ProdutoAbstrato):

    estoque={} # BASE DE DADOS EM MEMÓRIA USANDO UM DICIONÁRIO

    def cadastrar(self): #CADASTRA NOVO PRODUTO

        nome = input("Digite o nome do produto: ")
        preco = str(input("Digite o preço do produto: "))
        peso = str(input("Digite o peso do produto: "))
        qtde_em_estoque = str(input("Quantidade em estoque: "))

        if self.estoque.get(nome): #CHECA SE JÁ EXISTE PRODUTO COM ESTE NOME
            print("Este produto já existe ", nome)
        else:
            self.estoque[nome] = ("Preco:"+preco,"Peso:"+peso,"Quantidade:"+qtde_em_estoque)



    def atualizar(self): # ATUALIZA PRODUTO POR CHAVE, NOME DO PRODUTO
        print(self.estoque)
        nome = input("Produto a atualizar: ")
        preco = str(input("Novo preço do produto: "))
        peso = str(input("Novo peso do produto: "))
        qtde_em_estoque = str(input("Nova quantidade em estoque: "))

        if nome in self.estoque.keys():
            self.estoque[nome] = ("Preco:"+preco,"Peso:"+peso,"Quantidade:"+qtde_em_estoque)
        else: #CHECA SE O PRODUTO EXISTE NO ESTOQUE
            print("Não existe esse produto no estoque")
            self.imprime_estoque()


    def delete(self):  # REMOVER PRODUTO POR CHAVE, NOME DO PRODUTO
        for x in self.estoque:
            print(x)

        prod_delete = input("Digite o nome do produto a ser removido: ")
        self.estoque.pop(prod_delete, None)
        return print("Estoque atualizado:")

    def imprime_estoque(self): # FUNÇÃO PARA IMPRIMIR ESTOQUE NA TELA
        with open('relatorio_estoque.txt', 'r') as f:

            print(f.read().__str__())


    def exporta(self):# FUNÇÃO PARA FAZER A PERSISTÊNCIA EM ARQUIVO TXT
       with open('relatorio_estoque.txt', 'w') as f:

            f.write("===============RELATORIO DE ESTOQUE================")
            f.write('\n')
            f.write("===================================================")
            f.write('\n')
            for line in self.estoque.items():
                lista = ()
                lista = line.__str__()
                f.write(lista.__str__())
                f.write('\n')
            f.write("===================================================")
            f.write('\n')
            f.write("===================================================")
            f.write('\n')

    def exibir_menu(self):

        opcao = input(" 1 - Ver estoque \n 2 - Cadastrar novo produto ao estoque \n"
                          " 3 - Excluir produto do estoque \n 4 - Atualizar cadastro do produto \n 5 - Sair do programa \n Digite a opção desejada: " )
        if opcao.isnumeric(): # TESTE DE VALIDAÇÃO PARA CONTROLE DAS INSERÇÕES
            recebeopcao = int(opcao) # CAST DE CONVERSÃO PARA INTEIRO

            # INÍCIO DO LOOP E EXECUÇÃO DO PROGRAMA
            while recebeopcao != -1:
                if recebeopcao == 1:
                    self.imprime_estoque()
                    self.exporta()
                    self.exibir_menu()

                elif recebeopcao == 2:
                    self.cadastrar()
                    print("==================================")
                    print("novo produto cadastrado")
                    print("==================================")
                    self.exporta()
                    self.exibir_menu()
                elif recebeopcao == 3:
                    self.delete()
                    self.exporta()
                    self.imprime_estoque()
                    self.exibir_menu()
                elif recebeopcao == 4:
                    self.atualizar()
                    self.exporta()
                    self.exibir_menu()
                elif recebeopcao == 5:
                    print("==================================")
                    print("Saindo do programa...")
                    print("==================================")
                    self.exporta()
                    sys.exit()

                else:
                    print("************************************")
                    print("Digite uma opção válida.")
                    print("************************************")
                    self.exibir_menu()
        else: #CHECAGEM SE A FUNÇÃO ESCOLHIDA É UM NÚMERO
           print('não é uma opção valida')
           self.exibir_menu()

if __name__ == '__main__': #MÉTODO MAIN

    execute = Produto()
    execute.exibir_menu()



