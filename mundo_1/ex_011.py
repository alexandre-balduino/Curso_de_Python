'''
Desafio 011

Faça um programa que leia a largura 
e a altura de uma parede em metros, 
calcule a sua área e a quantidade 
de tinta para pintá-la, sabendo que 
cada litro de tinta pinta uma área 
de 2m².
'''

larg = float(input("Qual a largura da parede? "))
altu = float(input("Qual a altura da parede? "))
area = larg * altu
tint = area / 2
print(f"Uma parede com {larg} metros de largura e {altu} metros de altura tem uma área de {area} metros quadrados \nSerão preciso {tint} litros de tinta para pintá-la.")