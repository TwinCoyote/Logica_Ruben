# pylint: disable = C0304,C0103
#  * Crea un programa que determine si dos vectores son ortogonales.
#  * - Los dos array deben tener la misma longitud.
#  * - Cada vector se podría representar como un array. Ejemplo: [1, -2]


def comprobacion(f: list[tuple], s: list[tuple]) -> bool:
    """xd"""
    if len(f) != len(s):
        return False
    operacion = 0
    for x, _ in enumerate(f):
        operacion += f[x] * s[x]
    return operacion == 0


m = [1, -2]
r = [2, 1]


print(comprobacion(m, r))
