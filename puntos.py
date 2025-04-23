# Función que calcula los puntos totales a partir de los partidos ganados, empatados y perdidos
def Puntos(info):
    ganados, empatados, perdidos = info  # Desempaquetamos la tupla
    return ganados * 3 + empatados  # 3 puntos por victoria, 1 por empate, 0 por derrota
