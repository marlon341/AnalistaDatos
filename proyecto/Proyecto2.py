import cx_Oracle
import pandas as pd
import schedule
import time
# Configuración de conexión (¡usa tus datos!)
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
def obtener_discrepancias():
    try:
        # Conectar a Oracle
        conn = cx_Oracle.connect(user='system', password='oracle', dsn=dsn_tns)
        
        # consulta SQL
        consulta = """
            SELECT v.id_venta, v.fecha_venta, v.cantidad, p.nombre producto, c.nombre cliente, t.nombre tienda
            FROM ventas v
            JOIN productos p ON v.id_producto = p.id_producto
            JOIN clientes c ON v.id_cliente = c.id_cliente
            JOIN tiendas t ON v.id_tienda = t.id_tienda
        """
        
        # Ejecutar y convertir a DataFrame
        df = pd.read_sql(consulta, conn)
        print("Datos obtenidos. Registros:", len(df))
        
        # Guardar en CSV
        df.to_csv('discrepancias.csv', index=False)
        print("Archivo actualizado a las", pd.Timestamp.now())
        
        conn.close()
    
    except Exception as e:
        print("Error:", e)
# Programar cada 1 minutos
schedule.every(1).minutes.do(obtener_discrepancias)
print("Monitor activo. Presiona Ctrl+C para salir.")
while True:
    schedule.run_pending()
    time.sleep(1)
