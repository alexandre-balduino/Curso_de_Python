# Desafio 010

O secretário de saúde quer um relatório visual impresso direto no console para saber o tempo acumulado de atendimento (em minutos) por cada tipo de Agravo. Você deve puxar esses dados do banco usando SQL, agrupá-los e gerar um gráfico "raiz".

### Seu código inicial:
```python
import pandas as pd
import sqlite3

conexao = sqlite3.connect(':memory:')

dados = [
    (1, 'Dona Maria', 65, 'Hipertensão', 25),
    (2, 'Seu José', 72, 'Diabetes', 40),
    (3, 'Ana Júlia', 12, 'Asma', 15),
    (4, 'Carlos Silva', 58, 'Hipertensão', 20),
    (5, 'Dona Francisca', 48, 'Hipertensão', 30),
    (6, 'Seu Antônio', 80, 'Diabetes', 50)
]
conexao.close()
```

### Suas Tarefas:

1. **Inserção Completa**: Use a mesma conexão do banco em memória e garanta que os dados das visitas estejam salvos na tabela.

2. **Agrupamento SQL**: Faça uma consulta usando pd.read_sql_query que traga o tempo total somado de minutos agrupado por Agravo.
(Dica de SQL: "SELECT Agravo, SUM(Tempo_Minutos) as Total_Minutos FROM novas_visitas GROUP BY Agravo").

3. **O Gráfico Raiz**: Faça um laço (for) que percorra as linhas desse resultado e imprima o nome do Agravo seguido por barras feitas do caractere █ proporcionais ao tempo.
Exemplo de lógica dentro do print: Se o agravo teve 20 minutos, printe █ * 20. Se teve 35, printe █ * 35.
O resultado na tela deve ficar parecido com isso:


```
Diabetes     : ███████████████████████████████████ (35 min)
Exame Rotina : ███████████████ (15 min)
Hipertensão  : ████████████████████ (20 min)
```