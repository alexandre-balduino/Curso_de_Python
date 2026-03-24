'''
Desafio 089

Crie um programa que leia nome e 
duas notas de vários alunos e guarde 
tudo em uma lista composta.
No final, mostre um boletim contendo 
a média de cada um e permita que o 
usuário possa mostrar as notas de 
cada aluno individualmente.
'''

alunos = []

while True:
    nome = str(input("Digite o nome do aluno: ")).title()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    boletim = [nome, nota1, nota2, media]
    alunos.append(boletim[:])
    while True:
        opcao = str(input("Deseja cadastrar mais um aluno? S/N ")).strip().upper()
        if opcao in "SN":
            break
        else:
            print("Digite uma resposta válida.")
    if opcao == "N":
        break

print(f"\nBoletim: \n{'NOME':<20} | {'MEDIA'}")
for b in alunos:
    print(f"{b[0]:<20} | {b[3]:^5}")

while True:
    while True:
        opcao = str(input("Deseja continuar? S/N ")).strip().upper()
        if opcao in "SN":
            break
        else:
            print("Digite uma resposta válida.")
    if opcao == "N":
        break
    for i, a in enumerate(alunos):
        print(f"[ {i} ]  {a[0]}")
    while True:
        opcao = int(input("Digite o número do aluno para ver as notas individuais: "))
        if 0 <= opcao <= len(alunos):
            print(f"{'NOME':<12} | {'NOTA1':^5} | {'NOTA2':^5} | {'MEDIA':^5}")
            print(f"{alunos[opcao][0]:<12} | {alunos[opcao][1]:^5} | {alunos[opcao][2]:^5} | {alunos[opcao][3]:^5}")
        while True:
            opcao = str(input("Deseja ver mais notas individuais? S/N ")).strip().upper()
            if opcao in "SN":
                break
            else:
                print("Digite uma resposta válida.")
        if opcao == "N":
            break
