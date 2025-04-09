import csv  # Importamos la librería para trabajar con archivos CSV

# Función que lee el fichero liga.csv y devuelve una lista de diccionarios con los partidos
def LeerPartidos():
    partidos = []  # Lista vacía donde almacenaremos los partidos

    # Abrimos el archivo en modo lectura y codificación UTF-8
    with open('liga.csv', mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)  # Leemos el archivo como diccionarios

        # Recorremos cada fila (partido) y la añadimos a la lista
        for fila in lector:
            partidos.append(fila)

    return partidos  # Devolvemos la lista de partidos
