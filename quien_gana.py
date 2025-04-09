# Función que analiza el resultado del partido y devuelve:
#  1 si gana el equipo local
#  0 si es empate
# -1 si gana el equipo visitante
def QuienGana(resultado):
    goles_local, goles_visitante = map(int, resultado.split('-'))  # Convertimos el resultado en enteros

    if goles_local > goles_visitante:
        return 1  # Gana equipo local
    elif goles_local < goles_visitante:
        return -1  # Gana equipo visitante
    else:
        return 0  # Empate
