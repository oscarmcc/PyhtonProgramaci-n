"""
Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por
5 columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.

Author: Óscar Martín-Castaño Carrillo
Date: 16/11/2023
"""
import sys

print('Programa que pide 20 números y nos muestra una hoja de cálculo con la suma de los números')

ROWS = 4
COLUMNS = 5

array = [[0] * COLUMNS for _ in range(ROWS)]

while True:
    try:
        for row in range(ROWS):
            for column in range(COLUMNS):
                array[row][column] = int(input('Introduce un número entero por favor'))
        break
    except ValueError:
        print('Recuerda introducir un número válido \n', file=sys.stderr)

for row in range(ROWS):
    sum_row = 0
    for column in range(COLUMNS):
        sum_row += array[row][column]
        print(f"{array[row][column]:3d} ", end="")
    print(f"| {sum_row:3d}")

print("-" * (4*(COLUMNS+1) + 1))
sum_total = 0
for column in range(COLUMNS):
    sum_column = 0
    for row in range(ROWS):
        sum_column += array[row][column]
    print(f"{sum_column:3d} ", end="")
    sum_total += sum_column
print(f"| {sum_total:3d}")
