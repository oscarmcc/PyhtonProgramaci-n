"""
El director de una escuela está organizando un viaje de estudios,
y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe
pagar a la compañía de viajes por el servicio. La forma de cobrar es la
siguiente: si son 100 alumnos o más, el costo por cada alumno es
de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49,
de 95 euros, y si son menos de 30, el costo de la renta del autobús es
de 4000 euros, sin importar el número de alumnos. Realiza un programa
que permita determinar el pago a la compañía de autobuses y lo que debe
pagar cada alumno por el viaje.

Author: Óscar Martín-Castaño Carrillo
Date 22/10/2023
"""

print('Programa para determinar cuánto debe pagar un alumno para el viaje')

classmates = int(input('El numero de alumnos es '))

if classmates >= 100:
    price = 65
    final_price = 65 * classmates
    print('El precio por cada alumno es', price)
    print('El precio final es de', final_price)
elif 99 <= classmates >= 50:
    price = 70
    final_price = 70 * classmates
    print('EL precio por cada alumno es', price)
    print('El precio final es de', final_price)
elif 40 <= classmates >= 30:
    price = 95
    final_price = 95 * classmates
    print('El precio por cada alumno es', price)
    print('El precio final es de', final_price)
else:
    print('El precio final es de 4000 euros')
