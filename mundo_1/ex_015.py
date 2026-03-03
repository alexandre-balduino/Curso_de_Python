'''
Desafio 015

Escreva um programa que pergunte a 
quantidade de Km percorridos por 
um carro alugado e a quantidade de 
dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo 
que o carro custa R$60 por dia e 
R$0,15 por Km rodado.
'''

km = int(input("Quantos quilômetros foram percorridos com o carro? "))
dia = int(input("Por quantos dias o carro foi alugado? "))
valor = dia * 60 + km * 0.15
print(f"O valor a pagar será R${valor} reais")
