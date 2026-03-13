'''
Desafio 058

Melhore o jogo do Desafio 028 onde 
o computador "pensa" em um número 
entre 0 e 10. Só que agora o jogador 
vai tentar adivinhar até acertar, 
mostrando no final quantos palpites 
foram necessários para vencer.
'''

from random import randint

print("Pensei em um número de 0 a 5.")
n_comp = randint(0, 10)
n_user = int(input("Tente adivinhar qual foi: "))
tentativas = 1

while n_comp != n_user:
    print("Erro!")
    tentativas += 1
    n_user = int(input("Tente adivinhar qual foi: "))

print("Parabéns! Você acertou.")
print(f"Foram necessárias {tentativas} tentativas para acertar.")
