'''
Desafio 083

Crie um programa onde o usuário 
digite uma expressão qualquer que 
use parênteses. 
Seu aplicativo deverá analisar se 
a expressão passada está com os 
parênteses abertos e fechados na 
ordem correta.
'''

expressao = str(input("Digite a expressão: "))

pilha = []
for elemento in expressao:
    if elemento == "(":
        pilha.append(elemento)
    if elemento == ")":
        if len(pilha) > 0:
            pilha.pop()
    else:
        print("Não é uma expressão válida")
        break
