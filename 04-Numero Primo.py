# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

def primos(n):

    for i in range(2, n):
        if (n % i) == 0:
            return None

    return "Es primo"


for i in range(100 + 1):
    print(i, primos(i))
