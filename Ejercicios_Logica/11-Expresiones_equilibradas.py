
#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }


x = input("Ingresa la expresion: ")


def equilibrio(expresion):
    memory = []
    for i in expresion:
        if i in "{[(":
            memory.append(i)

        elif i in "}])":
            if i == memory[-1]:
                memory.pop(-1)
    return memory


print(equilibrio(x))
