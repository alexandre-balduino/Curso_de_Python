'''
Desafio 041

A Confederação Nacional de Natação 
precisa de um programa que leia o 
ano de nascimento de um atleta e 
mostre sua categoria, de acordo 
com a idade:
– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''

from datetime import datetime

ano_atual = datetime.now().year
ano_nasc = int(input("Digite o ano de nascimento do atleta: "))
idade = ano_atual - ano_nasc

if idade < 10:
    print("Mirim")
elif idade < 15:
    print("Infantil")
elif idade < 20:
    print("Junior")
elif idade < 26:
    print("Sênior")
else:
    print("Master")