import random

intentos = 10
juntas = ""

letras_adivinadas = ""


def Bienvenida():
    print("Bienvenido a le Juego del ahorcado: ")
    input("Selecciona cualquier tecla para empezar: ...")


def aleaword() -> str:
    palabras = ["oso"]
    pal = random.choice(palabras)
    return pal


def secretword(alea, letra):
    llenado = ""
    for i in alea:
        if i in letra:
            llenado += i

        else:
            llenado += "_"
    letras_adivinadas = llenado
    # return llenado
    return letras_adivinadas


letras_adivinadas = ""
palabra_secreta = "oso"
while intentos > 0:

    letra_elegida = input("Ingresa la letra: ").lower()
    if letra_elegida not in letras_adivinadas:
        letras_adivinadas += letra_elegida
    else:
        print("Ya habias ingresado esa letra...")

    palabra_mostrada = secretword(palabra_secreta, letras_adivinadas)
    print(palabra_mostrada)

    if letra_elegida not in palabra_secreta:
        intentos -= 1
        print(f"Fallaste. Intentos restantes: {intentos}")
        continue

    if "_" not in palabra_mostrada:
        print("¡Ganaste!")
        break

    if intentos == 0:
        input("Se acabo el juego quedan 0 intentos, presiona cualquier tecla para continuar...")
