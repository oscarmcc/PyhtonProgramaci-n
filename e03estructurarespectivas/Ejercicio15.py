"""
Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee
igual adelante que atrás.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""
import sys
print('Programa que nos indica si una cadena es un palíndromo o no')

user_string = input('Dame la cadena que deseas comprobar ')

reversed_user_string = ""
for c in user_string[::-1]:
    reversed_user_string += c
if reversed_user_string == user_string:
    print(f"La cadena {user_string} y la cadena {reversed_user_string} son un palíndromo")
else:
    print(f"Error;La cadena {user_string} y la cadena {reversed_user_string} no son un palíndromo", file=sys.stderr)
