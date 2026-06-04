"""Primer Proyecto de Web Scrapping para retos de programacion automatica"""
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101
import unicodedata
import requests
import os
from bs4 import BeautifulSoup
import json


def scrapper_reto() -> str:
    """Funcion Hace Web scrapping y retorna los retos en un json"""
    banco_de_retos = {}
    url = "https://retosdeprogramacion.com/ejercicios"
    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        print("Error al hacer la peticion")

    soup = BeautifulSoup(respuesta.text, 'html.parser')

    ejercicios = soup.find_all('div', class_='rt-Box css-1f7fslj')

    for reto in ejercicios:
        titulo = reto.find('h2', class_='css-1fpdnih')
        descripcion = reto.find('code')
        NReto = reto.find('h2')  # Es el numero de reto en str
        # Es el numero de reto en int
        Numero = int(NReto.text.replace("#", ""))

        acentos = unicodedata.normalize('NFKD', titulo.text).encode(
            'ASCII', 'ignore').decode('utf-8')  # * Se limpio de acentos
        limpio = acentos.replace("¿", "").replace(
            "?", "").replace('"', "").replace(" ", "_")

        banco_de_retos[Numero] = {

            "nombre": limpio,
            "descripcion": descripcion.text.strip()
        }

    # TODO: Hacer una opcion para traer los retos, actualizar la base y otra para solo generar el archivo

    with open("Retos_programacion.json", "w", encoding="utf-8") as archivo:
        try:
            json.dump(banco_de_retos, archivo, indent=4)
        except KeyError as e:
            print(f"Ha ocurrido un error {e}")
    return "Exito, se Han extraido los retos Correctamente!"


# def buscar_reto(numero)
# with open("Retos_programacion.json", "r", encoding="utf-8") as retos:
#     x = json.load(retos)
#     print(f"#{1}")
#     print(x["1"]["nombre"])
#     print(x["1"]["descripcion"])

# def archivo_python(direccion,nombre):
#     nombre=

#     with open(f"{nombre}.py")


print(scrapper_reto())
