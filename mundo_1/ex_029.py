'''
Desafio 029

Escreva um programa que leia a 
velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre 
uma mensagem dizendo que ele foi 
multado. 
A multa vai custar R$7,00 por cada 
Km acima do limite.
'''

km_h = int(input("Digite a velocidade do carro: "))
if km_h > 80:
    multa = 7 * (km_h - 80)
    print(f"Excesso de velocidade! \nVocê foi multado em R${multa:.2f}")
else:
    print("Tenha uma boa viagem!")
print("Dirija com cuidado")