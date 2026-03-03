'''
Desafio 013

Faça um algoritmo que leia o salário 
de um funcionário e mostre o seu 
novo salário, com 15% de aumento.
'''

salario = float(input("Digite o valor do salário: "))
aumento = salario * 1.15
print(f"Parabéns, você recebeu um aumento! \nO seu salário era R${salario:.2f} reais, com 15% de aumento você receberá R${aumento:.2f} reais.")