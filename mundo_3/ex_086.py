'''
Desafio 086

Crie um programa que declare uma 
matriz de dimensão 3x3 e preencha 
com valores lidos pelo teclado.
No final, mostre a matriz na tela, 
com a formatação correta.
'''

matriz =[[], [], []]

for lista in range(3):
    for num in range(3):
        matriz[lista].append(int(input("Digite um número: ")))

print("A matriz é:")
for lista in matriz:
    for i, num in enumerate(lista):
        print(f"[ {num} ] ", end="")
        if i == 2:
            print()
