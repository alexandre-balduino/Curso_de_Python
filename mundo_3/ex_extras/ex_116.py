'''
Desafio 116 extra

Crie um programa que leia um arquivo 
de texto e diga:
    quantas linhas tem
    quantas palavras tem    
'''

import os

arquivo = os.path.join(os.path.dirname(__file__), "ex_116.txt")
with open(arquivo, "r", encoding="utf-8") as arq:
    conteudo = arq.read()
    letras = sum(1 for l in conteudo if l.isalpha())
    linhas = len(conteudo.splitlines())
    palavras = len(conteudo.split())
    print(conteudo)
    print(f"Linhas: {linhas}")
    print(f"Palavras: {palavras}")
    print(f"Letras: {letras}")
