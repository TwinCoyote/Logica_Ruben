# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622

#  * EJERCICIO:
#  * Explora el patrón de diseño "singleton" y muestra cómo crearlo
#  * con un ejemplo genérico.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el patrón de diseño "singleton" para representar una clase que
#  * haga referencia a la sesión de usuario de una aplicación ficticia.
#  * La sesión debe permitir asignar un usuario (id, username, nombre y email),
#  * recuperar los datos del usuario y borrar los datos de la sesión.


# class PCB:
#     def __init__(self, material):
#         self.material = material

#     def mostrar(self):
#         print(f"la PCB es de {self.material}")


# placa = PCB("FR4")
# placa.mostrar()


# class Microcontrolador:
#     def __init__(self, nombre, frecuencia):
#         self.nombre = nombre
#         self.frecuencia = frecuencia

#     def mostrar_info(self):
#         print(f"{self.nombre} - {self.frecuencia}")


# micro = Microcontrolador("ESP32", "240MHz")

# micro.mostrar_info()

# class Robot:
#     _instancia = None

#     def __new__(cls):
#         if cls._instancia is None:
#             print("Creando Robot")
#             cls._instancia = super().__new__(cls)
#         else:
#             print("Usando robot existente")
#         return cls._instancia


# class SesionUsuario:
#     _xd = None

#     def __new__(cls):
#         if cls._xd is None:
#             print("Nueva sesion Creada")
#             cls._xd = super().__new__(cls)
#         else:
#             print("Usando sesion Existente")
#         return cls._xd


# a = SesionUsuario()
# b = SesionUsuario()


class SesionUsuario:

    _sesion = None
    flag = False

    def __new__(cls):
        if cls._sesion is None:
            print("Sesion Creada")
            cls._sesion = super().__new__(cls)
        else:
            print("Ya hay una Sesion creada")
        return cls._sesion

    def __init__(self):
        if not self.flag:
            self.id = None
            self.username = None
            self.nombre = None
            self.email = None
            self.flag = True

    def iniciar_sesion(self, id, username, nombre, email):
        self.id = id
        self.username = username
        self.nombre = nombre
        self.email = email

    def mostrar_usuario(self):
        if not self.username:
            print("No hay sesion iniciada")
            return
        else:
            print(
                f"\n El usuario {self.username} tiene los sigiuentes datos \n nombre: {self.nombre} \n id: {self.id} \n email: {self.email}")

    def cerrar_sesion(self):
        self.id = None
        self.username = None
        self.nombre = None
        self.email = None
        self.flag = False
        SesionUsuario._sesion = None
        print("Sesion cerrada con exito!")


a = SesionUsuario()

a.iniciar_sesion(
    1,
    "reyna",
    "Ruben",
    "ruben@gmail.com"
)

b = SesionUsuario()

print(a == b)

b.mostrar_usuario()

a.cerrar_sesion()

c = SesionUsuario()

c.mostrar_usuario()
