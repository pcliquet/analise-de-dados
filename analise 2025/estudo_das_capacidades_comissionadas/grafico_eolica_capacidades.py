import pandas as pd
import matplotlib.pyplot as plt

# Lê a planilha
df = pd.read_excel('202506 CELA_Intern Case Study_Data.xlsx')

# Converte data e extrai ano
df["Operation/ Commissioning Date"] = pd.to_datetime(
    df["Operation/ Commissioning Date"], format="%Y-%m-%d", errors='coerce'
)
df["Ano"] = df["Operation/ Commissioning Date"].dt.year

# Filtra projetos solares com status "Commissioned"
projetos_solares = df[
    (df["Sector"] == "Wind") &
    (df["Status"] == "Commissioned")
]

# Capacidade total por ano
capacidade_por_ano = projetos_solares.groupby("Ano")["Capacity"].sum()

# Identifica todos os anos que aparecem no filtro (mesmo que a soma seja 0)
anos_comissionados = projetos_solares["Ano"].dropna().unique()
anos_comissionados = sorted([int(ano) for ano in anos_comissionados])

print(anos_comissionados)
# Garante que todos os anos com projetos estejam presentes
capacidade_por_ano = capacidade_por_ano.reindex(anos_comissionados, fill_value=0)

# Cria gráfico
plt.figure(figsize=(12, 6))
plt.plot(anos_comissionados, capacidade_por_ano.values, marker='o', color='orange')

plt.title("Capacidade Eolica Instalada por Ano (MW)", fontsize=14, color='green')
plt.xlabel("Ano")
plt.ylabel("Capacidade Instalada (MW)")

# 👇 Força todos os anos como rótulos no eixo X
plt.xticks(anos_comissionados, rotation=45)

plt.grid(True)
plt.tight_layout()

# Salva com fundo transparente
plt.savefig("grafico_capacidade_eolica_por_ano.png", dpi=300, transparent=True)
# plt.show()
