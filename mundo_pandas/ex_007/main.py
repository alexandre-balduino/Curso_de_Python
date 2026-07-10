import pandas as pd

# Relatório bruto de atendimentos
dados_atendimentos = {
    'ID_Registro': [1, 2, 3, 4, 5, 6, 7, 8],
    'Bairro': ['Centro', 'Vila Nova', 'Centro', 'Vila Nova', 'Centro', 'Subúrbio', 'Vila Nova', 'Subúrbio'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro', 'Março', 'Março'],
    'Agravo/Doença': [' dengue ', 'DENGUE', ' Gripe', 'gripe', 'Dengue', 'Gripe ', ' Covid', 'COVID']
}

df = pd.DataFrame(dados_atendimentos)
print(df)

print("\n1. Padronizando os nomes da coluna 'Agravo/Doença':\n")
df["Agravo/Doença"] = df["Agravo/Doença"].str.strip().str.upper()
print(df["Agravo/Doença"])

print("\n2. Criando DataFrame 'matriz_atendimentos':\n")
matriz_atendimentos = df.pivot_table(
    index="Bairro",
    columns="Mês",
    values="Agravo/Doença",
    aggfunc="count",
    fill_value=0
)
print(matriz_atendimentos)

print("\n3. Adicionando nova linha com a com a soma de atendimentos:\n")
matriz_atendimentos.loc["Total"] = matriz_atendimentos.sum()
print(matriz_atendimentos)
