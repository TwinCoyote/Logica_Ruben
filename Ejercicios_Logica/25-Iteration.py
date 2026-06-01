# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622,C0200
#  * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
#  * ¿De cuántas maneras eres capaz de hacerlo?
#  * Crea el código para cada una de ellas.

# def normal(x):
#     for i in range(0, x+1):
#         print(i)
def normal(x):
    [print(i) for i in range(x+1)]


def recu(x):

    if x <= 100:
        print(x)
        return recu(x+1)


def ciclo(x):

    while x <= 99:
        x += 1
        print(x)


# ciclo(0)
normal(100)
# # recu(1)

# def line(x):
#     # [print(i) for i in range(1, 101)]
#     [print(i) for i in range(x)]


# line(10)
