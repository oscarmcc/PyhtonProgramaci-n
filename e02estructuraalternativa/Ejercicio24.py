"""
Diseña un programa que, dado un número real que debe representar
la calificación numérica de un examen, proporcione la calificación
cualitativa correspondiente al número dado. La calificación cualitativa
será una de las siguientes: «Suspenso» (nota menor que 5),
«Aprobado» (nota mayor o igual que 5, pero menor que 7),
«Notable» (nota mayor o igual que 7, pero menor que 9),
«Sobresaliente» (nota mayor o igual que 9, pero menor que 10), «Matrícula de Honor» (nota 10).

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para representar la calificación cualitativa')

mark = int(input('Introduce tu nota '))

match mark:
    case 1 | 2 | 3 | 4:
        print('Estas suspenso')
    case 5 | 6:
        print('Estás aprobado')
    case 7 | 8:
        print('Notable')
    case 9:
        print('Sobresaliente')
    case 10:
        print('Tienes una Matrícula de Honor')
