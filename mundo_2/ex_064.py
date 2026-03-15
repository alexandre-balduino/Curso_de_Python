'''
Desafio 064

Crie um programa que leia vários 
números inteiros pelo teclado. 
O programa só vai parar quando o 
usuário digitar o valor 999 
(condição de parada). 
No final, mostre quantos números 
foram digitados e qual foi a soma 
entre eles (desconsiderando o flag).
'''

num = int(input("Digite um valor: "))
soma = 0
quant = 0
while num != 999:
    soma += num
    quant += 1
    num = int(input("Digite um valor: "))
print(f"Foram digitados {quant} números e a soma entre eles é {soma}")
