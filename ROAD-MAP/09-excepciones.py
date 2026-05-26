
# # try:
# div = 10/0
# # except ZeroDivisionError as e:
# #     print("Error:", e)


# def error(x):
#     try:
#         lista = [1, 2, 3]
#         return lista[x]
#     except IndexError as e:
#         print(f"Error: {e}")


# print(error(5))

class MiError(Exception):
    def __init__(self, saldo_actual, cantidad_intento):
        self.saldo_actual = saldo_actual
        self.cantidad_intento = cantidad_intento
        self.mensaje = f"El numero en {saldo_actual} No puede ser negativo"

        super().__init__

try:
    numero = int(input("Ingrese su numero: "))
    x = numero / 4
    print(x)
except ValueError as e:
    print(f"Error: {e}")
