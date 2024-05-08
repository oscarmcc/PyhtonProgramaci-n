"""
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el
número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número
que había generado.

Author: Óscar Martín-Castaño Carrillo
Date: 29/10/2023
"""

import random

print('Programa para que adivines que número del 1 al 100 a elegido')

RAMDOM = random.randrange(1, 100)
TRY = 10

while TRY > 0:
    ASK = int(input('Dame el valor del número que creas que es '))
    if ASK == RAMDOM:
        print('Adivinaste el número!!', RAMDOM)
        break
    elif ASK > RAMDOM:
        print('El número debe ser menor')
    elif ASK < RAMDOM:
        print('El número debe ser mayor')
    TRY = TRY - 1
    print(f"Te quedan {TRY} intentos")
    if TRY == 0:
        print('Se te acabaron las oportunidades')
