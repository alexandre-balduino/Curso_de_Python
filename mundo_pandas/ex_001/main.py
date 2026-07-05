import pandas as pd


dados_loja = {
    'Produto': ['Teclado Mecânico', 'Mouse Wireless', 'Monitor 24"', 'Headset RGB'],
    'Preço': [250.00, 120.00, 899.90, 310.00],
    'Estoque': [15, 30, 7, 12]
}

df = pd.DataFrame(dados_loja)

print(f"\n1. A tabela completa: \n\n{df}")

print(f"\n2. As duas primeiras linhas \n\n{df.head(2)}")

print(f"\n3. A estrutura dos dados é: \n")
df.info()

novo_produto = {
    "Produto": ["Gabinete Gamer"],
    "Preço": [450],
    "Estoque": [8]
}
df = pd.concat(
    [
        df,
        pd.DataFrame(novo_produto)
    ],
    ignore_index=True
)
print(f"\n4. Produto adicionado: \n{df.iloc[len(df)-1]}")

total = (df["Preço"] * df["Estoque"]).sum()
print(f"\n5. O total do estoque da loja é: R${total:.2f}")
