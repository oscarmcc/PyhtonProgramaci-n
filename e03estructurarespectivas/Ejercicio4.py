"""
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

Author: Óscar Martín-Castaño Carrillo
Date: 29/10/2023
"""

print('Programa que nos imprime los números pares entre dos que hayamos dados')

NUM1 = int(input('Dame el primer número '))
NUM2 = int(input('Dame el número final '))

REST = NUM1 % 2

if REST == 0:
    while NUM1 < NUM2:
        if NUM1 == NUM2:
            print(NUM2)
        NUM1 = NUM1 + 2
        print(NUM1)

if REST != 0:
    NUM1 = NUM1 + 1
    print(NUM1)
    while NUM1 < NUM2:
        if NUM1 == NUM2:
            print(NUM2)
        NUM1 = NUM1 + 2
        print(NUM1)
