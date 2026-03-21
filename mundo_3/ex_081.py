'''
Desafio 081

Crie um programa que vai ler vários 
números e colocar em uma lista. 
Depois disso, mostre:
​A) Quantos números foram digitados.
​B) A lista de valores, ordenada de 
forma decrescente.
​C) Se o valor 5 foi digitado e está 
ou não na lista.
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

lista.sort(reverse=True)

print(f"Os {len(lista)} números que você digitou foram: {lista}")
if 5 in lista:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")

