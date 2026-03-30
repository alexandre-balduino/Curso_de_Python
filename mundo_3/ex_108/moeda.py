
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
