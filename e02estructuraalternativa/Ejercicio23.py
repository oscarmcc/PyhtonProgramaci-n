"""
Diseña un programa que, dados cinco números enteros, determine
cuál de los cuatro últimos números es más cercano al primero.
Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10,
el programa responderá que el número más cercano al 2 es el 1.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para dar como resultado un número de los 5 introducidos más cercano al primero')

print('Introduce los 5 números')
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

candidate = n2
distance = abs(n1 - n2)

if abs(n1 - n3) < distance:
    candidate = n3
    distance = abs(n1 - n3)
if abs (n1 - n4) < distance:
    candidate = n4
    distance = abs(n1 - n4)
if abs(n1 - n5) < distance:
    candidate = n5

print(f"{candidate} es el número con menos distancia a {n1}")
