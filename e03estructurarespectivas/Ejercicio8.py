"""
Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

Para hacer una espera en Python podemos usar el método sleep del módulo time.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""

import time

print('Programa que pone en marcha un cronómetro')

hour = int(input('Introduce las horas '))
minutes = int(input('Introduce los minutos '))
seconds = int(input('Introduce los segundos '))

while hour > 0 or minutes > 0 or seconds > 0:
    print(f"{hour} : {minutes} : {seconds}")
    time.sleep(1)
    if seconds == 0 and minutes > 0:
        minutes -= 1
        seconds = 60
    if minutes == 0 and hour > 0:
        hour -= 1
        minutes = 60
        seconds = 60
    seconds -= 1


print('Se acabó el tiempo')
