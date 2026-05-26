# Las 4 Reglas de Filtrado
# El Rango: El número debe estar entre 10 y 55 (ambos incluidos).
# Paridad: Solo sirven los números pares (los que terminan en 0, 2, 4, 6 u 8).
# La Excepción Única: El número no puede ser el 16.
# La Regla de los Múltiplos: El número no puede ser múltiplo de 3 (es decir, no aparece en la tabla del 3).


# for i in range(15, 56):
#     if i % 3 != 0 and i != 16 and i % 2 == 0:
#         print(i)

for i in range(10, 56):
    if i == 16 or i % 3 == 0:
        pass
    elif i % 2 == 0:
        print(i)
    else:
        pass
