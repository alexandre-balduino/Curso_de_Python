
def dobrar(num):
    return f"R${num * 2:.2f}"

def metade(num):
    return f"R${num / 2:.2f}"

def aumentar(num, taxa):
    return f"R${num + (num * taxa / 100):.2f}"

def diminuir(num, taxa):
    return f"R${num - (num * taxa / 100):.2f}"
