import requests
from acesso_cnpj import BuscaCnpj
from banco import Banco

while True:
    opcao = input("Digite uma opção: \n0-Sair\n1-Buscar CNPJ\n")
    if int(opcao) == 0:
        break
    if int(opcao) == 1:
        #cnpj = '82110818002760'
        cnpj = input('Digite um cnpj: ')
        objeto_cnpj = BuscaCnpj(cnpj)
        print(objeto_cnpj)

        cnpj, nome, cidade, uf = objeto_cnpj.acessa_via_cnpj()

        print(cnpj, nome, cidade, uf)
        #Credenciais do banco
        #Informe o nome do banco, o usuário e senha se houver
        obj = Banco('aplicacao_db', 'postgres', 'postgres')
        obj.insere_dados_cnpj(cnpj, nome, cidade, uf)
    else:
        print('\nOpção inválida!!!')



