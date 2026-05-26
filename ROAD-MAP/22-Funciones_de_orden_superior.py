# # pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622
# def sumar():
#     print("Estoy Sumando")


# def restar():
#     print("Estoy Restando")


# # operacion = sumar
# # print(operacion)


# numeros = [1, 2, 3, 4]

# resultado = []

# for numero in numeros:
#     resultado.append(numero * 2)

# print(resultado)


# def duplicar(numero):
#     return numero * 2 == 4


# numeros = [1, 2, 3, 4]

# resultado = map(duplicar, numeros)

# print(list(resultado))


# def es_par(numero):
#     return numero % 2 == 0


# resultado = filter(duplicar, numeros)
# print(list(resultado))


# micros = ["ESP32", "Arduino", "STM32"]

# resultado = sorted(micros,key=len)

# print(resultado)

# ? Ejercicio 1

# objetivo = [1, 2, 3, 4]

# def regla(xd: list):
#     return xd * 10

# hacer = map(regla, objetivo)

# print(list(hacer))

# ? Ejericio 2

# lista = [2, 7, 10, 1, 4, 9]


# def mayores(xd: list):
#     return xd > 5


# ls = filter(mayores, lista)
# print(list(ls))

# ? Ejericio 3
# lista = ["monitor", "mouse", "pcb", "arduino"]

# resultado = sorted(lista, key=len)

# print(list(resultado))

# TODO: Ejercicio Final


estudiantes = [
    {
        "nombre": "Ruben",
        "fecha_nacimiento": "2000-05-10",
        "calificaciones": [10, 9, 8]
    },
    {
        "nombre": "Andrea",
        "fecha_nacimiento": "2003-08-20",
        "calificaciones": [7, 8, 9]
    },
    {
        "nombre": "Daniel",
        "fecha_nacimiento": "1999-12-15",
        "calificaciones": [9, 10, 10]
    },
    {
        "nombre": "Ali",
        "fecha_nacimiento": "2004-01-11",
        "calificaciones": [6, 7, 8]
    }
]


objetivo = estudiantes[0]["calificaciones"]

# print(objetivo[0])


# def promedio(x):
#     return (x)/3


# x = map(promedio, estudiantes)

# print(list(x))
# print(sum(estudiantes[1]["calificaciones"]) /
#       len(estudiantes[1]["calificaciones"]))


def promedio_nombre(x):
    calificaciones = x["calificaciones"]
    nombre = x["nombre"]
    return f"{nombre}: {round((sum(calificaciones))/len(calificaciones))}"


def promedio(l):
    calificaciones = l["calificaciones"]
    return round((sum(calificaciones))/len(calificaciones))


m = map(promedio, estudiantes)


def validar(C):
    if promedio(C) >= 9:
        return True
    return False


def nombrar(N):
    return N["nombre"]


x = filter(validar, estudiantes)
z = map(nombrar, x)

print(list(z))
