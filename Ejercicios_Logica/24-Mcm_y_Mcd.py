# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,C0200
#  * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
#  * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.


def MCD(a: int, b: int) -> int:
    """Funcion para calulcar el maximo comun denominador"""
    answ = 0
    while b != 0:
        resi = a % b
        if resi == 0:
            answ = b
            return answ
        a = b
        b = resi
    return answ


def MCM(a: int, b: int) -> int:
    r = abs(a * b)//MCD(a, b)
    return r


# print(MCD(25, 15))


print(MCM(12, 15))
