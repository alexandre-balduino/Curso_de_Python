'''
Desafio 051

Desenvolva um programa que leia o 
primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros 
termos dessa progressão.
'''

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))

for n in range(termo, (termo + razao * 10), razao):
    print(n)