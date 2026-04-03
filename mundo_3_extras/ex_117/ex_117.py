'''
Desafio 117 extra

Leia o conteudo da pasta atual e 
permita ao usuário selecionar uma
pasta ou arquivo e responda se é uma 
pasta ou arquivo
'''

import os
def menu(pasta):
    os.chdir(pasta)
    print(os.getcwd())
    pasta = []
    for dir in os.listdir():
        pasta.append(dir)
    for i, p in enumerate(pasta):
        print(f"[{i:^5}] {p}")
    try:
        num_pasta = int(input("Digite o número da pasta: "))
    except (ValueError, TypeError):
        print("Digite um valor válido.")
    else:
        if os.path.isdir(pasta[num_pasta]):
            print(f"{pasta[num_pasta]} é uma pasta")
            return pasta[num_pasta]
        else:
            print(f"{pasta[num_pasta]} não é uma pasta")


base = os.getcwd()
menu(base)
