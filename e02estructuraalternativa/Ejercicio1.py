"""
Programa que pida dos números e indique si el primero es mayor que el segundo o no.
Author: Óscar Martín-Castaño Carrillo
Date: 20/10/2023
"""

print('Programa para saber que número es mayor')

# Pedimos los datos necesarios para realizar el programa
NUM1 = int(input('Dame el primer número '))
NUM2 = int(input('Dame el segundo número '))

# Ejecutamos el programa para que nos muestre el resultado
if NUM1 > NUM2:
    print('El numéro mayor es', NUM1)
else:
    print('El número mayor es', NUM2)
