# Función que recibe la lista de partidos y devuelve un conjunto con todos los equipos
def Equipos(datosliga):
    equipos = set()  # Usamos un conjunto para evitar duplicados

    for partido in datosliga:
        equipos.add(partido['Team 1'])  # Añadimos el equipo local
        equipos.add(partido['Team 2'])  # Añadimos el equipo visitante

    return equipos  # Devolvemos el conjunto con todos los equipos
