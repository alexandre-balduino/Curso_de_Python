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

from lib.interface.menu import menu, cabecalho
from lib.arquivo.dado import arquivoExiste, criarArquivo, lerArquivo
from time import sleep
from os import path, system

arq = path.join(path.dirname(__file__), "cursoemvideo.txt")

if  not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcao = menu(
        "Ver pessoas cadastradas", 
        "Cadastrar nova pessoa", 
        "Sair do sistema"
    )
    if opcao == "Ver pessoas cadastradas":
        cabecalho("PESSOAS CADASTRADAS")
        lerArquivo(arq)
        input("Digite 'Enter' para voltar")
        system("clear")
    elif opcao == "Cadastrar nova pessoa":
        print(opcao)
        sleep(0.5)
        system("clear")
    elif opcao == "Sair do sistema":
        print(opcao)
        sleep(0.5)
        system("clear")
        print("Até logo")
        break
