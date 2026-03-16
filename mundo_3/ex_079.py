'''
Desafio 079

Crie um programa onde o usuário 
possa digitar vários valores 
numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, 
ele não será adicionado. 
No final, serão exibidos todos os 
valores únicos digitados, em ordem 
crescente.
'''

valores = []

while True:
    num = int(input("Digite um valor: "))
    if num not in valores:
        valores.append(num)
    else:
        print("Erro! O valor já existe na lista.")
    while True:
        opcao = str(input("Quer continuar? S/N ")).upper().strip()[0]
        if opcao in "SN":
            break
        else:
            print("Digite uma resposta válida.")
    if opcao == "N":
        break

print(f"Você digitou os valores: {sorted(valores)}")
