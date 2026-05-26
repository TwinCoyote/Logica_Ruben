# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622
# 25 - LOGS

#  * EJERCICIO:
#  * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
#  * un ejemplo con cada nivel de "severidad" disponible.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
#  * y listar dichas tareas.
#  * - Añadir: recibe nombre y descripción.
#  * - Eliminar: por nombre de la tarea.
#  * Implementa diferentes mensajes de log que muestren información según la
#  * tarea ejecutada (a tu elección).
#  * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.

import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    datefmt="%Y/%m/%d %H:%M",
    format="%(levelname)s, %(message)s, %(asctime)s"
)
# logging.critical("Programa en estado CRITICO")
# logging.warning("Advertencia")
# logging.info("El programa inicio")
# logging.debug("Debugear")
# logging.error("Error de programa")


# def tiempo(funcion):
#     def wrapper(*args, **kwargs):
#         print("===========================================")
#         inicio = time.time()
#         resultado = funcion(*args, **kwargs)
#         final = time.time()
#         print(final - inicio)
#         print("===========================================")
#         return resultado

#     return wrapper


actividades = {"Ruben": {"tarea": "Limpiar", "descripcion": "Se deberan de limpiar los trastes"},
               "Carolina": {"tarea": "Arreglar", "descripcion": "Se debera de arreglar la lavadora"}}


def add(persona: str, tarea: str, text: str):
    inicio = time.time()
    actividades[persona] = {"tarea": tarea, "descripcion": text, }
    final = time.time()
    tiempo = final - inicio
    logging.info(f"Se agrego la tarea con exito! en {tiempo}")


def dele(persona: str):
    inicio = time.time()
    del actividades[f"{persona}"]
    final = time.time()
    logging.warning(
        f"El usuario {persona} se ha quedado sin actvidad. se completo en {final-inicio} S.")


def show():
    inicio = time.time()
    for i in actividades:
        print(f"{actividades[i]["tarea"]} : {actividades[i]["descripcion"]}")
    final = time.time()
    t = round((final-inicio), 6)
    logging.info(f"Se listaron las actividades. en {t} S.")


# add("Ruben", "barrer", "Solo sera barrer la banqueta")

add("Jorge", "Instruir", "Instruir en el levantamiento de pesas")
print("\n")
show()
print("\n")
dele("Jorge")
print("\n")
show()
# print(actividades)
# print(dele("Lalo"))
