'''
Desafio 022

Crie um programa que leia o nome 
completo de uma pessoa e mostre:
– O nome com todas as letras 
maiúsculas e minúsculas.
'''

nome = str(input("Digite seu nome: ")).strip()
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")
primeiro = nome.split()
print(f"Seu primeiro nome é {primeiro[0]} e tem {len(primeiro[0])} letras")