"""
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y
los radios r1,r2 de dos circunferencias y las clasifique en uno de estos
estados:

exteriores
tangentes exteriores
secantes
tangentes interiores
interiores
concéntricas

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa que te clasifica las circunferencias')

from math import sqrt

x1 = int(input('Dame el punto x central de la primera circunferencia '))
y1 = int(input('Dame el punto y central de la primera circunferencia '))
x2 = int(input('Dame el punto x central de la segunda circunferencia '))
y2 = int(input('Dame el punto y central de la segunda circunferencia '))
r1 = int(input('Dame el radio de la primera circunferencia '))
r2 = int(input('Dame el radio de la segunda circunferencia '))
distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distance < (r1 + r2):
    print('Las circunferencias son exteriores')
elif distance == (r1 + r2):
    print('Las circunferencias son tangentes exteriores')
elif (distance < (r1 - r2)) and (distance < (r1 - r2)):
    print('Las circunferencias son secantes')
elif distance == (r1 - r2):
    print('Las circunferencias son tangentes interiores')
elif (distance > 0) and (distance < (r1 - r2)):
    print('Las circunferencias son interiores')
else:
    print('Las circunferencias son concéntricas')
