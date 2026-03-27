'''
Desafio 099

Faça um programa que tenha uma função 
chamada maior(), que receba vários 
parâmetros com valores inteiros.
Seu programa tem que analisar todos 
os valores e dizer qual deles é o 
maior.
'''

def maior(*args):
    if len(args) == 0:
        print("Você não digitou nenhum número \nNão existe valor maior.")
    else:
        maior_valor = args[0]
        for num in args:
            if num > maior_valor:
                maior_valor = num
        print(f"Você digitou {len(args)} números \nO maior valor digitado foi {maior_valor}")


maior(4, 6, 2)
maior(7)
maior()
