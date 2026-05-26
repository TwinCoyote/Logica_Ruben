# pylint: disable = C0103,C0114

# import time


# def tarea(nombre: str, segundos: int) -> str:
#     """Funcion de prueba asincrona"""
#     inicio = time.time()
#     print(f"{nombre} empieza")
#     time.sleep(segundos)
#     final = time.time()
#     duracion = int(final - inicio)

#     print(f"{nombre} Termino en {duracion}")


# tarea("A", 1)
# tarea("B", 2)
# tarea("C", 3)
import time
import asyncio as r


async def tarea(nombre: str, segundos: int):
    """Funcion para probar async"""
    inicio = time.time()
    print(f"{nombre} empieza")
    await r.sleep(segundos)
    print(f"{nombre} termina")
    final = time.time()
    duracion = int(final - inicio)
    print(f"{nombre} duro {duracion} Segundos")


async def main():
    """Funcion main para el async"""

    await r.gather(
        tarea("A", 1),
        tarea("B", 2),
        tarea("C", 3)
    )
    await tarea("D", 1)

r.run(main())
