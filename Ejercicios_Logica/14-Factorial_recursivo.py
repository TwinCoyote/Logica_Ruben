
#  * Escribe una función que calcule y retorne el factorial de un número dado
#  * de forma recursiva.


def factorial(x: int) -> int:
    """Funcion para calcular un numero factorial de forma recursiva"""
    if x <= 1:
        return 1
    return x * factorial(x-1)


print(factorial(-5))
