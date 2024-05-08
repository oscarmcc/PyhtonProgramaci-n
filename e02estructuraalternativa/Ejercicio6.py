"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para detectar si la primera letra es mayúscula')

String = str(input('Necesito una cadena para realizar el programa '))

if String[0].isupper():
    print('La cadena empieza por mayúscula')
else:
    print('La cadena no empieza por mayúscula')
