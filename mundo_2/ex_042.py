'''
Desafio 042

Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar 
que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''

reta1 = int(input("Digite o tamanho da primeira reta: "))
reta2 = int(input("Digite o tamanho da segunda reta: "))
reta3 = int(input("Digite o tamanho da terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        print("Equilátero")
    elif reta1 != reta2 != reta3 != reta1:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Não é possível formar um triângulo :(")