"""
Realiza un programa que pida tres números enteros y diga cuál es el mayor.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para saber qué número es mayor')

NUM1 = float(input('Dame el primer número '))
NUM2 = float(input('Dame el segundo número '))
NUM3 = float(input('Dame el tercer número '))

if NUM1 > NUM2 and NUM1 > NUM3:
    print(NUM1, 'es mayor')
elif NUM2 > NUM1 and NUM2 > NUM3:
    print(NUM2, 'es mayor')
elif NUM3 > NUM1 and NUM3 > NUM2:
    print(NUM3, 'es mayor')
else:
    print('Hay algún número que es igual')
