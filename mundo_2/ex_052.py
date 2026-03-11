'''
Desafio 052

Faça um programa que leia um número 
inteiro e diga se ele é ou não um 
número primo.
'''

num = int(input("Digite um número: "))
total = 0
for n in range(1, num + 1):
    if num%n==0:
        total += 1
if total == 2:
    print("É primo")
else:
    print("Não é primo")