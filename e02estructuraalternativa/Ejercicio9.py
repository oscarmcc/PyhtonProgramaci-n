"""
Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje
«Es signo de puntuación» solo si el carácter leído es un signo de puntuación,
«Es una letra» si es una letra (da igual que sea mayúscula, minúscula o acentuada),
«Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y
«No es un carácter» si el usuario ha introducido más de un carácter.
Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""
import string

print('Programa para detectar que tipo de carácter es el que introducimos')

# Pedimos el carácter para el programa
Letter = input('Introduce el carácter deseado ')

if len(Letter) != 1:
    print('Introduce solo UN carácter')
elif Letter in string.punctuation:
    print('Es un signo de puntuación')
elif Letter.isalpha():
    print('Es una letra')
elif Letter.isdigit():
    print('Es un número')
else:
    print('Es otro carácter')
