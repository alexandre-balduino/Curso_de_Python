'''
Desafio 046

Faça um programa que mostre na 
tela uma contagem regressiva para 
o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 
1 segundo entre eles.
'''

from time import sleep
from os import system

for i in range(10, 0, -1):
    print(i)
    sleep(1)
    system("clear")
print("Acabou")
