'''
Desafio 063

Escreva um programa que leia um 
número n inteiro qualquer e mostre 
na tela os n primeiros elementos de 
uma Sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

num = int(input("Digite um número: "))

termo1 = 0
termo2 = 1

print(f'{termo1} -> {termo2}', end='')

cont = 3
while cont <= num:
    termo3 = termo1 + termo2
    print(f' -> {termo3}', end='')
    
    termo1 = termo2
    termo2 = termo3
    cont += 1