# pylint: disable = C0304,C0305
#  * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
#  * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
#  * - EXTRA: ¿Eres capaz de dibujar más figuras?


def figura(l: int, f: str) -> str:
    """Funcion que imprime los asteriscos"""
    h = 10  # Es la altura
    if f == "Cuadrado":
        for i in range(h):
            print("*"*l)
    elif f == "Triangulo":
        temp = 0
        for i in range(h):
            print("*" * temp)
            temp += 1


figura(19, "Triangulo")
