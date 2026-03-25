'''
Desafio 094

Crie um programa que leia nome, 
sexo e idade de várias pessoas, 
guardando os dados de cada pessoa 
em um dicionário e todos os 
dicionários em uma lista.
No final, mostre:
A quantidade de pessoas cadastradas
A média de idade do grupo
Uma lista com todas as mulheres
Uma lista com todas as pessoas com 
idade acima da média
'''

pessoas = []

while True:
    nome = str(input("Digite o nome: ")).strip().title()
    while True:
        sexo = str(input("Digite o sexo: M/F ")).upper()
        if sexo in "MF":
            break
        else:
            print("Digite um valor válido.")
    idade = int(input("Digite a idade: "))
    pessoa = {
        "nome": nome,
        "sexo": sexo,
        "idade": idade
    }
    pessoas.append(pessoa)
    while True:
        opcao = str(input("Quer continuar? S/N")).strip().upper()
        if opcao in "SN":
            break
        else:
            print("Digite um valor válido.")
    if opcao == "N":
        break

#for pessoa in pessoas:
    #print(pessoa)

print(f"\nForam cadastradas {len(pessoas)} pessoas")

media_idade = sum([pessoa["idade"] for pessoa in pessoas]) / len(pessoas)
print(f"A média de idade do grupo é {media_idade:.2f} anos")

mulheres = [p["nome"] for p in pessoas if p["sexo"] == "F"]
print(f"As mulheres cadastradas foram: ", end="")
for i, mulher in enumerate(mulheres):
    print(f"{mulher}", end="")
    if i < len(mulheres) - 1:
        print(", ", end="")
    else:
        print()

acima_da_media = [p["nome"] for p in pessoas if p["idade"] > media_idade]
print(f"As pessoas com idade acima da media são: ", end="")
for i, pessoa in enumerate(acima_da_media):
    print(f"{pessoa}", end="")
    if i < len(acima_da_media) - 1:
        print(", ", end="")
    else:
        print()
