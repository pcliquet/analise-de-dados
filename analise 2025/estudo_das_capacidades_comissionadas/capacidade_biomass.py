import pandas as pd


# Lê a planilha
df = pd.read_excel('202506 CELA_Intern Case Study_Data.xlsx')

df["Operation/ Commissioning Date"] = pd.to_datetime(df["Operation/ Commissioning Date"], errors='coerce')


#Query da capacidade do Setor Biomass & Waste 2013 - 2016
df["Ano"] = df["Operation/ Commissioning Date"].dt.year
filtro_capacidade_2012_16 = df[
    #(df["Ano"] <= 2013) &
    (df["Sector"] == "Biomass & Waste")&
    (df["Status"] == "Commissioned")
]
filtro_capacidade_2012_16_final = filtro_capacidade_2012_16["Capacity"].sum()
print("Capacidade Biomass & Waste ")
print(filtro_capacidade_2012_16_final)