import pandas as pd

# Ejemplo: DataFrame de ventas
data = {
    'Fecha': ['2025-05-01', '2025-05-02', '2025-05-03'],
    'Producto': ['Camisa', 'Pantalón', 'Zapatos'],
    'Ventas': [10, 15, 20]
}
df = pd.DataFrame(data)

# Exportar a un archivo .xlsx con openpyxl (por defecto)
df.to_excel('ventas.xlsx', index=False)

# MULTIPLES HOJAS EN UN MISMO ARCHIVO
with pd.ExcelWriter('informe_ventas.xlsx', engine='xlsxwriter') as writer:
    # Hoja “Resumen”
    df.groupby('Producto')['Ventas'].sum().to_frame('Total Ventas') \
      .to_excel(writer, sheet_name='Resumen')

    # Hoja “Detalle”
    df.to_excel(writer, sheet_name='Detalle', index=False)
    
# FORMATEO DE CELDAS (avanzado)   
df.to_excel('ventas_fmt.xlsx', index=False, engine='xlsxwriter')
wb = pd.ExcelWriter('ventas_fmt.xlsx', engine='xlsxwriter').book
ws = wb.add_worksheet('Sheet1')
formato_num = wb.add_format({'num_format': '#,##0'})# Definir un formato de número con separador de miles
ws.set_column(2, 2, 12, formato_num)# Aplicar formato a la columna ‘Ventas’ (columna C, índice 2)
wb.close()