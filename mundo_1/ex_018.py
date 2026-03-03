'''
Desafio 018

Faça um programa que leia um ângulo 
qualquer e mostre na tela o valor 
do seno, cosseno e tangente desse 
ângulo.
'''

from math import radians, sin, cos, tan

angu = float(input("Digite o ângulo: "))
seno = sin(radians(angu))
cose = cos(radians(angu))
tang = tan(radians(angu))
print(f"O ângulo de {angu}° tem: \nO seno de {seno:.2f} \nO cosseno de {cose:.2f} \nE o tangente de {tang:.2f}")
