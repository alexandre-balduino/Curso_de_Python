'''
Desafio 016

Crie um programa que leia um 
número Real qualquer pelo teclado e 
mostre na tela a sua porção Inteira.

# Opção usando int():
num = float(input("Digite um valor real: "))
print(f"A porção inteira de {num} é {int(num)}")
'''

from math import trunc

num = float(input("Digite um valor real: "))
print(f"A porção inteira de {num} é {trunc(num)}")
