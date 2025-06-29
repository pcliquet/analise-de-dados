import pandas as pd


# Lê a planilha
df = pd.read_excel('202506 CELA_Intern Case Study_Data.xlsx')

df["Operation/ Commissioning Date"] = pd.to_datetime(df["Operation/ Commissioning Date"], errors='coerce')

#Query da capacidade do Setor Solar 2013 - 2016
df["Ano"] = df["Operation/ Commissioning Date"].dt.year
filtro_capacidade_2012_16 = df[
    #(df["Ano"] <=2013) &
    (df["Sector"] == "Solar") &
    (df["Status"] == "Commissioned")
]
filtro_capacidade_2012_16_final = filtro_capacidade_2012_16["Capacity"].sum()
print("-----------------------------------")
print("Soma de todas as capacidades")
print(filtro_capacidade_2012_16_final)



#Primeiro Projeto Comissionado Solar
df["Ano"] = df["Operation/ Commissioning Date"].dt.year
primeiro_projeto_solar = df[
    (df["Ano"] == 1994) &
    (df["Sector"] == "Solar") &
    (df["Status"] == "Commissioned")
]
primeiro_projeto_solar_final = primeiro_projeto_solar["Capacity"].sum()
print("-----------------------------------")
print("Primeiro Projeto Solar ")
print(primeiro_projeto_solar[["Capacity", "Project Name"]])


df["Ano"] = df["Operation/ Commissioning Date"].dt.year
primeiro_projeto_solar = df[
    (df["Sector"] == "Solar") &
    (df["Status"] == "Commissioned")
]
primeiro_projeto_solar_final = primeiro_projeto_solar["Capacity"].sum()
print("-----------------------------------")
print("Primeiro Projeto Solar ")
print(primeiro_projeto_solar[["Capacity", "Project Name"]])