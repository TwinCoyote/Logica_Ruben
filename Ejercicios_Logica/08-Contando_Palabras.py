
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.


def verify(word: str, dic: dict) -> str:
    """Function for compare word in dictionary and add if it isn't there"""
    if word in dic:
        dic[word] += 1
        word = ""
    else:
        dic[word] = 1
        word = ""

    return ""


def words_counter(frase: str) -> dict:
    """Principal Function for words counter"""
    allowed = "abcdefghijklmnopqrstuvwxyz "
    dic = {}
    word = ""
    for z in frase:
        z = z.lower()
        if z in allowed:
            i = z
        else:
            return f"Caracteres no permitidos {z}"
        # i = i.lower()
        if i == " ":
            word = verify(word, dic)
            # if word in dic:
            #     dic[word] += 1
            #     word = ""
            # else:
            #     dic[word] = 1
            #     word = ""
        elif i != " ":
            word += i
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1
    return dic


print(words_counter(input("Ingrese su frase: ")))
