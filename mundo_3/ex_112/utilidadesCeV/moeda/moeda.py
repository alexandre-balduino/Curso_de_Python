
__all__ = ['aumentar', 'diminuir', 'dobrar', 'metade', 'moeda', 'resumo']


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return moeda(res) if formato else res


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return moeda(res) if formato else res


def dobrar(preco=0, formato=False):
    res = preco * 2
    return moeda(res) if formato else res


def metade(preco=0, formato=False):
    res = preco / 2
    return moeda(res) if formato else res


def moeda(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def resumo(preco=0, taxa_aum=0, taxa_red=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco):>10}')
    print(f'Dobro do preço: {dobrar(preco, True):>10}')
    print(f'Metade do preço: {metade(preco, True):>10}')
    print(f'{taxa_aum}% de aumento: {aumentar(preco, taxa_aum, True):>10}')
    print(f'{taxa_red}% de redução: {diminuir(preco, taxa_red, True):>10}')
    print('-' * 30)
