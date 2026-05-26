
#  * Escribe una función que calcule si un número dado es un número de Armstrong
#  * (o también llamado narcisista).
#  * Si no conoces qué es un número de Armstrong, debes buscar información
#  * al respecto.

def lista_numeros(x: int) -> list:
    """Funcion que convierte un numero en una lista"""
    numeros_separados = []
    ns = str(x)
    for i in ns:
        numeros_separados.append(i)
    return numeros_separados


def sumar_lista(x: list) -> bool:
    """Funcion que suma los numeros de una lista"""
    suma = 0
    potencia = len(x)
    for i in range(len(x)):
        numero = int(x[i])
        suma += numero**potencia
    return suma

    # print(lista_numeros(534))


def armstrong(x: int) -> str:
    """Funcion que compara la suma de numeros con su entrada original 
para comprobar si es un numero de armstrong """

    primera_etapa = lista_numeros(x)
    segunda_etapa = sumar_lista(primera_etapa)
    if segunda_etapa == x:
        return f"Felicidades has encontrado un numero de armstrong x = {x} y la suma es {segunda_etapa}"
    else:
        return f"No es un numero de armstrong  x = {x} y la suma es {segunda_etapa}"


print(armstrong(153))
