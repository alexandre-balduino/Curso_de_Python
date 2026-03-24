'''
Desafio 087

Aprimore o desafio anterior, 
mostrando no final:
- A soma de todos os valores pares 
digitados
- A soma dos valores da terceira 
coluna
- O maior valor da segunda linha
'''

matriz =[[], [], []]
soma_par = soma_col = maior = 0

for lista in range(3):
    for num in range(3):
        matriz[lista].append(int(input("Digite um número: ")))

print("A matriz é:")
for lista in matriz:
    for i, num in enumerate(lista):
        print(f"[{num:^3}]  ", end="")
        if i == 2:
            print()
            soma_col += num
        if num % 2 == 0:
            soma_par += num

print(f"A soma de todos os valores pares digitados é: {soma_par}")
print(f"A soma dos valores da terceira coluna é: {soma_col}")
print(f"O maior valor da segunda linha é: {max(matriz[1])}")
