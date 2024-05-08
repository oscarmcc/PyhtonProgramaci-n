"""
Realiza un programa que rellene un array de 6 filas por 10 columnas con números enteros positivos comprendidos
entre 0 y 1000 (ambos incluidos). A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.

Author: Óscar Martín-Castaño Carrillo
Date: 21/11/2023
"""
FINISH_LIST = 1000
START_LIST = 0
ROWS = 6
COLUMNS = 10

print('Programa que rellena un array de 6*10 dando el máximo y el mínimo')
import random


def maxi():
    global array
    global max_value
    global max_row
    global max_column
    for row in range(ROWS):
        for column in range(COLUMNS):
            if max_value < array[row][column]:
                max_value = array[row][column]
                max_row = row
                max_column = column
    print(f"El número máximo es {max_value} que se encuentra en la posición {max_row}, {max_column}")


def mini():
    global array
    global min_value
    global min_row
    global min_column
    for row in range(ROWS):
        for column in range(COLUMNS):
            if min_value > array[row][column]:
                min_value = array[row][column]
                min_row = row
                min_column = column
    print(f"El número mínimo es {min_value} que se encuentra en la posición {min_row}, {min_column}")


array = [[0] * COLUMNS for _ in range(ROWS)]

for row in range(ROWS):
    for column in range(COLUMNS):
        array[row][column] = random.randint(START_LIST, FINISH_LIST)

print(array)

while True:
    try:
        answer = input('¿Qué deseas ver? El número máximo (U) '
                       'o el número mínimo (L) con sus respectivos índices; pulsa enter para finalizar ').upper()
    except ValueError:
        print('Recuerda introducir la respuesta correcta \n')

    match answer:
        case 'U':
            max_value = array[0][0]
            max_row = 0
            max_column = 0
            maxi()
        case 'L':
            min_value = array[0][0]
            min_row = 0
            min_column = 0
            mini()
        case _:
            print('Has finalizado el programa gracias por utilizarlo')
            exit(0)
