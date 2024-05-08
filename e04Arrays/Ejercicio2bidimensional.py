"""
Modifica el programa anterior de tal forma que los números que se introducen en el array se generen de
forma aleatoria (valores entre 100 y 999).
"""
print('Programa que genera 20 números y nos muestra una hoja de cálculo con la suma de los números')

import random

ROWS = 4
COLUMNS = 5
LOWEST_NUM = 100
BIGGEST_NUM = 999
WIDTH_NUMBER = 5
array = [[0] * COLUMNS for _ in range(ROWS)]

for row in range(ROWS):
    for column in range(COLUMNS):
        array[row][column] = random.randint(LOWEST_NUM, BIGGEST_NUM)

for row in range(ROWS):
    sum_row = 0
    for column in range(COLUMNS):
        sum_row += array[row][column]
        print(f"{array[row][column]:{WIDTH_NUMBER}} ", end="")
    print(f"| {sum_row:{WIDTH_NUMBER}}")

print("-" * ((WIDTH_NUMBER+1)*(COLUMNS+1) + 1))
sum_total = 0
for column in range(COLUMNS):
    sum_column = 0
    for row in range(ROWS):
        sum_column += array[row][column]
    print(f"{sum_column:{WIDTH_NUMBER}} ", end="")
    sum_total += sum_column
print(f"| {sum_total:{WIDTH_NUMBER}}")
