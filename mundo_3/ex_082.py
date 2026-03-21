'''
Desafio 082

Crie um programa que vai ler vários 
números e colocar em uma lista. 
Depois disso, crie duas listas extras 
que vão conter apenas os valores 
pares e os valores ímpares digitados, 
respectivamente. 
Ao final, mostre o conteúdo das 
três listas geradas
'''

lista = []

while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    while True:
        opcao = str(input("Quer continuar? S/N ")).upper()
        if opcao in "SN":
            break
        else:
            print("Digite uma resposta válida.")
    if opcao == "N":
                break

pares = []
impares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("-" * 32)
print(f"Os números digitados foram: {lista}")
print(f"O números pares foram: {pares}")
print(f"Os ímpares foram: {impares}")
