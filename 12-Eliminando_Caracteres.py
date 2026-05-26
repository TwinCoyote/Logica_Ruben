"""#12"""

#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.


def letter_counter(palabra: str) -> dict:
    """Funcion para pasar la palabra a un diccionario"""

    dic = {}
    for i in palabra:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


def sub_comparacion(diccionario1: dict, diccionario2: dict) -> list:
    """Comparacion interna"""
    temp_list = []
    for i in diccionario1:
        if i not in diccionario2:
            temp_list.append(i)
    # if not temp_list:
    #     return False
    return temp_list


def comparacion(pal1: str, pal2: str) -> str:
    """Funcion para Comparar los diccionarios"""

    dic1 = letter_counter(pal1.lower())
    dic2 = letter_counter(pal2.lower())

    # Letras que faltan en el diccionario 1 que el 2 si tiene
    faltantes_dic1 = sub_comparacion(dic2, dic1)
    # Letras que faltan en el diccionario 2 que el 1 si tiene
    faltantes_dic2 = sub_comparacion(dic1, dic2)
    if not faltantes_dic1 and not faltantes_dic2:
        return "Las palabras tiene las mismas letras, podria ser un anagrama!"
    return f"""Las letras que faltan en el diccionario 1 que el 2 si tiene son: {faltantes_dic1} 
y las letras faltantes del diccionario 2 que si tiene el 1 son: {faltantes_dic2}"""


palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if palabra1.isalpha() and palabra2.isalpha():
    print(comparacion(palabra1, palabra2))
else:
    print("Solo se pueden ingresar caracteres que sean letras")
