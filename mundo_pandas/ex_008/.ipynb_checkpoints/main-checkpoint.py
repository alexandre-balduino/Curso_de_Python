
import pandas as pd
import sqlite3

# --- PREPARAÇÃO DO BANCO DE DADOS SIMULADO (Não mexa aqui) ---
# Cria um banco de dados temporário na memória do celular
conexao = sqlite3.connect(':memory:')
cursor = conexao.cursor()

# Cria a tabela estilo banco de dados relacional
cursor.execute('''
    CREATE TABLE visitas (
        id INTEGER PRIMARY KEY,
        Paciente TEXT,
        Idade INTEGER,
        Agravo TEXT,
        Tempo_Minutos INTEGER
    )
''')

# Insere dados de exemplo no banco
dados_exemplo = [
    (1, 'Dona Maria', 65, 'Hipertensão', 25),
    (2, 'Seu José', 72, 'Diabetes', 40),
    (3, 'Ana Júlia', 12, 'Asma', 15),
    (4, 'Carlos Silva', 58, 'Hipertensão', 20),
    (5, 'Dona Francisca', 48, 'Hipertensão', 30),
    (6, 'Seu Antônio', 80, 'Diabetes', 50)
]
cursor.executemany('INSERT INTO visitas VALUES (?, ?, ?, ?, ?)', dados_exemplo)
conexao.commit()
print("-> Banco de dados simulado criado com sucesso! \n")
# -------------------------------------------------------------

# --- DAQUI PARA FRENTE É COM VOCÊ, GAFANHOTO! ---

# 1 e 2. Faça o SELECT usando o Pandas:
# Dica de sintaxe: df = pd.read_sql_query("SEU COMANDO SQL AQUI", conexao)


# 3. Rode o Raio-X estatístico (.describe()):


# 4. Faça a consulta filtrada direto pelo SQL e jogue em um novo DataFrame:


# No final do código, lembre-se sempre de fechar a conexão com o banco:
conexao.close()
