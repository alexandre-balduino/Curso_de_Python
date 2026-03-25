'''
Desafio 092

Crie um programa que leia nome, 
ano de nascimento e carteira de 
trabalho e cadastre-os (com idade) 
em um dicionário.
Se por acaso a CTPS for diferente 
de ZERO, o dicionário receberá 
também o ano de contratação e o 
salário.
Calcule e acrescente, além da idade, 
com quantos anos a pessoa vai se 
aposentar.
'''

from datetime import datetime

nome = str(input("Digite o nome: ")).title()
ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nasc

pessoa = {
    "nome": nome,
    "nasc": ano_nasc,
    "idade": idade
}

if idade >= 16:
    ctps = int(input("Digite o número da carteira de trabalho: (0 se não tiver) "))
    if ctps != 0:
        ano_contrat = int(input("Em que ano você começou a trabalhar? "))
        salario = float(input("Digite o salário R$"))
        pessoa["ctps"] = ctps
        pessoa["ano_contratacao"] = ano_contrat
        pessoa["salario"] = salario
        pessoa["aposentadoria"] = idade + ((ano_contrat + 35) - ano_atual)

print()
for dado in pessoa.items():
    print(f"{dado[0].upper():<15} | {dado[1]}")
