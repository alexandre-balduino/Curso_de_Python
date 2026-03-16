'''
Desafio 078

Faça um programa que leia 5 valores 
numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e 
o menor valor digitado e as suas 
respectivas posições na lista.
'''

numeros = []
for n in range(5):
    numeros.append(int(input("Digite um número: ")))
print(f"Você digitou os números {numeros}")
maior = max(numeros)
menor = min(numeros)
print(f"O maior número digitado foi {max(numeros)} nas posições ", end="")
for pos, num in enumerate(numeros):
    if num == maior:
        print(f"{pos}... ", end="")
print()
print(f"E o menor número digitado foi {min(numeros)} nas posições ", end="")
for pos, num in enumerate(numeros):
    if num == menor:
        print(f"{pos}... ", end="")
print()
