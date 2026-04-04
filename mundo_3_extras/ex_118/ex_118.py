'''
Desafio 118

Faça um programa que renomeie um 
arquivo
'''

import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())
for dir in os.listdir():
    if os.path.isfile(dir):
        nome, extensao = os.path.splitext(dir)
        #print(nome, extensao)
        if extensao == ".jpg":
            print(f"{dir} é uma foto")
            print("deve ser renomeada")
        elif extensao == ".py":
            print(f"{dir} é codigo")