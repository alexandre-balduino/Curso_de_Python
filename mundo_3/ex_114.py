'''
Desafio 114

Crie um código em Python que teste 
se o site do Pudim está acessível 
pelo computador usado.
'''

import urllib.request

try:
    site = urllib.request.urlopen(
        urllib.request.Request(
            "http://www.pudim.com.br",
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )
    )
except Exception as e:
    print('Erro ao acessar:', e)
else:
    print('Consegui acessar o site!')
    print(site.read())