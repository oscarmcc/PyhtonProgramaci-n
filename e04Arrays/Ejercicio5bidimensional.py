"""
Modifica el programa anterior de tal forma que no se repita ningún número en el array.

Author: Óscar Martín-Castaño Carrillo
Date: 21/11/2023
"""

FINISH_LIST = 1000
START_LIST = 0
ROWS = 6
COLUMNS = 10

print('Programa que rellena un array de 6*10 dando el máximo y el mínimo')
import random


def generate():   # Función para generar el array
    global array
    global aux_array
    for row in range(ROWS):
        for column in range(COLUMNS):
            while True:
                n = random.randint(START_LIST, FINISH_LIST)
                aux_in_array = False
                for i in range(row + 1):
                    if n in array[i]:
                        aux_in_array = True
                        break
                if not aux_in_array:
                    aux_in_array = False
                    break
            array[row][column] = n
    print(array)


def maxi():    # Función para encontrar el número máximo
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


def mini():     # Función para encontrar el número mínimo
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
aux_array = [[0] * COLUMNS for _ in range(ROWS)]
generate()

print(f"U. Número Máximo \n"
      f"L. Número mínimo \n"
      f" Finalizar")
print("__________________")

while True:
    answer = input('¿Qué deseas ver? Elige escribiendo lo requerido en el menú de opciones, '
                   'cualquier otra tecla finaliza el programa ').upper()
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
