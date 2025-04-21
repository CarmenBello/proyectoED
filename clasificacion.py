# Función que ordena la clasificación de mayor a menor en función de los puntos
def Clasificacion(datos):
    return sorted(datos, key=lambda x: x[4], reverse=True)  # x[4] es el número de puntos
