import pandas as pd

# Creamos un DataFrame de ejemplo
data = {'Nombre': ['Ana', 'Luis', 'Pedro', 'Maria', 'Juan'],
        'Edad': [23, 30, 35, 40, 29],
        'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Bogotá', 'Medellín']}

df = pd.DataFrame(data)
print(df)
# Agrupar por ciudad y calcular la edad promedio
df_grouped = df.groupby('Ciudad')['Edad'].mean()
print(df_grouped)
