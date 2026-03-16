'''
Desafio 075

Crie um programa que vai gerar cinco 
números aleatórios e colocar em uma 
tupla. 
Depois disso, mostre a listagem de 
números gerados e também indique o 
menor e o maior valor que estão na 
tupla.
'''

from random import randint

numeros = (randint(1, 10) for n in range(5))

print('Os valores sorteados foram: ', end='')
maior = menor = 0
for i, n in enumerate(numeros):
    if i == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
