'''
Desafio 091

Crie um programa onde 4 jogadores 
joguem um dado e tenham resultados 
aleatórios.
Guarde esses resultados em um 
dicionário.
No final, coloque esse dicionário 
em ordem, sabendo que o vencedor 
tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {}

for j in range(4):
    jogo[f"jogador{j + 1}"] = randint(1, 6)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, p in enumerate(ranking):
    if i == 0:
        print("\n🥇", end= "")
    elif i == 1:
        print("🥈", end="")
    elif i == 2:
        print("🥉", end="")
    elif i == 3:
        print("  ", end="")
    print(f"{i + 1}º lugar: {p[0]} com {p[1]} pontos")
    sleep(0.5)
