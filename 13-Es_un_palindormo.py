# 13

#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#   * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.


def normalize(palabra: str) -> str:
    """Funcion para solo dejar letras, sin espacios y en minusculas"""
    palabra = palabra.lower().replace(" ", "").replace(".", "").replace(",", "")
    if palabra.isalpha():
        return palabra
    return False


def palindromo(palabra: str) -> str:
    """Funcion que invierte los caracteres"""
    palabra = normalize(palabra)
    temporal = ""
    if palabra is not False:
        for i in palabra[::-1]:
            temporal += i
        return temporal
    return False


def comparacion(palabra1: str) -> bool:
    """Funcion que compara la palabra con el """
    comparable = palindromo(palabra1)
    if comparable is False:
        return False
    if comparable == normalize(palabra1):
        return True


print(comparacion("Ana lleva, al oso la avellana."))
