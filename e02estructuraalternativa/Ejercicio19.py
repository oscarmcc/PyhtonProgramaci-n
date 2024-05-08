"""
Escribe un programa que pida un número entero entre uno y doce
e imprima el número de días que tiene el mes correspondiente.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para decir cuantos días tiene el mes')

month = int(input('Dime el número al que corresponde el mes '))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print('El mes tiene 31 días')
    case 2:
        print('El mes de febrero tiene 28 días, pero en año bisiesto tiene 29')
    case 4 | 6 | 9 | 11:
        print('El mes tiene 30 días')
    case _:
        print('El número introducido no corresponde a ningún mes')
