from datos_reporting import ventas_por_producto
import matplotlib.pyplot as plt

# Crear figura
plt.figure(figsize=(8, 5))  # Define el tamaño de la figura (ancho, alto)

# Crear gráfico de barras
plt.bar(
    ventas_por_producto['Producto'],  # Eje X: Productos
    ventas_por_producto['Ventas'],    # Eje Y: Ventas
    color='skyblue'                   # Color de las barras
)

# Añadir títulos y etiquetas
plt.title('Ventas Totales por Producto')  # Título del gráfico
plt.xlabel('Producto')                   # Etiqueta del eje X
plt.ylabel('Ventas')                     # Etiqueta del eje Y

# Ajustar márgenes automáticamente
plt.tight_layout()

# Guardar el gráfico como imagen PNG
plt.savefig('ventas_por_producto.png')

# Mostrar el gráfico en pantalla
plt.show()