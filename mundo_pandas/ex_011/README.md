# Desafio 011

Você tem a tabela de Atendimentos com a duração das consultas e o agravo, mas os nomes das doenças estão bagunçados. E você tem a tabela de Pacientes com as idades. Você precisa limpar, cruzar, calcular e extrair a estatística descritiva.

### O Código Inicial:

```python
import pandas as pd

# Tabela 1: Registros de Atendimentos do Consultório
dados_atendimentos = {
    'ID_Atendimento': [1001, 1002, 1003, 1004, 1005, 1006],
    'ID_Paciente': [1, 2, 3, 4, 5, 6],
    'Agravo': [' dengue ', 'gripe', 'DENGUE', ' gripe ', 'Hipertensão', 'hipertensão'],
    'Tempo_Minutos': [25, 15, 30, 20, 45, 40]
}
df_atendimentos = pd.DataFrame(dados_atendimentos)

# Tabela 2: Cadastro de Pacientes (Idades)
dados_pacientes = {
    'ID_Paciente': [1, 2, 3, 4, 5, 6],
    'Nome': ['Carlos', 'Ana', 'Seu Antenor', 'Julia', 'Marcos', 'Eva'],
    'Idade': [24, 28, 88, 26, 52, 54]
}
df_pacientes = pd.DataFrame(dados_pacientes)
```

### Suas Tarefas:

1. **Limpeza de Strings**: Na tabela de atendimentos, os textos da coluna 'Agravo' vieram com espaços e letras misturadas. Padronize a coluna deixando tudo em Maiúsculo e sem espaços nas pontas usando .str.strip().str.upper().

2. **O Cruzamento Perfeito**: Faça um merge (INNER JOIN) entre a tabela de atendimentos e a tabela de pacientes usando a coluna em comum (ID_Paciente). Salve no df_consolidado.

3. **Análise Estatística Descritiva**: Utilizando o seu df_consolidado, agrupe os dados por Agravo e, para a coluna Idade, calcule de uma só vez: a Média, a Mediana e o Desvio Padrão

4. **Interpretação do Analista**: Olhando para o resultado do seu código, printe uma resposta em texto respondendo: Qual agravo possui a maior diferença entre a Média e a Mediana (o que indica a presença de um paciente com idade muito fora do padrão/outlier)?