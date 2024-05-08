"""
Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero,
 o un mensaje de aviso en caso contrario.
Author: Óscar Martín-Castaño Carrillo
Date: 20/10/2023
"""

print('Programa para mostrar la división de dos números')

# Pedir los datos para el programa necesario
NUM1 = int(input('Dame el primer número '))
NUM2 = int(input('Dame el segundo número '))

# Comparar los datos para realizar el programa
if NUM2 == 0:
    print('Para mostrar la división el segundo número no puede ser 0')
else:
    D = NUM1 / NUM2
    print(f'{NUM1}/{NUM2}={D}')
