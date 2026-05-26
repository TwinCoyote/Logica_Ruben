# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622

def saludar():
    return "Hola que tal?"


def despedirse():
    return "Adios Ruben"


def imprimir(s: str):
    print(s)


imprimir(saludar)

def greeting_process(callback):
    callback()
