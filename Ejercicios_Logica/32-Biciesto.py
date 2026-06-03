"""Años biciestos"""
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622
#  * Crea una función que imprima los 30 próximos años bisiestos
#  * siguientes a uno dado.
#  * - Utiliza el menor número de líneas para resolver el ejercicio.

def biciesto(numero: int, contador: int = 0) -> int:
    """Funcion recursiva para imprimir los 30 años biciestos"""
    if contador >= 30:
        return
    if (numero % 4 == 0 and numero % 100 != 0) or (numero % 400 == 0):
        contador += 1
        print(f"{contador} - {numero}")

    return biciesto(numero + 1, contador)


biciesto(2000)
