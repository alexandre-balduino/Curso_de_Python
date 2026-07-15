
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

print(df_atendimentos)
print(df_pacientes)

df_atendimentos["Agravo"] = df_atendimentos["Agravo"].str.strip().str.upper()
print(df_atendimentos["Agravo"])

df_consolidado = pd.merge(
    df_pacientes,
    df_atendimentos,
    on="ID_Paciente",
    how="inner"
)
print(df_consolidado)

print(df_consolidado.groupby("Agravo")["Idade"].agg(["mean", "median", "std"]))

print("O Agravo com maior diferença de idade é: Dengue")
