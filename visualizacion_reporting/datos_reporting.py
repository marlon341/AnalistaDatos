import pandas as pd

# Datos de ventas de ejemplo
data = {
    'Producto': ['Camisa', 'Pantalón', 'Zapatos', 'Camisa', 'Zapatos', 'Pantalón'],
    'Ventas':    [10,        15,         20,       8,         25,         12]
}

df = pd.DataFrame(data)

# Agrupar por producto y sumar las ventas
ventas_por_producto = df.groupby('Producto')['Ventas'].sum().reset_index()

print(ventas_por_producto)


