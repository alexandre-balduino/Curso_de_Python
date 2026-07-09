# Desafio 008

Imagine que o sistema de prontuários ou visitas da sua unidade de saúde salva tudo em um banco de dados MariaDB/MySQL. O seu chefe quer que você puxe esses dados usando comandos SQL de dentro do Python, use o Pandas para fazer uma análise descritiva completa (.describe()) e filtre os resultados.
​
Para que você consiga rodar esse código direto no seu celular (Termux/Jupyter) sem precisar configurar um servidor de banco de dados externo agora, nós vamos simular um banco de dados local na memória usando a biblioteca sqlite3 

### Seu código inicial:

```python
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

```

### Suas tarefas:

1. **Criar a Conexão**: Crie a conexão com o banco de dados simulado e carregue a tabela inicial (o código para criar o banco já está pronto ali embaixo).
​
2. **O Grande SELECT**: Use o comando pd.read_sql_query() para executar um SELECT * FROM visitas e trazer os dados do banco direto para um DataFrame do Pandas.
​
3. **O Raio-X Estatístico**: Use o método .describe() do Pandas para exibir na tela o resumo estatístico das colunas numéricas (Idade e Tempo de Atendimento).
​
4. **Filtro SQL Avançado**: Faça uma nova consulta ao banco trazendo apenas os registros onde a Idade seja maior que 50 anos E o Agravo seja igual a 'Hipertensão'. Exiba essa tabela final.
