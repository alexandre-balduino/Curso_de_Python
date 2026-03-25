'''
Desafio 088

Faça um programa que ajude um jogador 
da Mega Sena a criar palpites.
O programa vai perguntar quantos 
jogos serão gerados e vai sortear 6 
números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
'''

from random import randint

quant = int(input("Quantos jogos: "))
palpite = []
for j in range(quant):
    jogo = []
    for n in range(6):
        jogo.append(randint(1, 60))
    palpite.append(jogo)

for i, j in enumerate(palpite):
    j.sort()
    print(f"{i + 1}ª aposta: {j}")
