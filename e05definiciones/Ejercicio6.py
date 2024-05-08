"""
Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres.

Por ejemplo, el 213 es el ..___ .____ ...__ en Morse. Utiliza esta función en un programa para comprobar que funciona
bien.

Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

Author: Óscar Martín-Castaño Carrillo
Date: 13/12/2023
"""
import funciones

funciones.print_title('Programa que imprime el número dado por nosotros en código morse')


def convert_to_morse(numero):
    morse_code = {
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'
    }

    morse = ''
    space = False

    for digito in str(numero):
        if space:
            morse += ' '
        morse += morse_code[digito]
        space = True

    return morse


def main():
    number_to_convert = funciones.input_int()
    result = convert_to_morse(number_to_convert)
    print(f"El número {number_to_convert} en código Morse es: {result}")


if __name__ == "__main__":
    main()
