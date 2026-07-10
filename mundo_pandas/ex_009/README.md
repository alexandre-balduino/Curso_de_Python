# Desafio 009

Imagine que você coletou dados novos de visitas de campo em um arquivo local ou dicionário. Sua missão é usar o Pandas para estruturar esses novos dados e inseri-los de uma vez só em uma nova tabela dentro do nosso banco de dados. Depois, para garantir que funcionou, você fará uma consulta SQL básica para ler o que foi salvo.
​
### Seu código inicial:

```python
import pandas as pd
import sqlite3

# 1. Conexão com o banco em memória
conexao = sqlite3.connect(':memory:')

# Dados novos que chegaram do campo e precisam ser salvos no SQL
dados_novos = {
    'Paciente': ['Seu Joaquim', 'Dona Ivone', 'Beatriz Cruz'],
    'Idade': [74, 61, 23],
    'Agravo': ['Diabetes', 'Hipertensão', 'Exame Rotina'],
    'Tempo_Minutos': [35, 20, 15]
}

# --- DAQUI PARA FRENTE É COM VOCÊ, GAFANHOTO! ---

# 1. Transforme o dicionário dados_novos em um DataFrame chamado df_novos:


# 2. Salve o df_novos no banco de dados usando o .to_sql() na tabela 'novas_visitas':


# 3. Use o pd.read_sql_query para dar um SELECT * na tabela 'novas_visitas' e comprove que funcionou:


# Lembre-se sempre de fechar a conexão no final do script!
conexao.close()
```

### Suas Tarefas:

1. **Criar o DataFrame Novo**: Monte o DataFrame com os novos dados de visitas que estão no código inicial abaixo.

2. **Gravar no Banco** (to_sql): Use o comando df.to_sql() para salvar esse DataFrame em uma tabela chamada novas_visitas.

> - Dica de ouro: A sintaxe básica é:

```python
df.to_sql('nome_da_tabela', conexao, if_exists='replace', index=False)
```

> - O parâmetro if_exists='replace' diz ao banco: "Se a tabela já existir, substitua". Se quisesse apenas adicionar linhas a uma tabela existente, usaria 'append'. O index=False evita que o índice do Pandas vire uma coluna no banco.

3. **A Prova Real** (SELECT): Para testar se o banco realmente recebeu os dados, faça um pd.read_sql_query("SELECT * FROM novas_visitas", conexao) e exiba o resultado na tela.
