# Desafio 006

Você recebeu um relatório com o registro de visitas de campo de uma equipe. O relatório contém a data da visita (como texto) e o tempo de duração em minutos. Seu chefe precisa de uma análise temporal dessas visitas para planejar o próximo mês.
​
### Suas Tarefas:
​
- **Conversão de Datas**: A coluna 'Data_Visita' veio originalmente como texto. Converta essa coluna para o formato real de data do Pandas (datetime).

> (Dica de ouro: Use `pd.to_datetime(df['Coluna'], format='%Y-%m-%d')`).
​
- **Extração de Períodos**: Crie duas novas colunas no seu DataFrame:
​
> - 'Ano': Extraia apenas o ano da data convertida.
​
> - 'Mes': Extraia apenas o número do mês da data convertida.

>   (Dica: O Pandas permite usar .dt.year e .dt.month em colunas que são do tipo datetime).
​
- **Função Personalizada**: Crie uma função normal em Python chamada classificar_duracao(minutos). Se a visita durou até 30 minutos, retorne 'Rápida'. Se durou entre 31 e 60 minutos, retorne 'Padrão'. Se durou mais de 60 minutos, retorne 'Longa'.

  Aplique essa função no DataFrame criando uma nova coluna chamada 'Classificacao'.

> (Dica: Para aplicar uma função sua em uma coluna inteira, use: `df['Nova_Coluna'] = df['Coluna_Antiga'].apply(sua_funcao)`).
​
- **Contagem por Categoria**: Descubra quantas visitas de cada 'Classificacao' (Rápida, Padrão, Longa) aconteceram no total.

> (Dica: O comando `df['Coluna'].value_counts()` conta quantas vezes cada texto aparece).
​
### O Código Inicial:

```python
# Relatório bruto do sistema de visitas
dados_visitas = {
    'ID_Visita': [1001, 1002, 1003, 1004, 1005, 1006],
    'Data_Visita': ['2026-01-10', '2026-01-15', '2026-02-02', '2026-02-20', '2026-03-05', '2026-03-12'],
    'Duração_Minutos': [20, 45, 15, 80, 35, 120]
}
```
