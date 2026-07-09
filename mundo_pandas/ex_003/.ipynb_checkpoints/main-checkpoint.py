import pandas as pd

dados_informatica = {
    'Produto': ['Notebook Dell', 'Teclado Mecânico', 'Monitor LG 29"', 'Mouse Gamer', 'Impressora HP', 'SSD 1TB'],
    'Categoria': ['Notebooks', 'Periféricos', 'Monitores', 'Periféricos', 'Printers', 'Armazenamento'],
    'Preço': [4200.00, 250.00, 1350.00, 180.00, 890.00, 410.00],
    'Estoque': [5, 15, 4, 22, 3, 18]
}

df = pd.DataFrame(dados_informatica)
print(df)

print(f"\n1. A categoria da linha 4 era {df.loc[4, 'Categoria']} e foi modificada para ", end="")
df.loc[4, "Categoria"] = "Periféricos"
print(df.loc[4, "Categoria"])

print(f"\n2. Os preços eram:\n{df[['Produto', 'Preço']]} \nReceberam 10% de aumento e foram para:")
df["Preço"] = df["Preço"] * 1.1
print(df[["Produto", "Preço"]])

print(f"\n3. Estoque total de produtos por categoria: \n{df.groupby('Categoria')['Estoque'].sum()}")
