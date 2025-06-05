import os
os.environ["PATH"] = r"C:\oracle\instantclient_19_26" + ";" + os.environ["PATH"]

import cx_Oracle
import pandas as pd
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="conexion_oracle.log",
    filemode="a"
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

def conectar_oracle():
    try:
        # Datos de conexión (actualiza con tus credenciales)
        dsn = cx_Oracle.makedsn(
            host="localhost",
            port=1522,
            sid="xe"  # o service_name según tu configuración
        )
        conn = cx_Oracle.connect(
            user="system",
            password="oracle",
            dsn=dsn
        )
        logging.info("Conexión a Oracle exitosa")
        return conn
    except cx_Oracle.DatabaseError as e:
        logging.error(f"Error al conectar a Oracle: {e}")
        raise

def extraer_datos(conn):
    try:
        # Consulta SQL para extraer datos
        query = """
            SELECT v.id_venta, v.fecha_venta, v.cantidad, p.nombre producto, c.nombre cliente, t.nombre tienda
            FROM ventas v
            JOIN productos p ON v.id_producto = p.id_producto
            JOIN clientes c ON v.id_cliente = c.id_cliente
            JOIN tiendas t ON v.id_tienda = t.id_tienda
        """
        # Leer los datos en un DataFrame
        df = pd.read_sql(query, conn)
        logging.info("Datos extraídos correctamente")
        return df
    except Exception as e:
        logging.error(f"Error al extraer datos: {e}")
        raise

if __name__ == "__main__":
    try:
        # Conectar a Oracle
        conn = conectar_oracle()
        # Extraer datos
        df = extraer_datos(conn)
        # Mostrar los primeros 5 registros
        print(df.head())
    except Exception as e:
        logging.error(f"Error en el proceso principal: {e}")
    finally:
        # Cerrar la conexión
        if 'conn' in locals():
            conn.close()
            logging.info("Conexión cerrada")