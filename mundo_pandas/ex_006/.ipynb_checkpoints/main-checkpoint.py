import pandas as pd

# Relatório bruto do sistema de visitas
dados_visitas = {
    'ID_Visita': [1001, 1002, 1003, 1004, 1005, 1006],
    'Data_Visita': ['2026-01-10', '2026-01-15', '2026-02-02', '2026-02-20', '2026-03-05', '2026-03-12'],
    'Duração_Minutos': [20, 45, 15, 80, 35, 120]
}

df = pd.DataFrame(dados_visitas)
print(df)

print(f"\n1. Convertendo datas de string \n{df['Data_Visita']}\npara datetime:", end="")
df["Data_Visita"] = pd.to_datetime(df["Data_Visita"], format="%Y-%m-%d")
print(f"\n{df['Data_Visita']}")

print(f"\n2. Criando novas colunas para ano e mês: ")
df["Ano"] = df["Data_Visita"].dt.year
df["Mês"] = df["Data_Visita"].dt.month
print(df[['Ano', 'Mês']])

print("\n3. Classificando visitas como 'Rápida', 'Padrão' e 'Longa'")

def classificar_duracao(minutos):
    if minutos <= 30:
        return "Rápida"
    elif minutos <= 60:
        return "Padrão"
    else:
        return "Longa"

df["Classificação"] = df["Duração_Minutos"].apply(classificar_duracao)
print(df["Classificação"])

print(f"\n4. Quantas visitas de cada classificação: \n{df['Classificação'].value_counts()}")
