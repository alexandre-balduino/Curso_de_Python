'''
Desafio 060

Faça um programa que leia um número 
qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

num = int(input("Digite seu número: "))
fatorial = 1
print(f"{num}! = ", end="")
while num > 0:
    print(f"{num}", end="")
    print(" x " if num>1 else " = ", end="")
    fatorial *= num
    num -= 1
print(f"{fatorial}")
