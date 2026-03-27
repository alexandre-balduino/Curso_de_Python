'''
Desafio 104

Crie um programa que tenha a função 
leiaInt(), que vai funcionar de 
forma semelhante à função input() do 
Python, só que fazendo a validação 
para aceitar apenas um valor numérico.
'''

def leiaInt(msg="Digite um número: "):
    while True:
        num = input(msg).strip()
        if num.lstrip("-").isnumeric():
            return int(num)
        else:
            print("Erro! Valor inválido.")


num = leiaInt()
print(f"Você digitou o valor {num}")
