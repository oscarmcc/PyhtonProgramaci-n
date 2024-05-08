"""
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array.
El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y
todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.

Author: Óscar Martín-Castaño Carrillo
Date: 16/11/2023
"""

print('Programa que pasa a las primeras posiciones los números pares en una lista')

import random

TOTAL_NUMBERS = 20
MIN_NUMBER = 0
MAX_NUMBER = 100

numbers = []
for _ in range(TOTAL_NUMBERS):
    numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
print("La lista original dada a sido: ", numbers)

pair_numbers = []
odd_numbers = []
for n in numbers:
    if n % 2 == 0:
        pair_numbers.append(n)
    else:
        odd_numbers.append(n)

numbers = pair_numbers + odd_numbers
print("La lista que ha resultado en el programa es:", numbers)
