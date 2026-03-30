
def dobrar(num=0, formato=False):
    res = num * 2
    return res if not formato else moeda(res)

def metade(num=0, formato=False):
    res = num / 2
    return res if not formato else moeda(res)

def aumentar(num=0, taxa=0, formato=False):
    res = num + (num * taxa / 100)
    return res if not formato else moeda(res)

def diminuir(num=0, taxa=0, formato=False):
    res = num - (num * taxa / 100)
    return res if not formato else moeda(res)

def moeda(num=0):
    return f"R${num:.2f}"

def resumo(num=0, taxa_aum=0, taxa_red=0):
    print('-' * 32)
    print('RESUMO DO VALOR'.center(32))
    print('-' * 32)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobrar(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(num, taxa_aum, True)}')
    print(f'{taxa_red}% de redução: \t{diminuir(num, taxa_red, True)}')
    print('-' * 32)