import pandas as pd

# Tabela A: Movimentação de Vendas
dados_vendas = {
    'ID_Cliente': [101, 102, 101, 103, 102, 104],
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Notebook', 'Teclado'],
    'Preço': [4000.00, 150.00, 250.00, 1200.00, 4000.00, 250.00],
    'Quantidade': [1, 2, 3, 1, 1, 5]
}
df_vendas = pd.DataFrame(dados_vendas)

# Tabela B: Cadastro de Clientes
dados_cadastro = {
    'ID_Cliente': [101, 102, 103, 104],
    'Nome_Cliente': ['Alexandre', 'Vivian', 'Estevão', 'Ester'],
    'Região': ['Sul', 'Sul', 'Sudeste', 'Nordeste']
}
df_cadastro = pd.DataFrame(dados_cadastro)

print(f"\nTabela de vendas: \n{df_vendas}")
print(f"\nTabela de Cadastro: \n{df_cadastro}")

df_final = pd.merge(df_vendas, df_cadastro, on="ID_Cliente", how="inner")
print(f"\n1. Juntando os dois DataFrames: \n{df_final}")

df_final["Faturamento"] = df_final["Preço"] * df_final["Quantidade"]
print(f"\n2. Calculando faturamento: \n{df_final}")

print(f"\n3. Faturamento por região: \n{df_final.groupby('Região')['Faturamento'].sum()}")

print(f"\n4. Faturamento maior que R$1000,00: \n{df_final[df_final['Faturamento'] > 1000]}")
