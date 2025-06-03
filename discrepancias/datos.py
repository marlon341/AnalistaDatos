import pandas as pd

# Crear un diccionario con datos
data = {
    'Nombre': ['Ana', 'Juan', 'Luis', 'Maria'],
    'Edad': [25, 30, 35, 28],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla']
}
# Convertir el diccionario a dataframe
df = pd.DataFrame(data)
# Mostrar dataframe
print(df)
# Filtrar personas mayores de 28 años
mayores_28 = df[df['Edad'] > 28]
print("\nPersonas mayores de 28 años:")
print(mayores_28)
#añadir una nueva columna
df['codigo'] = [11,22,33,44]

# Ordenar por edad de menor a mayor
df_ordenado = df.sort_values(by='Edad')
print("\nDataFrame ordenado por edad:")
print(df_ordenado)

# Seleccionar solo la columna 'Nombre'
nombres = df['Nombre']
print("\nLista de nombres:")
print(nombres.to_list())  # Convertimos la columna a una lista
