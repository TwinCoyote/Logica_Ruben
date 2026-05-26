#   Escribe un programa que imprima los 50 primeros números de la sucesión
#   de Fibonacci empezando en 0.
#   - La serie Fibonacci se compone por una sucesión de números en
#     la que el siguiente siempre es la suma de los dos anteriores.
#     0, 1, 1, 2, 3, 5, 8, 13...


# TODO recuerda usar una variable temporal para almacenar el antiguo valor de la sucesion asi como lo viste en la leccion 5 - valores y referencia

n = 50


def fibo(n):
    a = 0
    b = 1
    for i in range(0, n):
        print(a)
        c = a + b
        a = b
        b = c
        return b
