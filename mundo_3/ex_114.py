'''
Desafio 114

Crie um código em Python que teste 
se o site do Pudim está acessível 
pelo computador usado.
'''

import urllib.request

url = 'http://www.pudim.com.br'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

req = urllib.request.Request(url, headers=headers)

try:
    site = urllib.request.urlopen(req)
except Exception as e:
    print('Erro ao acessar:', e)
else:
    print('Consegui acessar o site!')
    print(site.read())