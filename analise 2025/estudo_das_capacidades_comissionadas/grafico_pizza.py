import matplotlib.pyplot as plt

# Dados
valores = [17810.18, 30107.93, 860.77, 663.21]
rotulos = ['Solar', 'Eólica', 'Hidro', 'Biomass']
cores_verdes = ['#a1d99b', '#74c476', '#41ab5d', '#238b45']

# Calcula porcentagem total
total = sum(valores)

# Formata os rótulos para a legenda
rotulos_formatados = [
    f'{nome} ({valor:.1f} MW, {valor / total * 100:.1f}%)'
    for nome, valor in zip(rotulos, valores)
]

# Cria o gráfico
fig, ax = plt.subplots()

# Apenas dois valores retornados, já que autopct está None
wedges, texts = ax.pie(
    valores,
    labels=None,  # rótulos vão só na legenda
    autopct=None,
    startangle=90,
    colors=cores_verdes
)

# Deixa o gráfico redondo
ax.axis('equal')

# Título
plt.title('Distribuição por Setor', color='green')

# Legenda com nome, valor e porcentagem
ax.legend(wedges, rotulos_formatados, title="Setores", loc="center left", bbox_to_anchor=(1, 0.5))

# Salva como imagem com fundo transparente
plt.savefig("grafico_setores.png", transparent=True, dpi=300, bbox_inches='tight')
# plt.show()
