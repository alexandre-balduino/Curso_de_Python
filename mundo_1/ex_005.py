'''
Desafio 005

Faça um programa que leia um número 
inteiro e mostre na tela o seu 
sucessor e o seu antecessor.
'''

num = int(input("Digite um número: "))
ant = num - 1
suc = num + 1
print(f"O número digitado foi {num}")
print(f"O antecessor é {ant}")
print(f"E o sucessor é {suc}")
