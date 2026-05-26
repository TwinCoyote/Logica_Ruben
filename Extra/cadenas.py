
# # #  * Imprime el primer carácter
# # #  * Imprime el último carácter
# # #  * Imprime el carácter que está a la mitad
# # #  *💡 Objetivo: entender índices positivos y negativos.

# # # texto = "Programación"
# # # # l = round((len(texto) - 1)/2)
# # # x = len(texto)
# # # l = texto[1:]
# # # print(l)
# # # print(texto[l])


# # # def palabra(word: str):
# # #     x = len(word)
# # #     print(f"Su palabra tiene {x} caracteres.")

# # #     if x >= 8:
# # #         return "Su palabra tiene mas de 8 caracteres."
# # #     elif x == 0:
# # #         return "No tiene caracteres."


# # # f = input("Ingrese su palabra: ")
# # # print(palabra(f))
# # # input("Presione cualquier tecla para salir. ")


# # # def min(w: str) -> str:
# # #     word = w.lower()
# # #     return word


# # # def spa(w: str) -> str:
# # #     # f = w.replace(" ", "")
# # #     f = w
# # #     f = f.strip()
# # #     return f


# # # def juntar(w: str) -> str:
# # #     return spa(min(w))


# # # print(juntar(" HolA "))


# # # palabra = "python"


# # # def ul(word: str) -> str:
# # #     count_o = 0
# # #     for i in word:
# # #         print(i)
# # #         if "o" in i:
# # #             count_o += 1
# # #     return count_o


# # # print(ul("hola xd ooo "))

# # # print(palabra[::2])

# # # def replaces(w: str) -> str:
# # #     for i in w:
# # #         if "a" in w:
# # #             l = w.replace("a", "@")
# # #             x = l.replace(" ", "_")
# # #     return x


# # # print(replaces("hola Reyna"))

# #  * BLOQUE 3

# # # frase = input("Ingrese su frase: ")

# # frase = "El futuro pertenece a quienes creen en la belleza de sus sueños"
# # palabras = []
# # palabra_actual = ""

# # for i in frase:
# #     if i == " ":
# #         if palabra_actual:
# #             palabras.append(palabra_actual)
# #             palabra_actual = ""
# #     else:
# #         palabra_actual += i

# # if palabra_actual:
# #     palabras.append(palabra_actual)


# # # print(palabras[4])

# # # print(len(palabras))


# # def counter(cadena):
# #     ultima_palabra = ""
# #     for i in range(0, len(cadena)):
# #         if len(cadena[i]) > len(ultima_palabra):
# #             ultima_palabra = cadena[i]
# #         else:
# #             ultima_palabra = ultima_palabra
# #     # z = len(ultima_palabra)
# #     return ultima_palabra


# # print(palabras)
# # print(len(palabras))
# # print(counter(palabras))


# letras = ["p", "y", "t", "h", "o", "n"]


# def unir(letras):
#     juntas = ""
#     for i in letras:
#         juntas += i
#     return juntas


# letras = ["p", "y", "t", "h", "o", "n"]


# def barra(letras):
#     juntar = ""
#     for i in letras:

#         juntar += i
#         if i in letras:
#             juntar += "-"
#     return juntar[:-1]


# print(barra(letras))


# * Bloque 4

pal = input("Ingrese una palabra: ")
pal2 = input("Ingrese su segunda palabra: ")


# def invertir(pal):
#     x = pal[::-1]
#     if x == pal:
#         return f"Las palabras son iguales! {x}"
#     else:
#         return "Son diferentes"


# print(invertir(pal))

def iso(Pal):
    lista = {}
    for i in pal:
        if i in lista:
            lista[i] += 1
        else:
            lista[i] = 1
    return lista


# print(iso(pal))

def comparacion(pal1, pal2):
    palabras = {}
    pal1 = pal1.lower()
    pal2 = pal2.lower()

    if len(pal1) == len(pal2):
        return f"tienen la misma longitud {len(pal1)}"

    if iso(pal1) == iso(pal2):
        return ("Tienen las mismas letras")


print(comparacion(pal, pal2))
