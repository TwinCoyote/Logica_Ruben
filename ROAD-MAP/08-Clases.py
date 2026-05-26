# # class Personaje:

# #     def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
# #         self.nombre = nombre
# #         self.fuerza = fuerza
# #         self.inteligencia = inteligencia
# #         self.defensa = defensa
# #         self.vida = vida

# #     def atributos(self):
# #         print(self.nombre, ":", sep="")
# #         print("* Fuerza", self.fuerza)
# #         print("* Inteligencia", self.inteligencia)
# #         print("* Defensa", self.defensa)
# #         print("* Vida", self.vida)

# #     def subir_nivel(self, fuerza, inteligencia, defensa):
# #         self.fuerza = self.fuerza + fuerza
# #         self.inteligencia = self.inteligencia + inteligencia
# #         self.defensa = self.defensa + defensa

# #     def esta_vivo(self):
# #         return self.vida > 0

# #     def morir(self):
# #         self.vida = 0
# #         print(self.nombre, "Ha Muerto")

# #     def daño(self, enemigo):
# #         return self.fuerza - enemigo.defensa

# #     def atacar(self, enemigo):
# #         daño = self.daño(enemigo)
# #         enemigo.vida = enemigo.vida - daño
# #         print(self.nombre, "ha realizado", daño,
# #               "puntos de daño a", enemigo.nombre)
# #         if enemigo.esta_vivo():
# #             print("La vida de", enemigo.nombre, "es", enemigo.vida)
# #         else:
# #             enemigo.morir()


# # class Guerrero(Personaje):
# #     pass

# #     def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
# #         # * Personaje.__init__(self, nombre, fuerza, inteligencia, defensa, vida)
# #         # Otra forma de hacer eso es con la funcion super(), que no neceseita poner self
# #         super().__init__(nombre, fuerza, inteligencia, defensa, vida)
# #         self.espada = espada

# #     def cambiar_arma(self):
# #         opcion = int(input(
# #             "Elige un arma: (1)Acero Valyrio, daño 8, (2)Matadragones, daño 10: "))
# #         if opcion == 1:
# #             self.espada = 8
# #         elif opcion == 2:
# #             self.espada = 10
# #         else:
# #             print("Numero de arma incorrecto")

# #     def atributos(self):
# #         super().atributos()
# #         print("Espada: ", self.espada)

# #     def daño(self, enemigo):
# #         return self.fuerza * self.espada - enemigo.defensa


# # class Mago(Personaje):
# #     def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
# #         super().__init__(nombre, fuerza, inteligencia, defensa, vida)
# #         self.libro = libro

# #     def atributos(self):
# #         super().atributos()
# #         print("* Libro ", self.libro)

# #     def daño(self, enemigo):
# #         return self.inteligencia*self.libro - enemigo.defensa


# # alexis = Personaje("Alexis", 20, 20, 30, 100)
# # guts = Guerrero("Ruben", 20, 20, 30, 100, 5)
# # lolo = Mago("Lolo", 20, 20, 30, 100, 5)

# # alexis.atacar(guts)
# # guts.atacar(lolo)
# # lolo.atacar(alexis)


# # alexis.atributos()
# # print("///////////////////////////////////")
# # guts.atributos()
# # print("///////////////////////////////////")
# # lolo.atributos()
# # print("///////////////////////////////////")


# # # print(guts.nombre)
# # # print(guts.esta_vivo())
# # # guts.cambiar_arma()
# # # guts.atributos()
# # # print(guts.espada)

# # # def get_fuerza(self):
# # #     return self.fuerza

# # # def set_fuerza(self, fuerza):
# # #     if fuerza < 0:
# # #         print("Error, has introducido un valor negativo")
# # #     else:
# # #         self.fuerza = fuerza


# # # mi_personaje = Personaje("BigBoss", 100, 90, 50, 390)
# # # mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 5)
# # # mi_personaje.nombre = "Ralaze"
# # # mi_personaje.fuerza = 10
# # # print("El nombre del jugador es: ", mi_personaje.nombre)
# # # print("La fuerza del jugador es: ", mi_personaje.fuerza)
# # # mi_personaje.atributos()
# # # mi_personaje.subir_nivel(1, 2, 3)
# # # mi_personaje.atributos()

# # # print(mi_personaje.esta_vivo())
# # # mi_personaje.morir()
# # # mi_personaje.atributos()
# # # print(mi_personaje.daño(mi_enemigo))
# # # mi_personaje.atacar(mi_enemigo)
# # # print("*////*")
# # # mi_enemigo.atributos()
# # # # print(mi_personaje.fuerza)
# # # mi_personaje.fuerza = 0
# # # print(mi_personaje.atributos())
# # # mi_personaje.atacar(mi_enemigo)

# # # print(mi_personaje.set_fuerza(10))
# # # mi_personaje.atributos()


# # class Ruben:

# #     def __init__(self, nombre, edad):
# #         self.nombre = nombre
# #         self.edad = edad

# #     def imprimir(self):
# #         print(f"Su nombre es {self.nombre}")
# #         print(f"Su edad es {self.edad} Años")


# # P1 = Ruben("Lino", 24)

# # P1.imprimir()

# # P1.nombre = "Lino R."


# # class Pila:

# #     def __init__(self):
# #         p = self.lista = []
# #         return p

# #     def watch1(self):
# #         return self.lista

# #     def add(self, argumento):
# #         self.lista.append(argumento)

# #     def dele(self,):
# #         if len(self.lista) == 0:
# #             return "La lista esta vacia"
# #         p = self.lista.pop(-1)
# #         return p

# #     def watch(self):
# #         p = self.lista[-1]
# #         return p

# #     def size(self):
# #         p = len(self.lista)
# #         return p

# # lista = ["Adios", "Soy yo"]
# # lista.append("Hola")
# # print(lista)

# # print(lista[-1])


# # p = Pila()
# # p.add(1)
# # p.add(2)
# # p.add(3)
# # p.watch()
# # p.dele()
# # p.watch1()


# class Cola:
#     def __init__(self):
#         self.cola = []

#     def add(self, arg):
#         self.cola.append(arg)

#     def dele(self):
#         if len(self.cola) == 0:
#             return "No hay nada"
#         self.cola.pop(0)

#     def con(self):
#         p = len(self.cola)
#         return p

#     def ver(self):
#         return self.cola


# # r = Cola()

# # r.add("hola")
# # r.add("soy")
# # r.add("Ruben")

# # r.ver()
# # r.con()
# # r.add("Prueba")
# # r.ver()
# # r.con()

# # r.dele()
# # r.ver()


# # lista = ["Hola", "que tal", "Ruben", "Reyna"]

# # lista.append("1")
# # print(lista)
# # print(lista[0])


# class Pila:
#     def __init__(self):
#         self.cola = []

#     def add(self, arg):
#         self.cola.append(arg)
#         return f"Se agrego: {arg} Correctamente"

#     def dele(self):
#         x = self.cola[-1]
#         self.cola.pop(-1)
#         return f"Se ha eliminado: '{x}'"

#     def ver(self):
#         return self.cola

#     def how(self):
#         return len(self.cola)


# z = Pila()

# z.add("Hola")
# z.add("que")
# z.add("tal")

# print(z.ver())

# print(z.dele())

# print(z.how())


# class Perro:
#     def __init__(self, nombre, raza):
#         self.nombre = nombre
#         self.raza = raza

#     def ladrar(self):
#         print(f"{self.nombre} dice: !GUAU!")

#     def __str__(self):
#         return f"{self.nombre} by {self.raza}"


# mi_perro = Perro("Rex", "labrador")
# mi_perro.ladrar()
