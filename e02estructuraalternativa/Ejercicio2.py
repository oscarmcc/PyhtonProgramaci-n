"""
Realiza el ejercicio 56 (página 100) del libro "Introducción a la Programación con Python 3".
Author: Óscar Martín-Castaño Carrillo
Date: 20/10/2023
"""

print('Programa para resolver ecuaciones de primer grado')

# Pido los datos necesarios para realizar el programa
a = float(input('Dame un valor para a '))
b = float(input('Dame un valor para b '))

# Después de pedir los datos, los comparo para hallar el resultado de la ecuación
if a != 0:
    x = -b/a
    print('El valor de x es', x)
if a == 0:
    if b != 0:
        print('La ecuación no tiene solución')
    if b == 0:
        print('La ecuación tiene infinitas soluciones')
