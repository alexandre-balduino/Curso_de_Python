'''
Desafio 065

Crie um programa que leia vários 
números inteiros. 
No final da execução, mostre a média 
entre todos os valores e qual foi o 
maior e o menor valores lidos. 
O programa deve perguntar ao 
usuário se ele quer ou não 
continuar a digitar valores.
'''

respo = "S"
maior = cont = menor = soma = 0

while respo in "S":
    num = int(input("Digite um valor: "))
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    cont += 1
    respo = str(input("Quer continuar? S/N ")).upper().strip()[0]

media = soma / cont

print(f"A media entre os {cont} valores digitados é {media}")
print(f"O maior valor digitado foi {maior}")
print(f"E o menor valor digitado foi {menor}")
