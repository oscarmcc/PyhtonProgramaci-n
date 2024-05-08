"""
Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
realiza un programa que cuente cuantas palabras tiene.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""

print('Programa que nos indica cuántas palabras tiene la cadena introducida')

user_string = input('Dame una cadena ')
user_string = str.lower(user_string)
character = " "

word = 1
for c in user_string:
    if c.isspace():
        word += 1
print(f"Para la cadena {user_string} hay {word} palabras")
