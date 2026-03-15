'''
Desafio 070

Crie um programa que leia o nome e 
o preço de vários produtos. 
O programa deverá perguntar se o 
usuário vai continuar. 
No final, mostre:
​A) Qual é o total gasto na compra.
​B) Quantos produtos custam mais de R$ 1000.
​C) Qual é o nome do produto mais barato.
'''

total_gasto = produto_caro = produto_barato = cont = 0
nome_produto_barato = ""

while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    total_gasto += preco
    if preco > 1000:
        produto_caro += 1
    cont += 1
    if cont == 1:
        produto_barato = preco
        nome_produto_barato = nome
    else:
        if preco < produto_barato:
            produto_barato = preco
            nome_produto_barato = nome
    while True:
        opcao = str(input("Deseja continuar? S/N ")).upper().strip()[0]
        if opcao in "SN":
            break
        else:
            print("Digite uma opção válida.")
    if opcao == "N":
        break

print(f"O total da compra é {total_gasto}")
print(f"{produto_caro} produtos custam mais de R$1000,00")
print(f"{nome_produto_barato} é o produto mais barato, custando R${produto_barato:.2f}")
