"""Ordena la lista"""
# pylint: disable = C0305,C0103,C0301,C0200
#  * Crea una función que ordene y retorne una matriz de números.
#  * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
#  *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#  *   o de mayor a menor.
#  * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
#  *   automáticamente.


def sort(x: list, orden: str) -> list:
    """Funcion para ordenar"""
    if orden == "Asc":
        for i in range(len(x)):
            for i in range(len(x)-1):
                if x[i] > x[i+1]:
                    x[i], x[i+1] = x[i+1], x[i]
        return x
    elif orden == "Desc":
        for i in range(len(x)):
            for i in range(len(x)-1):
                if x[i] < x[i+1]:
                    x[i], x[i+1] = x[i+1], x[i]
        return x


m = [5, 4, 3, 2, 1]
print(sort(m, "Desc"))
