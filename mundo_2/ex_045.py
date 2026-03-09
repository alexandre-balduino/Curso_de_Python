'''
Desafio 045

Crie um programa que faça o 
computador jogar Jokenpô com você.
'''

from random import randint
from time import sleep

comp = randint(1,3)
user = int(input('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Escolha uma opção: 
'''))
print("JO")
sleep(0.75)
print("KEN")
sleep(0.75)
print("PÔ")
sleep(0.75)
if user == comp:
    print("Empate")
elif user == 1 and comp == 2:
    print("Você perdeu :(")
elif user == 1 and comp == 3:
    print("Você ganhou :)")
elif user == 2 and comp == 1:
    print("Você ganhou :)")
elif user == 2 and comp == 3:
    print("Você perdeu :(")
elif user == 3 and comp == 1:
    print("Você perdeu :(")
elif user == 3 and comp == 2:
    print("Você ganhou :)")
else:
    print("Opção inválida :[")