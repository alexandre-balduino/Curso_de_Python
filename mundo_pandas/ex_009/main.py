import pandas as pd
import sqlite3

conexao = sqlite3.connect(':memory:')

dados = {
    'Paciente': ['Seu Joaquim', 'Dona Ivone', 'Beatriz Cruz'],
    'Idade': [74, 61, 23],
    'Agravo': ['Diabetes', 'Hipertensão', 'Exame Rotina'],
    'Tempo_Minutos': [35, 20, 15]
}

df = pd.DataFrame(dados)
print(f"\n1. DataFrame criado com as novas visitas: \n\n{df}")

df.to_sql(
    "novas_visitas",
    conexao,
    if_exists="replace",
    index=False
)
print("\n2. DataFrame com novas visitas salvo na tabela novas_visitas do sqlite.\n")

df2 = pd.read_sql_query(
    "SELECT * FROM novas_visitas",
    conexao
)
print(f"3. DataFrame criado com os dados da tabela novas_visitas do sqlite:\n\n{df2}")

conexao.close()
