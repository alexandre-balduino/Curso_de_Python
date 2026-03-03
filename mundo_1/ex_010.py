'''
Desafio 010

Crie um programa que leia quanto 
dinheiro uma pessoa tem e mostre 
quantos dólares ela pode comprar.

Considere:
U$$1.00 = R$5.23
'''

real = float(input("Quantos reais você tem? "))
dolar = real / 5.23
print(f"Com R${real:.2f} reais você pode comprar U$${dolar:.2f} dólares")