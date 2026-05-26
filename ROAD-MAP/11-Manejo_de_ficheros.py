# pylint: disable=W0621,C0116,C0103,C0301,c0200,c0114

#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo que se llame como
#  * tu usuario de GitHub y tenga la extensión .txt.
#  * Añade varias líneas en ese fichero:
#  * - Tu nombre.
#  * - Edad.
#  * - Lenguaje de programación favorito.
#  * Imprime el contenido.
#  * Borra el fichero.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un programa de gestión de ventas que almacena sus datos en un
#  * archivo .txt.
#  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt


# archivo = open("mi_archivo.txt", "w")
# archivo.write("Hola Mundo")
# archivo.close()

# with open("prueba.txt", "w", encoding="utf-8") as archivo:
#     archivo.write("hola \n  línea  2\n línea 3\n")


# with open("prueba.txt", "r", encoding="utf-8") as archivo:
#     print(archivo.read())


# with open("solo.txt", "w") as archivo:
#     archivo.write("Hola\n Ruben\n que tal?")

# with open("solo.txt", "r") as archivo:
#     print(archivo.read())

# import os
# os.remove("solo.txt")

# import os

# with open("ejercicio.txt", "w", encoding="utf-8") as archivo:
#     archivo.write("Ruben777 \t Lino Ruben\t 24 Años \t python")


# with open("ejercicio.txt", "r", encoding="utf-8") as archivo:
#     print(archivo.read().split(", "))


# os.remove("ejercicio.txt")


# linea = "manzana, 10, 5.50"
# partes = linea.split(", ")
# print(partes)

# partes = ['manzana', '10', '50.50']
# # print(partes[1]+partes[2])
# cantidad = int(partes[1])
# precio = float(partes[2])
# print(cantidad + precio)

import os


def busquedas(opcion: str):
    with open("tienda.txt", "r", encoding="utf-8")as archivo:
        for i in archivo.readlines():
            if opcion in i:
                return f"\n {i}"

        return "No se encontro ese nombre"


def busquedas_comprobacion(opcion: str) -> bool:
    with open("tienda.txt", "r", encoding="utf-8")as archivo:
        for i in archivo.readlines():
            if opcion in i:
                return True

        return False


Flag = True
with open("tienda.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Sistema de Ingreso articulos \n \t \tRuben Reyna\n \n \n")
while Flag:

    print("\n Bienvenido al sistema de ventas: \n Ruben Reyna \n")
    print("Ingrese la opcion que desea selecciona: \n 1- Añadir producto\n 2- Consultar Producto\n 3- Eliminar Producto\n 4- Actualizar producto\n 5- Salir\n ")
    x = int(input("Ingrese la opccion: "))

    if x == 1:
        ingreso = input("Ingrese el articulo añadir: ")
        if busquedas_comprobacion(ingreso):
            print("\nYa existe un registro con ese nombre")
            input("\n Enter para continuar\n")
        else:
            cantidad_vendida = input("Ingrese la cantidad Vendida: ")
            precio = input("ingrese el precio del articulo: ")

            with open("tienda.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"{ingreso},{cantidad_vendida},{precio}\n")
                input("\n Enter para continuar\n")

    if x == 2:
        busqueda = input("Ingrese el articulo a buscar: ")
        print(busquedas(busqueda))
        input("\n Enter para continuar\n")

    if x == 3:
        f = input("Ingrese el articulo a eliminar: ")
        if busquedas_comprobacion(f):
            with open("tienda.txt", "r", encoding="utf-8")as archivo:
                documento = archivo.readlines()
                lista_nueva = []
                for linea in documento:
                    if f not in linea:
                        lista_nueva.append(linea)
                        documento = lista_nueva
            with open("tienda.txt", "w", encoding="utf-8")as archivo:
                archivo.writelines(documento)
            print("Exito en la elimiacion")

    if x == 4:
        f = input("Ingrese el articulo a actualizar: ")
        cantidad = input("Ingrese la cantidad: ")
        precio = input("Ingrese el precio: ")
        if busquedas_comprobacion(f):
            with open("tienda.txt", "r", encoding="utf-8") as archivo:
                documento = archivo.readlines()
                for i in range(len(documento)):
                    if f in documento[i]:
                        r = documento[i].split(",")
                        documento[i] = f"{f},{cantidad},{precio}"
            with open("tienda.txt", "w", encoding="utf-8")as archivo:
                archivo.writelines(documento)

    if x == 5:
        Flag = False
        os.remove("tienda.txt")
