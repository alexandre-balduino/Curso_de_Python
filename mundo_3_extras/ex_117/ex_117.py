'''
Desafio 117 extra

Leia o conteudo da pasta atual e 
permita ao usuário selecionar uma
pasta ou arquivo e responda se é uma 
pasta ou arquivo
'''

import os

while True:
    print("\nDiretório atual:", os.getcwd())

    arquivos = os.listdir()

    for i, item in enumerate(arquivos):
        print(f"[{i}] {item}")

    escolha = input("Digite o número (ou 'sair', 'voltar'): ")

    if escolha == "sair":
        break
        
    elif escolha == "voltar":
        os.chdir("..")
        
    elif escolha.isdigit():
        item = arquivos[int(escolha)]

        if os.path.isdir(item):
            os.chdir(item)
        else:
            print("Isso é um arquivo")
