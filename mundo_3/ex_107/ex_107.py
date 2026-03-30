'''
Desafio 107

Crie um módulo chamado moeda.py que 
tenha funções incorporadas para 
aumentar, diminuir, dobrar e reduzir 
os preços, retornando os valores com 
duas casas decimais.
'''

import moeda

preco = float(input("Digite o preço: R$ "))

print(f"A metade de R${preco:.2f} é {moeda.metade(preco)}")
print(f"O dobro de R${preco:.2f} é {moeda.dobrar(preco)}")
print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10)}")
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13)}')
