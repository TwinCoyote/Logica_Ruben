# pylint: disable = C0103,C0114

#  * EJERCICIO:
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?


# ? Ejercicio 1

# for i in range(5, 11):
#     print(i)


# ? Ejercicio 2

# conta = 10

# while conta >= 1:
#     print(conta)
#     conta -= 1

# ? Ejercicio 3

# micros = ["ESP32", "Arduino", "STM32"]

# for micro in micros:
#     print(f"Proyecto con {micro}")

# ? Ejercicio 4

# micros = ["ESP32", "Arduino", "STM32"]

# for i, micro in enumerate(micros):
#     print(f"{i} - {micro}")

# ! Prueba Ruben

# numeros = [i for i in range(0, 6)]
# print(numeros)


# ? Ejercicio 5
# cuadrados = [(i ** 2) for i in range(1, 10)]
# print(cuadrados)
# for o in range(0, 1):
#     print(o)

# ? Ejercicio 6
# for i in range(0, 11):
#     if i == 7:
#         continue
#     print(i)

# ! RETO FINAL

# ? Parte 1
# Imprime del 1 al 10 usando:
# for
# while
# otro mecanismo distinto


# for i in range(1, 11):
#     print(i)

# count = 1

# while count <= 10:
#     print(count)
#     count += 1


# def iterar(n: int) -> int:
#     """Funcion"""
#     if n > 10:
#         return
#     print(n)
#     return iterar(n+1)


# iterar(1)


# ? Parte 2

# for i in range(1, 11)[::-1]:
#     print(i)


# temp = 10

# while temp >= 1:
#     print(temp)
#     temp -= 1

# def itera(n):
#     '''Funcion para iterar'''
#     if n <= 0:
#         return
#     print(n)
#     return itera(n-1)


# itera(10)

# ? Parte 3

# temperaturas = [22, 25, 19, 31, 28, 35, 18]

# for temperatura in temperaturas:
#     if temperatura > 34:
#         break
#     if temperatura > 25:
#         print(temperatura)

# ? Parte 4

# for i in range(1, 6):
#     print(i * "*")

# ! Prueba
for i in range(10, 0, -1):
    print(i)
