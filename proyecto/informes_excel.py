import pandas as pd
from conexion_db import conectar_oracle, extraer_datos
from proesamiento_datos import procesar_datos
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="generacion_informe.log",
    filemode="a"
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

def generar_informe_excel(df_procesado, ventas_por_producto, ventas_por_cliente):
    try:
        # Crear un escritor de Excel
        with pd.ExcelWriter('informe_ventas.xlsx', engine='xlsxwriter') as writer:
            # Escribir los datos procesados en la hoja "Datos"
            df_procesado.to_excel(writer, sheet_name='Datos', index=False)
            logging.info("Datos procesados guardados en la hoja 'Datos'")

            # Escribir las ventas por producto en la hoja "Ventas por Producto"
            ventas_por_producto.to_excel(writer, sheet_name='Ventas por Producto', index=False)
            logging.info("Ventas por producto guardadas en la hoja 'Ventas por Producto'")

            # Escribir las ventas por cliente en la hoja "Ventas por Cliente"
            ventas_por_cliente.to_excel(writer, sheet_name='Ventas por Cliente', index=False)
            logging.info("Ventas por cliente guardadas en la hoja 'Ventas por Cliente'")

        logging.info("Informe generado con éxito: 'informe_ventas.xlsx'")

    except Exception as e:
        logging.error(f"Error al generar el informe Excel: {e}")
        raise

if __name__ == "__main__":
    try:
        # Conectar a Oracle y extraer datos
        conn = conectar_oracle()
        df = extraer_datos(conn)

        # Procesar datos
        df_procesado, ventas_por_producto, ventas_por_cliente = procesar_datos(df)

        # Generar el informe en Excel
        generar_informe_excel(df_procesado, ventas_por_producto, ventas_por_cliente)

    except Exception as e:
        logging.error(f"Error en el proceso principal: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            logging.info("Conexión cerrada")