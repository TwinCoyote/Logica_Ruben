# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622
#  * Crea una función que sume 2 números y retorne su resultado pasados
#  * unos segundos.
#  * - Recibirá por parámetros los 2 números a sumar y los segundos que
#  *   debe tardar en finalizar su ejecución.
#  * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#  *   asíncrona, es decir, sin detener la ejecución del programa principal.
#  *   Se podría ejecutar varias veces al mismo tiempo.
# import time
import asyncio


# async def suma(x: int, y: int, tiempo: int) -> int:
#     """Funcion asincrona que tarda `tiempo` segundos y devuelve la suma.
#     Si se proporciona `nombre`, imprime inicio/fin y duración.
#     """
#     await asyncio.sleep(tiempo)
#     sumar = x + y
#     return sumar


# async def main():
#     resultados = await asyncio.gather(
#         suma(5, 4, 2),
#         suma(2, 3, 5),

#     )
#     print(resultados)


# asyncio.run(main())
import time
H = "Hamburguesa"
E = "Ensalada"
P = "Pasta"


async def tardanza(tiempo: int, comida: str):
    inicio = time.time()
    await asyncio.sleep(tiempo)
    final = time.time()
    estimado = final - inicio
    return comida, round(estimado)


async def kitchen():

    platillos = await asyncio.gather(
        tardanza(4, H),
        tardanza(1, E),
        tardanza(3, P)
    )
    print(platillos)

asyncio.run(kitchen())
# print(comidas["Hamburguesa"])
