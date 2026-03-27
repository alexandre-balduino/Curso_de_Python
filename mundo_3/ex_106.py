'''
Desafio 106

Faça um mini sistema que utilize o 
Interactive Help do Python.
O usuário vai digitar o nome de um 
comando e o programa vai mostrar o 
manual desse comando.
Quando o usuário digitar "FIM", o 
programa deve encerrar.
'''

def ajuda():
    while True:
        cmd = input("Digite o nome da Função ou Biblioteca: ").strip()
        if cmd == "fim":
            break
        else:
            help(cmd)


ajuda()
