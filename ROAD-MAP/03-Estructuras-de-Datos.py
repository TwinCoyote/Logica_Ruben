
#  * -Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#  *   y a continuación los datos necesarios para llevarla a cabo.
#  * - También se debe proponer una operación de finalización del programa.

again = True


def Bienvenida() -> int:
    print("""Bienvenido!, Ingresa la operacion que quieras realizar
            A continuacion se presenta la lista de opciones:
            1 - Buscar un contacto
            2 - Editar un contacto
            3 - Eliminar un contacto
            4 - Añadir un contacto
            5 - salir""")

    Numero = int(input("Ingrese el numero de la operacion que desea hacer: "))
    return (Numero)


agenda = {
    "ruben": "8443711982",
    "ana": "8123456789",
    "luis": "8112345678"
}

cuenta_dic = len(agenda)


def form(nam: str) -> str:
    f = nam.lower()
    return f


def buscar(nombre: str) -> str:
    if nombre in agenda:
        return f"Se encontro: {nombre}\n Con el numero: {agenda[nombre]}"
    else:
        return f"no se encontro el nombre {nombre}"


def agregar(nombre: str, numero: str):
    if nombre not in agenda:
        agenda[nombre] = numero
        return f"Se agregó {nombre} con éxito"
    else:
        return f"{nombre} ya se encuentra registrado."


def editar(name: str):
    if name in agenda:
        print(
            f"Usted ha seleccionado el contacto {name} con el numero {agenda[name]}")

        e = int(input("""¿Qué desea editar?
                            1 - Editar nombre
                            2 - Editar número
                            Opción: """))

        if e == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            agenda[nuevo_nombre] = agenda[name]
            del agenda[name]
            print("Nombre actualizado con éxito")

        elif e == 2:
            nuevo_numero = input(f"Ingrese el nuevo numero de {name}: ")
            agenda.update({name: nuevo_numero})
            print("Número actualizado con éxito")

        else:
            print("Opción no válida")

    else:
        print(f"{name} no está en la agenda")


def wait():
    input("Presione alguna tecla para continuar.")
    return


def delete(name: str) -> str:
    name = form(name)
    if name in agenda:
        del agenda[name]
        print(f"El contacto: {name} Se ha elimiando Correctamente.")
    else:
        print(f"No se ha encotrado eliminar {name}")


# print(agenda(editar("Rubennnn")))
while again:
    var = Bienvenida()
    if var == 1:
        nom = input("Ingrese el nombre: ")
        nom = form(nom)
        print(buscar(nom))
        print(wait())
    elif var == 2:
        edit = input("Ingrese el nombre que desea editar: ")
        edit = form(edit)
        if edit in agenda:
            print(editar(edit))
            print(wait())
        else:
            print("No se ha encontrado ese nombre, intente nuevamente. ")
            print(wait())
    elif var == 3:
        na = input("Ingrese el nombre para eliminar: ")
        na = form(na)
        if na in agenda:
            print(delete(na))
            print(wait())
        else:
            print("No se ha encontrado ese nombre.")
            print(wait())
    elif var == 4:
        nombre = input("Ingrese el nombre del nuevo contacto: ")
        nombre = form(nombre)
        numero = input("Ingrese el numero del nuevo contacto: ")
        print(agregar(nombre, numero))
        print(wait())
    elif var == 5:
        again = False
        print("Regrese Pronto")
