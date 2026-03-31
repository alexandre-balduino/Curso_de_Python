
def menu(*opcoes):
    for i, o in enumerate(opcoes):
        print(f"[{i:^3}] {o}")
    print()
    while True:
        res = leiaInt("Digite o número da opção: ")
        if 0 <= res < len(opcoes):
            break
        else:
            print(f"Erro. Digite um número entre 0 e {len(opcoes) - 1}")
    return opcoes[res]


def leiaInt(msg="Digite um número: "):
    while True:
        try:
            num = int(input(msg))
            return num
        except (ValueError, TypeError):
            print(f"Erro: Digite um número inteiro válido.")
            continue
        except KeyboardInterrupt:
            print("Erro: Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return num