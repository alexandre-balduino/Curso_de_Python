'''
Desafio 098

Faça um programa que tenha uma 
função chamada contador(), que 
receba três parâmetros: 
    início, 
    fim e 
    passo, 
e realize a contagem.
'''

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim:
        passo = abs(passo)
        fim += 1
    else:
        passo = -abs(passo)
        fim -= 1
    for cont in range(inicio, fim, passo):
        print(cont, end=" ")
    print()


contador(1, 10, 1)
contador(10, 0, -2)
contador(5, 30, 3)
contador(2, 12, 0)
contador(2, 2, 1)
