'''
Desafio 036

Escreva um programa para aprovar o 
empréstimo bancário para a compra 
de uma casa. Pergunte o valor da 
casa, o salário do comprador e em 
quantos anos ele vai pagar. A 
prestação mensal não pode exceder .
30% do salário ou então o 
empréstimo será negado.
'''

valor = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o salário do comprador: "))
parcela = int(input("Em quantos anos você pretende pagar? ")) * 12
valor_parcela = valor / parcela
if valor_parcela <= (salario * 0.3):
    print("Parabéns! o empréstimo foi aprovado!")
    print(f"O imóvel será comprado em {parcela} parcelas de R${valor_parcela:.2f}")
else:
    print("Empréstimo negado :(")