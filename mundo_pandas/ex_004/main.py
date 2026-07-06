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
print("--- DATAFRAME ORIGINAL ---")
print(df)
print("-" * 26)
