"""Marco de palabras"""
# pylint: disable = C0305,C0103,C0301,C0200
#  * Crea una función que reciba un texto y muestre cada palabra en una línea,
#  * formando un marco rectangular de asteriscos.
#  * - ¿Qué te parece el reto? Se vería así:
#  *   **********
#  *   * ¿Qué   *
#  *   * te     *
#  *   * parece *
#  *   * el     *
#  *   * reto?  *
#  *   **********


t = "Hola Ruben y tu como has "



def reto(s: str):
    lens = []
    palabras = []

    s += " "
    acumulado = ""
    for i in s:
        if i == " ":
            palabras.append(acumulado)
            lens.append(len(acumulado))
            acumulado = ""
            continue
        acumulado += i
    largo = max(lens) * 2 - 1

    print("*"*largo)
    for i in palabras:
        print('*', f"{i:<5}", '*')
    print("*"*largo)


print(reto(t))

# t += " "
# print(t)
