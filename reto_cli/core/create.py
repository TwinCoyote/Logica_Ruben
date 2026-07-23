

from repository.challenge_repository import find_challenge
import os
import json
import sys


ROOT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


def clean_file_name(nombre: str) -> str:
    """Elimina caracteres inválidos para nombres de archivo en Windows."""
    valid_characters = '<>:"/\\|?*'
    for character in valid_characters:
        nombre = nombre.replace(character, "")
    return nombre.strip()


def create_challenge_file(number: int) -> str:
    """# Create a file with the json data"""

    # TODO: Migrate all constants to new file '.env' or 'constants' or something like that idk
    destination_folder = "Ejercicios_Logica"
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder, exist_ok=True)
    data = find_challenge(number)
    if not data:
        return "Error", f"Not data in challenge {number}.", None
    file_name = clean_file_name(
        f"{data.get("number")}_{data.get("name")}.py")
    path = os.path.join(destination_folder, file_name)
    if os.path.exists(path):
        return "already exist file"
    # Título del archivo en docstring
    with open(path, "w", encoding="utf-8") as file:
        file.write(f"'''{data.get("name").replace("_", " ")}'''\t")
        # Dificultad como comentario en el formato solicitado
        if data.get("dificulty") == "Dificil":
            file.write(f"#! Dificulty: {data.get("dificulty")}\n")
        else:
            file.write(f"#? Dificulty: {data.get("dificulty")}\n")
        file.write(
            "# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101\n")
        # No presentar el primer y ulitmo character porque es un '#' vacio
        file.write(f"#{data.get("description")[1:-1]}")
    return "success", "File created successfully", path


# print(create_challenge_file(99))
