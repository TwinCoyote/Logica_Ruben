

# def recursividad(n: int) -> int:
#     if n < 0:
#         return
#     print(n)
#     recursividad(n - 1)
#     return


# recursividad(5)

# def misterio(n: int):
#     if n < 0:
#         return
#     misterio(n - 1)  # La llamada va ANTES
#     print(n)


# misterio(4)

# def factorial(n: int) -> int:
#     if n > 125:
#         return
#     print(n)
#     input("Presiona...")
#     factorial(n * (n-1))
#     return


# print(factorial(5))


# def suma_hasta(n):
#     if n <= 1:
#         return 1
#     resultado = n + suma_hasta(n-1)
#     return resultado


# print(suma_hasta(5))

# def sumarec(n: int) -> int:
#     if n <= 1:
#         return 1
#     return n + sumarec(n-1)


# print(sumarec(5))


# def farec(n):
#     if n <= 1:
#         return 1
#     s = n * farec(n-1)
#     print(s)
#     return s


# print(farec(5))

# list = ["pablo", "zuri", "beth", "Ruben"]


# def listrec(lista, i):
#     if i != len(lista):
#         print(lista[i])
#         listrec(lista, i + 1)
#         return 1


# print(listrec(list, 0))

# TODO  = Caso Base es la condicion de parada de nuestra recursion

# def cuenta(n):
#     if n >= 101:
#         return
#     print(n)
#     return cuenta(n + 1)


# print(cuenta(1))

# def fact(n):
#     if n == 0:
#         return 1
#     factor = n * fact(n-1)
#     print(factor)
#     return factor


# print(fact(5))


# def eco(pal: str, n: int) -> str:
#     # Caso Base
#     if n <= 0:
#         return
#     ##############

#     print(pal)
#     return eco(pal, n - 1)


# print(eco("hola", 5))

# def griton(pal: str):
#     if pal == "":
#         return ""
#     return pal[1:] + "-" + griton(pal[1 + 1])


# print(griton("hola"))

# ! Ejercicios gemini

# def count(n: int) -> str:
#     if n <= 0:
#         return "Ignicion"
#     print(f"Iniciando...{n}")
#     return count(n - 1)


# print(count(5))

# def proh(n: int) -> int:
#     if n <= 0:
#         return "."

#     if n % 2 == 0:
#         print(n)
#     return proh(n-1)


# print(proh(10))

# def impar(n: int) -> int:
#     if n <= 0:
#         return 0
#     elif n % 2 != 0:
#         print(n)
#         return n + impar(n - 1)
#     else:
#         return impar(n-1)


# print(impar(5))


# def griton(pal: str) -> str:
#     if pal == "":
#         return ""
#     llevada = pal[0].upper() + " "

#     return llevada + griton(pal[1:])


# print(griton("hola"))

# def griton_selectivo(pal: str) -> str:
#     # 1. Caso Base: ¿Se acabó la palabra?
#     if pal == "":
#         return ""

#     # 2. Proceso la primera letra
#     letra_actual = pal[0].upper() + " "

#     # 3. La pego al resultado de procesar el resto
#     return letra_actual + griton_selectivo(pal[1:])


# print(griton_selectivo("hola"))  # "H O L A "


# def espacios(pal: str) -> str:
#     if pal == "":
#         return ""
#     llevada = pal[0].replace(" ", "")
#     return llevada + espacios(pal[1:])


# print(espacios(" H o l a _ R u b 3 n "))


# def det(pal: str, letra: str) -> bool:
#     if pal == "":
#         return False
#     llevada = pal[0]
#     if letra in llevada:
#         return True
#     return det(pal[1:], letra)


# print(det("Hola", "a"))


# def palabras(pal:str):
#     if pal
#     return

# pal = "hola"
# print(pal[-1])

# def primera_y_ultima(pal: str) -> str:
#     # Guardamos la primera letra una sola vez
#     primera = pal[0]

#     # Usamos una función interna para buscar la última
#     def buscar_ultima(p):
#         if len(p) == 1: # Caso base: solo queda una letra
#             return p
#         return buscar_ultima(p[1:]) # Recortamos hasta llegar al final

#     ultima = buscar_ultima(pal)
#     return primera + ultima

# print(primera_y_ultima("HOLA")) # "HA"

# def facto(n: int) -> int:
#     if n <= 0:
#         return 1
#     print(n)
#     return n * facto(n-1)


# print(facto(5))

# def fibo(n):
#     if n <= 5:
#         return 1
#     f = fibo(n-1) + fibo(n-2)
#     return f


# print(fibo(15))

# def a(n):
#     if n <= 0:
#         return 0
#     print(n)
#     return a(n-1)


# print(a(5))

# def lista(n):
#     if n <= 0:
#         return []
#     return lista(n-1) + [n]


# print(lista(8))

# def tabla(n: int) -> list:
#     if n <= 0:
#         return [0]
#     return [n] + tabla(n-1)


# print(tabla(5))


# def x(n):
#     a = []
#     for i in range(1, 11):
#         f = a.append(i * n)
#     return a[::-1]


# print(x(5))

# def cuenta(n):
#     if n <= 0:
#         return [0]
#     return [n] + cuenta(n-1)


# print(cuenta(5))

# def suma(n):
#     if n <= 0:
#         return 0
#     print(n)
#     return n + suma(n-1)


# print(suma(5))


# def fibo(n):
#     print("Llamando a fibo(", n, ")")

#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     return fibo(n-1) + fibo(n-2)


# print(fibo(4))


# def factorial(n):
#     if n <= 0:
#         return 1
#     return n * factorial(n-1)


# print(factorial(5))
