# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,C0200
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
#  *   o "S" (tijera).
#  * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".

tabla = {
    "R": "S",
    "P": "R",
    "S": "P"
}


# def R_P_S(f: list) -> str:
#     """Funcion que es el programa de Piedra, Papel o Tijera"""
#     player_1 = 0
#     player_2 = 0

#     for i in range(len(f)):
#         if f[i][0] == f[i][1]:
#             continue
#         elif f[i][0] == tabla[f"{f[i][1]}"]:
#             player_1 += 1
#         elif f[i][1] == tabla[f"{f[i][0]}"]:
#             player_2 += 1
#     return "Player 1" if player_1 > player_2 else "Player 2" if player_2 > player_1 else "Tie"


def R_P_S(f: list) -> str:
    """Funcion que es el programa de Piedra, Papel o Tijera"""
    player_1 = 0
    player_2 = 0

    for j1, j2 in f:
        if j1 == j2:
            continue
        if tabla[j1] == j2:
            player_1 += 1
        elif tabla[j2] == j1:
            player_2 += 1

    return "Player 1" if player_1 > player_2 else "Player 2" if player_2 > player_1 else "Tie"


x = [("R", "S"), ("S", "R"), ("S", "S")]


print(R_P_S(x))
