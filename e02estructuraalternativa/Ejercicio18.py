"""
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
Si introducimos otro número nos da un error.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para saber que día de la semana es del 1 al 7')

day = int(input('Dime el número del día de la semana '))

match day:
    case 1:
        print('El día es Lunes')
    case 2:
        print('El dia es Martes')
    case 3:
        print('El día es Miércoles')
    case 4:
        print('El día es Jueves')
    case 5:
        print('El día es Viernes')
    case 6:
        print('El día es Sábado')
    case 7:
        print('El día es Domingo')
    case _:
        print('ERRROR: no corresponde con ningún día de la semana')
