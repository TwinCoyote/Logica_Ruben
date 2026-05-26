
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.


def convert(num: int) -> list:
    """Funcion Recursiva para convertir decimal a binario bit por bit"""
    # numero = []
    if num < 1 or num == 1:
        return [num]
    # else:
    z = num % 2
    #     if z == 0:
    #         numero.append(0)
    #     else:
    #         numero.append(1)
    return convert(num // 2) + [z]


# def acomodo(di: list) -> list:
#     """Acomoda la lista para que los bits salgan en el orden correcto"""
#     data = di
#     lista_plana = []

#     for i in data:
#         lista_plana.append(i[0])
#     return lista_plana[::-1]


# def decimal_binario(decimal: int) -> list:
#     """Funcion que organiza el orden de ejecucion de las funciones"""
#     binario = convert(decimal)

#     return acomodo(binario)


Ingreso = int(input("Ingresa el numero que quieras convertir a binario: "))

print(convert(Ingreso))
