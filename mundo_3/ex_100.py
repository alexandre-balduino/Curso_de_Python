'''
Desafio 100

Faça um programa que tenha uma lista 
chamada números e duas funções 
chamadas sorteia() e somaPar().
- A função sorteia() vai sortear 5 
  números e colocá-los dentro da 
  lista
- A função somaPar() vai mostrar a 
  soma entre todos os valores pares 
  sorteados pela função anterior
'''

from random import randint

def sorteia(lista):
    print("Sorteando 5 valores ", end="")
    for _ in range(5):
        n = randint(0, 100)
        lista.append(n)
        print(n, end=" ")
    print()


def somaPar(lista):
    soma = sum(n for n in lista if n % 2 == 0)
    print(f"A soma entre todos os valores pares digitados é {soma}")


numeros = []
sorteia(numeros)
somaPar(numeros)
