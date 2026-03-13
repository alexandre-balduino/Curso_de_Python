'''
Desafio 059

Crie um programa que leia dois 
valores e mostre um menu:
1. ​Somar 
2. Multiplicar 
3. Maior 
4. Novos números 
5. Sair do programa.
Seu programa deve realizar a 
operação solicitada em cada caso.
'''

from os import system
from time import sleep

opcao = 0
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while opcao != 5:
    opcao = int(input(
'''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
'''
    ))
    if opcao == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opcao == 2:
        print(f"{num1} x {num2} = {num1 * num2}")
    elif opcao == 3:
        if num1 > num2:
            print(f"{num1} é maior que {num2}")
        elif num2 > num1:
            print(f"{num2} é maior que {num1}")
        else:
            print("Não existe maior, os dois números são iguais!")
    elif opcao == 4:
        print("Informe os números novamente...")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    elif opcao == 5:
        print("Até logo!")
    else:
        print("Opção inválida.")
    sleep(1.5)
    system("clear")
print("Até logo!")