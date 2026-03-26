'''
Desafio 095

Aprimore o desafio 093 para que ele 
funcione com vários jogadores, 
incluindo um sistema de visualização 
de detalhes do aproveitamento de 
cada jogador.
O programa deve:
- Ler os dados de vários jogadores 
(nome, partidas e gols por partida)
- Guardar tudo em uma lista de 
dicionários
- Mostrar uma tabela com:
  - Código do jogador
  - Nome
  - Lista de gols
  - Total de gols
- Permitir que o usuário escolha um 
jogador pelo código para ver os 
dados detalhados (gols por partida)
'''

jogadores = []

while True:
    nome = str(input("Digite o nome do jogador: ")).title()
    quant = int(input(f"Quantas partidas {nome} jogou? "))
    partidas = []
    for p in range(quant):
        partidas.append(int(input(f"Quantos gols {nome} fez na {p + 1}ª partida? ")))
    jogador = {
        "nome": nome,
        "total_de_gols": sum(partidas),
        "gols_por_partida": partidas
    }
    jogadores.append(jogador)
    while True:
        opcao = str(input("Deseja cadastrar mais jogadores? S/N ")).strip().upper()
        if opcao in "SN":
            break
    if opcao == "N":
        break

print(f"{'ID':>3} | {'NOME':<12}| {'GOLS':<5}| {'GOLS POR PARTIDA'}")
for k, jogador in enumerate(jogadores):
    print(f'{k:>3} | ', end='')
    for i, dado in enumerate(jogador.values()):
        if i == 0:
            print(f"{dado:<12}| ", end="")
        elif i == 1:
            print(f"{dado:<5}| ", end="")
        else:
            print(dado)

while True:
    opcao = int(input("Digite o ID do jogador para ver mais informações ou 999 para parar: "))
    if opcao == 999:
        break
    elif 0 < opcao >= len(jogadores):
        print(f"Erro! Não existe jogador com o codigo {opcao}")
    else:
        print(f"Infornações sobre o jogador {jogadores[opcao]['nome']}")
        print(f"{jogadores[opcao]['nome']} jogou {len(jogadores[opcao]['gols_por_partida'])} partidas")
        for i, g in enumerate(jogadores[opcao]["gols_por_partida"]):
            print(f"- No jogo {i+1} fez {g} gols.")
        print(f"Um total de {jogadores[opcao]['total_de_gols']} gols")
