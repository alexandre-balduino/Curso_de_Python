'''
Desafio 028

Escreva um programa que faça o 
computador “pensar” em um número 
inteiro entre 0 e 5 e peça para o 
usuário tentar descobrir qual foi 
o número escolhido pelo computador. 
O programa deverá escrever na tela 
se o usuário venceu ou perdeu.
'''

from random import randint

print("Pensei em um número de 0 a 5.")
n_comp = randint(0, 5)
n_user = int(input("Tente adivinhar qual foi: "))
if n_comp == n_user:
    print("Parabéns! Você acertou.")
else:
    print(f"Você escolheu {n_user} mas o computador escolheu {n_comp}. Não foi dessa vez, tente de novo!")
