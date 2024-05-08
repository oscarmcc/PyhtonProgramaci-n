"""
Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción
(por su número) y devuelve la opción escogida. Modifica el último programa para que use esta función.

Author: Óscar Martín-Castaño Carrillo
Date: 30/11/2023
"""

import funciones

funciones.print_title('Programa que pide dos valores y puedes elegir que operación realizar')

ARRAY_OF_OPERATIONS = ['Introducir variables', 'Sumar', 'Restar', 'Multiplicar', 'Dividir', 'Finalizar']


def main():
    b = 0
    a = 0
    while True:
        funciones.menu(ARRAY_OF_OPERATIONS)
        try:
            selector = int(input('Elige la opción que desees '))
            print()
            match selector:
                case 1:
                    a = funciones.input_int()
                    b = funciones.input_int()
            if a != 0 and b != 0:
                match selector:
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
            else:
                print('Recuerda debes introducir primero los valores de a y de b; debe ser alguno distinto de 0')
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
