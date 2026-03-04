'''
Desafio 031

Desenvolva um programa que pergunte 
a distância de uma viagem em Km. 
Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens 
de até 200Km e R$0,45 para viagens 
mais longas.
'''

km = int(input("Digite a distância: "))
if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print(f"A passagem custará {preco}")