import cx_Oracle
import pandas as pd
import schedule
import time
# Configuración de conexión (¡usa tus datos!)
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XEPDB1')
def obtener_discrepancias():
    try:
        # Conectar a Oracle
        conn = cx_Oracle.connect(user='system', password='m4rl0n2233*', dsn=dsn_tns)
        
        # consulta SQL
        consulta = """
        SELECT cp.INVOICE_NUM,
                cp.AMOUNT AS AMOUNT,
                dp.VALOR_PAGADO AS VALOR_PAGADO,
                dp.REGISTROS AS RegistrosEnDetalle,
                cp.AMOUNT - dp.VALOR_PAGADO AS DIFERENCIA
        FROM (SELECT cp.INVOICE_NUM,sum(cp.AMOUNT) AS AMOUNT FROM ICEBERG.CUNPTP cp WHERE cp.APPROVAL_CODE = 1 GROUP BY cp.INVOICE_NUM) cp
        INNER JOIN (SELECT dp.REFERENCIA, count(dp.REFERENCIA) AS Registros, sum(dp.VALOR_PAGADO) AS VALOR_PAGADO 
                    FROM PORTAL_PAGOS.DETALLE_PAGO dp GROUP BY dp.REFERENCIA) dp
        ON cp.INVOICE_NUM = dp.REFERENCIA
        WHERE cp.AMOUNT - dp.VALOR_PAGADO != 0
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
