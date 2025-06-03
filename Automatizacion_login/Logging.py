import logging

# Configuración básica para guardar logs en un archivo
logging.basicConfig(
    level=logging.INFO,                              # Nivel mínimo a capturar
    format="%(asctime)s [%(levelname)s] %(message)s", # Formato del mensaje
    datefmt="%Y-%m-%d %H:%M:%S",                     # Formato de la fecha/hora
    filename="exportacion_estudiantes.log",          # Archivo donde se guardarán los logs
    filemode="a"                                     # "a" = append; "w" = sobrescribir
)

# Agregar handler para mostrar logs en la consola
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)