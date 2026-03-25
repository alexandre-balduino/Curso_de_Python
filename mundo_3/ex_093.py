'''
Desafio 093

Crie um programa que gerencie o 
aproveitamento de um jogador de 
futebol.
O programa vai ler o nome do jogador 
e quantas partidas ele jogou.
Depois, vai ler a quantidade de 
gols feitos em cada partida.
No final, tudo isso será guardado 
em um dicionário, incluindo o total 
de gols feitos durante o campeonato.
'''

nome = str(input("Digite o nome do jogador: ")).title()
quant = int(input(f"Quantas partidas {nome} jogou? "))
partidas = []
for p in range(quant):
    partidas.append(int(input(f"Quantos gols {nome} fez na {p + 1}ª partida? ")))

jogador = {
    "nome": nome,
    "quantas_partidas": quant,
    "total_de_gols": sum(partidas),
    "gols_por_partida": partidas
}

print(f"\nO jogador {jogador['nome']} jogou {jogador['quantas_partidas']} partidas.")
for i, gols in enumerate(jogador["gols_por_partida"]):
    print(f"- Na partida {i+1}, fez {gols} gols.")
print(f"Foi um total de {jogador['total_de_gols']} gols.")
