'''
Desafio 109

Modifique as funções que foram 
criadas no exercício 108 para que 
elas aceitem um parâmetro a mais, 
informando se o valor retornado deve 
ser ou não formatado pela função 
moeda(), desenvolvida no exercício 108.
'''

import moeda

preco = float(input("Digite o preço: R$ "))

print(f"A metade de R${preco:.2f} é {moeda.metade(preco, True)}")
print(f"O dobro de R${preco:.2f} é {moeda.dobrar(preco, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}")
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}')
