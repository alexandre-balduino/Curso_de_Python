'''
Desafio 118

Faça um programa que renomeie um 
arquivo
'''

import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

contador = 1

for nome_arquivo in sorted(os.listdir()):
    if os.path.isfile(nome_arquivo):
        nome, extensao = os.path.splitext(nome_arquivo)
        if extensao.lower() == ".jpg":
            novo_nome = f"foto_{contador}{extensao}"
            print(f"{nome_arquivo} renomeado para {novo_nome}")
            os.rename(nome_arquivo, novo_nome)
            contador += 1
