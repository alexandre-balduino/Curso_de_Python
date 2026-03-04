'''
Desafio 034

Escreva um programa que pergunte o 
salário de um funcionário e calcule 
o valor do seu aumento. 
Para salários superiores a R$1250,00, 
calcule um aumento de 10%. 
Para os inferiores ou iguais, o 
aumento é de 15%.
'''

salario = float(input("Digite o salário atual: "))
if salario <= 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.1
print(f"Parabéns! Você recebeu um aumento. \nSeu novo salário será de R${aumento:.2f}")