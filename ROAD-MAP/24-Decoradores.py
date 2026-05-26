# pylint: disable = E0001, C0103, C0114,C0115, C0116,W0622


#  * EJERCICIO:
#  * Explora el concepto de "decorador" y muestra cómo crearlo
#  * con un ejemplo genérico.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un decorador que sea capaz de contabilizar cuántas veces
#  * se ha llamado a una función y aplícalo a una función de tu elección.


# def decorador(funcion):
#     def envolver():
#         print("===============[ Decorador ]================")
#         print(funcion())
#         print("============================================")
#     return envolver


# @decorador
# def nombre():
#     return "Ruben"


# nombre()


# def decorador(funcion):

#     cuenta = 0

#     def contar():
#         nonlocal cuenta
#         cuenta += 1
#         funcion()
#         return print(f"la cuenta va en {cuenta}")
#     return contar


# @decorador
# def nombres():
#     return "Hola Ruben"


# print(nombres())


# def decorador(funcion):
#     counter = 0

#     def contar():
#         nonlocal counter
#         counter += 1
#         x = funcion()

#         print(f"La cuenta va en {counter}")
#         return x
#     return contar


# @decorador
# def name():
#     return "My Name is Ruben"


# for i in range(5):
#     print(name())


from typing import List
nums = [3, 3]
objetivo = 6


# def encontrar(x, obj):

#     for indice_p, numero_p in enumerate(x):
#         for sub_i, numero_s in enumerate(x[1:], start=1):
#             suma = numero_p + numero_s
#             if suma == obj:
#                 return indice_p, sub_i


# print(encontrar(nums, objetivo))


# class Solution:
#     def twoSum(self,nums:list[int],target:int) -> List[int]:
#         for indice_p, numero_p in enumerate(nums):
#             for sub_i, numero_s in enumerate(nums[1:],start =1):
#                 suma = numero_p + numero_s
#                 if suma == target:
#                     return [indice_p, sub_i]


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 suma = nums[i]+nums[j]
#                 if suma == target:
#                     return [i, j]
