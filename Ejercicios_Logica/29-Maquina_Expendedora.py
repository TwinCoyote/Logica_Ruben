"""Module providing a function printing python version."""
# pylint: disable = C0305,C0103,C0301
#  * Simula el funcionamiento de una máquina expendedora creando una operación
#  * que reciba dinero (array de monedas) y un número que indique la selección
#  * del producto.
#  * - El programa retornará el nombre del producto y un array con el dinero
#  *   de vuelta (con el menor número de monedas).
#  * - Si el dinero es insuficiente o el número de producto no existe,
#  *   deberá indicarse con un mensaje y retornar todas las monedas.
#  * - Si no hay dinero de vuelta, el array se retornará vacío.
#  * - Para que resulte más simple, trabajaremos en céntimos con monedas
#  *   de 5, 10, 50, 100 y 200.
#  * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.


productos = {
    1: {"nombre": "Coca-Cola", "precio": 150},
    2: {"nombre": "Papas Fritas", "precio": 120},
    3: {"nombre": "Chocolate", "precio": 100},
    4: {"nombre": "Agua Embotellada", "precio": 95},
    5: {"nombre": "Galletas de Avena", "precio": 85},
    6: {"nombre": "Jugo de Naranja", "precio": 135}
}

MONEDAS_SOPORTADAS = [200, 100, 50, 10, 5]

ingreso = [100, 100]


def maquina(articulo: int, monedas: list):
    """Maquina de snacks"""
    devolucion = []
    total_ingresado = 0
    if articulo in productos:
        print(
            f"Usted ha seleccionado '{productos[articulo]['nombre']}' con un precio de ${productos[articulo]['precio']}")
    else:
        return "Producto no valido", monedas
    precio = int(productos[articulo]["precio"])
    for i in monedas:
        if i in MONEDAS_SOPORTADAS:
            total_ingresado += int(i)
        else:
            return f"ERROR: Moneda ${i} No valida", monedas
    cantidad = precio - total_ingresado
    if cantidad < 0:
        cantidad = abs(cantidad)
        while cantidad > 0:
            for i in MONEDAS_SOPORTADAS:
                # if cantidad % i == 0:
                if i <= cantidad:
                    cantidad -= i
                    devolucion.append(i)
                    break
    elif total_ingresado < precio:
        return "La cantidad ingresada no es suficiente", monedas
    else:
        return productos[articulo]["nombre"], []

    return productos[articulo]["nombre"], devolucion


print(maquina(6, ingreso))
