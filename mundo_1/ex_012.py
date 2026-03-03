'''
Desafio 012

Faça um algoritmo que leia o preço 
de um produto e mostre o seu novo 
preço, com 5% de desconto.
'''

preco = float(input("Digite o preço do produto: "))
desco = preco * 0.95
print(f"O produto que custava R${preco:.2f} reais teve 5% de desconto e está custando R${desco:.2f} reais.")