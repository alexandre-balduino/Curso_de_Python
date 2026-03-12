'''
Desafio 056

Desenvolva um programa que leia o 
nome, idade e sexo de 4 pessoas. 
No final do programa, mostre:
- ​A média de idade do grupo.
- ​Qual é o nome do homem mais velho.
- ​Quantas mulheres têm menos de 20 anos
'''

total_idade: int = 0
nome_homem_velho: str = ""
idade_homem_velho: int = 0
quant_mulher_nova: int = 0

for p in range(4):
    nome = str(input(f"Digite o nome da {p + 1}ª pessoa: "))
    idade = int(input("Digite a idade: "))
    total_idade += idade
    sexo = str(input("Digite o sexo (M/F): ")).upper()
    
    if sexo[0] == "M":
        if p == 0:
            nome_homem_velho: str = nome
            idade_homem_velho: int = idade
        else:
            if idade > idade_homem_velho:
                nome_homem_velho: str = nome
                idade_homem_velho: int = idade
    elif sexo[0] == "F" and idade < 20:
        quant_mulher_nova += 1
        
media_idade: float = total_idade / 4

print(f"A média de idade do grupo é {media_idade} anos")
print(f"O homem mais velho é {nome_homem_velho} com {idade_homem_velho} anos")
print(f"{quant_mulher_nova} mulheres tem menos de 20 anos")
