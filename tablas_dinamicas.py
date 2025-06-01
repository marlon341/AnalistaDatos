import pandas as pd

data = {'Nombre': ['Ana', 'Luis', 'Pedro', 'Maria', 'Juan'],
        'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Bogotá', 'Medellín'],
        'Ventas': [100, 200, 150, 300, 250]}

df = pd.DataFrame(data)

# Crear tabla dinámica que muestre la suma de ventas por ciudad
df_pivot = df.pivot_table(values='Ventas', index='Ciudad', aggfunc='sum')
print(df_pivot)
