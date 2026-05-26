
#  * EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
#  *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
#  *   interpolación, verificación...
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas


Palabra1 = input("Ingrese su primera palabra: ")
Palabra2 = input("Ingrese su segunda palabra: ")


def palindromo(pal1: str) -> str:
    p1 = pal1[::-1]
    if p1 == pal1:
        print("Tu palabra 1 es un palindromo.")
        return pal1
    else:
        print("No es palindromo")
    return


def ana(Pal):

    lista = {}
    for i in Pal:
        if i in lista:
            lista[i] += 1
        else:
            lista[i] = 1
    return lista


def isograma(pala):
    lista = {}
    for i in pala:
        if i in lista:
            return "No es un isograma"
        else:
            lista[i] = 1

    return lista


# print(palindromo("ana", "hola"))
# print(ana("ana"))
activador = True

while activador:
    print(palindromo(Palabra1))
    print(ana(Palabra1))
    print(isograma(Palabra1))

    input("Ahora con la segunda Palabra: ")
    print(palindromo(Palabra2))
    print(ana(Palabra2))
    print(isograma(Palabra2))
    x = input("Fue todo presiona cualquier tecla para acabar")
    if x:
        activador = False
