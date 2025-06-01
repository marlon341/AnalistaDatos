import matplotlib.pyplot as plt
import pandas as pd
# Datos de ejemplo: venta diaria
data_linea = {
    'Fecha': ['2025-05-01', '2025-05-02', '2025-05-03', '2025-05-04', '2025-05-05'],
    'Ventas': [100, 150, 125, 200, 175]
}

df_linea = pd.DataFrame(data_linea)
df_linea['Fecha'] = pd.to_datetime(df_linea['Fecha'])  # Convertir a tipo fecha

# Crear gráfico de líneas
plt.figure(figsize=(8, 5))
plt.plot(
    df_linea['Fecha'],  # Eje X: Fechas
    df_linea['Ventas'], # Eje Y: Ventas
    marker='o'          # Añadir marcadores en cada punto
)

# Personalizar gráfico
plt.title('Ventas Diarias')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.xticks(rotation=45)  # Rotar etiquetas del eje X
plt.tight_layout()

# Guardar y mostrar
plt.savefig('ventas_diarias.png')
plt.show()