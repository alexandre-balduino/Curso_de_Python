'''
Desafio 044

Elabore um programa que calcule o 
valor a ser pago por um produto, 
considerando o seu preço normal e 
condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço normal 

– 3x ou mais no cartão: 20% de juros
'''

valor = float(input("Digite o valor do produto: "))
pagamento = int(input('''
[ 1 ] A vista dinheiro/pix
[ 2 ] A vista cartão de crédito
[ 3 ] Parcelado

Escolha a forma de pagamento: 
'''))

if pagamento == 1:
    print(f"O produto custará {valor * 0.9}")
elif pagamento == 2:
    print(f"O produto custará {valor * 0.95}")
elif pagamento == 3:
    parcela = int(input("Em quantas vezes você vai pagar? "))
    if parcela == 2:
        print(f"O produto custará {valor}")
    elif parcela > 2:
        print(f"O produto custará {valor * 1.2}")
    else:
        print("Opção inválida :(")
else:
    print("Opção inválida :(")
