from datetime import timedelta
from datetime import datetime

'''Los lanzamientos de the legend of zelda'''  # ? Dificultad: Medio
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101
# * ¡Han anunciado un nuevo "The Legend of Zelda"!
# * Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
# * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
# * "The Legend of Zelda" de la historia?
# * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
# * que tú selecciones.
# * - Debes buscar cada uno de los títulos y su día de lanzamiento
# *   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)


TearsOfTheKingdom = "12/05/2023"

TheWindWaker = "13/12/2002"


def dates(d1: str, d2: str) -> str:
    '''Retorna los años y los meses que tienen de diferencia las fechas'''
    Fecha1 = datetime.strptime(d1, "%d/%m/%Y")
    Fecha2 = datetime.strptime(d2, "%d/%m/%Y")

    dias = Fecha1 - Fecha2

    year = int(dias.days // 365.25)
    dia = int(dias.days % 365.25)
    return f"Han pasado {year} Años y {dia} Dias."


print(dates(TearsOfTheKingdom, TheWindWaker))
