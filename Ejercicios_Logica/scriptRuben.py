'''Primer Proyecto de Web Scrapping para retos de programacion automatica'''
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
        if not titulo or not descripcion:
            continue
        NReto = reto.find('h2')  # Es el numero de reto en str
        # Es el numero de reto en int
        Numero = int(NReto.text.replace("#", ""))

        acentos = unicodedata.normalize('NFKD', titulo.text).encode(
            # * Se limpio de acentos
            'ASCII', 'ignore').decode('utf-8').replace(" ", "_")
        excluir = ["¿", "?", '"']
        for i in excluir:
            acentos = acentos.replace(i, "")
        limpio = acentos.lower().capitalize()
        # limpio = acentos.replace("¿", "").replace(
        #     "?", "").replace('"', "").replace(" ", "_").lower().capitalize()
        descripcion_comentada = descripcion.text.strip().replace(
            "\n", "\n#").replace("*/", "").replace("/*", "")

        banco_de_retos[Numero] = {

            "nombre": limpio,
            "descripcion": descripcion_comentada.strip("/* \n")
        }

    with open("Retos_programacion.json", "w", encoding="utf-8") as archivo:
        json.dump(banco_de_retos, archivo, indent=4)
        return "Exito, se Han extraido los retos Correctamente!"


def buscar_reto(numero: int) -> str:
    """Busca el reto en el Json y entrega un archivo con toda la info"""
    try:
        carpeta_destino = "Ejercicios_Logica"
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        numero = str(numero)
        with open("Retos_programacion.json", "r", encoding="utf-8") as retos:
            lineas = json.load(retos)
            nombre = lineas[numero]["nombre"]
            descripcion = lineas[numero]["descripcion"]
            numero = int(numero)
            nombre_archivo = f"{numero}_{nombre}.py"
            ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
            if ruta_completa:
                return "Ya hay un archivo asi creado"
            with open(ruta_completa, "w", encoding="utf-8") as archivo:
                archivo.write(f"'''{nombre.replace("_", " ")}'''\n")
                archivo.write(
                    "# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101\n")
                # No presentar el primer y ulitmo caracter porque es un '#' vacio
                archivo.write(f"#{descripcion[1:-1]}")
        return "Exito"
    except KeyError:
        return f"No hay un reto {numero}"
    except NameError:
        return f"No se pueden usar letras {numero}"


print(scrapper_reto())
print(buscar_reto(43))
