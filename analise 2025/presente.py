import pandas as pd
import matplotlib.pyplot as plt
import os

# Lê a planilha
df = pd.read_excel('202506 CELA_Intern Case Study_Data.xlsx')

# Converte datas e extrai ano
df["Operation/ Commissioning Date"] = pd.to_datetime(df["Operation/ Commissioning Date"], errors='coerce')
df["Ano"] = df["Operation/ Commissioning Date"].dt.year

# Define status e setores
status_list = [
    'Comissioned'
]
fator_capacidade_solar = 0.19
fator_capacidade_eolica = 0.38
sector_list = [
    'Solar', 'Wind', 'Biofuels', 'Biomass & Waste',
    'Small Hydro', 'Geothermal', 'Marine'
]

filtro_capacidade_2012_16 = df[
    (df["Ano"] <= 2021) &
    (df["Status"] == "Commissioned")
]
total_capacidades = filtro_capacidade_2012_16["Capacity"].sum()
print("Soma das Capacidades ate 2021")
print(total_capacidades)

energia_produzida_2021 = 240000000*(1-0.28)
energia_produzida_2021_n = 240000000*(0.28)
print(f'Energia produzida {energia_produzida_2021}')
print("")

filtro_quantidade_solar = df[
    (df["Ano"] <= 2021) &
    (df["Status"] == "Commissioned") &
    (df["Sector"] == 'Solar')
]
total_projetos_solar = len(filtro_quantidade_solar)
capacidade_solar = filtro_quantidade_solar["Capacity"].sum()
print("-------------------------")
print("Total de projetos solar")
print(total_projetos_solar)
print(capacidade_solar)
print("-------------------------")
print("Geração em 1 ano solar")
print(capacidade_solar * fator_capacidade_solar * 8760)

filtro_quantidade_eolico = df[
    (df["Ano"] <= 2021) &
    (df["Status"] == "Commissioned") &
    (df["Sector"] == 'Wind')
]
total_projetos_eolica = len(filtro_quantidade_eolico)
capacidade_eolica = filtro_quantidade_eolico["Capacity"].sum()
print("-------------------------")
print("Total de projetos eolica")
print(total_projetos_eolica)
print(capacidade_eolica)
print("-------------------------")
print("Geração em 1 ano eolica")
print(capacidade_eolica * fator_capacidade_eolica * 8760)


filtro_quantidade_todos = df[
    (df["Ano"] <= 2021) &
    (df["Status"] == "Commissioned") 
]
total_projetos_todos = len(filtro_quantidade_todos)
print("-------------------------")
print("Todos os projetos")
print(total_projetos_todos)



gerado_por_solar = (capacidade_solar * fator_capacidade_solar * 8760)

gerado_por_eolica = (capacidade_eolica * fator_capacidade_eolica * 8760)

reultado_solar = gerado_por_solar/energia_produzida_2021*100
resultado_eolica = gerado_por_eolica/energia_produzida_2021*100


print("-------------------------")
print("Resultados")

print("Solar")
print(reultado_solar)
print("Eolica")
print(resultado_eolica)
print("-------------------------")
print("Custos Solar")
print(gerado_por_solar*31)
print(gerado_por_solar*40)
print("-------------------------")
print("Custos Eólica")
print(gerado_por_eolica*26)
print(gerado_por_eolica*59)

print(energia_produzida_2021_n)

print(1*67.2/0.26)