import oracledb    # en lugar de cx_Oracle
import pandas as pd
import logging
import os

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
        # ------------------------------------------------------------
        # 1) Inicializar el cliente Oracle en modo THICK (librerías DLL)
        # ------------------------------------------------------------
        # Aquí le indicamos la carpeta donde están las DLLs del Instant Client:
        instant_client_dir = r"C:\oracle\instantclient_19_26"
        os.environ["PATH"] = instant_client_dir + ";" + os.environ["PATH"]
        oracledb.init_oracle_client(lib_dir=instant_client_dir)
        # ------------------------------------------------------------

        # ------------------------------------------------------------
        # 2) Construir el dsn para la XE que corre en Docker en port 1522
        # ------------------------------------------------------------
        #   - host: localhost
        #   - port: 1522   (mapeo Docker: 1522 en Windows → 1521 en contenedor)
        #   - service_name: "XE"  (SID del contenedor XE 11g) XEPDB1
        dsn = oracledb.makedsn("localhost", 1521, service_name="XEPDB1")
        # ------------------------------------------------------------

        # ------------------------------------------------------------
        # 3) Conectar con credenciales de Docker XE
        #    Usuario y contraseña que definimos por defecto en el contenedor:
        #      user = "system"
        #      password = "oracle"
        # ------------------------------------------------------------
        conn = oracledb.connect(
            user="MARLON",
            password="1122",
            dsn=dsn
        )
        logging.info("Conexión a Oracle exitosa (modo THICK)")
        return conn

    except oracledb.DatabaseError as e:
        logging.error(f"Error al conectar a Oracle: {e}")
        raise

def extraer_datos(conn):
    try:
        query = """
            SELECT v.id_venta, v.fecha_venta, v.cantidad, p.nombre producto, p.precio, c.nombre cliente, t.nombre tienda
            FROM ventas v
            JOIN productos p ON v.id_producto = p.id_producto
            JOIN clientes c ON v.id_cliente = c.id_cliente
            JOIN tiendas t ON v.id_tienda = t.id_tienda
        """
        df = pd.read_sql(query, conn)
        logging.info("Datos extraídos correctamente")
        return df
    except Exception as e:
        logging.error(f"Error al extraer datos: {e}")
        raise

if __name__ == "__main__":
    try:
        conn = conectar_oracle()
        df = extraer_datos(conn)
        print(df) #muestra solo los los 5 primeros registros de la consulta para no extenderse
    except Exception as e:
        logging.error(f"Error en el proceso principal: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            logging.info("Conexión cerrada")