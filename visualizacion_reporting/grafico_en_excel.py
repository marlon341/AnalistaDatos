from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Crear un nuevo libro de Excel
wb = Workbook()
ws = wb.active

# Insertar imagen
img = Image('ventas_por_producto.png')  # Ruta de la imagen generada
ws.add_image(img, 'A1')  # Insertar en la celda A1

# Guardar el libro de Excel
wb.save('reporte_ventas.xlsx')