# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,C0200
#  * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
#  * resultado e imprímelo.
#  * - El .txt se corresponde con las entradas de una calculadora.
#  * - Cada línea tendrá un número o una operación representada por un
#  *   símbolo (alternando ambos).
#  * - Soporta números enteros y decimales.
#  * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
#  *   y división "/".
#  * - El resultado se muestra al finalizar la lectura de la última
#  *   línea (si el .txt es correcto).
#  * - Si el formato del .txt no es correcto, se indicará que no se han
#  *   podido resolver las operaciones.


def calcular(numeros: list, op: list) -> float:
    """Funcion para detectar operaciones y calcularlas"""

    if len(op) == len(numeros) - 1:
        try:
            resultado = numeros[0]
            for i in range(len(numeros)-1):
                if op[i] == "+":
                    resultado += numeros[i+1]
                elif op[i] == "-":
                    resultado -= numeros[i+1]
                elif op[i] == "/":
                    resultado = resultado / numeros[i+1]
                elif op[i] == "*":
                    resultado *= numeros[i+1]
            return resultado
        except ZeroDivisionError as e:
            return f"Ha habido un error por: {e}"
    else:
        # Si las longitudes no cuadran, el formato es incorrecto
        return "No se han podido resolver las operaciones."


formato_valido = True
lista = []
operadores = []
letters = True
with open("Calculadora.txt", "r", encoding="utf-8") as archivo:
    m = archivo.readlines()
    equal = 0

    for p in range(len(m)):
        obj = m[p].strip()
        if obj == '+' or obj == "-" or obj == "/" or obj == "*":
            operadores.append(obj)
        else:
            try:
                lista.append(float(obj))
            except ValueError:
                formato_valido = False
                break

if formato_valido:
    print(calcular(lista, operadores))
else:
    print("No se han podido resolver las operaciones.")
