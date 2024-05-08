"""
Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
Las variables se inicializan a cero

Author: Óscar Martín-Castaño Carrillo
Date: 30/11/2023
"""

import funciones

funciones.print_title('Programa que pide dos valores y puedes elegir que operación realizar')

ARRAY_OF_OPERATIONS = ['Introducir variables', 'Sumar', 'Restar', 'Multiplicar', 'Dividir', 'Finalizar']


def main():
    a = 0
    b = 0
    while True:
        for i in range(len(ARRAY_OF_OPERATIONS)):
            print(f"{i + 1}. {ARRAY_OF_OPERATIONS[i]}")
        print('-' * len(ARRAY_OF_OPERATIONS) * 3)
        try:
            selector = int(input('Elige la opción que desees '))
            print()
            match selector:
                case 1:
                    a = funciones.input_int()
                    b = funciones.input_int()
                case 2:
                    number_sum(a, b)
                case 3:
                    number_subtract(a, b)
                case 4:
                    number_multiplication(a, b)
                case 5:
                    number_division(a, b)
                case 6:
                    print('Gracias por utilizar este programa, hasta la próxima')
                    exit(0)
        except ValueError:
            print('Recuerda introducir una opción correcta')


def number_sum(a, b):
    print(f"La suma de {a} y {b} da como resultado {a + b}\n")


def number_subtract(a, b):
    print(f"La resta de {a} y {b} da como resultado {a - b}\n")


def number_multiplication(a, b):
    print(f"La multiplicación de {a} y {b} da como resultado {a * b}\n")


def number_division(a, b):
    if b == 0:
        print('Oye, no puedo dividir entre 0 ya que b vale 0')
    else:
        print(f"La división de {a} y {b} da como resultado {a / b}\n")


if __name__ == '__main__':
    main()
