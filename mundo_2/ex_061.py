'''
Desafio 061

Refaça o Desafio 051, lendo o 
primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da 
progressão usando a estrutura while.
'''

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
cont = termo
fim = termo + razao * 10

while cont < fim:
    print(cont)
    cont += razao
