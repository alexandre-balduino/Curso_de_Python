# Desafio 005

Você recebeu dois relatórios separados do sistema da empresa. O primeiro relatório contém as Vendas do mês, mas possui apenas o ID_Cliente. O segundo relatório é o Cadastro de Clientes, que liga o ID_Cliente ao Nome e à Região dele.
​
Seu objetivo é cruzar essas duas tabelas para gerar um relatório unificado e responder a algumas perguntas da diretoria.
​
### Suas Tarefas:
​
- **O Cruzamento** (O "INNER JOIN" do Pandas): Junte os dois DataFrames em um único chamado df_final usando como base a coluna em comum (ID_Cliente).
> (Dica de ouro: Use o comando `pd.merge(tabela_A, tabela_B, on='Coluna_Em_Comum', how='inner')`).
​
- **Faturamento por Produto**: Utilizando o df_final, calcule e mostre na tela o Faturamento Total de cada produto (Preço × Quantidade). Adicione essa informação como uma nova coluna chamada 'Faturamento'.
​
- **Análise Regional** (Group By): Descubra qual Região gerou o maior faturamento total para a empresa. Agrupe os dados por 'Região' e some o 'Faturamento'.
​
- **Filtro de Elite**: Exiba uma tabela contendo apenas as vendas onde o faturamento por linha foi maior que R$ 1.000,00.
​
### O Código Inicial (com as duas tabelas separadas):

```python
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
```
