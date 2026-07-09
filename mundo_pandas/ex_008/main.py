
import pandas as pd
import sqlite3

# --- PREPARAÇÃO DO BANCO DE DADOS SIMULADO (Não mexa aqui) ---
# Cria um banco de dados temporário na memória do celular
conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()

# Cria a tabela estilo banco de dados relacional
cursor.execute(
    """
    CREATE TABLE visitas (
        id INTEGER PRIMARY KEY,
        Paciente TEXT,
        Idade INTEGER,
        Agravo TEXT,
        Tempo_Minutos INTEGER
)
    """
)

# Insere dados de exemplo no banco
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
    "SELECT * FROM visitas",
    conexao
)
print(df)

print(df.describe())


df2 = pd.read_sql_query(
    """
    SELECT * FROM visitas
    WHERE Idade > 50 AND Agravo = 'Hipertensão'
    """,
    conexao
)
print(df2)

conexao.close()
