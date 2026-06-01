# # pylint: disable=C00114,C0304,C0200,W0621,C0116,C0303
# #! Ejercicio 1
# # frutas = ["manzana\n", "leche\n", "pan\n", "manzana verde\n"]

# # for i in range(len(frutas)):
# #     if "leche" in frutas[i]:
# #         frutas[i] = "cafe\n"
# # print(frutas)

# #! Ejercicio 2
# # productos = ["manzana,10,5.50\n", "leche,3,20.00\n", "pan,15,12.00\n"]
# # for i in range(len(productos)):
# #     if "leche" in productos[i]:
# #         print(productos[i])
# #         productos[i] = "leche,99,20.00"
# # print(productos)


# #! Ejercicio 3
# # Crea un archivo amigos.txt con 4 nombres, uno por línea.
# # Luego escribe un programa que pregunte qué nombre quieres cambiar y por cuál,
# # y sobreescriba el archivo con el cambio.

# # with open("amigos.txt", "w", encoding="utf-8") as archivo:
# #     archivo.write("ali\n daniel\n andrea\n brayan\n ")


# # def cambiar_nombre(anterior: str, nuevo: str):
# #     anterior = anterior.lower()
# #     nuevo = nuevo.lower()
# #     with open("amigos.txt", "r", encoding="utf-8") as archivo:
# #         documento = archivo.readlines()
# #         for i in range(len(documento)):
# #             if anterior in documento[i]:
# #                 documento[i] = f"{nuevo}\n"
# #     with open("amigos.txt", "w", encoding="utf-8")as archivo:
# #         archivo.writelines(documento)
# #     return "Exito"


# # print(cambiar_nombre("ali", "ruben"))

# #! Ejercicio 4
# # Tienes productos con este formato nombre,cantidad,precio.
# # Escribe un programa que encuentre un producto por nombre y
# # solo actualice el precio si la cantidad es mayor a 5. Si no,
# # imprime "Cantidad insuficiente para actualizar".

# # with open("ejercicio.txt", "w", encoding="utf-8")as archivo:
# #     archivo.writelines("manzana,4,100 \n platano,3,400 \n zanahoria,4,500")


# # def busqueda(buscar: str, valores: int):
# #     with open("ejercicio.txt", "r", encoding="utf-8") as archivo:
# #         documento = archivo.readlines()
# #         for i in range(len(documento)):
# #             if buscar in documento[i]:
# #                 f = documento[i].split(",")
# #                 valor = f[1]
# #                 if int(valor) <= 5:
# #                     valor = str(valores)
# #                     documento[i] = f"{f[0]},{valor},{f[2]}"

# #     with open("ejercicio.txt", "w", encoding="utf-8") as archivo:
# #         archivo.writelines(documento)
# #     return "Actualizado: ", documento


# # print(busqueda("zanahoria", 6))


# # # ! Prueba rara 5
# # pokemon = {
# #     "types": [
# #         {
# #             "slot": 1,
# #             "type": {
# #                 "name": "electric",
# #                 "url": "https://pokeapi.co/api/v2/type/13/"
# #             }
# #         },
# #         {
# #             "slot": 2,
# #             "type": {
# #                 "name": "flying",
# #                 "url": "https://pokeapi.co/api/v2/type/14/"
# #             }
# #         }
# #     ],
# #     "weight": 60
# }
#     # for i in len(pokemon["types"]):
#     #     busqueda = pokemon["types"][i]["type"]["name"]
#     #     print(busqueda)

#     # print(len(pokemon["types"]))
#     # for i in range(len(pokemon["types"])):
#     #     print(pokemon["types"][i]["type"]["name"])

#     # for i in pokemon["types"]:
#     #     print(i["type"]["name"])


#     # for i, pok in enumerate(pokemon["types"], start=1):
#     #     busqueda = pok["type"]["name"]
#     #     urls = pok["type"]["url"]
#     #     print(f"Tipo {i}: {busqueda}\n URL: {urls}")


# x = -121


# def Palin(m: int):
#     if m < 0:
#         return False
#     f = int(str(m)[::-1])
#     if f == m:
#         return True
#     return False


# print(Palin(1234))

# Reto Inicial (Fuera de LeetCode): Suma de Dígitos.
# Toma el número 456 y haz un bucle
#  que sume 4 + 5 + 6. (Pista: Usa un while x > 0,
# extrae con x % 10 y encoge con x // 10).

# ? Logica Bit a Bit
# x = 456967890


# def suma(m):
#     while m > 0:
#         suma = (m // 100) + ((m % 100)//10) + (m % 10)
#         break
#     return suma


# print(suma(x))


# def sumar(m: int) -> int:
#     temp = 0
#     while m > 0:
#         temp += (m % 10)
#         m = (m // 10)

#     return temp


# print(sumar(x))
# print(x % 10)  # 6
# # # print(x % 100)  # 56
# # # print(x//10)  # 45
# # # print(x//100)  # 4
# # print((x % 100) % 10)  # 5

# print(x // 100)
# print((x % 100)//10)
# print(x % 10)

# ? Ejercicio 2


# x = 127

# uno = x % 10
# x = x // 10
# dos = x % 10
# x = x//10

# print(uno)7
# # print(x)
# print(dos)2
# # print(x)
# print(x % 10)1


# def sumar(x: int) -> int:
#     cuenta = 0
#     while x > 0:
#         cuenta += x % 10
#         x = x // 10
#         # print(x)
#         # print(cuenta)
#     return cuenta


# print(sumar(1279))
# x = 1
# s //= 10
# print(x//10)
# print(s)


# def palin(x):

#     temp = 0
#     while x > 0:
#         temp += x % 10
#         x = x // 10

#     return temp


# print(palin(127))


# x = 128
# # print(((x // 10) // 10)//10)


# def palin(x):
#     m = x
#     temp = 0
#     while m > 0:
#         temp = temp * 10 + (m % 10)
#         m = m//10

#     return temp == x


# print(palin(x))


romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


# x = romanos.items()
# temp = {}
# for v, c in x:
#     temp[c] = v

# if 1 in temp:
#     print("si")
#     print(temp[1])
# else:
#     print("No")


# def romanos_int(x):
#     # ? Separando
#     # E_R = {}
#     # for v, c in romanos.items():
#     #     E_R[c] = v
#     temp = 0
#     cuenta = 0
#     for i in x[::-1]:
#         if i in romanos:
#             # print(romanos[i])
#             s = romanos[i]

#             if int(s) < temp:

#                 cuenta -= int(s)

#             cuenta += int(s)
#             print(f"Este es 's' {s}")


#             temp = int(s)


#         else:
#             print("Eso q MEN?")
#     print(cuenta)


# def romanos_int(x):
#     x = x.upper()
#     # ? Separando
#     temp = 0
#     cuenta = 0
#     for i in x[::-1]:
#         if i in romanos:
#             m = int(romanos[i])
#             if m < temp:
#                 cuenta -= m
#             else:
#                 cuenta += m
#             temp = m
#     return cuenta


# print(romanos_int("MCMXCIV"))

# F = len("hola")
# for i in range(F, -1, -1):
#     print(list(i))


strs = ["flower", "flow", "flight"]


# print(strs[1])

# [print(list(i)) for i in strs[1]]

# acumulador = []


# def acumular(s: list[str]):
#     referencia = s[0]

#     for i in referencia:
#         letra =


# print(strs[1:])


# reverse = "The greatest victory is that which requires no battle"
# def voletar(s):
#     n = s.split()
#     palabra = ""
#     for i in range(len(n) - 1, -1, -1):
#         palabra += n[i] + " "
#     return palabra.strip()


# x = "yoda doesn't speak like this"
# print(voletar(x))

# pal = "Hello"


# def volt(pal):
#     return pal[::-1]


# print(volt(pal))

# def create_phone_number(n: list[int]):
#     if len(n) > 10 or len(n) < 10:
#         return "Formato incorrecto, revisa el numero"
#     # codigo = n[0:2]
#     return f"{n[0:3]} {n[3:6]}-{n[6:]}"


# def create_phone_number(n: list[int]):
#     if len(n) > 10 or len(n) < 10:
#         return "Formato incorrecto, revisa el numero"
#     numero = ""
#     for i in n:
#         numero += str(i)
#     return f"({numero[0:3]}) {numero[3:6]}-{numero[6:]}"


# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


# string = "12334e"


# def filter_numbers(string):
#     return "".join(x for x in string if not x.isdigit())


# print(filter_numbers(string))

