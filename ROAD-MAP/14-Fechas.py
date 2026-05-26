# pylint: disable=C0103
"""Modulo para aprender a usar DataTime"""
#  !   EJERCICIO:
#  * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
#  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
#  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
#  * Calcula cuántos años han transcurrido entre ambas fechas.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
#  * 10 maneras diferentes. Por ejemplo:
#  * - Día, mes y año.
#  * - Hora, minuto y segundo.
#  * - Día de año.
#  * - Día de la semana.
#  * - Nombre del mes.
#  * (lo que se te ocurra...)


# from datetime import datetime

# ahora = datetime.now()
# print(ahora.second)
# print(type(ahora.day))
import locale
from datetime import datetime

mi_fecha = datetime(2001, 9, 3, 12, 45, 33)
ahora = datetime.now()

print(f"{mi_fecha}\n{ahora}")

diferencia = (ahora - mi_fecha)
preparacion = int(diferencia.days / 365.25)
print(preparacion)

locale.setlocale(locale.LC_ALL, "es_MX")
print(mi_fecha.strftime("%B").capitalize())
print(mi_fecha.strftime("%A %d de %B de %Y"))
print(mi_fecha.strftime("Naciste el dia %j del año"))
print(mi_fecha.strftime("Naciste a las %H:%M"))
print(mi_fecha.strftime("Naciste en el segundo %S"))
print(mi_fecha.strftime("En la semana %W"))
print(mi_fecha.strftime("En el año %Y"))
print(mi_fecha.strftime(" %d/%m/%Y"))
print(mi_fecha.strftime("%H:%M:%S"))
print(mi_fecha.strftime("Aqui %H:%M:%S"))
