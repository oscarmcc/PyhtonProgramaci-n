"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las
dimensiones de los lados de un triángulo. El programa debe determinar
que tipo de triangulo es, teniendo en cuenta los siguiente:

Si se cumple Pitágoras entonces es triángulo rectángulo
Si sólo dos lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno.
Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para clasificar un triángulo')

# Importamos la raíz cuadrada de la librería math y pedimos los datos necesarios
from math import sqrt
HIPO = float(input('Dame el valor de la hipotenusa'))
CAT1 = float(input('Dame el valor del primer cateto '))
CAT2 = float(input('Dame el valor del segundo cateto '))

# Comparamos los datos para llegar al resultado
if HIPO == CAT1 == CAT2:
    print('El triángulo es equilátero')
elif HIPO == sqrt(CAT1 ** 2 + CAT2 ** 2):
    print('El triángulo es rectángulo')
elif HIPO == CAT1 or HIPO == CAT2 or CAT1 == CAT2:
    print('El triángulo es isósceles')
else:
    print('El triángulo es escaleno')
