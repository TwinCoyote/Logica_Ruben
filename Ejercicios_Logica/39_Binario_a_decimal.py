'''Binario a decimal'''  # ? Dificultad: Medio
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101
# * Crea un programa se encargue de transformar un número binario
# * a decimal sin utilizar funciones propias del lenguaje que
# * lo hagan directamente.


Bin = "101010"


def decimal(bins: str) -> int:
    '''Retorna el binario a decimal'''
    count = 0
    for i, n in enumerate(bins[::-1]):
        R = int(n)
        if R != 0:
            count += 2**int(i)
    return count


print(decimal(Bin))
