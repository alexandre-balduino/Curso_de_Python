'''
Desafio 017

Faça um programa que leia o 
comprimento do cateto oposto e 
do cateto adjacente de um 
triângulo retângulo. 
Calcule e mostre o comprimento da 
hipotenusa.

# Opção usando a fórmula de báscara:
opost = int(input("Digite o cumprimento do cateto oposto: "))
adjac = int(input("Digite o cumprimento do cateto adjacente: "))
hipot = (opost ** 2 + adjac ** 2) ** 0.5
print(f"O cateto oposto é {opost}, o cateto adjacente é {adjac} e a hipotenusa é {hipot:.1f}")
'''

from math import hypot

opost = int(input("Digite o cumprimento do cateto oposto: "))
adjac = int(input("Digite o cumprimento do cateto adjacente: "))
hipot = hypot(opost, adjac)
print(f"O cateto oposto é {opost}, o cateto adjacente é {adjac} e a hipotenusa é {hipot:.1f}")
