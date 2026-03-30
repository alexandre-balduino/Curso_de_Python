
def dobrar(num, formato=False):
    res = num * 2
    return res if not formato else moeda(res)

def metade(num, formato=False):
    res = num / 2
    return res if not formato else moeda(res)

def aumentar(num, taxa, formato=False):
    res = num + (num * taxa / 100)
    return res if not formato else moeda(res)

def diminuir(num, taxa, formato=False):
    res = num - (num * taxa / 100)
    return res if not formato else moeda(res)

def moeda(num):
    return f"R${num:.2f}"
