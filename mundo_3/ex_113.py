'''
Desafio 113

Reescreva a função leiaInt() que 
fizemos no desafio 104, incluindo 
agora a possibilidade da digitação 
de um número de tipo inválido. 
Aproveite e crie também uma função 
leiaFloat() com a mesma 
funcionalidade.
'''

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


def leiaFloat(msg="Digite um número: "):
    while True:
        try:
            num = float(input(msg))
            return num
        except (ValueError, TypeError):
            print(f"Erro: Digite um número válido.")
            continue
        except KeyboardInterrupt:
            print("Erro: Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return num


num1 = leiaInt()
num2 = leiaFloat()
print(num1)
print(num2)