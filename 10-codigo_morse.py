
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.


TEXT_TO_MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--.."
}

MORSE_TO_TEXT = {
    ".-": "A",    "-...": "B",  "-.-.": "C",  "-..": "D",
    ".": "E",     "..-.": "F",  "--.": "G",   "....": "H",
    "..": "I",    ".---": "J",  "-.-": "K",   ".-..": "L",
    "--": "M",    "-.": "N",    "---": "O",   ".--.": "P",
    "--.-": "Q",  ".-.": "R",   "...": "S",   "-": "T",
    "..-": "U",   "...-": "V",  ".--": "W",   "-..-": "X",
    "-.--": "Y",  "--..": "Z"
}


def change(x):
    """Funcion para cambiar las letras"""
    x = x.upper()
    palabra = ""
    if x[0].isalpha():
        for i in x:
            if i != " ":
                palabra += TEXT_TO_MORSE[i]
                palabra += " "
            elif i == " ":
                palabra += " "
        return palabra
    else:
        acumulador = ""
        traduccion = ""
        espacios = 0
        x = x+" "

        for i in x:
            if i == " ":
                espacios += 1
                if acumulador:
                    traduccion += MORSE_TO_TEXT[acumulador]
                    acumulador = ""
            else:
                if espacios == 2:
                    traduccion += " "
                espacios = 0
                acumulador += i
        return traduccion


print(change(input("Ingrese los caracteres a convertir: ")))
