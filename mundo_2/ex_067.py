'''
Desafio 067

Faça um programa que mostre a 
tabuada de vários números, um de 
cada vez, para cada valor digitado 
pelo usuário. 
O programa será interrompido quando 
o número solicitado for negativo.
'''

while True:
    num = int(input("Digite um número: "))
    if num > 0:
        cont = 1
        for n in range(1, 11):
            print(f"{num} x {cont} = {num * cont}")
            cont += 1
    else:
        break