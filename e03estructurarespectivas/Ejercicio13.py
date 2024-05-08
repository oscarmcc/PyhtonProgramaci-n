"""
Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""
print('Programa que intercambia mayúscula por minúscula')

user_string = input('Introduce una cadena ')

final_string = ""

for c in user_string:
    if c.isupper():
        final_string += c.lower()
    else:
        final_string += c.upper()
print(f"La cadena nueva sería: {final_string}")
