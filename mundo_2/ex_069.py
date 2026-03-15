'''
Desafio 069

Crie um programa que leia a idade e 
o sexo de várias pessoas. 
A cada pessoa cadastrada, o 
programa deverá perguntar se o 
usuário quer ou não continuar. 
No final, mostre:
​A) Quantas pessoas tem mais de 18 anos.
​B) Quantos homens foram cadastrados.
​C) Quantas mulheres tem menos de 20 anos.
'''

maior_idade = 0
quant_homens = 0
quant_mulher = 0

while True:
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        maior_idade += 1
    while True:
        sexo = str(input("Digite o sexo: M/F ")).upper().strip()[0]
        if sexo in "MF":
            if sexo == "M":
                quant_homens += 1
                break
            elif sexo == "F":
                break
        else:
            print("Digite um valor válido.")
    if idade < 20 and sexo == "F":
        quant_mulher += 1
    while True:
        opcao = str(input("Quer continuar? S/N ")).upper().strip()[0]
        if opcao in "SN":
            break
        else:
            print("Digite uma resposta válida. ")
    if opcao == "N":
        break

print(f"{maior_idade} pessoas tem mais de 18 anos")
print(f"{quant_homens} homens foram cadastrados")
print(f"{quant_mulher} mulheres tem menos de 20 anos")
