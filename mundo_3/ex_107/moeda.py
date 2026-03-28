
def dobrar(num):
    return f"{num * 2:.2f}"

def metade(num):
    return f"{num / 2:.2f}"

def aumentar(num, taxa):
    porcent = num * taxa / 100
    return f"{porcent + num:.2f}"

def diminuir(num, taxa):
    porcent = num * taxa / 100
    return f"{porcent - num:.2f}"
