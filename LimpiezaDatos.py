import pandas as pd
# Crear diccionario de valores nulos y duplicados
datos = {
    'nombres': ['marlon', 'marlon', 'danilo', None],
    'apellido': ['diaz', 'basto', None, 'basto'],
    'edad': [22, None, 33, 22]  # Asegurar misma cantidad de elementos
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Mostrar duplicados correctamente
print(df.duplicated())  # Devuelve una Serie de True/False
print(df[df.duplicated()])  # Muestra solo las filas duplicadas
