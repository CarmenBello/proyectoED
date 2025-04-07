import csv  # Importamos la librería para trabajar con archivos CSV

def LeerPartidos():
    partidos = []  # Creamos una lista vacía donde guardaremos los partidos

    # Abrimos el archivo 'liga.csv' en modo lectura y con codificación UTF-8
    with open('liga.csv', mode='r', encoding='utf-8') as archivo:
        # Usamos DictReader para leer cada línea del CSV como un diccionario
        lector = csv.DictReader(archivo)
        
        # Recorremos cada fila del archivo y la añadimos a la lista de partidos
        for fila in lector:
            partidos.append(fila)
    
    # Devolvemos la lista con todos los partidos en forma de diccionario
    return partidos


# Llamamos a la función y guardamos el resultado
partidos = LeerPartidos()
# Imprimimos los 3 primeros partidos para ver si funciona  
for partido in partidos[:3]:
    print(partido)