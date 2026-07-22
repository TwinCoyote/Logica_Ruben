'''Primer Proyecto de Web Scrapping para retos de programacion automatica'''
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101
import unicodedata
import requests
import os
from bs4 import BeautifulSoup
import json
import sys


def scrapper_reto() -> str:
    """Funcion Hace Web scrapping y retorna los retos en un json"""
    banco_de_retos = {}
    url = "https://retosdeprogramacion.com/ejercicios"
    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        return f"Error al hacer la petición. Código HTTP: {respuesta.status_code}"

    soup = BeautifulSoup(respuesta.text, 'html.parser')

    ejercicios = soup.find_all('div', class_='rt-Box css-1f7fslj')

    for reto in ejercicios:
        titulo = reto.find('h2', class_='css-1fpdnih')
        dificultad = reto.find('span', class_='rt-variant-soft')
        descripcion = reto.find('code')
        if not titulo or not descripcion:
            continue
        NReto = reto.find('h2')  # Es el numero de reto en str
        # Es el numero de reto en int
        Numero = int(NReto.text.replace("#", ""))
        dificultad = unicodedata.normalize('NFKD', dificultad.text).encode(
            # * Se limpio de acentos
            'ASCII', 'ignore').decode('utf-8')
        acentos = unicodedata.normalize('NFKD', titulo.text).encode(
            # * Se limpio de acentos
            'ASCII', 'ignore').decode('utf-8').replace(" ", "_")
        excluir = ["¿", "?", '"']
        for i in excluir:
            acentos = acentos.replace(i, "")
        limpio = acentos.lower().capitalize()
        descripcion_comentada = descripcion.text.strip().replace(
            "\n", "\n#").replace("*/", "").replace("/*", "")

        banco_de_retos[Numero] = {

            "name": limpio,
            "dificulty": dificultad,
            "description": descripcion_comentada.strip("/* \n")

        }

    with open("Retos_programacion.json", "w", encoding="utf-8") as archivo:
        json.dump(banco_de_retos, archivo, indent=4)
        return "Exito, se Han extraido los retos Correctamente!"


def buscar_reto(numero: int) -> str:
    """Busca el reto en el Json y entrega un archivo con toda la info"""
    try:
        carpeta_destino = "Ejercicios_Logica"
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino, exist_ok=True)
        numero = str(numero)
        with open("Retos_programacion.json", "r", encoding="utf-8") as retos:
            lineas = json.load(retos)
            nombre = lineas[numero]["name"]
            descripcion = lineas[numero]["description"]
            dificultad = lineas[numero]["dificulty"]
            numero = int(numero)
            nombre_archivo = limpiar_nombre_archivo(f"{numero}_{nombre}.py")
            ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
            if os.path.exists(ruta_completa):
                return "Ya hay un archivo asi creado"
            with open(ruta_completa, "w", encoding="utf-8") as archivo:
                # Título del archivo en docstring
                archivo.write(f"'''{nombre.replace("_", " ")}'''\t")
                # Dificultad como comentario en el formato solicitado
                if dificultad == "Dificil":
                    archivo.write(f"#! Dificultad: {dificultad}\n")
                else:
                    archivo.write(f"#? Dificultad: {dificultad}\n")

                # archivo.write("#\n")
                archivo.write(
                    "# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101\n")
                # No presentar el primer y ulitmo caracter porque es un '#' vacio
                archivo.write(f"#{descripcion[1:-1]}")
        return "Exito"
    except KeyError:
        return f"No hay un reto {numero}"
    except NameError:
        return f"No se pueden usar letras {numero}"


def limpiar_nombre_archivo(nombre: str) -> str:
    """Elimina caracteres inválidos para nombres de archivo en Windows."""
    caracteres_invalidos = '<>:"/\\|?*'
    for caracter in caracteres_invalidos:
        nombre = nombre.replace(caracter, "")
    return nombre.strip()


def print_banner(titulo: str) -> None:
    linea = "=" * 60
    print(f"\n{linea}\n{titulo}\n{linea}")


def print_estado(mensaje: str, exito: bool = True) -> None:
    etiqueta = "[OK]" if exito else "[ERROR]"
    print(f"{etiqueta} {mensaje}\n")


if __name__ == "__main__":
    print_banner("Scrapper de Retos de Programación")
    resultado_scrapper = scrapper_reto()
    print_estado(resultado_scrapper,
                 exito=resultado_scrapper.startswith("Exito"))

    if len(sys.argv) > 1:
        argumento = sys.argv[1]
        print_banner(f"Generando archivo para el reto {argumento}")

        try:
            numero_reto = int(argumento)
            resultado = buscar_reto(numero_reto)
            print_estado(resultado, exito=resultado == "Exito")
            if resultado == "Exito":
                print("Archivo generado en la carpeta: Ejercicios_Logica\n")
        except ValueError:
            print_estado(f"Error: '{argumento}' no es valido.", exito=False)
    else:
        print("Por favor, introduce el número del reto. Ejemplo: python scriptRuben.py 4")


# print(buscar_reto(70))
