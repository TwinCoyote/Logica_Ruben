
# * Crea un programa que invierta el orden de una cadena de texto
# * sin usar funciones propias del lenguaje que lo hagan de forma automática.
# * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invertir(cadena):
    j = ""
    for i in range(len(cadena)-1, -1, -1):
        j += cadena[i]
    return j


print(invertir("Hola mundo"))

# print(len("Hola Mundo"))
