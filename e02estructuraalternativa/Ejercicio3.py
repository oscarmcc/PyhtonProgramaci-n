"""
Escribe un programa que lea un número e indique si es par o impar.
Author: Óscar Martín-Castaño Carrillo
Date: 20/10/2023
"""

print('Programa para saber si un número es par o impar')

# Pido los datos necesarios para realizar el programa
NUM = int(input('Dame el valor del número deseado '))

# Realizo el cálculo para saber si el resto da 0
R = NUM % 2

# Comparo el resultado para saber si el número es par o impar
if R == 0:
    print('El número es par')
else:
    print('El número es impar')
