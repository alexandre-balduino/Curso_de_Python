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

print("--- TABELA DE VENDAS ---")
print(df_vendas)
print("\n--- TABELA DE CLIENTES ---")
print(df_cadastro)
print("-" * 30)
