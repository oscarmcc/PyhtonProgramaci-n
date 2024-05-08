"""
Realiza un programa que pida cinco números enteros y diga cuál es el mayor.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para averiguar de 5 números el mayor')

NUM1 = float(input('Dame el primer número '))
NUM2 = float(input('Dame el segundo número '))
NUM3 = float(input('Dame el tercer número '))
NUM4 = float(input('Dame el cuarto número '))
NUM5 = float(input('Dame el quinto número '))


if NUM1 > NUM2 and NUM1 > NUM3 and NUM1 > NUM4 and NUM1 > NUM5:
    print(NUM1, 'es mayor')
elif NUM2 > NUM1 and NUM2 > NUM3 and NUM2 > NUM4 and NUM2 > NUM5:
    print(NUM2, 'es mayor')
elif NUM3 > NUM1 and NUM3 > NUM2 and NUM3 > NUM4 and NUM3 > NUM5:
    print(NUM3, 'es mayor')
elif NUM4 > NUM1 and NUM4 > NUM2 and NUM4 > NUM3 and NUM4 > NUM5:
    print(NUM4, 'es mayor')
elif NUM5 > NUM1 and NUM5 > NUM2 and NUM5 > NUM3 and NUM5 > NUM4:
    print(NUM5, 'es el mayor')
else:
    print('Hay algún número que es igual')
