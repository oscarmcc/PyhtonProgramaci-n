"""
Realiza un programa que pida por teclado el resultado (dato entero)
obtenido al lanzar un dado de seis caras y muestre por pantalla el número
en letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6,
se mostrará el mensaje: “ERROR: número incorrecto.”.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa que nos dice cual es el número opuesto en un dado')

NUM = int(input('Dame el número que ha salido en el dado'))

match NUM:
    case 1:
        print('El número opuesto es 6')
    case 2:
        print('El número opuesto es 5')
    case 3:
        print('El número opuesto es 4')
    case 4:
        print('El número opuesto es 3')
    case 5:
        print('El número opuesto es 2')
    case 6:
        print('El número opuesto es 6')
    case _:
        print('ERROR: número incorrecto')
