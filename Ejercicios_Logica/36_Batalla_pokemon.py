'''Batalla pokemon'''  # ? Dificultad: Medio
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101
# * Crea un programa que calcule el daño de un ataque durante
# * una batalla Pokémon.
# * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
# * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
# * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico
# *   (buscar su efectividad)
# * - El programa recibe los siguientes parámetros:
# *  - Tipo del Pokémon atacante.
# *  - Tipo del Pokémon defensor.
# *  - Ataque: Entre 1 y 100.
# *  - Defensa: Entre 1 y 100.


efectividad = {
    "agua": {"agua": 0.5, "fuego": 2, "planta": 0.5, "electrico": 1},
    "fuego": {"agua": 0.5, "fuego": 0.5, "planta": 2,   "electrico": 1},
    "planta": {"agua": 2, "fuego": 0.5, "planta": 0.5, "electrico": 1},
    "electrico": {"agua": 2, "fuego": 1, "planta": 0.5, "electrico": 0.5}
}


def poke_damage(type_A: str, Atack: int, Defense: int, type_D: str):
    if type_A in efectividad and type_D in efectividad:
        damage = 50 * (Atack/Defense) * (efectividad[type_A][type_D])
        return damage
    else:
        return "Los Nombres no existen"


print("Programa para calcula daño en pokemones")
atacante = input("Ingresa tu Atacante: ").lower()
Defensor = input("Ingresa tu Defensor: ").lower()
Ataque = int(input("Ingresa tu Ataque: "))
Defensa = int(input("Ingresa tu Defensa: "))

if 1 <= Ataque <= 100 and 1 <= Defensa <= 100:
    print("Tu Daño es ", poke_damage(atacante, Ataque, Defensa, Defensor))
else:
    print("El ataque y la defensa deben de ser menores a 100")
