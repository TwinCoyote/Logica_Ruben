"""Modulo de pruebas"""

import xml.etree.ElementTree as ET
import json
# import os


# persona = {
#     'nombre': 'Ruben',
#     'edad': 24,
#     'fecha de nacimiento': "3 de septiembre 2001",
#     'lista de lenguajes': ['python', 'c++', 'c']
# }
# # f = json.dumps(persona, indent=4)
# # print(f)

# with open("archivo.json", "w", encoding="utf-8") as archivo:
#     json.dump(persona, archivo, indent=4)

# with open("archivo.json", "r", encoding="utf-8") as archivo:
#     f = json.load(archivo)
#     # print("El tipo de dato es:", type(f))
#     # print(f)


# raiz = ET.Element("Persona")
# nombre = ET.SubElement(raiz, "nombre")
# nombre.text = "Ruben"
# edad = ET.SubElement(raiz, "edad")
# edad.text = "24"
# fecha = ET.SubElement(raiz, "fecha")
# fecha.text = "3 de septiembre 2001"

# lenguajes_lista = ['python', 'c++', 'c']

# lenguajes = ET.SubElement(raiz, "Lenguajes")
# for i in lenguajes_lista:
#     lenguaje = ET.SubElement(lenguajes, "Lenguaje")
#     lenguaje.text = i
# # print(persona)

# with open("persona.xml", "w", encoding="utf-8") as archivo:
#     ET.indent(raiz)
#     f = ET.tostring(raiz, encoding="unicode")
#     archivo.write(f)

# os.remove("persona.xml")
# os.remove("archivo.json")


# class Persona:
# """Clase Persona"""

# def __init__(self, nombre, edad, fecha_nacimiento, lenguajes):
#     self.nombre = nombre
#     self.edad = edad
#     self.fecha_nacimiento = fecha_nacimiento
#     self.lenguajes = lenguajes

# @classmethod
# def desde_json(cls, archivo):
#     """Funcion para prbar extraer datos de un json desde nuna clase"""
#     with open(archivo, "r", encoding="utf-8")as f:
#         m = json.load(f)
#         return cls(m["nombre"], m["edad"], m["fecha"], m["lenguajes"])

# def __str__(self):
#     return f"Prensentando a la persona \n su nombre es: {self.nombre}\n tiene {self.edad} años de edad\n nacio el {self.fecha_nacimiento}\n y domina estos lenguajes: {self.lenguajes}"


# persona = Persona.desde_json("archivo.json")

# print(persona)
# # yo = Persona("ruben", "24", "3 de septiembre de 2001", "python,C++")
# # print(yo)


class Persona:
    """Clase Persona"""

    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes

    @classmethod
    def desde_json(cls, archivo):
        """Funcion para prbar extraer datos de un json desde nuna clase"""
        with open(archivo, "r", encoding="utf-8")as f:
            m = json.load(f)
            return cls(m["nombre"], m["edad"], m["fecha"], m["lenguajes"])

    @classmethod
    def desde_xml(cls, archivo):
        with open(archivo, "r", encoding="utf-8")as x:
            tree = ET.parse(x)
            raiz = tree.getroot()
            nombre = raiz.find("nombre").text
            edad = raiz.find("edad").text
            fecha = raiz.find("fecha").text

            return cls(nombre, edad, fecha, [l.text for l in raiz.find("Lenguajes")])

    def __str__(self):
        return f"Prensentando a la persona \n su nombre es: {self.nombre}\n tiene {self.edad} años de edad\n nacio el {self.fecha_nacimiento}\n y domina estos lenguajes: {self.lenguajes}"


persona = Persona.desde_xml("persona.xml")
print(persona)
