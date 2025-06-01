import pandas as pd
# Primer DataFrame (datos personales)
df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Nombre': ['Ana', 'Luis', 'Pedro'],
                    'Edad': [23, 30, 35]})

# Segundo DataFrame (datos de ciudades)
df2 = pd.DataFrame({'ID': [1, 2, 3],
                    'Ciudad': ['Bogotá', 'Medellín', 'Cali']})

# Unimos los DataFrames usando la columna "ID"
df_merged = pd.merge(df1, df2, on='ID')
print(df_merged)


