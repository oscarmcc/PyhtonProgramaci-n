"""
Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""
import sys
print('Programa que nos indica si una cadena tiene una subcadena')

user_string = input('Introduce la cadena deseada ')
sub_string = input('Introduce la subcadena que deseas buscar ')

if sub_string in user_string:
    print(f"Muy bien la cadena {sub_string} se encuentra en la cadena {user_string}")
else:
    print(f"Error; la subcadena {sub_string} no se encuentra en la cadena {user_string}.", file=sys.stderr)
