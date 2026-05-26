
#  * Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.

def separar(x: str) -> list:
    if x[-1] == ' ':
        pass
    else:
        x = x + " "
    palabra = ""
    lista = []
    for i in x:
        if i == " ":
            lista.append(palabra)
            palabra = ""
        else:
            palabra += i
    return lista


def mayuscula(x: str) -> str:
    """Funcion que convierte la primera letra de una str en mayuscula."""
    palabra = ""
    for i in x:
        if palabra == "":
            palabra += x[0].upper()
        else:
            palabra += i
    return palabra


def reconstruir_frase(x: list) -> str:
    """Funcion para reconstruir la frase dada una lista"""
    frase = ""
    for i in range(len(x)):
        palabra = mayuscula(x[i])
        frase += " "+palabra
    if frase[0] == " ":
        frase = frase[1:]
    return frase


def programa(frase: str) -> str:
    """funcion para llamar a todas las funciones en una es como un main"""
    if frase == '':
        return "Ingrese una frase"
    frase = separar(frase)
    frase = reconstruir_frase(frase)
    return frase


print(programa("hola ruben que tal "))
