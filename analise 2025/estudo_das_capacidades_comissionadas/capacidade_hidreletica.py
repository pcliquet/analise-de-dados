import pandas as pd


# Lê a planilha
df = pd.read_excel('202506 CELA_Intern Case Study_Data.xlsx')

df["Operation/ Commissioning Date"] = pd.to_datetime(df["Operation/ Commissioning Date"], errors='coerce')

df["Ano"] = df["Operation/ Commissioning Date"].dt.year
filtro_capacidade_2012_16 = df[
    (df["Ano"] == 1952) &
    (df["Sector"] == "Small Hydro")&
    (df["Status"] == "Commissioned")
]
filtro_capacidade_2012_16_final = filtro_capacidade_2012_16["Capacity"].sum()
#print(filtro_capacidade_2012_16[["Capacity", "Project Name"]])



#Calculos para 1952
df["Ano"] = df["Operation/ Commissioning Date"].dt.year
filtro_capacidade_1952 = df[
    (df["Ano"] == 1952) &
    (df["Sector"] == "Small Hydro")&
    (df["Status"] == "Commissioned")
]
filtro_capacidade_1952_final = filtro_capacidade_1952["Capacity"].sum()
print("-----------------------------------")
print("Capacidade Small Hydro ")
print(filtro_capacidade_2012_16_final)
print("-----------------------------------")
print(((85.66+filtro_capacidade_2012_16_final)-85.66)/85.66)
print(18.23/filtro_capacidade_2012_16_final)
print(1.1/filtro_capacidade_2012_16_final)
print(38.08/filtro_capacidade_2012_16_final)
print(0.3175+0.0191+0.6632)


#Calculos para 1988

df["Ano"] = df["Operation/ Commissioning Date"].dt.year
filtro_capacidade_1988 = df[
    (df["Ano"] == 1988) &
    (df["Sector"] == "Small Hydro")&
    (df["Status"] == "Commissioned")
]

filtro_capacidade_1988_final = filtro_capacidade_1988["Capacity"].sum()

print("-----------------------------------")
print(f'capacidade total dos projetos: {filtro_capacidade_1988_final}')
print("-----------------------------------")
print(filtro_capacidade_1988[["Capacity", "Project Name"]])


#Max capacidade por projeto
projeto_maior_capacidade = df[
    (df["Sector"] == "Small Hydro") &
    (df["Status"] == "Commissioned")
]

# Ordena pela capacidade em ordem decrescente e pega os 10 primeiros
projeto_maior_capacidade_top10 = projeto_maior_capacidade[["Capacity", "Project Name", "Ano"]].sort_values(
    by="Capacity", ascending=False
).head(10)

print("-----------------------------------")
print(projeto_maior_capacidade_top10)


#Capacidade dos projetos de 1930
projetos_de_1930 = df[
    (df["Ano"] == 1930) &
    (df["Sector"] == "Small Hydro")&
    (df["Status"] == "Commissioned")
]

print("-----------------------------------")
print("Projetos de 1930")
print(projetos_de_1930[["Capacity", "Project Name"]])