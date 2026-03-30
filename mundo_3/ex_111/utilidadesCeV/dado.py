
def leiaDinheiro(msg="Digite o valor: "):
    valido = False
    while not valido:
        num = input(msg).replace(",", ".").strip()
        if num.isalpha() or num == '':
            print(f'ERRO: "{num}" é um preço inválido!')
        else:
            valido = True
            return float(num)