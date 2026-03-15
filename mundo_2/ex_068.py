'''
Desafio 068

Faça um programa que jogue par ou 
ímpar com o computador. 
O jogo só será interrompido quando 
o jogador PERDER, mostrando o total 
de vitórias consecutivas que ele 
conquistou no final do jogo.
'''

from random import randint

vitor = 0

while True:
    while True:
        escolha = int(input("[ 0 ] Par \n[ 1 ] Ímpar \n"))
        
        if escolha == 0:
            escolha = "par"
            print("Você escolheu par! o computador escolheu ímpar!")
            break
        elif escolha == 1:
            escolha = "impar"
            print("Você escolheu ímpar! o computador escolheu par!")
            break
        else:
            print("Opção inválida! Tente de novo!")
    
    n_comp = randint(0, 10)
    n_user = int(input("Digite um número: "))
    print(f"Você escolheu {n_user}! O computador escolheu {n_comp}")
    
    if (n_comp + n_user) % 2 == 0:
        result = "par"
        print("Par")
    else:
        result = "impar"
        print("Ímpar")
    
    if escolha == result:
        print("Você venceu!")
        vitor += 1
    else:
        break
print(f"Game Over! Você ganhou {vitor} partidas")