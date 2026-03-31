
def linha(tam):
    print("-" * tam)
    
    
def cabecalho(titulo, tam=32):
    linha(tam)
    print(titulo.center(tam))
    linha(tam)


def menu(*opc):
    cabecalho("MENU PRINCIPAL", 32)
    for i, o in enumerate(opc):
        print(f"[{i:^3}] {o}")
    linha(32)
    while True:
        res = leiaInt("Digite o número da opção: ")
        if 0 <= res <= len(opc)-1:
            break
        else:
            print(f"Erro. Digite uma resposta válida")
    return opc[res]


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