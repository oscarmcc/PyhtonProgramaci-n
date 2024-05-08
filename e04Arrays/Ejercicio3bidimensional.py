"""
Modifica el programa anterior de tal forma que las sumas parciales y la suma total aparezcan en la pantalla
con un pequeño retardo, dando la impresión de que el ordenador se queda “pensando” antes de mostrar los números.

Author: Óscar Martín-Castaño Carrillo
Date: 21/11/2023
"""

print(print('Programa que genera 20 números y nos muestra una hoja de cálculo con la suma de los números'))

import random
import time

ROWS = 4
COLUMNS = 5
LOWEST_NUM = 100
BIGGEST_NUM = 999
WIDTH_NUMBER = 5
array = [[0] * COLUMNS for _ in range(ROWS)]

while True:
    for row in range(ROWS):
        for column in range(COLUMNS):
            array[row][column] = random.randint(LOWEST_NUM, BIGGEST_NUM)
    for row in range(ROWS):
        sum_row = 0
        for column in range(COLUMNS):
            sum_row += array[row][column]
            print(f"{array[row][column]:{WIDTH_NUMBER}} ", end="")
        print(f"| {sum_row:{WIDTH_NUMBER}}")
        time.sleep(1)
    time.sleep(2)
    print("-" * ((WIDTH_NUMBER+1)*(COLUMNS+1) + 1))
    sum_total = 0
    for column in range(COLUMNS):
        sum_column = 0
        for row in range(ROWS):
            sum_column += array[row][column]
        print(f"{sum_column:{WIDTH_NUMBER}} ", end="")
        sum_total += sum_column
    print(f"| {sum_total:{WIDTH_NUMBER}}")
    exit(0)