
# * Crea una función que reciba días, horas, minutos y segundos(como enteros)
# * y retorne su resultado en milisegundos.


def conversor(dias: int, horas: int, minutos: int, segundos: int) -> int:
    """función que recibe días, horas, minutos y segundos"""
    millis = 1000
    segundos_count = (dias * 86400) + (horas * 3600) + \
        (minutos * 60) + segundos
    return segundos_count * millis


print(conversor(1, 0, 0, 1))
