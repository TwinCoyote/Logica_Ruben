'''Ciclo sexagenario chino'''  # ? Dificultad: Medio
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101
# * Crea un función, que dado un año, indique el elemento
# * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
# * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
# * - El ciclo sexagenario se corresponde con la combinación de los elementos
# *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
# *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
# *   (en este orden).
# * - Cada elemento se repite dos años seguidos.
# * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).

elements = ["madera", "fuego", "tierra", "metal", "agua"]
animals = ["rata", "buey", "tigre", " conejo", "dragón", "serpiente",
           "caballo", " oveja", "mono", "gallo", " perro", " cerdo"]


def csc(year: int) -> tuple:
    """Challenge 34"""
    FIRST_YEAR = 1984
    ANIMALS = 12
    position = year - FIRST_YEAR
    res = position % ANIMALS
    ciclo_10 = position % 10
    temp = ciclo_10 // 2

    return elements[temp], animals[res]


print(csc(1980))


# x = 16

# print(x // -2)
# print(x % 2)
