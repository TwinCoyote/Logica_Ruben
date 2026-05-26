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


actividades = {"Ruben": {"tarea": "Limpiar", "descripcion": "Se deberan de limpiar los trastes"},
               "Carolina": {"tarea": "Arreglar", "descripcion": "Se debera de arreglar la lavadora"}}


def add(persona: str, tarea: str, text: str):
    actividades[f"{persona}"]["tarea"] = f"{tarea}"
    actividades[f"{persona}"]["descripcion"] = f"{text}"
    logging.info("Se agrego la tarea con exito!")


add("Ruben", "barrer", "Solo sera barrer la banqueta")
print(actividades)
