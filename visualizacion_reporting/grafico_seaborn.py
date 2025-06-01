import seaborn as sns
import matplotlib.pyplot as plt
from datos_reporting import ventas_por_producto

# Reutilizamos el DataFrame 'ventas_por_producto'
plt.figure(figsize=(8, 5))
sns.barplot(
    data=ventas_por_producto,
    x='Producto',  # Eje X
    y='Ventas'     # Eje Y
)

# Personalizar gráfico
plt.title('Ventas Totales por Producto (Seaborn)')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.tight_layout()

# Guardar y mostrar
plt.savefig('ventas_seaborn.png')
plt.show()