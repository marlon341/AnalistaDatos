import matplotlib.pyplot as plt
import pandas as pd

# Datos de ejemplo: porcentaje de mercado por marca
data_pie = {
    'Marca': ['MarcaA', 'MarcaB', 'MarcaC', 'MarcaD'],
    'Porcentaje': [40, 25, 20, 15]
}

df_pie = pd.DataFrame(data_pie)

# Crear gráfico de pastel
plt.figure(figsize=(6, 6))
plt.pie(
    df_pie['Porcentaje'],  # Valores
    labels=df_pie['Marca'],  # Etiquetas
    autopct='%1.1f%%',      # Mostrar porcentaje con un decimal
    startangle=90           # Ángulo inicial
)

# Personalizar gráfico
plt.title('Participación de Mercado por Marca')
plt.axis('equal')  # Hacer que el gráfico sea un círculo perfecto

# Guardar y mostrar
plt.savefig('participacion_mercado.png')
plt.show()