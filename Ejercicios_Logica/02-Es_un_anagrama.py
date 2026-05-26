#  Escribe una función que reciba dos palabras (String) y retorne
#  verdadero o falso (Bool) según sean o no anagramas.
#  - Un Anagrama consiste en formar una palabra reordenando TODAS
#    las letras de otra palabra inicial.
#  - NO hace falta comprobar que ambas palabras existan.
#  - Dos palabras exactamente iguales no son anagrama.

p1 = input("Ingrese la primera palabra: ")
p2 = input("Ingrese la segunda palabra: ")


def contar(x: str):
    lista = {}
    palabra = x
    for i in palabra:
        if i in lista:
            lista[i] += 1
        else:
            lista[i] = 1
    return (lista)

def comparar(x: dict, y: dict) -> bool:
    if x == y:
        return True
    else:
        return False


print(comparar(contar(p1),contar(p2)))


# def Anagrama(Palabra: str) -> str:
#     palabra_lista1 = []
#     for i in Palabra[::-1]:
#         palabra_lista1.append(i)
#     resultado = "".join(palabra_lista1)
#     return resultado


# def comparacion(x: str, y: str) -> bool:
#     if x == y:
#         return True
#     else:
#         return False


# print(comparacion((Anagrama(p1)), (Anagrama(p2))))
