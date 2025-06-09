import pandas as pd
import logging
from conexion_db import conectar_oracle, extraer_datos

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="procesamiento_datos.log",
    filemode="a"
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

def procesar_datos(df):
    try:
        # Crear una copia del DataFrame para no modificar el original
        df_procesado = df.copy()

        # Verificar valores nulos
        logging.info("Verificando valores nulos...")
        nulos = df_procesado.isnull().sum()
        logging.info(f"Valores nulos:\n{nulos}")

        # Eliminar filas con valores nulos (si es necesario)
        df_procesado = df_procesado.dropna()
        logging.info("Filas con valores nulos eliminadas.")

        # Eliminar duplicados
        logging.info("Eliminando duplicados...")
        df_procesado = df_procesado.drop_duplicates()
        logging.info(f"Duplicados eliminados. Total filas: {len(df_procesado)}")

        # Calcular el total de ventas por producto (CANTIDAD * PRECIO)
        logging.info("Calculando el total de ventas por producto...")
        df_procesado['TOTAL_VENTA'] = df_procesado['CANTIDAD'] * df_procesado['PRECIO']

        # Agrupar datos por producto y cliente
        logging.info("Agrupando datos por producto y cliente...")
        ventas_por_producto = df_procesado.groupby('PRODUCTO')['TOTAL_VENTA'].sum().reset_index()
        ventas_por_cliente = df_procesado.groupby('CLIENTE')['TOTAL_VENTA'].sum().reset_index()

        logging.info("Procesamiento de datos completado.")

        # Guardar el DataFrame procesado en un archivo CSV
        df_procesado.to_csv('datos_procesados.csv', index=False)
        logging.info("DataFrame procesado guardado en 'datos_procesados.csv'")

        return df_procesado, ventas_por_producto, ventas_por_cliente

    except Exception as e:
        logging.error(f"Error al procesar datos: {e}")
        raise

if __name__ == "__main__":
    try:
        # Conectar a Oracle y extraer datos
        conn = conectar_oracle()
        df = extraer_datos(conn)

        # Procesar datos
        df_procesado, ventas_por_producto, ventas_por_cliente = procesar_datos(df)

        # Mostrar los primeros 5 registros del DataFrame procesado
        print(df_procesado.head())

    except Exception as e:
        logging.error(f"Error en el proceso principal: {e}")
    finally:
        if 'conn' in locals():
            conn.close() #CERRAR CONEXION
            logging.info("Conexión cerrada")