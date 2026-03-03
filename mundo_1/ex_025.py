'''
Desafio 025

Crie um programa que leia o nome 
de uma pessoa e diga se ela tem “
SILVA” no nome.
'''

nome = input("Digite seu nome: ")
print(f"Seu nome tem SILVA? {'SILVA' in nome.upper()}")