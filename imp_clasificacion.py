from equipos import Equipos  # Función para obtener el conjunto de equipos
from info_equipos import InfoEquipos  # Función para obtener estadísticas de los equipos
from clasificacion import Clasificacion  # Función para ordenar la clasificación

# Función que imprime la clasificación final por pantalla
def impClasificacion(liga):
    equipos = Equipos(liga)  # Obtenemos el conjunto de equipos
    info = InfoEquipos(liga, equipos)  # Obtenemos estadísticas de cada equipo
    clasificacion = Clasificacion(info)  # Ordenamos por puntos

    # Cabecera de la tabla
    print(f"{'Pos':<4}{'Equipo':<15}{'G':<4}{'E':<4}{'P':<4}{'Pts':<5}")
    print("-" * 36)

    # Imprimimos cada fila de la clasificación
    for i, equipo in enumerate(clasificacion, 1):
        nombre, ganados, empatados, perdidos, puntos = equipo
        print(f"{i:<4}{nombre:<15}{ganados:<4}{empatados:<4}{perdidos:<4}{puntos:<5}")
