'''
Desafio 112

Dentro do pacote utilidadesCeV que 
criamos no desafio anterior, temos 
um módulo chamado moeda. 
Crie uma nova pasta chamada dados e 
mova a função leiaDinheiro() para lá. 
Faça com que o programa principal 
continue funcionando normalmente, 
importando corretamente os módulos 
e pacotes.
'''

from utilidadesCeV.moeda import moeda
from utilidadesCeV.dado import dado

valor = dado.leiaDinheiro()
moeda.resumo(valor, 80, 35)
