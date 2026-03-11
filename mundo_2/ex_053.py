'''
Desafio 053

Crie um programa que leia uma frase 
qualquer e diga se ela é um 
palíndromo, desconsiderando os 
espaços. 
Exemplos de palíndromos:

APÓS A SOPA, 
A SACADA DA CASA, 
A TORRE DA DERROTA, 
O LOBO AMA O BOLO, A
NOTARAM A DATA DA MARATONA.
'''

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo!')
