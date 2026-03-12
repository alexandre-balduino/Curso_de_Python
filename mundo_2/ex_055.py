'''
Desafio 055

Faça um programa que leia o peso de 
cinco pessoas. 
No final, mostre qual foi o maior e 
o menor peso lidos.
'''

maior = 0
menor = 0

for p in range(5):
    peso = float(input("Digite o peso: "))
    if p == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f"O maior peso digitado foi {maior}kg e o menor peso digitado foi {menor}kg")