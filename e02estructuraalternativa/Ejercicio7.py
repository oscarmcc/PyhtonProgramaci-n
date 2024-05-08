"""
Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente.
 Pueden ocurrir tres cosas:

El exponente sea positivo, solo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para realizar una potencia')

# Pedimos los datos para realizar el programa
NUM = int(input('Dame el número que quieras '))
POT = int(input('Dame la potencia a la que vas a elevar el número'))

# Comparamos los datos para encontrar una solución
if POT > 0:
    x = NUM**POT
    print('La solución es', x)
elif POT == 0:
    print('El resultado es 1')
else:
    x = 1 / NUM**(-POT)
    print('La solución es', x)
