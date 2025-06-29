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
    'Announced / planning begun',
    'Financing secured / under construction',
    'Permitted'
]

sector_list = [
    'Solar', 'Wind'
]

# Cria pasta para salvar os gráficos
os.makedirs("graficos_pizza_setores", exist_ok=True)

# Paleta com cores variadas (matplotlib tab10, tab20, etc.)
import itertools
cores_base = plt.cm.tab20.colors  # 20 cores diferentes
cores_ciclo = itertools.cycle(cores_base)

# Gera gráfico de pizza para cada setor
solar = []
wind = []
biofuel = []
biomass = []
hidro = []
geo = []
marine = []

solar_c = []
wind_c = []
biofuel_c = []
biomass_c = []
hidro_c = []
geo_c = []
marine_c = []

filtro_capacidade_2012_16 = df[
    (df["Ano"] == 2013) &
    (df["Sector"] == "Wind")&
    (df["Status"] == "Commissioned")
]
filtro_capacidade_2013_16_final = filtro_capacidade_2012_16["Capacity"].sum()
print("Capacidade Eólica")
print(filtro_capacidade_2013_16_final)


for estado in status_list:
    contagens = []
    capacidade = []
    for setor in sector_list:
        count = len(df[(df["Sector"] == setor) & (df["Status"] == estado)])
        capacidade_real = (df[(df["Sector"] == setor) & (df["Status"] == estado)]["Capacity"].sum())
        capacidade.append(capacidade_real)
        contagens.append(count)
        #print(capacidade)

    #print(contagens)
    total = sum(contagens)
    if total == 0:
        continue

    solar.append(contagens[0])
    wind.append(contagens[1])
    # biofuel.append(contagens[2])
    # biomass.append(contagens[3])
    # hidro.append(contagens[4])
    # geo.append(contagens[5])
    # marine.append(contagens[6])
    solar_c.append(capacidade[0])
    wind_c.append(capacidade[1])
    # biofuel_c.append(capacidade[2])
    # biomass_c.append(capacidade[3])
    # hidro_c.append(capacidade[4])
    # geo_c.append(capacidade[5])
    # marine_c.append(capacidade[6])


total_solar = sum(solar)
total_wind = sum(wind)

capacidade_solar_estimada = sum(solar_c)
capacidade_eolica_estimada = sum(wind_c)

fator_c_eolica = 0.38
fator_c_solar = 0.19

print(f'total solar: {total_solar}')


a2021_c = 240000000*(1-0.28)
print(a2021_c)
print("-------------------------")
print("Geração anual")
print((capacidade_solar_estimada*fator_c_solar*8760)/1000000)
print((capacidade_eolica_estimada*fator_c_eolica*8760)/1000000)


print("-------------------------")
print("Custo de geração Solar")
print(capacidade_solar_estimada*fator_c_solar*8760*31)
print(capacidade_solar_estimada*fator_c_solar*8760*40)

print("-------------------------")
print("Custo de geração Eolica")
print(capacidade_eolica_estimada*fator_c_eolica*8760*26)
print(capacidade_eolica_estimada*fator_c_eolica*8760*59)