'''Los numeros perdidos'''  # ? Dificultad: Medio
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101
# * Dado un array de enteros ordenado y sin repetidos,
# * crea una función que calcule y retorne todos los que faltan entre
# * el mayor y el menor.
# * - Lanza un error si el array de entrada no es correcto.


numbers = [1, 3, 5]


def lost_numbers(array: list[int]) -> int:
    numeros = []
    mayor = array[-1]
    men = array[0]
    if men != min(array) or mayor != max(array) or len(array) < 2:
        raise ValueError("This is a custom error message")

    for index in range(len(array)-1):
        if array[index] >= array[index + 1]:
            raise ValueError("bailaste")

    for i in range(men, mayor):
        if i not in array:
            numeros.append(i)
    return numeros


print(lost_numbers(numbers))
# print(sorted(numbers))
