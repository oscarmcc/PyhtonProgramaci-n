"""
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el
superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las
siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Informa si hemos introducido algún número igual a los límites del intervalo.

Author: Óscar Martín-Castaño Carrillo
Date: 29/10/2023
"""

print('Programa que dando nosotros un intervalo y unos números nos diga la suma de los que están dentro del '
      'intervalo,los que estan fuera y si hay algún número igual al límite')

ADDITION = 0
OUTSIDE = 0
EQUAL = 0

LIMIT1 = int(input('Dame el número que da inicio al intervalo '))
LIMIT2 = int(input('Dame el número que da fin al intervalo '))

if LIMIT1 > LIMIT2 or LIMIT1 == LIMIT2:
    print('El límite inicial debe ser menor al límite final ')

    LIMIT1 = int(input('Dame el número que da inicio al intervalo '))
    LIMIT2 = int(input('Dame el número que da fin al intervalo '))

NUM = int(input('Dame el número deseado '))

while NUM > 0:
    NUM = int(input('Dame el número deseado '))

    if LIMIT1 < NUM < LIMIT2:
        ADDITION += NUM

    elif NUM < LIMIT1 or NUM > LIMIT2:
        OUTSIDE += 1

    elif NUM == LIMIT1 or NUM == LIMIT2:
        EQUAL += 1

print(f"La suma de los números que están dentro del intervalo es {ADDITION}")
print(f"Los números que están fuera del intervalo son {OUTSIDE}")
print(f"Los números que son iguales a los límites son {EQUAL}")
