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

print(f"A metade de {preco:.2f} é {moeda.metade(preco)}")
print(f"O dobro de {preco:.2f} é {moeda.dobrar(preco)}")
print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10)}")
