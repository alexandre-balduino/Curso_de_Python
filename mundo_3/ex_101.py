'''
Desafio 101

Crie um programa que tenha uma 
função chamada voto(), que vai 
receber como parâmetro o ano de 
nascimento de uma pessoa, 
retornando um valor literal 
indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATÓRIO nas 
eleições.
'''

from datetime import datetime

def voto(ano_nasc):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc
    if idade < 16:
        return f"Com idade {idade} anos o voto é NEGADO"
    elif idade < 18 or idade >= 65:
        return f"Com idade {idade} anos o voto é OPCIONAL"
    elif idade < 65:
        return f"Com idade {idade} anos o voto é OBRIGATÓRIO"


print(voto(1998))
print(voto(2010))
print(voto(2015))
print(voto(1958))
