'''Git y github'''  # ! Dificultad: Dificil
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101
# * ¡Estoy de celebración! He publicado mi primer libro:
# * "Git y GitHub desde cero"
# * - Papel: mouredev.com/libro-git
# * - eBook: mouredev.com/ebook-git
# *
# * ¿Sabías que puedes leer información de Git y GitHub desde la gran
# * mayoría de lenguajes de programación?
# *
# * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
# * - Hash
# * - Autor
# * - Mensaje
# * - Fecha y hora
# *
# * Ejemplo de salida:
# * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
# *
# * Se permite utilizar librerías que nos faciliten esta tarea.


import requests as r
from datetime import datetime


# * info:
# * repos/{owner}/{repo}/commits
# * owner = mouredev
# * repo = retos-programacion-2023


url = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits"


def print_commits(x: int) -> print:
    """Imprimira los ultimos 10 commits de un repo"""
    respuesta = r.get(url)
    f = respuesta.json()
    for i in range(x):
        commit_number = i
        hashs = f[commit_number]["sha"][:5]
        autor = f[commit_number]["commit"]["author"]["name"]
        message = f[commit_number]["commit"]["message"].strip()
        date = f[commit_number]["commit"]["author"]["date"]

        # * Convertimos la fecha a un formato usable
        constuc_date = date.replace("Z", "+00:00")
        convert_date = datetime.fromisoformat(constuc_date)
        better_date = convert_date.strftime("%d/%m/%Y %H:%M")
        print(f"Commit {i} | {hashs} | {autor} | {message} | {better_date} \n")


print_commits(10)

