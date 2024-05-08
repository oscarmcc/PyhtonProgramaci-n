"""
Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""

print('Programa para encontrar un carácter que queramos en una cadena que escribamos')

user_string = input('Dame una cadena ')
character = input('Dime el carácter que deseas buscar ')
user_string = str.lower(user_string)

while len(character) != 1:
    character = input(f"{character} no es una cadena por favor introduce un carácter válido ")

occurrences_character = 0
for c in user_string:
    if c == character:
        occurrences_character += 1

print(f"El carácter {character} se encuentra en la cadena {user_string}, {occurrences_character} veces")
