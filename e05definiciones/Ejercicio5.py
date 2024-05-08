"""
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres.

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
pantalla, solo se debe usar print desde el programa principal.

Author: Óscar Martín-Castaño Carrillo
Date: 9/12/2023
"""

import funciones

funciones.print_title('Al introducir un número nos lo pasa al sistema de palotes')


def stick_sistem():
    number = funciones.input_int()
    representation = [
            '-----', '|', '||---', '|||--', '||||-', '|||||', '-||||', '--|||', '---||', '----|'
        ]

    sticks = ''
    for digito in str(number):
        sticks += representation[int(digito)] + ' - '
    sticks = sticks[:-2]
    return sticks


if __name__ == '__main__':
    print(stick_sistem())
