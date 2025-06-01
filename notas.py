import pandas as pd
#diccionario dataframe
datos={
    'nombre':['marlon','danilo','emerson','david'],
    'edad':[24,23,22,35],
    'carrera':['sistemas','software','industrial','vagancia'],
    'promedio':[2.0,3.0,4.0,5.0],
}
df = pd.DataFrame(datos)
print(df,'\n')
# Agregar la nueva columna 'estado' con valores calculados
df["estado"] = None  # Se crea la columna y se inicializa con None
df.loc[df["promedio"] >= 3.5, "estado"] = "aprobado"
df.loc[df["promedio"] < 3.5, "estado"] = "reprobado"
print(df)

aprobados = df[df['estado']=='aprobado']
# OTRA FORMA DE Agregar la columna "estado" con valores según la condición
df["estado"] = ["Pasa" if x >= 3.0 else "No pasa" for x in df["promedio"]]

with pd.ExcelWriter('estudiantes_resumen.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Datos', index=False)
    aprobados.to_excel(writer, sheet_name='resumen')