# pylint: disable=C0111,C0103,C0200
#  * Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras
#  *        "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo)
#  *        o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#  *        será correcto y no variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.


def normalizer(x: str, allowed: str):
    """Funcion para normalizar el texto y convertirlo a una lista de palabras permitidas"""
    # allowed_words = "run", "jump"
    allowed = allowed.split(",")
    x = x+" "
    x = x.lower()
    palabras = ""
    lista = []
    for i in x:
        if " " in i:
            lista.append(palabras)
            palabras = ""
        else:
            palabras += i
    for i in range(len(lista)):
        if lista[i] in allowed:
            pass
        else:
            return f"'{lista[i]}' no esta permitida."
    return lista


def recorrer(x: str, y: str):
    salida = ""
    x = normalizer(x, "run,jump")
    y = normalizer(y, "_,|")
    win = True
    for i, accion in enumerate(x):
        if accion == "run" and y[i] == "_":
            salida += "_"
        elif accion == "jump" and y[i] == "|":
            salida += "|"
        elif accion == "run" and y[i] == "|":
            salida += "/"
            win = False
        else:
            salida += "x"
            win = False
    print(salida)
    return win


# def recorrer(x: str, y: str):
#     salida = ""
#     x = normalizer(x, "run,jump")
#     y = normalizer(y, "_,|")
#     win = True
#     for i in range(len(x)):
#         if x[i] == "run" and y[i] == "_":
#             salida += "_"
#         elif x[i] == "jump" and y[i] == "|":
#             salida += "|"
#         elif x[i] == "run" and y[i] == "|":
#             salida += "/"
#             win = False
#         else:
#             salida += "x"
#             win = False
#     print(salida)
#     return win


print(recorrer("jump run jump", "| _ |"))
