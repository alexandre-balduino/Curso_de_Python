'''
Desafio 111

Crie um pacote chamado utilidadesCeV 
que tenha dois módulos internos 
chamados moeda e dado. 
Transfira todas as funções 
utilizadas nos desafios anteriores 
para o módulo moeda, mantendo tudo 
funcionando. 
No módulo dado, crie uma função 
chamada leiaDinheiro() que seja 
capaz de funcionar como um input(), 
mas com uma validação de dados para 
aceitar apenas valores que sejam 
monetários.”
'''

from utilidadesCeV import moeda, dado

valor = dado.leiaDinheiro()
moeda.resumo(valor, 80, 35)
