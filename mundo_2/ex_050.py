'''
Deaafio 050

Desenvolva um programa que leia 
seis números inteiros e mostre a 
soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, 
desconsidere-o.
'''

soma = 0
for n in range(6):
    num = int(input("Digite um número: "))
    if num%2==0:
        soma += num

print(f"A soma dos números pares é {soma}")