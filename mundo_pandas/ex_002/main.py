import pandas as pd

dados_informatica = {
    'Produto': ['Notebook Dell', 'Teclado Mecânico', 'Monitor LG 29"', 'Mouse Gamer', 'Impressora HP', 'SSD 1TB'],
    'Categoria': ['Notebooks', 'Periféricos', 'Monitores', 'Periféricos', 'Printers', 'Armazenamento'],
    'Preço': [4200.00, 250.00, 1350.00, 180.00, 890.00, 410.00],
    'Estoque': [5, 15, 4, 22, 3, 18]
}

df = pd.DataFrame(dados_informatica)
print(df)

print(f"\n1. Produtos que pertencem à categoria 'Periféricos': \n\n{df[df['Categoria'] == 'Periféricos']}")

print(f"\n2. Produtos estão com menos de 5 unidades no estoque: \n\n{df[df['Estoque'] < 5]}")

print(f"\n3. Tabela ordenada do produto mais caro ao mais barato: \n\n{df.sort_values('Preço', ascending=False)}")

print(f"\n4. Nome e Preço do produto da linha 4: \n\n{df.loc[4, ['Produto', 'Preço']]}
