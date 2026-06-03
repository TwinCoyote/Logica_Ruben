"""El Segundo"""
# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622
#  * Dado un listado de números, encuentra el SEGUNDO más grande

numeros = [10, 20, 24, 35, 46, 35, 1, 23]


# def find(o: list):
#     for _ in range(len(o)):
#         for i in range(len(o)-1):
#             if o[i] > o[i+1]:
#                 o[i], o[i+1] = o[i+1], o[i]
#     return o[-2]


# print(find(numeros))


def find(o: list):
    """Funcion que regresa el segundo mas grande"""
    s_m = o[0]  # Segundo maximo
    m = o[0]  # Maximo
    for i in o:
        if i > m:
            s_m = m
            m = i
    return s_m


print(find(numeros))
