"""
Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que
 ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para saber que persona tiene más edad')

# Pedimos los datos para el programa necesario
E1 = int(input('Dame la edad de la primera persona '))
E2 = int(input('Dame la edad de la segunda persona '))

# Comparamos los datos para la resolución del programa
if E1 > E2:
    print('La Primera persona es mayor que la segunda')
elif E2 > E1:
    print('La Segunda persona es mayor que la primera')
else:
    print('Las dos personas tienen la misma edad')
