'''
Desafio 073

Crie uma tupla preenchida com os 20 
primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, 
na ordem de colocação. 
Depois mostre:
​A) Os 5 primeiros times.
​B) Os últimos 4 colocados.
​C) Times em ordem alfabética.
​D) Em que posição está o time da Chapecoense.
'''

times = (
    "Palmeiras", "São Paulo", "Fluminense", "Bahia", "Flamengo", 
    "Coritiba", "Corinthians", "Red Bull Bragantino", "Grêmio", "Athletico-PR", 
    "Vitória", "Mirassol", "Santos", "Chapecoense", "Atlético-MG", 
    "Vasco", "Botafogo", "Remo", "Internacional", "Cruzeiro"
)

print("Lista de times do Brasileirão 2026:")
for t in times:
    print(t)

print(f"\nOs 5 primeiros são:")
for t in times[0:5]:
    print(t)

print(f"\nOs 4 últimos são:")
for t in times[-4:]:
    print(t)

print(f"\nTimes em ordem alfabética:")
for t in sorted(times):
    print(t)

time_alvo = "Chapecoense"
if time_alvo in times:
    posicao = times.index(time_alvo) + 1
    print(f"O {time_alvo} está na {posicao}ª posição")
else:
    print(f"O time {time_alvo} não foi encontrado na lista.")
