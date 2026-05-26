# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622
#  * EJERCICIO:
#  * Empleando tu lenguaje, explora la definición del tipo de dato
#  * que sirva para definir enumeraciones (Enum).
#  * Crea un Enum que represente los días de la semana del lunes
#  * al domingo, en ese orden. Con ese enumerado, crea una operación
#  * que muestre el nombre del día de la semana dependiendo del número entero
#  * utilizado (del 1 al 7).
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un pequeño sistema de gestión del estado de pedidos.
#  * Implementa una clase que defina un pedido con las siguientes características:
#  * - El pedido tiene un identificador y un estado.
#  * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
#  * - Implementa las funciones que sirvan para modificar el estado:
#  *   - Pedido enviado
#  *   - Pedido cancelado
#  *   - Pedido entregado
#  *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
#  * - Implementa una función para mostrar un texto descriptivo según el estado actual.
#  * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.

# from enum import Enum


# class Dias(Enum):
#     """Clase prueba Enum"""
#     lunes = 1
#     martes = 2
#     miercoles = 3
#     jueves = 4
#     viernes = 5
#     sabado = 6
#     domingo = 7

# ? Ejercicio 1

# print(Dias.lunes.name)


# # ? Ejercicio 2
# nombre = Dias.miercoles.name
# valor = Dias.miercoles.value
# print(nombre, valor)

# ? Ejercicio 3
# print(Dias(1))

# def QueDia(n: int) -> str:
#     """Funcion que retorna el dia apartir de un numero"""
#     if n >= len(Dias) or n < 1:
#         return print("Ese dia no existe men, que te pasa?")

#     return print(Dias(n))


# QueDia(5)

# TODO Actividad Extra

from enum import Enum


class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4


class Pedido:
    def __init__(self, id):
        self.id = id
        self.estado = EstadoPedido.PENDIENTE

    def enviar(self):
        if self.estado != EstadoPedido.ENTREGADO:
            if self.estado != EstadoPedido.CANCELADO:
                self.estado = EstadoPedido.ENVIADO
                print(f"Su pedido {self.id} Fue Enviado")

    def Entregado(self):
        if self.estado != EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
            print(f"Su pedido {self.id} Fue entregado correctamente")
        elif self.estado == EstadoPedido.PENDIENTE:
            print(
                f"Su pedido {self.id} no puede ser entregado por el estatus de su producto")

    def Cancelado(self):
        self.estado = EstadoPedido.CANCELADO
        print(f"Su pedido {self.id} Fue cancelado")


pedido1 = Pedido(1)
pedido2 = Pedido(2)

pedido1.enviar()
