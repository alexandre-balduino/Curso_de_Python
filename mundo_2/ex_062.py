'''
Desafio 062

Melhore o Desafio 061, perguntando 
para o usuário se ele quer mostrar 
mais alguns termos. 
O programa encerra quando ele disser 
que quer mostrar 0 termos.
'''

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
cont = termo
fim = termo + razao * 10

while cont < fim:
    print(cont)
    cont += razao
    if cont == fim:
        mais = int(input("Quer mostrar mais quantos? "))
        fim = fim + razao * mais