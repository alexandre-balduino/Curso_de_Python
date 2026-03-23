'''
Desafio 084

Faça um programa que leia nome e 
peso de várias pessoas, guardando 
tudo em uma lista. 
No final, mostre:"
​A) Quantas pessoas foram cadastradas.
​B) Uma listagem com as pessoas mais 
pesadas.
​C) Uma listagem com as pessoas mais 
leves.
'''

lista = []
quant = maior_peso = menor_peso = 0

while True:
    pessoa = []
    nome = str(input("Digite o nome: "))
    pessoa.append(nome)
    peso = float(input("Digite o peso: "))
    pessoa.append(peso)
    if quant == 0:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
    lista.append(pessoa[:])
    quant += 1
    while True:
        opcao = str(input("Quer continuar? S/N ")).upper()
        if opcao in "SN":
            break
        else:
            print("Digite uma opção válida.")
    if opcao == "N":
        break

print()
print(f"Foram cadastradas {quant} pessoas: {lista,}")
print("As pessoas mais pesadas foram: ",end="")
for pessoa in lista:
    if pessoa[1] == maior_peso:
        print(f"{pessoa[0]}... ", end="")
print(f" com {maior_peso}kg.")

print("As pessoas menos pesadas foram: ",end="")
for pessoa in lista:
    if pessoa[1] == menor_peso:
        print(f"{pessoa[0]}... ", end="")
print(f" com {menor_peso}kg.")
