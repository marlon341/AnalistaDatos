import pandas as pd
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="exportacion_estudiantes.log",
    filemode="a"
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

def main():
    try:
        logging.info("Iniciando el proceso de exportación de estudiantes a Excel.")

        # Diccionario para el DataFrame
        datos = {
            'nombre': ['marlon', 'danilo', 'emerson', 'david'],
            'edad': [24, 23, 22, 35],
            'carrera': ['sistemas', 'software', 'industrial', 'vagancia'],
            'promedio': [2.0, 3.0, 4.0, 5.0],
        }
        logging.info("Datos de entrada preparados.")

        df = pd.DataFrame(datos)
        logging.debug(f"DataFrame creado:\n{df}")

        # Crear la columna "estado"
        df["estado"] = None
        df.loc[df["promedio"] >= 3.5, "estado"] = "aprobado"
        df.loc[df["promedio"] < 3.5, "estado"] = "reprobado"
        logging.info("Columna 'estado' calculada correctamente.")

        # Filtrar a los aprobados
        aprobados = df[df["estado"] == "aprobado"]
        logging.info(f"Alumnos aprobados filtrados: {len(aprobados)} encontrados.")

        # Exportar a Excel
        output_file = 'estudiantes_resumen.xlsx'
        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Datos', index=False)
            aprobados.to_excel(writer, sheet_name='Aprobados', index=False)
        logging.info(f"Archivo Excel '{output_file}' creado con éxito.")

    except Exception as e:
        logging.error(f"Ocurrió un error durante la exportación: {e}", exc_info=True)

if __name__ == "__main__":
    main()