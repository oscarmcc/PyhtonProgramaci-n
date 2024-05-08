"""
Realizar un algoritmo que pida números
(se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos
son mayores que 0, menores que 0 e iguales a 0.

Author: Óscar Martín-Castaño Carrillo
Date: 29/10/2023
"""

print('Este es un programa para decir que número es igual a 0, son mayores o son menores')

print('Introduce 5 números')
TRY = 5

while TRY > 0:
    NUM = int(input())
    if NUM < 0:
        print('Este número es menor que 0')
    elif NUM > 0:
        print('Este número es mayor que 0')
    else:
        print('Este número es igual a 0')
    TRY = TRY - 1
