'''
Desafio 115

Vamos criar um menu em Python, 
usando modularização. 
Crie um sistema simples com as 
seguintes opções:
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema
O sistema deve armazenar os dados 
em um arquivo de texto e utilizar 
funções para cada funcionalidade.
'''

from lib.interface import menu

opcao = menu.menu("Ver", "Cadastrar", "Sair")
print(opcao)
