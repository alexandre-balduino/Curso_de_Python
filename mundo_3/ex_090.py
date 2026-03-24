'''
Desafio 090

Faça um programa que leia nome e 
média de um aluno, guardando também 
a situação em um dicionário.
No final, mostre o conteúdo da 
estrutura na tela.
'''

alunos = {}

nome = str(input("Digite o nome do aluno: ")).title()
media = float(input("Digite a media: "))
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"
boletim = {"nome": nome, "media": media, "situacao": situacao}

print(boletim)