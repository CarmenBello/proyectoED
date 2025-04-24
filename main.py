from leer_partidos import LeerPartidos  # Importamos la función para leer los partidos
from imp_clasificacion import impClasificacion  # Importamos la función para imprimir la clasificación

# Punto de entrada del programa
if __name__ == '__main__':
    liga = LeerPartidos()  # Leemos los partidos desde el archivo CSV
    impClasificacion(liga)  # Mostramos la clasificación final
