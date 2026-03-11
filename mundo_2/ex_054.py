'''
Desafio 054

Crie um programa que leia o ano de 
nascimento de sete pessoas. 
No final, mostre quantas pessoas 
ainda não atingiram a maioridade e 
quantas já são maiores.
'''

from datetime import datetime

ano_atual = datetime.now().year
maior = 0
menor = 0

for p in range(7):
    ano_nasc = int(input("Digite o ano de nascimento: "))
    if ano_atual - ano_nasc >= 18:
        maior += 1
    else:
        menor += 1

print(f"{maior} pessoas são maiores de idade e {menor} pessoas são menores de idade")