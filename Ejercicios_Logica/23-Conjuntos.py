# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,C0200
#  * Crea una función que reciba dos array, un booleano y retorne un array.
#  * - Si el booleano es verdadero buscará y retornará los elementos comunes
#  *   de los dos array.
#  * - Si el booleano es falso buscará y retornará los elementos no comunes
#  *   de los dos array.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.


array1 = [1, 2, 3, 4, 0, 0]
array2 = [3, 4, 5, 6]


# def Venn(a1: list, a2: list,compa:bool) -> bool:
#     compartidos = []
#     diferentes = []
#     if compa:
#         for i in a1:
#             if i in a2:
#                 compartidos.append(i)
#             else:
#                 diferentes.append(i)
#         return compartidos


# def Venn(a1: list, a2: list, comp: bool) -> bool:
#     todos = []
#     diferentes = []
#     similares = []
#     for i in a1:
#         todos.append(i)
#     for i in a2:
#         todos.append(i)
#     if comp:
#         for i in todos:
#             if i in a1 and i in a2:
#                 if i not in similares:
#                     similares.append(i)
#         return similares
#     else:
#         for i in todos:
#             if i in a1 and i not in a2 and i not in diferentes:
#                 diferentes.append(i)
#             if i in a2 and i not in a1 and i not in diferentes:
#                 diferentes.append(i)
#         return diferentes


def Venn(a1: list, a2: list, comp: bool) -> bool:
    todos = []
    diferentes = []
    similares = []
    for i in a1:
        todos.append(i)
    for i in a2:
        todos.append(i)
    if comp:
        for i in todos:
            if i in a1 and i in a2:
                if i not in similares:
                    similares.append(i)
        return similares
    else:
        for i in a1:
            if i not in a2 and i not in diferentes:
                diferentes.append(i)
        for i in a2:
            if i not in a1 and i not in diferentes:
                diferentes.append(i)
        return diferentes


print(Venn(array1, array2, False))
