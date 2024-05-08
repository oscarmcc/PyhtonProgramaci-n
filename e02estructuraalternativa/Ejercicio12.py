"""
Escribir un programa que lea un año indicar si es bisiesto.
Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para saber si un año es bisiesto')

# Pedimos los datos necesarios para el programa
year = int(input('introduce el año que mas te guste'))

"""
Para llegar al resultado debemos saber que un año bisiesto 
es divisible por 4 pero no por 100, excepto si es divisible por 400
"""
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Este año es bisiesto')
else:
    print('no es bisiesto')
