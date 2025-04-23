from quien_gana import QuienGana  # Importamos función para determinar el resultado
from puntos import Puntos  # Importamos función para calcular los puntos

# Función que calcula las estadísticas de cada equipo:
# Devuelve una lista de tuplas con: (equipo, ganados, empatados, perdidos, puntos)
def InfoEquipos(datosliga, equipos):
    info = []

    for equipo in equipos:
        ganados = empatados = perdidos = 0  # Inicializamos contadores

        for partido in datosliga:
            local = partido['Team 1']
            visitante = partido['Team 2']
            resultado = partido['FT']

            if equipo == local:
                r = QuienGana(resultado)
                if r == 1:
                    ganados += 1
                elif r == 0:
                    empatados += 1
                else:
                    perdidos += 1

            elif equipo == visitante:
                r = QuienGana(resultado)
                if r == -1:
                    ganados += 1
                elif r == 0:
                    empatados += 1
                else:
                    perdidos += 1

        puntos = Puntos([ganados, empatados, perdidos])  # Calculamos puntos totales
        info.append((equipo, ganados, empatados, perdidos, puntos))  # Añadimos la tupla

    return info  # Devolvemos la lista de estadísticas
