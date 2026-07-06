import pandas as pd
import numpy as np

# Dados brutos enviados pelo sistema
dados_clientes = {
    'Nome': ['Alexandre', 'Vivian', None, 'Estevão', 'Ester', None],
    'Idade': [28, 26, 35, np.nan, 12, 44],
    'E-mail': ['alexandre@email.com', None, 'compras@email.com', 'estevao@email.com', 'ester@email.com', None],
    'Cidade': ['Paraná', 'Paraná', 'São Paulo', 'Paraná', 'Minas Gerais', 'Bahia']
}

df = pd.DataFrame(dados_clientes)
print(df)

print(f"\n1. Quantidade de dados nulos: \n{df.isnull().sum()}")

df["Nome"] = df["Nome"].fillna("Não Informado")
print(f"\n2. Substituindo nomes nulos por 'Não Informado': \n{df['Nome']}")

df["Idade"] = df["Idade"].fillna(int(df["Idade"].mean()))
print(f"\n3. Substituindo idades nulas pela media de idade: \n{df['Idade']}")

df.dropna(subset=["E-mail"], inplace=True)
print(f"\n4. Registros sem email, apagados")
print(f"\nDataFrame final, limpo e corrigido: \n{df}")

df.to_csv("clientes_limpos.csv", index=False)
print(f"\n5. Dataframe salvo em 'clientes_limpos.csv'")
