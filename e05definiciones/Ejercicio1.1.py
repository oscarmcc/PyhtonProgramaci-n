"""
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar,
restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y
muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú
se volverá a mostrar, a menos que no se de a la opción terminar.

Author: Óscar Martín-Castaño Carrillo
Date: 30/11/2023
"""

import funciones

funciones.print_title('Programa que pide dos valores y puedes elegir que operación realizar')

ARRAY_OF_OPERATIONS = ['Sumar', 'Restar', 'Multiplicar', 'Dividir', 'Finalizar']


def main():
    a = funciones.input_int()
    b = funciones.input_int()
    while True:
        for i in range(len(ARRAY_OF_OPERATIONS)):
            print(f"{i + 1}. {ARRAY_OF_OPERATIONS[i]}")
        print('-' * len(ARRAY_OF_OPERATIONS) * 3)
        try:
            selector = int(input('Elige la opción que desees '))
            print()
            match selector:
                case 1:
                    number_sum(a, b)
                case 2:
                    number_subtract(a, b)
                case 3:
                    number_multiplication(a, b)
                case 4:
                    number_division(a, b)
                case 5:
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
