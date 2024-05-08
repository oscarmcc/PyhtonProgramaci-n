"""
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa
termina cuando se introduce un espacio.

Author: Óscar Martín-Castaño Carrillo
Date: 29/10/2023
"""

print('Programa para saber si el carácter introducido es una vocal o no')
print('Pulsa enter para salir del programa')

while True:
    VOWEL = input('Introduce el carácter deseado en minúscula por favor ').lower()
    if VOWEL == 'a' or VOWEL == 'e' or VOWEL == 'i' or VOWEL == 'o' or VOWEL == 'u':
        print('Es una vocal')
    elif VOWEL == '':
        exit(0)
    else:
        print('No es una vocal')
