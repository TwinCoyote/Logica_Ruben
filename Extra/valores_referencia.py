

# * Bloque 1 - Asignacion Basica.
# // Ejercicio 1
a = 10
b = a
b += 5

R = "Cuando se usa una variable como las tipicas de int, str... y se usa despues ese valor, se copia para poder ser usado por ser un valor inmutable"

# print(a)
# print(b)

# // Ejercicio 2

lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)

# print(lista1)
# print(lista2)

Re = "Las listas cambian porque son valores mutables y estos cuando se usan despues de ser declaradas en vez de hacer una copia, para una referencia poreso" \
    "en este caso se declara la lista1 y la referenecia se le pasa a la lista2 como si fuera un link(A como lo quise ver) para luego poder ser alterado" \
    "por ser un valor mutable"

# * Bloque 2 - Funciones
# // Ejercicio 3


def fun(x):
    x = x*2
    return f"Dentro de la funcion el numero es {x}"


x = 7
# print(fun(x))
# print(f"Fuera de la funcion su numero es {x}")

res = "La variable original, no cambio en nada, pero dentro de la funcion si cambio"
# // Ejercicio 4
lista = [1, 2, 3, 4]


def cambio(li):
    z = li.append(5)
    return f"Dentro de la funcion {li}"


# print(f"Fuera de la funcion {lista}")
# print(cambio(lista))

resp = "Si cambio la lista original al ser mutable tuvo un cambio desde la referencia y algo que note es que no pude imprimir la variable z y tuve que volver" \
    "a poner la variable de entrada en este caso en la funcion era li, y de esa forma se pudo imprimir ya que como tal al agregar el append y no ser mutable regresa 'none'" \
    ",pero si cambia la lista original"

# * Bloque 3 - copias
# // Ejercicio 5

a = [1, 2, 3]

li = a.copy()
f = li.append(4)

# print(f"Original: {a}")
# print(f"copia: {li}")

# //Ejercicio 6

dic = {"ruben": 24}

di = dic.copy()
z = di["ruben"] = 15


# print(f"Original: {dic}")
# print(f"copia: {di}")


# //Ejercicio 7

a = [1, 2]
b = a
b = b + [3]

# print(a)
# print(b)
respu = "el valor de a no cambio en nada, lo que hizo es que en b se le asigna una referencia y cuando se suma se crea un nuevo objeto con el '+' "

# //Ejercicio 8


def sex(li):
    z = li + [5]
    return z


# print(f"antes: {a}")
# print(f"Despues: {sex(a)}")
# print(f"antes: {a}")

# temp = 0
# for i in range(1, 11):
#     va = i
#     print(f"Valor inicial: {va}, el valor anterior: {temp}")
#     temp = va


# acumulador = 0
# for i in range(0, 6):
#     print(acumulador)
#     acumulador += 2


# a = 1
# b = 2
# temp = 0
# for i in range(0, 3):
#     print(f"a = {a}")
#     print(b)
#     temp = b
#     a = a + b
#     b += temp


# TODO MY FIBONACCI!!

# n = 50

# a = 0
# b = 1
# for i in range(0, n):
#     print(a)
#     c = a + b
#     a = b
#     b = c


# libros = [50, 400, 230, 500, 600, 43, 23, 45, 56, 78, 98, 67, 56]

# paginas = 0
# for i in libros:
#     paginas += i

# print(paginas)


def cuenta(n):
    if n > 0:
        print(n)
        cuenta(n + 1)
    else:
        return


print(cuenta(10))
