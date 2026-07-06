# Desafio 004

Você recebeu uma planilha de cadastro de clientes de uma plataforma online. Porém, a tabela está cheia de informações faltando (None ou NaN). O seu chefe quer que você limpe esses dados seguindo regras de negócio específicas e, no final, salve o resultado limpo em um arquivo CSV.
​
### Suas Tarefas:

​- **Identificar o problema**: Mostre na tela quantos dados nulos/faltantes existem em cada coluna da tabela.
> (Dica: Use df.isnull().sum()).
​
- **Tratar os nomes**: Quem não preencheu o nome deve receber o texto "Não Informado".
> (Dica: Para preencher dados nulos em uma coluna específica, usamos: df['Coluna'] = df['Coluna'].fillna('Valor')).
​
- **Tratar as idades**: Quem não preencheu a idade deve receber a média de idade dos outros clientes da tabela.
> (Dica: Você pode calcular a média com df['Idade'].mean() e depois usar o fillna nessa coluna).
​
- **Remover Linhas Críticas**: Clientes que não informaram o E-mail não servem para a campanha de marketing. Delete as linhas onde o e-mail esteja nulo.
> (Dica: Para apagar linhas com valores nulos baseando-se em uma coluna, usamos: df.dropna(subset=['Coluna'], inplace=True)).
​
- **Exportar**: Salve o seu DataFrame final, totalmente limpo e corrigido, em um arquivo chamado clientes_limpos.csv.
> (Dica: Use df.to_csv('nome_do_arquivo.csv', index=False) para salvar sem exportar a coluna de índices numéricos).
​
---

### O Código Inicial (com os dados "sujos"):

Como o Pandas usa a biblioteca numpy para representar valores nulos numéricos (NaN), vamos importar o numpy apenas para gerar a tabela inicial:

```python
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
```
