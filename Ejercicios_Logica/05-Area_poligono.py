
# * Crea una única función (importante que sólo sea una) que sea capaz
# * de calcular y retornar el área de un polígono.
# * La función recibirá por parámetro sólo UN polígono a la vez.
# * Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# * Imprime el cálculo del área de un polígono de cada tipo.

def area(base, altura, poligono):
    if poligono == 1:
        multi = base * altura
        resultado = multi / 2
        return f"El area de su Triangulo {resultado}\n"
    elif poligono == 2:
        return f"El area de su Cuadrado {base * base}\n"
    elif poligono == 3:
        return f"El area de su Rectangulo {base * altura}\n"
    else:
        return "Error, ese no es un numero seleccionable."


s = True
while s:
    try:
        x = int(input("""
                1- Iniciar
                2- Cerrar   
                    
                    Ingrese Su numero: """)
                )

        if x == 1:

            b = int(input("Ingrese su base: "))
            h = int(input("\n Ingrese su altura: "))
            print("\n------ Resultados ------\n")
            print(area(b, h, 1))
            print(area(b, h, 2))
            print(area(b, h, 3))
            print("---------------------------\n")
            input("Presione cualquier Tecla para continuar...")
        elif x == 2:
            s = False

        else:
            input("Error, escoge un  numero disponible.")
    except ValueError:
        print("""Ingresa un numero
              
              
              









              """)
