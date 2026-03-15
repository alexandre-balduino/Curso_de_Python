'''
Desafio 066

Crie um programa que leia vários 
números inteiros. 
O programa só para quando o usuário 
digitar 999. 
No final, mostre quantos números 
foram digitados e qual foi a soma 
entre eles (usando break).
'''

cont = 0
soma = 0

while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    cont += 1
    soma += num

print(f"Você digitou {cont} números e a soma entre eles é {soma}")