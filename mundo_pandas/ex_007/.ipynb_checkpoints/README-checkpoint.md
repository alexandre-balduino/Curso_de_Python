# Desafio 007

Você recebeu um relatório de registros de atendimentos de saúde comunitária. Porém, os nomes das doenças foram digitados de qualquer jeito pelos agentes, e o relatório final precisa cruzar os bairros com os meses de atendimento em formato de matriz para a gestão tomar decisões.
​
### Suas Tarefas:
​
- **Padronização de Texto** (Limpeza de Strings): Os nomes na coluna 'Agravo/Doença' vieram bagunçados (ex: " dengue ", "DENGUE", "Dengue"). Deixe todos os textos dessa coluna padronizados: sem espaços em branco nas pontas e com todas as letras em maiúsculo.

> (Dica de ouro: O Pandas permite aplicar funções de string usando .str. Você pode usar `df['Coluna'].str.strip().str.upper()`).
​
- **Criar a Tabela Dinâmica** (Pivot Table): Crie um novo DataFrame chamado matriz_atendimentos que cruze as informações da seguinte forma:
​  
  - As Linhas devem ser os Bairros.
​
  - As Colunas devem ser os Meses.
​
  - Os Valores internos devem ser a Contagem de atendimentos que aconteceram naquele cruzamento.

  > (Dica: Use `df.pivot_table(index='Coluna_Linha', columns='Coluna_Coluna', values='Coluna_Valor', aggfunc='count', fill_value=0)`. O fill_value=0 serve para colocar o número 0 onde não houve nenhum atendimento).
​
- **Totalizadores**: Adicione uma linha final chamada "TOTAL" na sua Tabela Dinâmica que mostre a soma de atendimentos de cada mês (soma das colunas).

> (Dica: `matriz_atendimentos.loc['TOTAL'] = matriz_atendimentos.sum()`).
​
### O Código Inicial:

```python
# Relatório bruto de atendimentos
dados_atendimentos = {
    'ID_Registro': [1, 2, 3, 4, 5, 6, 7, 8],
    'Bairro': ['Centro', 'Vila Nova', 'Centro', 'Vila Nova', 'Centro', 'Subúrbio', 'Vila Nova', 'Subúrbio'],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro', 'Março', 'Março'],
    'Agravo/Doença': [' dengue ', 'DENGUE', ' Gripe', 'gripe', 'Dengue', 'Gripe ', ' Covid', 'COVID']
}
```
