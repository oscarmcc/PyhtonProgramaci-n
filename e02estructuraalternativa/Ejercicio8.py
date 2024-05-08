"""
Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre
el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’.
En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones
se debe mostrar ‘NO ACEPTADA’.
Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para ver si una persona es aceptada')

# Pedimos los datos necesarios para el programa
NOTE = int(input('Dame la nota de la persona '))
AGE = int(input('Dame la edad de la persona '))
SEX = input('Dame el sexo de la persona ').upper()

# Comparamos los datos para encontrar la solución
if NOTE >= 5 and AGE >= 18:
    if SEX == 'F':
        print('La persona es aceptada')
    else:
        print('POSIBLE')
else:
    print('Esta persona no está aceptada')
