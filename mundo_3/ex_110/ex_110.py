'''
Desafio 110

Adicione ao módulo moeda.py criado 
nos desafios anteriores, uma função 
chamada resumo(), que mostre na tela 
algumas informações geradas pelas 
funções que já temos no módulo 
criado até aqui.”
'''

import moeda

preco = float(input("Digite o preço: R$ "))
aumento = int(input("Qual a taxa de aumento: "))
reducao = int(input("Qual a taxa de reducao: "))

#print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}")
#print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobrar(preco, True)}")
#print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}")
#print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}')
moeda.resumo(preco, aumento, reducao)