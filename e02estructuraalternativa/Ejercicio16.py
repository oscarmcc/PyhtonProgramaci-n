"""
La política de cobro de una compañía telefónica es: cuando se realiza
una llamada, el cobro es por el tiempo que ésta dura, de tal forma que
los primeros cinco minutos cuestan 1 euro por minuto, los siguientes
tres, 80 céntimos por minuto, los siguientes dos minutos,
70 céntimos por minuto, y a partir del décimo minuto, 50 céntimos por minuto.

Además, se carga un impuesto de 3% cuando es domingo, y si es otro día,
en turno de mañana, 15%, y en turno de tarde, 10%. Realice un algoritmo
para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para averiguar cuánto debe pagar un usuario en cada llamada')

minutes = int(input('De cuantos minutos ha sido la llamada realizada '))
day = int(input('Dime del 1 al 7 el día de la llamada '))
shift = int(input('Dime el turno donde se ha realizado la llamada mañana(1) o tarde(2) '))

if minutes >= 5:
    price = minutes * 1

elif minutes <= 8:
    price = 5 * 1 + (minutes - 5) * 0.8

elif minutes <= 10:
    price = 5 * 1.0 + 3 * 0.8 + (minutes - 8) * 0.7

else:
    price = 5 * 1.0 + 3 * 0.8 + 2 * 0.7 + (minutes - 10) * 0.5

match day:
    case 1 | 2 | 3 | 4 | 5 | 6:
        if shift == 1:
            tax = price * 0.15

        elif shift == 2:
            tax = price * 0.10

        else:
            print('Introduce el número correcto')

    case 7:
        tax = price * 0.03

final_price = price + tax

print(f"El precio final será de {final_price} €")
