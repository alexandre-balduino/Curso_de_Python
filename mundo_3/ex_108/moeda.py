
def dobrar(num):
    return num * 2

def metade(num):
    return num / 2

def aumentar(num, taxa):
    return num + (num * taxa / 100)

def diminuir(num, taxa):
    return num - (num * taxa / 100)

def moeda(num):
    return f"R${num:.2f}"
