"""
Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter
en la cadena por el segundo carácter.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""
import sys
print('Programa que sustituye un carácter por otro en una cadena')
while True:
    user_string = input('Dime una cadena ')
    select_character = input('Dime el carácter que quieres cambiar ')
    change_character = input('Dime el carácter por el que quieres cambiar ')

    if len(select_character) != 1 or len(change_character) != 1:
        print('Error; Por favor introduce un carácter válido.\n', file=sys.stderr,)
        select_character = input('\nDime el carácter que quieres cambiar ')
        change_character = input('Dime el carácter por el que quieres cambiar ')

    final_string = ""
    for c in user_string:
        if c == select_character:
            final_string += change_character
        else:
            final_string += c
    print(f"La cadena se quedaría como: {final_string}")
