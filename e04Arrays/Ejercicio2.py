"""
Escribe un programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir,
el primero que se introduce es el último en mostrarse y viceversa.

Author: Óscar Martín-Castaño Carrillo
Date: 16/11/2023
"""
print('Programa que pide 10 números en una lista y nos la muestra dada la vuelta')
COUNT = 10
i = 0
list_to_add = []
while i < COUNT:
    number_to_add = float(input('Dame el número que quieras '))
    list_to_add.append(number_to_add)
    i += 1

print(f"Esta es la lista introducida: {list_to_add}\n")
list_to_add.reverse()
print(f"Esta es la lista dada la vuelta {list_to_add}")
