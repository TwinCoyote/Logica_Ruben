# pylint: disable = C0103,C0114
#  * EJERCICIO:
#  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
#  * operaciones (debes utilizar una estructura que las soporte):
#  * - Añade un elemento al final.
#  * - Añade un elemento al principio.
#  * - Añade varios elementos en bloque al final.
#  * - Añade varios elementos en bloque en una posición concreta.
#  * - Elimina un elemento en una posición concreta.
#  * - Actualiza el valor de un elemento en una posición concreta.
#  * - Comprueba si un elemento está en un conjunto.
#  * - Elimina todo el contenido del conjunto.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.

# micros = ["Arduino", "STM32"]
# agregar = "ESP32"
# # micros.append(agregar)
# # print(micros)
# micros.insert(0, agregar)
# print(micros)

# lista = []
# lista.extend(["React", "Node", "Python"])
# print(lista)


# ? Ejercicio 4

# lista = [1, 2, 6]
# lista[2:2] = [3, 4, 5]
# print(lista)

# ? Ejercicio 5

# lista = ["esp32", "tiva", "Arduino", "STM32"]
# print(lista)
# lista.remove("STM32")
# print(lista)

# ? Ejercicio 6

# lista = ["Arduino", "PIC"]
# lista[0] = "ESP32"
# print(lista)

# ? Ejercicio 7
# lista = ["Arduino", "PIC", "ESP32"]
# if "ESP32" in lista:
#     print("Si esta")

# ? Ejercicio Final P1
# alumnos = ["Ruben", "Daniel", "Brayan", "Turco", "Boca-Negra", "Andrea", "Ali"]
# print("la lista es: ", alumnos)

# alumnos.append("ABEL")
# print("Se agrego un alumno: ", alumnos)

# alumnos.extend(["Juan", "Ignacio", "Oscar"])
# print("Se agregaron varios alumnos: ", alumnos)

# alumnos.pop(1)
# print("Se elimino uno", alumnos)

# alumnos[2] = "Cedrez"
# print("Se actualizo el nombre de 'Brayan:", alumnos)

# if "Ruben" in alumnos:
#     print("Si esta 'Ruben' en la lista")


# alumnos.clear()
# print("Se vacio la lista, mira ", alumnos)


# ? Final Parte 2
# frontend = {"HTML", "CSS", "JavaScript", "React", "Tailwind"}

# backend = {"Python", "JavaScript", "NodeJS", "SQL", "Docker"}


# print(frontend | backend)
# print(frontend & backend)
# print(frontend - backend)
# print(frontend ^ backend)

# ? Bonus
jugadores1 = {"Ruben", "Daniel", "Turco"}
jugadores2 = {"Turco", "Andrea", "Ali"}

print("Jugadores Totales", jugadores1 | jugadores2)

print("jugadores repetidos", jugadores1 & jugadores2)
