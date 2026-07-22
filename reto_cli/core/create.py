
import os
import json


ROOT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from repository.challenge_repository import find_challenge

def limpiar_nombre_archivo(nombre: str) -> str:
    """Elimina caracteres inválidos para nombres de archivo en Windows."""
    caracteres_invalidos = '<>:"/\\|?*'
    for caracter in caracteres_invalidos:
        nombre = nombre.replace(caracter, "")
    return nombre.strip()


def create_challenge_file(numero: int) -> str:
    """Busca el reto en el Json y entrega un archivo con toda la info"""
    try:
        carpeta_destino = "Ejercicios_Logica"
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino, exist_ok=True)
            numero = str(numero)
            data = find_challenge(numero)
            nombre_archivo = limpiar_nombre_archivo(f"{data.get("number")}_{data.get("name")}.py")
            ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
            if os.path.exists(ruta_completa):
                return "Ya hay un archivo asi creado"
            with open(ruta_completa, "w", encoding="utf-8") as archivo:
                # Título del archivo en docstring
                archivo.write(f"'''{data.get("name").replace("_", " ")}'''\t")
                # Dificultad como comentario en el formato solicitado
                if data.get("dificulty") == "Dificil":
                    archivo.write(f"#! Dificultad: {data.get("dificulty")}\n")
                else:
                    archivo.write(f"#? Dificultad: {data.get("dificulty")}\n")
                archivo.write(
                    "# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101\n")
                # No presentar el primer y ulitmo caracter porque es un '#' vacio
                archivo.write(f"#{data.get("description")[1:-1]}")
        return "Exito", "Archivo creado correctamente", ruta_completa
    except KeyError:
        return "Error", numero
    except NameError:
        return "Error", numero
