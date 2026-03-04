'''
Desafio 033

Faça um programa que leia três 
números e mostre qual é o maior e 
qual é o menor.
'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = num1
if num2 > num1:
    maior = num2
if num3 > num1:
    maior = num3
print(f"O maior número é o {maior}")
