import random

# pila = []


# pila.append("A")
# pila.append("B")
# pila.append("C")
# # print(pila)

# # ultimo = pila.pop()
# # print("Salio:", ultimo)
# # print("Pila ahora", pila)

# print("Cima", pila[-1])
# print("Pila sigue igual", pila)

# pila = []

# pila.append(1)
# pila.append(2)
# pila.append(3)

# last = pila.pop()
# last2 = pila.pop()
# print(pila)


# cola = []

# cola.append("Juan")
# cola.append("Ana")
# cola.append("Luis")

# # print(cola)


# primero = cola.pop(0)

# print("Salio", primero)
# print("Sigue", cola)


# colas = []

# colas.append("Ruben")
# colas.append("Angel")
# colas.append("Beth")
# colas.append("Arnulfo")

# colas.pop()
# colas.pop()

# ultimo = colas.pop(0)
# print("ultimo", ultimo)
# print("Sigue", colas)


# pila = []
# pila.append(10)
# pila.append(20)
# pila.append(30)
# f = pila.pop(0)

# print(f"Se saco: {f}")
# print(f"En la lista siguen: {pila}")

# def push(pila, elemento):
#     if elemento == isinstance(elemento, str):
#         pila.append(f"{elemento}")
#         print(f"Se agrego: {elemento}")
#     else:
#         pila.append(elemento)
#         print(f"Se agrego: {elemento}")
#     pass


# def pop_pila(pila):
#     print(pila.pop(-1))


# pila = ["C", "D"]

# push(pila, "A")
# push(pila, "B")
# print(pop_pila(pila))
# print(pop_pila(pila))
# print(pop_pila(pila))


# def palabra(pal: str) -> str:
#     h = ""
#     pila = []
#     for i in pal:
#         pila.append(i)
#     print(pila)
#     for i in range(len(pila)):
#         h += pila.pop(-1)
#     return h


# print(palabra("Hola"))


# cola = []
# cola.append("Pedro")
# cola.append("Luis")
# cola.append("Ana")
# atendiendo = cola.pop(0)
# siguiente = cola[0]
# print(f"Se esta atendiendo a: {atendiendo}")
# print("Sigue: ", siguiente)


# def enqueue(cola, elemento):
#     cola.append(elemento)
#     pass


# def dequeue(cola):
#     if len(cola) < 0:
#         return None
#     return cola.pop(0)


# pilas = ["Chuy", "Liz", "Beth"]

# # enqueue(pilas, "Ruben")
# # dequeue(pilas)

# print(dequeue(pilas))

# pila = []


# def verif(n: str) -> bool:
#     for i in n:
#         if i == "(":
#             pila.append(i)
#         elif pila == []:
#             return "La pila esta vacia"
#         elif i == ")" and pila[-1] == "(":
#             pila.pop()
#         else:
#             return

#     return pila


# # pila = ["(", "("]
# # print(pila[-1])
# # print(pila)

# pila.append("(")
# pila.append("(")
# pila.append(")")
# pila.append("(")
# print(verif(")"))


# pila = []


# def ver(n):
#     for i in n:
#         if i == "(":
#             pila.append(i)
#         elif pila == [] and i == ")":
#             return False
#         elif i == ")":
#             pila.pop(-1)
#     if pila == []:
#         return True
#     else:
#         return False, pila


# print(ver("(()())("))


# pila = []

# # ad = adelante
# # at = atras


# paginas = [
#     "google.com",
#     "youtube.com",
#     "wikipedia.org",
#     "elrincondelvago.com",
#     "miniclip.com",
#     "stackoverflow.com",
#     "github.com",
#     "reddit.com",
#     "bing.com",
#     "yahoo.com",
#     "mozilla.org",
#     "medium.com",
#     "coursera.org",
#     "udemy.com",
#     "khanacademy.org",
#     "bbc.com",
#     "cnn.com",
#     "xataka.com",
#     "genbeta.com",
#     "forocoches.com"
# ]


# def Pagran():
#     p = random.choice(paginas)

#     return p


# def nav(p):
#     if p == "ad":
#         b = pila.append(Pagran())

#         return pila[-1]
#     elif p == "at" and pila == []:
#         return "No hay nada atras"

#     elif p == "at":

#         if not pila[0]:
#             return "No hay nada atras"

#         else:
#             f = pila[-1]
#             pila.pop(-1)
#             return f


# activador = True
# while activador:
#     x = input("Ingrese la accion: ")
#     if x == "no":
#         activador = False
# print(nav(x))

# print(pila[-2])
# print(pila)


lista = ["Proyecto_Final_v2.pdf", "Captura_Pantalla_Error.png", "Receta_Abuela.docx",
         "Balance_Ventas_Enero.xlsx", "Ticket_Vuelo_Madrid.pdf", "Presentacion_Sin_Titulo.pptx", "Foto_Gatito.jpg"]

# ag = agregar
# imp = imprimir

cola = []

cont = True
while cont:
    o = input("ag o imp? ")
    if o == "sal":
        cont = False
    elif o == "ag":
        x = random.choice(lista)
        if x in cola:
            print("El documento ya estaba en la cola")
        else:
            cola.append(x)
            print(f"Se agrego con exito: {x}")
    elif o == "imp":
        if cola == []:
            print("No hay nada en la cola de impresion.")
        else:
            print(f"Se imprimira {cola[0]}")
            cola.pop(0)

 