# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622
#  * EJERCICIO:
#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores

# import requests
# import json

# f = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
# with open("lectura.txt", "w", encoding="utf-8")as archivo:
#     if f.status_code == 200:
#         r = f.json()
#         l = json.dumps(r, indent=4, ensure_ascii=False)
#         # l = json.dumps(r, indent=4, ensure_ascii=False)
#         archivo.write(l)

# respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

# procesado = respuesta.json()
# print(procesado["name"])
# print(procesado["height"])
# print(procesado["weight"])
# print(procesado["id"])


# # ? Ejericio 1
import requests


print("Bienvenido a la consulta de pokemones")
poke = input("Ingrese el nombre o id del pokemon: ")
poke = poke.strip().lower()
consulta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}")

if consulta.status_code == 200:
    respuesta = consulta.json()
    print("===== POKEDEX =====")
    print(f"NAME: {respuesta['name']}")
    print(f"HEIGHT: {respuesta['height']}")
    print(f"WEIGHT: {respuesta['weight']}")
    print(f"ID: {respuesta['id']}")
    print("Tipos: ")
    for i, poke in enumerate(respuesta["types"], start=1):
        print(f" {i}.- {poke['type']['name']}")
else:
    print("Ese nombre no es valido o esta mal escrito")
