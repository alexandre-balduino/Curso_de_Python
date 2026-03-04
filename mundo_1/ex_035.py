'''
Desafio 035

Desenvolva um programa que leia o 
comprimento de três retas e diga 
ao usuário se elas podem ou não 
formar um triângulo.
'''
reta1 = int(input("Digite o tamanho da primeira reta: "))
reta2 = int(input("Digite o tamanho da segunda reta: "))
reta3 = int(input("Digite o tamanho da terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("As retas acima podem formar um triângulo")
else:
    print("As retas acima não podem formar um triângulo")
