'''
Desafio 096

Faça um programa que tenha uma 
função chamada area(), que receba as 
dimensões de um terreno retangular 
(largura e comprimento) e mostre a 
área do terreno.
'''

def area(larg, comp):
    resultado = larg * comp
    print(f"A área de um terreno {larg} x {comp} é {resultado}")

area(50, 100)
