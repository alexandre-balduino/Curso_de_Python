'''
Desafio 102

Crie um programa que tenha uma 
função fatorial(), que receba dois 
parâmetros:
- o número a calcular o fatorial
- um parâmetro opcional chamado show, 
que será um valor lógico (True/False)
Se show for True, será mostrado o 
cálculo do fatorial.
Caso contrário, será mostrado apenas 
o resultado final.
'''

def fatorial(num, show=False):
    fator = 1
    for n in range(num, 0, -1):
        fator *= n
    if show:
        print(f"{num}! = ", end="")
        for n in range(num, 0, -1):
            print(n, end="")
            print(" x " if n>1 else " = ", end="")
    print(fator)


fatorial(6)
fatorial(5, True)
