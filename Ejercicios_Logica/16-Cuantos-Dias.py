import datetime


#  * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
#  * de texto que representen fechas.
#  * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
#  * - La función recibirá dos String y retornará un Int.
#  * - La diferencia en días será absoluta (no importa el orden de las fechas).
#  * - Si una de las dos cadenas de texto no representa una fecha correcta se
#  *   lanzará una excepción.

FECHA_1 = "03/09o/2001"
FECHA_2 = "06/09/2001"


def calcular_fechas(fecha_1: str, fecha_2: str):
    """Funcion para calcular los dias que hay entre cada fecha"""
    try:
        formato = "%d/%m/%Y"
        fecha1 = datetime.datetime.strptime(fecha_1, formato).date()
        fecha2 = datetime.datetime.strptime(fecha_2, formato).date()
        resta = fecha1 - fecha2
        return abs(resta.days)
    except ValueError as e:
        return f"Error: El formato de la fecha no es el correcto: {e}"


print(calcular_fechas(FECHA_1, FECHA_2))
