'''
Faça um programa que leia o ano de 
nascimento de um jovem e informe, 
de acordo com a sua idade, se ele 
ainda vai se alistar ao serviço 
militar, se é a hora exata de se 
alistar ou se já passou do tempo 
do alistamento. 
Seu programa também deverá mostrar 
o tempo que falta ou que passou do 
prazo.
'''

from datetime import datetime
ano_atual = datetime.now().year
ano_nasc = int(input("Em que ano você nasceu? "))
idade = ano_atual - ano_nasc

if idade < 18:
    print(f"Ainda não é a hora de se alistar! falta {18 - idade} anos")
elif idade == 18:
    print("Está na hora de se alistar!")
else:
    print(f"Você deveria ter se alistado à {idade - 18} anos")