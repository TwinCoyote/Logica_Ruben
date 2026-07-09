'''Los anillos de poder'''  # ? Dificultad: Medio
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,W3101
# * ¡La Tierra Media está en guerra! En ella lucharán razas leales
# * a Sauron contra otras bondadosas que no quieren que el mal reine
# * sobre sus tierras.
# * Cada raza tiene asociado un "valor" entre 1 y 5:
# * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
# *   Númenóreanos (4), Elfos (5)

# * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
# *   Huargos (3), Trolls (5)
# * Crea un programa que calcule el resultado de la batalla entre
# * los 2 tipos de ejércitos:
# * - El resultado puede ser que gane el bien, el mal, o exista un empate.
# *   Dependiendo de la suma del valor del ejército y el número de integrantes.
# * - Cada ejército puede estar compuesto por un número de integrantes variable
# *   de cada raza.
# * - Tienes total libertad para modelar los datos del ejercicio.
# * Ej: 1 Peloso pierde contra 1 Orco
# *     2 Pelosos empatan contra 1 Orco
# *     3 Pelosos ganan a 1 Orco


Razas = {
    "bondadosas": {
        "pelosos": 1,
        "sureños buenos": 2,
        "enanos": 3,
        "numeroenanos": 4,
        "elfos": 5,
    },
    "malvadas": {
        "sureños malos": 2,
        "orcos": 2,
        "goblins": 2,
        "huargos": 3,
        "trolls": 5
    }
}


# * Easy Way
# def names(num: int, name: str) -> str:
#     """Eliminate the last 's' when is less to 2"""
#     if num <= 1:
#         return name[:-1]
#     return name


# def fight(N1: int, ARMY1: str, N2: int, ARMY2: str) -> str:
#     """Make the math"""
#     if ARMY1 in Razas["bondadosas"] and ARMY2 in Razas["malvadas"] and N1 >= 1 and N2 >= 1:
#         valor1 = Razas["bondadosas"][ARMY1]
#         ValorArmy1 = N1 * valor1
#         valor2 = Razas["malvadas"][ARMY2]
#         ValorArmy2 = N2 * valor2
#     else:
#         return f"Revisa la entrada, ingresaste: {N1} {ARMY1} y {N2} {ARMY2}"

#     if ValorArmy1 > ValorArmy2:
#         return f"{N1} {names(N1, ARMY1)} ganan contra {N2} {names(N2, ARMY2)}"
#     if ValorArmy1 < ValorArmy2:
#         return f"{N1} {names(N1, ARMY1)} pierden contra {N2} {names(N2, ARMY2)}"
#     return f"{N1} {names(N1, ARMY1)} empatan contra {N2} {names(N2, ARMY2)}"


# print(fight(0, "pelosos", 1, "orcos"))

Ejercito1 = {"orcos": 2, "huargos": 3, "trolls": 1, "enanos": 2, "elfos": 2}
Ejercito2 = {"goblins": 3, "trolls": 5, "numeroenanos": 5, "pelosos": 4}


def numeros(E1: dict) -> int:
    '''Retorna el total de un ejercito'''
    cuenta = 0
    for i, n in E1.items():
        cuenta += Razas["bondadosas"].get(i, 0)*n
        cuenta += Razas["malvadas"].get(i, 0)*n
    return cuenta


# def ganador(n1: int, n2: int) -> int:
#     '''Retorna el numero mayor de dos'''
#     return max(n1, n2)


def game(A1, A2):
    army1 = numeros(A1)
    army2 = numeros(A2)
    if army1 > army2:
        for x, n in A1.items():
            print(f"{n} {x}")
        print("\nvencieron a: \n")
        for i, n in A2.items():
            print(f"{n} {i}")
    elif army1 < army2:
        for x, n in A1.items():
            print(f"{n} {x}")
        print("\nPerdieron contra: \n")
        for i, n in A2.items():
            print(f"{n} {i}")
    else:
        for x, n in A1.items():
            print(f"{n} {x}")
        print("\nEmpataron con: \n")
        for i, n in A2.items():
            print(f"{n} {i}")


game(Ejercito1, Ejercito2)
