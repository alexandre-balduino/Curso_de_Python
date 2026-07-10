
import pandas as pd
import sqlite3

conexao = sqlite3.connect(':memory:')
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE visitas (
        id INTEGER PRIMARY KEY,
        Paciente TEXT,
        Idade INTEGER,
        Agravo TEXT,
        Tempo_Minutos INTEGER
    )
""")

dados = [
    (1, "Dona Maria", 65, "Hipertensão", 25),
    (2, "Seu José", 72, "Diabetes", 40),
    (3, "Ana Júlia", 12, "Asma", 15),
    (4, "Carlos Silva", 58, "Hipertensão", 20),
    (5, "Dona Francisca", 48, "Hipertensão", 30),
    (6, "Seu Antônio", 80, "Diabetes", 50)
]
cursor.executemany(
    "INSERT INTO visitas VALUES (?, ?, ?, ?, ?)",
    dados
)
conexao.commit()

df = pd.read_sql_query(
    """
    SELECT Agravo, SUM(Tempo_Minutos) as Total_Minutos
    FROM visitas GROUP BY Agravo
    """,
    conexao
)
print(df)

tam = df["Agravo"].str.len().max()
for l1, l2 in zip(df["Agravo"], df["Total_Minutos"]):
    print(f"{l1:<{tam+1}}: \n{'█'*l2} ({l2} min)\n")
